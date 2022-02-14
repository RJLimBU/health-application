# skeleton code of device API

class DeviceInfo(NamedTuple):
	name: str
	deviceType: str
	data: list

class Status(NamedTuple):
	success: bool
	error: str

def readData(deviceInfo, key):
	if deviceInfo is None:
		return Status(success=False, error="No Device Info")

	if Type(key) is not str:
		return Status(success=False, error="incorrect api Key")

	if type(deviceInfo.data) is not list:
		return Status(success=False, error="No Data Found")

	return Status(success=True, error="")

