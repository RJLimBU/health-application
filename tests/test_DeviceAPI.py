import deviceAPI
from deviceAPI import readData

def test_deviceapi1:
	bloodDevice = DeviceInfo("bloodPressureMachine","blood_pressure_device", [120])
	key = "4329018"

	status = readData(bloodDevice, key)

	assert status.success == True and status.error == ""

def test_deviceapi2:
	bloodDevice = DeviceInfo("bloodPressureMachine","blood_pressure_device", [120])
	key = 4329018

	status = readData(bloodDevice,key)

	assert status.success == False and status.error == "Incorrect api Key"