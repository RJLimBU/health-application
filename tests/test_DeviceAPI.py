#import deviceAPI
from deviceAPI import *

def test_deviceapi1():
	#bloodDevice = DeviceInfo("bloodPressureMachine","blood_pressure_device", [120])
	key = "432901890"
	filename = "deviceinfo.json"

	status = readData(filename, key)

	assert status.success == True and status.error == ""

def test_deviceapi2():
	#bloodDevice = DeviceInfo("bloodPressureMachine","blood_pressure_device", [120])
	key = "4329018"
	filename = "deviceinfo.json"

	status = readData(filename,key)

	assert status.success == False and status.error == "Incorrect api Key"

def test_deviceapi3():
	key = "890183781"
	filename = "deviceinfo_f"

	status = readData(filename, key)

	assert status.success == False and status.error == "unit not found"
