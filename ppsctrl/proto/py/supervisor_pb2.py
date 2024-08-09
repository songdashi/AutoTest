# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: supervisor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import util_pb2 as util__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10supervisor.proto\x12\x18SupervisorAlgorithmProto\x1a\nutil.proto\"O\n\rConvertorBase\x12\x12\n\nis_primary\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x1b\n\x13tablecontrol_result\x18\x03 \x01(\x01\"q\n\x0f\x43onvertorLinear\x12\x1d\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndex\x12?\n\x0e\x63onvertor_base\x18\x02 \x01(\x0b\x32\'.SupervisorAlgorithmProto.ConvertorBase\"i\n\x0e\x43onvertorPitch\x12\x16\n\x0ez_screw_height\x18\x01 \x01(\x01\x12?\n\x0e\x63onvertor_base\x18\x02 \x01(\x0b\x32\'.SupervisorAlgorithmProto.ConvertorBase\"P\n\rConvertorRoll\x12?\n\x0e\x63onvertor_base\x18\x01 \x01(\x0b\x32\'.SupervisorAlgorithmProto.ConvertorBase\"\xf1\x01\n\x0fSensor2Position\x12\x45\n\x10\x63onvertor_linear\x18\x01 \x01(\x0b\x32).SupervisorAlgorithmProto.ConvertorLinearH\x00\x12\x43\n\x0f\x63onvertor_pitch\x18\x02 \x01(\x0b\x32(.SupervisorAlgorithmProto.ConvertorPitchH\x00\x12\x41\n\x0e\x63onvertor_roll\x18\x03 \x01(\x0b\x32\'.SupervisorAlgorithmProto.ConvertorRollH\x00\x42\x0f\n\rAxisConvertor\"\xf1\x01\n\x0fPosition2Sensor\x12\x45\n\x10\x63onvertor_linear\x18\x01 \x01(\x0b\x32).SupervisorAlgorithmProto.ConvertorLinearH\x00\x12\x43\n\x0f\x63onvertor_pitch\x18\x02 \x01(\x0b\x32(.SupervisorAlgorithmProto.ConvertorPitchH\x00\x12\x41\n\x0e\x63onvertor_roll\x18\x03 \x01(\x0b\x32\'.SupervisorAlgorithmProto.ConvertorRollH\x00\x42\x0f\n\rAxisConvertor\"t\n\x15Sensor2PositionResult\x12\x1d\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndex\x12\x0e\n\x06result\x18\x02 \x01(\x01\x12\x12\n\nis_primary\x18\x03 \x01(\x08\x12\x18\n\x10tablectrl_result\x18\x04 \x01(\x01\"t\n\x15Position2SensorResult\x12\x1d\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndex\x12\x0e\n\x06result\x18\x02 \x01(\x01\x12\x12\n\nis_primary\x18\x03 \x01(\x08\x12\x18\n\x10tablectrl_result\x18\x04 \x01(\x01\",\n\x0bSampleValue\x12\x0e\n\x06length\x18\x01 \x01(\x01\x12\r\n\x05\x61ngle\x18\x02 \x01(\x01\"d\n\x12\x43\x61librationSamples\x12\x36\n\x07samples\x18\x01 \x03(\x0b\x32%.SupervisorAlgorithmProto.SampleValue\x12\x16\n\x0esamples_number\x18\x02 \x01(\x05\"\xa7\x01\n\x11\x43\x61librationLinear\x12\x1d\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndex\x12\x12\n\nis_primary\x18\x02 \x01(\x08\x12I\n\x13\x63\x61libration_samples\x18\x03 \x01(\x0b\x32,.SupervisorAlgorithmProto.CalibrationSamples\x12\x14\n\x0ctable_result\x18\x04 \x03(\x01\"\x8b\x01\n\x10\x43\x61librationPitch\x12\x16\n\x0ez_screw_height\x18\x01 \x01(\x01\x12I\n\x13\x63\x61libration_samples\x18\x02 \x01(\x0b\x32,.SupervisorAlgorithmProto.CalibrationSamples\x12\x14\n\x0ctable_result\x18\x03 \x03(\x01\"r\n\x0f\x43\x61librationRoll\x12I\n\x13\x63\x61libration_samples\x18\x01 \x01(\x0b\x32,.SupervisorAlgorithmProto.CalibrationSamples\x12\x14\n\x0ctable_result\x18\x02 \x03(\x01\"\xfb\x01\n\x0b\x43\x61libration\x12I\n\x12\x63\x61libration_linear\x18\x01 \x01(\x0b\x32+.SupervisorAlgorithmProto.CalibrationLinearH\x00\x12G\n\x11\x63\x61libration_pitch\x18\x02 \x01(\x0b\x32*.SupervisorAlgorithmProto.CalibrationPitchH\x00\x12\x45\n\x10\x63\x61libration_roll\x18\x03 \x01(\x0b\x32).SupervisorAlgorithmProto.CalibrationRollH\x00\x42\x11\n\x0f\x41xisCalibration\"\x83\x01\n\x11\x43\x61librationResult\x12\x1d\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndex\x12\x12\n\nis_primary\x18\x02 \x01(\x08\x12\x15\n\rparameter_num\x18\x03 \x01(\x05\x12\x14\n\x0ctable_result\x18\x04 \x03(\x01\x12\x0e\n\x06result\x18\x05 \x03(\x01\"\x1b\n\x05Point\x12\x12\n\naxis_value\x18\x01 \x03(\x01\"\xaa\x01\n\x0eTransformation\x12\x34\n\x0bstart_point\x18\x01 \x01(\x0b\x32\x1f.SupervisorAlgorithmProto.Point\x12\x32\n\tend_point\x18\x02 \x01(\x0b\x32\x1f.SupervisorAlgorithmProto.Point\x12\x14\n\x0cis_iso_based\x18\x03 \x01(\x08\x12\x18\n\x10tablectrl_result\x18\x04 \x03(\x01\"a\n\x14TransformationResult\x12\x14\n\x0cis_iso_based\x18\x01 \x01(\x08\x12\x19\n\x11supervisor_result\x18\x02 \x03(\x01\x12\x18\n\x10tablectrl_result\x18\x03 \x03(\x01\"(\n\x10\x43orrectionMatrix\x12\x14\n\x0cmatrix_value\x18\x01 \x03(\x01\"\xeb\x01\n\x0f\x43orrectionShift\x12:\n\x06matrix\x18\x01 \x01(\x0b\x32*.SupervisorAlgorithmProto.CorrectionMatrix\x12\x30\n\x07\x63urrent\x18\x02 \x01(\x0b\x32\x1f.SupervisorAlgorithmProto.Point\x12/\n\x06target\x18\x03 \x01(\x0b\x32\x1f.SupervisorAlgorithmProto.Point\x12\x39\n\x10tablectrl_result\x18\x04 \x01(\x0b\x32\x1f.SupervisorAlgorithmProto.Point\"\x8e\x01\n\x15\x43orrectionShiftResult\x12\x39\n\x10tablectrl_result\x18\x01 \x01(\x0b\x32\x1f.SupervisorAlgorithmProto.Point\x12:\n\x11supervisor_result\x18\x02 \x01(\x0b\x32\x1f.SupervisorAlgorithmProto.Point\"N\n\x19SupervisorCalFinishedInfo\x12\x1d\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndex\x12\x12\n\nis_primary\x18\x02 \x01(\x08\"K\n\x16ReloadAfterCalibration\x12\x1d\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndex\x12\x12\n\nis_primary\x18\x02 \x01(\x08\"`\n\tReloadXML\x12\"\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndexH\x00\x88\x01\x01\x12\x17\n\nis_primary\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\x07\n\x05_axisB\r\n\x0b_is_primary\"\xa6\x04\n\x08ServerTx\x12\x14\n\x0c\x61lgorithm_id\x18\x01 \x01(\r\x12I\n\x14sensor_position_info\x18\x02 \x01(\x0b\x32).SupervisorAlgorithmProto.Sensor2PositionH\x00\x12I\n\x14position_sensor_info\x18\x03 \x01(\x0b\x32).SupervisorAlgorithmProto.Position2SensorH\x00\x12\x41\n\x10\x63\x61libration_info\x18\x04 \x01(\x0b\x32%.SupervisorAlgorithmProto.CalibrationH\x00\x12G\n\x13transformation_info\x18\x05 \x01(\x0b\x32(.SupervisorAlgorithmProto.TransformationH\x00\x12J\n\x15\x63orrection_shift_info\x18\x06 \x01(\x0b\x32).SupervisorAlgorithmProto.CorrectionShiftH\x00\x12\x39\n\nreload_xml\x18\x07 \x01(\x0b\x32#.SupervisorAlgorithmProto.ReloadXMLH\x00\x12T\n\x18reload_after_calibration\x18\x08 \x01(\x0b\x32\x30.SupervisorAlgorithmProto.ReloadAfterCalibrationH\x00\x42\x05\n\x03Msg\"\x9a\x04\n\x08ServerRx\x12\x14\n\x0c\x61lgorithm_id\x18\x01 \x01(\r\x12Q\n\x16sensor_position_result\x18\x02 \x01(\x0b\x32/.SupervisorAlgorithmProto.Sensor2PositionResultH\x00\x12Q\n\x16position_sensor_result\x18\x03 \x01(\x0b\x32/.SupervisorAlgorithmProto.Position2SensorResultH\x00\x12I\n\x12\x63\x61libration_result\x18\x04 \x01(\x0b\x32+.SupervisorAlgorithmProto.CalibrationResultH\x00\x12O\n\x15transformation_result\x18\x05 \x01(\x0b\x32..SupervisorAlgorithmProto.TransformationResultH\x00\x12R\n\x17\x63orrection_shift_result\x18\x06 \x01(\x0b\x32/.SupervisorAlgorithmProto.CorrectionShiftResultH\x00\x12[\n\x1csupervisor_cal_finished_info\x18\x07 \x01(\x0b\x32\x33.SupervisorAlgorithmProto.SupervisorCalFinishedInfoH\x00\x42\x05\n\x03Msgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'supervisor_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_CONVERTORBASE']._serialized_start=58
  _globals['_CONVERTORBASE']._serialized_end=137
  _globals['_CONVERTORLINEAR']._serialized_start=139
  _globals['_CONVERTORLINEAR']._serialized_end=252
  _globals['_CONVERTORPITCH']._serialized_start=254
  _globals['_CONVERTORPITCH']._serialized_end=359
  _globals['_CONVERTORROLL']._serialized_start=361
  _globals['_CONVERTORROLL']._serialized_end=441
  _globals['_SENSOR2POSITION']._serialized_start=444
  _globals['_SENSOR2POSITION']._serialized_end=685
  _globals['_POSITION2SENSOR']._serialized_start=688
  _globals['_POSITION2SENSOR']._serialized_end=929
  _globals['_SENSOR2POSITIONRESULT']._serialized_start=931
  _globals['_SENSOR2POSITIONRESULT']._serialized_end=1047
  _globals['_POSITION2SENSORRESULT']._serialized_start=1049
  _globals['_POSITION2SENSORRESULT']._serialized_end=1165
  _globals['_SAMPLEVALUE']._serialized_start=1167
  _globals['_SAMPLEVALUE']._serialized_end=1211
  _globals['_CALIBRATIONSAMPLES']._serialized_start=1213
  _globals['_CALIBRATIONSAMPLES']._serialized_end=1313
  _globals['_CALIBRATIONLINEAR']._serialized_start=1316
  _globals['_CALIBRATIONLINEAR']._serialized_end=1483
  _globals['_CALIBRATIONPITCH']._serialized_start=1486
  _globals['_CALIBRATIONPITCH']._serialized_end=1625
  _globals['_CALIBRATIONROLL']._serialized_start=1627
  _globals['_CALIBRATIONROLL']._serialized_end=1741
  _globals['_CALIBRATION']._serialized_start=1744
  _globals['_CALIBRATION']._serialized_end=1995
  _globals['_CALIBRATIONRESULT']._serialized_start=1998
  _globals['_CALIBRATIONRESULT']._serialized_end=2129
  _globals['_POINT']._serialized_start=2131
  _globals['_POINT']._serialized_end=2158
  _globals['_TRANSFORMATION']._serialized_start=2161
  _globals['_TRANSFORMATION']._serialized_end=2331
  _globals['_TRANSFORMATIONRESULT']._serialized_start=2333
  _globals['_TRANSFORMATIONRESULT']._serialized_end=2430
  _globals['_CORRECTIONMATRIX']._serialized_start=2432
  _globals['_CORRECTIONMATRIX']._serialized_end=2472
  _globals['_CORRECTIONSHIFT']._serialized_start=2475
  _globals['_CORRECTIONSHIFT']._serialized_end=2710
  _globals['_CORRECTIONSHIFTRESULT']._serialized_start=2713
  _globals['_CORRECTIONSHIFTRESULT']._serialized_end=2855
  _globals['_SUPERVISORCALFINISHEDINFO']._serialized_start=2857
  _globals['_SUPERVISORCALFINISHEDINFO']._serialized_end=2935
  _globals['_RELOADAFTERCALIBRATION']._serialized_start=2937
  _globals['_RELOADAFTERCALIBRATION']._serialized_end=3012
  _globals['_RELOADXML']._serialized_start=3014
  _globals['_RELOADXML']._serialized_end=3110
  _globals['_SERVERTX']._serialized_start=3113
  _globals['_SERVERTX']._serialized_end=3663
  _globals['_SERVERRX']._serialized_start=3666
  _globals['_SERVERRX']._serialized_end=4204
# @@protoc_insertion_point(module_scope)
