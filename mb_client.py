import asyncio
import time
from threading import Thread
from pymodbus.client.asynchronous.tcp import AsyncModbusTCPClient as ModbusClient
from pymodbus.client.asynchronous import schedulers


UNIT = 0x01

