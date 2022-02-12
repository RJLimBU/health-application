# skeleton code of device API

class deviceInfo:
	name= ""
	deviceType= ""
	data= []

class status:
	success=True
	error=""

def readData(deviceInfo, status, key):
	if deviceInfo is None:
		status.success=False
		status.error = "No Device Info"

	if key is None:
		status.success=False
		status.error = "No Key Info"

	if type(deviceInfo.data) is not list:
		status.success=False
		status.error = "No Data Found"

	status.success=True
