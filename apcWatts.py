# https://download.schneider-electric.com/files?p_enDocType=Quick+start+guide&p_File_Name=990-9840B-EN.pdf&p_Doc_Ref=SPD_LFLG-A32G3L_EN

import time
from pyModbusTCP.client import ModbusClient
from utils import getConfig
from logger import logger

config = getConfig()
host = config['modbus']['host']
port = config['modbus']['port']
c = ModbusClient(host=host, port=port, unit_id=1, auto_open=True)

def getAmps():
  amps = c.read_holding_registers(140, 1)
  if amps:
    return amps[0] / 32
  else:
    return getAmps()

def getVolts():
  volts = c.read_holding_registers(142, 1)
  if volts:
    return volts[0] / 64
  else:
    return getVolts()

def watts():
  return getVolts() * getAmps()

while True:
  currentWatts = watts()
  print('Current power draw: {:.2f}W'.format(currentWatts))

  telemetry = { 'watts': currentWatts }

  logger.info("Current power draw", es=telemetry)
  time.sleep(1)

