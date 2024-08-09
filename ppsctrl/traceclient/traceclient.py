import zmq
import sys
import os
import logging
import threading
import gc
import ctypes
import inspect


class TraceClient:
    _traceclientinstance = None

    def __init__(self, serverIp, port=6662, identity=1):
        self._die = False
        self._host = serverIp
        self._port = port
        self._identity = identity
        # self._func = func
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.DEALER)
        self._socket.setsockopt_string(zmq.IDENTITY, "id_123")
        self._lock = threading.Lock()
        self._messages = []
        self._buffer = bytes()
        # self._replies = {}
        self._connect()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    @staticmethod
    def get_trace_client(request):
        if TraceClient._traceclientinstance is None:
            host = request.config.getoption("--target-host")
        TraceClient._traceclientinstance = TraceClient(host, 6662)
        return TraceClient._traceclientinstance

    def __del__(self):
        self._die = True
        if self._thread.is_alive():
            self._thread.join()

    def _append(self, msg: str):
        # logging.info(msg)
        with self._lock:
            self._messages.append(msg)

    def _connect(self):
        print("Connecting to ...[%s]%s\n" % (self._host, self._port))
        logging.info("Connecting to %s:%d...", self._host, self._port)
        try:
            self._socket.connect("tcp://{0}:{1}".format(self._host, self._port))
            logging.info("Connected")
        except TimeoutError as ex:
            raise TimeoutError(
                f"Timeout connecting to {self._host}:{self._port}"
            ) from ex

    def _run(self):
        while not self._die:
            if not self._socket.closed:
                message = self._socket.recv()
                self._append(message)
            else:
                logging.error("sock is closed,can't receive any message...")
                break

    def sendMsg(self, data):
        if not self._socket.closed:
            self._socket.send(data)
            del data
            gc.collect()
        else:
            logging.error("sock is closed,can't send message...")

    def readMsg(self):
        with self._lock:
            if len(self._messages) > 0:
                # msg = self._messages[0]
                # msg =  self._messages.pop(0)
                return self._messages.pop(0)
        return None
