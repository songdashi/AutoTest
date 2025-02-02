# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tblservicemode.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import util_pb2 as util__pb2
import tblctl_pb2 as tblctl__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14tblservicemode.proto\x12\x13TblServiceModeProto\x1a\nutil.proto\x1a\x0ctblctl.proto\"\x8e\x02\n\x03Req\x12\x12\n\nENABLE_BAR\x18\x01 \x01(\x08\x12\x13\n\x0bRESET_MOTOR\x18\x02 \x01(\x08\x12\x13\n\x0bSTOP_MOTION\x18\x03 \x01(\x08\x12\x1c\n\x14\x43OLUMN_BRAKE_RELEASE\x18\x04 \x01(\x08\x12\x1a\n\x12MAIN_POWER_FAILURE\x18\x05 \x01(\x08\x12\x15\n\rZ_LIMIT_TOUCH\x18\x06 \x01(\x08\x12\x10\n\x08VAC_HOST\x18\x07 \x01(\x08\x12\x11\n\tSHUT_DOWN\x18\x08 \x01(\x08\x12\x10\n\x08HWME_RDY\x18\t \x01(\x08\x12\x15\n\rTABLE_ASU_RDY\x18\n \x01(\x08\x12\x15\n\rLINAC_ASU_RDY\x18\x0b \x01(\x08\x12\x13\n\x0b\x41RM_ASU_RDY\x18\x0c \x01(\x08\"O\n\x05State\x12\x14\n\x0cRECEIVER_RDY\x18\x01 \x01(\x08\x12\x18\n\x10STAND_ALONE_MODE\x18\x02 \x01(\x08\x12\x16\n\x0e\x45MERGENCY_MODE\x18\x03 \x01(\x08\"\xcc\x01\n\x05UIMAW\x12\x15\n\rUIMA_CAN_FAIL\x18\x01 \x01(\x08\x12\x1a\n\x12UIMA_ENB_BAR_STUCK\x18\x02 \x01(\x08\x12\x1d\n\x15UIMA_JOY_STICK1_STUCK\x18\x03 \x01(\x08\x12\x1d\n\x15UIMA_JOY_STICK2_STUCK\x18\x04 \x01(\x08\x12\x1e\n\x16UIMA_RESET_MOTOR_STUCK\x18\x05 \x01(\x08\x12\x16\n\x0eUIMA_TGO_STUCK\x18\x06 \x01(\x08\x12\x1a\n\x12UIMA_ENB_BAR_FIRST\x18\x07 \x01(\x08\"\xcc\x01\n\x05UIMBW\x12\x15\n\rUIMB_CAN_FAIL\x18\x01 \x01(\x08\x12\x1a\n\x12UIMB_ENB_BAR_STUCK\x18\x02 \x01(\x08\x12\x1d\n\x15UIMB_JOY_STICK1_STUCK\x18\x03 \x01(\x08\x12\x1d\n\x15UIMB_JOY_STICK2_STUCK\x18\x04 \x01(\x08\x12\x1e\n\x16UIMB_RESET_MOTOR_STUCK\x18\x05 \x01(\x08\x12\x16\n\x0eUIMB_TGO_STUCK\x18\x06 \x01(\x08\x12\x1a\n\x12UIMB_ENB_BAR_FIRST\x18\x07 \x01(\x08\"\xc3\x02\n\x05HHCAW\x12\x15\n\rHHCA_CAN_FAIL\x18\x01 \x01(\x08\x12\x1a\n\x12HHCA_ENB_BAR_STUCK\x18\x02 \x01(\x08\x12\x1c\n\x14HHCA_JOY_STICK_STUCK\x18\x03 \x01(\x08\x12\x1e\n\x16HHCA_RESET_MOTOR_STUCK\x18\x04 \x01(\x08\x12\x16\n\x0eHHCA_TGO_STUCK\x18\x05 \x01(\x08\x12\x1e\n\x16HHCA_THUMB_WHEEL_STUCK\x18\x06 \x01(\x08\x12\x1a\n\x12HHCA_ENB_BAR_FIRST\x18\x07 \x01(\x08\x12 \n\x18HHCA_AXIS_SWITCH_WARNING\x18\x08 \x01(\x08\x12(\n HHCA_ARM_CTRL_OBJ_SWITCH_WARNING\x18\t \x01(\x08\x12)\n!HHCA_DIAL_CTRL_SEL_SWITCH_WARNING\x18\n \x01(\x08\"\xc3\x02\n\x05HHCBW\x12\x15\n\rHHCB_CAN_FAIL\x18\x01 \x01(\x08\x12\x1a\n\x12HHCB_ENB_BAR_STUCK\x18\x02 \x01(\x08\x12\x1c\n\x14HHCB_JOY_STICK_STUCK\x18\x03 \x01(\x08\x12\x1e\n\x16HHCB_RESET_MOTOR_STUCK\x18\x04 \x01(\x08\x12\x16\n\x0eHHCB_TGO_STUCK\x18\x05 \x01(\x08\x12\x1e\n\x16HHCB_THUMB_WHEEL_STUCK\x18\x06 \x01(\x08\x12\x1a\n\x12HHCB_ENB_BAR_FIRST\x18\x07 \x01(\x08\x12 \n\x18HHCB_AXIS_SWITCH_WARNING\x18\x08 \x01(\x08\x12(\n HHCB_ARM_CTRL_OBJ_SWITCH_WARNING\x18\t \x01(\x08\x12)\n!HHCB_DIAL_CTRL_SEL_SWITCH_WARNING\x18\n \x01(\x08\"\xb7\x02\n\x02OW\x12\x15\n\rENB_BAR_BREAK\x18\x01 \x01(\x08\x12\x11\n\tSTM_STUCK\x18\x02 \x01(\x08\x12\x1e\n\x16LONGITUDE_CON_CONFLICT\x18\x03 \x01(\x08\x12\x1c\n\x14LATERAL_CON_CONFLICT\x18\x04 \x01(\x08\x12\x18\n\x10ISO_CON_CONFLICT\x18\x05 \x01(\x08\x12\x1d\n\x15VERTICAL_CON_CONFLICT\x18\x06 \x01(\x08\x12\x1a\n\x12PITCH_CON_CONFLICT\x18\x07 \x01(\x08\x12\x19\n\x11ROLL_CON_CONFLICT\x18\x08 \x01(\x08\x12\x1c\n\x14\x42RAKE_POWER_ABNORMAL\x18\t \x01(\x08\x12\x1d\n\x15\x44RIVER_POWER_ABNORMAL\x18\n \x01(\x08\x12\x1c\n\x14\x43OLUMN_BUZZER_ACTIVE\x18\x0b \x01(\x08\"\xf9\x02\n\x0bVersionInfo\x12\x12\n\nBUILD_DATE\x18\x01 \x01(\t\x12\x13\n\x0bSVN_VERSION\x18\x02 \x01(\r\x12\x17\n\x0fUIMA_SW_VERSION\x18\x03 \x01(\r\x12\x17\n\x0fUIMB_SW_VERSION\x18\x04 \x01(\r\x12\x17\n\x0fHHCA_SW_VERSION\x18\x05 \x01(\r\x12\x17\n\x0fHHCB_SW_VERSION\x18\x06 \x01(\r\x12\x1f\n\x17RECEIVER_ARM_SW_VERSION\x18\x07 \x01(\r\x12\x1b\n\x13RECEIVER_SW_VERSION\x18\x08 \x01(\r\x12\x17\n\x0fUIMA_HW_VERSION\x18\t \x01(\x04\x12\x17\n\x0fUIMB_HW_VERSION\x18\n \x01(\x04\x12\x17\n\x0fHHCA_HW_VERSION\x18\x0b \x01(\x04\x12\x17\n\x0fHHCB_HW_VERSION\x18\x0c \x01(\x04\x12\x1b\n\x13RECEIVER_HW_VERSION\x18\r \x01(\x04\x12\x1e\n\x16RECEIVER_SERIAL_NUMBER\x18\x0e \x01(\x04\"m\n\x11\x41utoCalOperateReq\x12\x1d\n\x04\x61xes\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndex\x12\x39\n\x0e\x61uto_cal_stage\x18\x02 \x01(\x0e\x32!.TblServiceModeProto.AutoCalStage\"0\n\x0f\x41utoCalAbortReq\x12\x1d\n\x04\x61xes\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndex\"3\n\x12OperationEnableReq\x12\x1d\n\x04\x61xes\x18\x01 \x03(\x0e\x32\x0f.Util.AxisIndex\"4\n\x13OperationDisableReq\x12\x1d\n\x04\x61xes\x18\x01 \x03(\x0e\x32\x0f.Util.AxisIndex\"\x89\x01\n\x10\x43ountMoveAxisReq\x12\x1d\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndex\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\x12\x16\n\x0e\x63ount_velocity\x18\x03 \x01(\x03\x12/\n\x04mode\x18\x04 \x01(\x0e\x32!.TblServiceModeProto.PositionMode\"C\n\x0c\x43ountMoveReq\x12\x33\n\x04reqs\x18\x01 \x03(\x0b\x32%.TblServiceModeProto.CountMoveAxisReq\"\x81\x01\n\x13PositionMoveAxisReq\x12\x1d\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndex\x12\x0b\n\x03pos\x18\x02 \x01(\x01\x12\r\n\x05speed\x18\x03 \x01(\x01\x12/\n\x04mode\x18\x04 \x01(\x0e\x32!.TblServiceModeProto.PositionMode\"I\n\x0fPositionMoveReq\x12\x36\n\x04reqs\x18\x01 \x03(\x0b\x32(.TblServiceModeProto.PositionMoveAxisReq\"a\n\x13VelocityMoveAxisReq\x12\x1d\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndex\x12\x1c\n\x03\x64ir\x18\x02 \x01(\x0e\x32\x0f.Util.Direction\x12\r\n\x05speed\x18\x03 \x01(\x01\"I\n\x0fVelocityMoveReq\x12\x36\n\x04\x61xes\x18\x01 \x03(\x0b\x32(.TblServiceModeProto.VelocityMoveAxisReq\"\xa2\x01\n\x19ServiceShiftCorrectionReq\x12\x15\n\rshift_lateral\x18\x01 \x01(\x01\x12\x1a\n\x12shift_longitudinal\x18\x02 \x01(\x01\x12\x16\n\x0eshift_vertical\x18\x03 \x01(\x01\x12\x13\n\x0bshift_pitch\x18\x04 \x01(\x01\x12\x12\n\nshift_roll\x18\x05 \x01(\x01\x12\x11\n\tshift_iso\x18\x06 \x01(\x01\"\x92\x01\n\x15ServiceIec61217AsuReq\x12\x13\n\x0bpos_lateral\x18\x01 \x01(\x01\x12\x18\n\x10pos_longitudinal\x18\x02 \x01(\x01\x12\x14\n\x0cpos_vertical\x18\x03 \x01(\x01\x12\x11\n\tpos_pitch\x18\x04 \x01(\x01\x12\x10\n\x08pos_roll\x18\x05 \x01(\x01\x12\x0f\n\x07pos_iso\x18\x06 \x01(\x01\"\x12\n\x10\x46\x61ultListInitReq\"f\n\x0e\x46\x61ultHandleReq\x12+\n\x0e\x66\x61ult_commands\x18\x01 \x01(\x0e\x32\x13.Util.FaultCommands\x12\'\n\x0c\x66\x61ult_option\x18\x02 \x01(\x0b\x32\x11.Util.FaultOption\"\x13\n\x11GetVersionInfoReq\"\x17\n\x15GetEmulationStatusReq\"6\n\x11\x41utoCalOperateRep\x12!\n\x06status\x18\x01 \x01(\x0e\x32\x11.Util.ReplyStatus\"4\n\x0f\x41utoCalAbortRep\x12!\n\x06status\x18\x01 \x01(\x0e\x32\x11.Util.ReplyStatus\"7\n\x12OperationEnableRep\x12!\n\x06status\x18\x01 \x01(\x0e\x32\x11.Util.ReplyStatus\"8\n\x13OperationDisableRep\x12!\n\x06status\x18\x01 \x01(\x0e\x32\x11.Util.ReplyStatus\"1\n\x0c\x43ountMoveRep\x12!\n\x06status\x18\x01 \x01(\x0e\x32\x11.Util.ReplyStatus\"4\n\x0fPositionMoveRep\x12!\n\x06status\x18\x01 \x01(\x0e\x32\x11.Util.ReplyStatus\"4\n\x0fVelocityMoveRep\x12!\n\x06status\x18\x01 \x01(\x0e\x32\x11.Util.ReplyStatus\">\n\x19ServiceShiftCorrectionRep\x12!\n\x06status\x18\x01 \x01(\x0e\x32\x11.Util.ReplyStatus\":\n\x15ServiceIec61217AsuRep\x12!\n\x06status\x18\x01 \x01(\x0e\x32\x11.Util.ReplyStatus\"7\n\x10\x46\x61ultListInitRep\x12#\n\x06\x66\x61ults\x18\x01 \x03(\x0b\x32\x13.Util.FaultMetadata\"3\n\x0e\x46\x61ultHandleRep\x12!\n\x06status\x18\x01 \x01(\x0e\x32\x11.Util.ReplyStatus\"K\n\x11GetVersionInfoRep\x12\x36\n\x0cversion_info\x18\x01 \x01(\x0b\x32 .TblServiceModeProto.VersionInfo\"-\n\x15GetEmulationStatusRep\x12\x14\n\x0cis_emulation\x18\x01 \x01(\x08\"\x9f\x02\n\x11ServiceAxisStatus\x12\x1d\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndex\x12\x18\n\x10primary_position\x18\x02 \x01(\x01\x12\x1a\n\x12secondary_position\x18\x03 \x01(\x01\x12\x10\n\x08velocity\x18\x04 \x01(\x01\x12\x15\n\rprimary_count\x18\x05 \x01(\x03\x12\x17\n\x0fsecondary_count\x18\x06 \x01(\x03\x12\x16\n\x0e\x63ount_velocity\x18\x07 \x01(\x03\x12\x15\n\rmotor_current\x18\x08 \x01(\x05\x12\x19\n\x11is_target_reached\x18\t \x01(\x08\x12\x15\n\rposition_diff\x18\n \x01(\x01\x12\x12\n\nerror_code\x18\x0b \x01(\t\"I\n\x11ServiceStatusPush\x12\x34\n\x04\x61xes\x18\x01 \x03(\x0b\x32&.TblServiceModeProto.ServiceAxisStatus\"|\n\x11\x41utoCalStatusPush\x12\x1d\n\x04\x61xes\x18\x01 \x01(\x0e\x32\x0f.Util.AxisIndex\x12\x39\n\x0e\x61uto_cal_stage\x18\x02 \x01(\x0e\x32!.TblServiceModeProto.AutoCalStage\x12\r\n\x05\x65vent\x18\x03 \x03(\x05\"\xd1\x02\n\x11\x44iagnosisInfoPush\x12%\n\x03req\x18\x01 \x01(\x0b\x32\x18.TblServiceModeProto.Req\x12\x19\n\x11\x61xis_brake_action\x18\x02 \x01(\x05\x12)\n\x05state\x18\x03 \x01(\x0b\x32\x1a.TblServiceModeProto.State\x12)\n\x05uimaw\x18\x04 \x01(\x0b\x32\x1a.TblServiceModeProto.UIMAW\x12)\n\x05uimbw\x18\x05 \x01(\x0b\x32\x1a.TblServiceModeProto.UIMBW\x12)\n\x05hhcaw\x18\x06 \x01(\x0b\x32\x1a.TblServiceModeProto.HHCAW\x12)\n\x05hhcbw\x18\x07 \x01(\x0b\x32\x1a.TblServiceModeProto.HHCBW\x12#\n\x02ow\x18\x08 \x01(\x0b\x32\x17.TblServiceModeProto.OW\"\xb9\x08\n\x08ServerRx\x12\x46\n\x14\x61uto_cal_operate_req\x18\x01 \x01(\x0b\x32&.TblServiceModeProto.AutoCalOperateReqH\x00\x12;\n\x0e\x63ount_move_req\x18\x02 \x01(\x0b\x32!.TblServiceModeProto.CountMoveReqH\x00\x12<\n\x0cpos_move_req\x18\x03 \x01(\x0b\x32$.TblServiceModeProto.PositionMoveReqH\x00\x12=\n\nenable_req\x18\x04 \x01(\x0b\x32\'.TblServiceModeProto.OperationEnableReqH\x00\x12?\n\x0b\x64isable_req\x18\x05 \x01(\x0b\x32(.TblServiceModeProto.OperationDisableReqH\x00\x12\x42\n\x12\x61uto_cal_abort_req\x18\x06 \x01(\x0b\x32$.TblServiceModeProto.AutoCalAbortReqH\x00\x12\x41\n\x11velocity_move_req\x18\x07 \x01(\x0b\x32$.TblServiceModeProto.VelocityMoveReqH\x00\x12\x31\n\rstop_move_req\x18\x08 \x01(\x0b\x32\x18.TblCtlProto.StopMoveReqH\x00\x12\x35\n\x0f\x66\x61ult_reset_req\x18\t \x01(\x0b\x32\x1a.TblCtlProto.FaultResetReqH\x00\x12;\n\x12\x66\x61ult_override_req\x18\n \x01(\x0b\x32\x1d.TblCtlProto.FaultOverrideReqH\x00\x12N\n\x14shift_correction_req\x18\x0b \x01(\x0b\x32..TblServiceModeProto.ServiceShiftCorrectionReqH\x00\x12\x46\n\x10iec61217_asu_req\x18\x0c \x01(\x0b\x32*.TblServiceModeProto.ServiceIec61217AsuReqH\x00\x12\x44\n\x13\x66\x61ult_list_init_req\x18\r \x01(\x0b\x32%.TblServiceModeProto.FaultListInitReqH\x00\x12?\n\x10\x66\x61ult_handle_req\x18\x0e \x01(\x0b\x32#.TblServiceModeProto.FaultHandleReqH\x00\x12\x46\n\x14get_version_info_req\x18\x0f \x01(\x0b\x32&.TblServiceModeProto.GetVersionInfoReqH\x00\x12N\n\x18get_emulation_status_req\x18\x10 \x01(\x0b\x32*.TblServiceModeProto.GetEmulationStatusReqH\x00\x42\x05\n\x03Msg\"\xf7\n\n\x08ServerTx\x12\x46\n\x14\x61uto_cal_operate_rep\x18\x01 \x01(\x0b\x32&.TblServiceModeProto.AutoCalOperateRepH\x00\x12;\n\x0e\x63ount_move_rep\x18\x02 \x01(\x0b\x32!.TblServiceModeProto.CountMoveRepH\x00\x12<\n\x0cpos_move_rep\x18\x03 \x01(\x0b\x32$.TblServiceModeProto.PositionMoveRepH\x00\x12=\n\nenable_rep\x18\x04 \x01(\x0b\x32\'.TblServiceModeProto.OperationEnableRepH\x00\x12\x45\n\x13service_status_push\x18\x05 \x01(\x0b\x32&.TblServiceModeProto.ServiceStatusPushH\x00\x12?\n\x0b\x64isable_rep\x18\x06 \x01(\x0b\x32(.TblServiceModeProto.OperationDisableRepH\x00\x12\x42\n\x12\x61uto_cal_abort_rep\x18\x07 \x01(\x0b\x32$.TblServiceModeProto.AutoCalAbortRepH\x00\x12;\n\x12integrity_mode_ind\x18\x08 \x01(\x0b\x32\x1d.TblCtlProto.IntegrityModeIndH\x00\x12\x41\n\x11velocity_move_rep\x18\t \x01(\x0b\x32$.TblServiceModeProto.VelocityMoveRepH\x00\x12\x31\n\rstop_move_rep\x18\n \x01(\x0b\x32\x18.TblCtlProto.StopMoveRepH\x00\x12\x35\n\x0f\x66\x61ult_reset_rep\x18\x0b \x01(\x0b\x32\x1a.TblCtlProto.FaultResetRepH\x00\x12;\n\x12\x66\x61ult_override_rep\x18\x0c \x01(\x0b\x32\x1d.TblCtlProto.FaultOverrideRepH\x00\x12\x46\n\x14\x61uto_cal_status_push\x18\r \x01(\x0b\x32&.TblServiceModeProto.AutoCalStatusPushH\x00\x12N\n\x14shift_correction_rep\x18\x0e \x01(\x0b\x32..TblServiceModeProto.ServiceShiftCorrectionRepH\x00\x12\x46\n\x10iec61217_asu_rep\x18\x0f \x01(\x0b\x32*.TblServiceModeProto.ServiceIec61217AsuRepH\x00\x12\x45\n\x13\x64iagnosis_info_push\x18\x10 \x01(\x0b\x32&.TblServiceModeProto.DiagnosisInfoPushH\x00\x12\x44\n\x13\x66\x61ult_list_init_rep\x18\x11 \x01(\x0b\x32%.TblServiceModeProto.FaultListInitRepH\x00\x12?\n\x10\x66\x61ult_handle_rep\x18\x12 \x01(\x0b\x32#.TblServiceModeProto.FaultHandleRepH\x00\x12)\n\x0c\x66\x61ult_report\x18\x13 \x01(\x0b\x32\x11.Util.FaultReportH\x00\x12\x46\n\x14get_version_info_rep\x18\x14 \x01(\x0b\x32&.TblServiceModeProto.GetVersionInfoRepH\x00\x12N\n\x18get_emulation_status_rep\x18\x15 \x01(\x0b\x32*.TblServiceModeProto.GetEmulationStatusRepH\x00\x42\x05\n\x03Msg*8\n\x0cPositionMode\x12\x13\n\x0f\x41\x42SOLUTE_MOTION\x10\x00\x12\x13\n\x0fRELATIVE_MOTION\x10\x01*\xb7\x02\n\x0c\x41utoCalStage\x12\x1a\n\x16START_AUTO_CALIBRATION\x10\x00\x12\x19\n\x15\x43ONFIRM_SAFTY_WARNING\x10\x01\x12 \n\x1c\x43ONFIRM_MOVE_TO_LASER_CENTER\x10\x02\x12\x13\n\x0fSTART_TO_B_SIDE\x10\x03\x12\x10\n\x0cREACH_B_SIDE\x10\x04\x12\x13\n\x0fSTART_TO_A_SIDE\x10\x05\x12\x10\n\x0cREACH_A_SIDE\x10\x06\x12\x13\n\x0fSTART_TO_CENTER\x10\x07\x12\x10\n\x0cREACH_CENTER\x10\x08\x12\x18\n\x14SAVE_AUTO_CAL_RESULT\x10\t\x12\x19\n\x15\x41\x42ORT_AUTO_CAL_RESULT\x10\n\x12$\n AUTO_CAL_RESULT_PROCESS_COMPLETE\x10\x0b\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tblservicemode_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_POSITIONMODE']._serialized_start=7586
  _globals['_POSITIONMODE']._serialized_end=7642
  _globals['_AUTOCALSTAGE']._serialized_start=7645
  _globals['_AUTOCALSTAGE']._serialized_end=7956
  _globals['_REQ']._serialized_start=72
  _globals['_REQ']._serialized_end=342
  _globals['_STATE']._serialized_start=344
  _globals['_STATE']._serialized_end=423
  _globals['_UIMAW']._serialized_start=426
  _globals['_UIMAW']._serialized_end=630
  _globals['_UIMBW']._serialized_start=633
  _globals['_UIMBW']._serialized_end=837
  _globals['_HHCAW']._serialized_start=840
  _globals['_HHCAW']._serialized_end=1163
  _globals['_HHCBW']._serialized_start=1166
  _globals['_HHCBW']._serialized_end=1489
  _globals['_OW']._serialized_start=1492
  _globals['_OW']._serialized_end=1803
  _globals['_VERSIONINFO']._serialized_start=1806
  _globals['_VERSIONINFO']._serialized_end=2183
  _globals['_AUTOCALOPERATEREQ']._serialized_start=2185
  _globals['_AUTOCALOPERATEREQ']._serialized_end=2294
  _globals['_AUTOCALABORTREQ']._serialized_start=2296
  _globals['_AUTOCALABORTREQ']._serialized_end=2344
  _globals['_OPERATIONENABLEREQ']._serialized_start=2346
  _globals['_OPERATIONENABLEREQ']._serialized_end=2397
  _globals['_OPERATIONDISABLEREQ']._serialized_start=2399
  _globals['_OPERATIONDISABLEREQ']._serialized_end=2451
  _globals['_COUNTMOVEAXISREQ']._serialized_start=2454
  _globals['_COUNTMOVEAXISREQ']._serialized_end=2591
  _globals['_COUNTMOVEREQ']._serialized_start=2593
  _globals['_COUNTMOVEREQ']._serialized_end=2660
  _globals['_POSITIONMOVEAXISREQ']._serialized_start=2663
  _globals['_POSITIONMOVEAXISREQ']._serialized_end=2792
  _globals['_POSITIONMOVEREQ']._serialized_start=2794
  _globals['_POSITIONMOVEREQ']._serialized_end=2867
  _globals['_VELOCITYMOVEAXISREQ']._serialized_start=2869
  _globals['_VELOCITYMOVEAXISREQ']._serialized_end=2966
  _globals['_VELOCITYMOVEREQ']._serialized_start=2968
  _globals['_VELOCITYMOVEREQ']._serialized_end=3041
  _globals['_SERVICESHIFTCORRECTIONREQ']._serialized_start=3044
  _globals['_SERVICESHIFTCORRECTIONREQ']._serialized_end=3206
  _globals['_SERVICEIEC61217ASUREQ']._serialized_start=3209
  _globals['_SERVICEIEC61217ASUREQ']._serialized_end=3355
  _globals['_FAULTLISTINITREQ']._serialized_start=3357
  _globals['_FAULTLISTINITREQ']._serialized_end=3375
  _globals['_FAULTHANDLEREQ']._serialized_start=3377
  _globals['_FAULTHANDLEREQ']._serialized_end=3479
  _globals['_GETVERSIONINFOREQ']._serialized_start=3481
  _globals['_GETVERSIONINFOREQ']._serialized_end=3500
  _globals['_GETEMULATIONSTATUSREQ']._serialized_start=3502
  _globals['_GETEMULATIONSTATUSREQ']._serialized_end=3525
  _globals['_AUTOCALOPERATEREP']._serialized_start=3527
  _globals['_AUTOCALOPERATEREP']._serialized_end=3581
  _globals['_AUTOCALABORTREP']._serialized_start=3583
  _globals['_AUTOCALABORTREP']._serialized_end=3635
  _globals['_OPERATIONENABLEREP']._serialized_start=3637
  _globals['_OPERATIONENABLEREP']._serialized_end=3692
  _globals['_OPERATIONDISABLEREP']._serialized_start=3694
  _globals['_OPERATIONDISABLEREP']._serialized_end=3750
  _globals['_COUNTMOVEREP']._serialized_start=3752
  _globals['_COUNTMOVEREP']._serialized_end=3801
  _globals['_POSITIONMOVEREP']._serialized_start=3803
  _globals['_POSITIONMOVEREP']._serialized_end=3855
  _globals['_VELOCITYMOVEREP']._serialized_start=3857
  _globals['_VELOCITYMOVEREP']._serialized_end=3909
  _globals['_SERVICESHIFTCORRECTIONREP']._serialized_start=3911
  _globals['_SERVICESHIFTCORRECTIONREP']._serialized_end=3973
  _globals['_SERVICEIEC61217ASUREP']._serialized_start=3975
  _globals['_SERVICEIEC61217ASUREP']._serialized_end=4033
  _globals['_FAULTLISTINITREP']._serialized_start=4035
  _globals['_FAULTLISTINITREP']._serialized_end=4090
  _globals['_FAULTHANDLEREP']._serialized_start=4092
  _globals['_FAULTHANDLEREP']._serialized_end=4143
  _globals['_GETVERSIONINFOREP']._serialized_start=4145
  _globals['_GETVERSIONINFOREP']._serialized_end=4220
  _globals['_GETEMULATIONSTATUSREP']._serialized_start=4222
  _globals['_GETEMULATIONSTATUSREP']._serialized_end=4267
  _globals['_SERVICEAXISSTATUS']._serialized_start=4270
  _globals['_SERVICEAXISSTATUS']._serialized_end=4557
  _globals['_SERVICESTATUSPUSH']._serialized_start=4559
  _globals['_SERVICESTATUSPUSH']._serialized_end=4632
  _globals['_AUTOCALSTATUSPUSH']._serialized_start=4634
  _globals['_AUTOCALSTATUSPUSH']._serialized_end=4758
  _globals['_DIAGNOSISINFOPUSH']._serialized_start=4761
  _globals['_DIAGNOSISINFOPUSH']._serialized_end=5098
  _globals['_SERVERRX']._serialized_start=5101
  _globals['_SERVERRX']._serialized_end=6182
  _globals['_SERVERTX']._serialized_start=6185
  _globals['_SERVERTX']._serialized_end=7584
# @@protoc_insertion_point(module_scope)
