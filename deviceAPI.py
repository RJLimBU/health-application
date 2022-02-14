# skeleton code of device API
from collections import namedtuple

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

	if type(key) is not str:
		return Status(success=False, error="Incorrect api Key")

	if type(deviceInfo.data) is not list:
		return Status(success=False, error="No Data Found")

	return Status(success=True, error="")

