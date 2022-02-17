# skeleton code of device API
from collections import namedtuple
from typing import NamedTuple
import json

class DeviceInfo(NamedTuple):
	name: str
	deviceType: str
	unit: str
	data: list

class Status(NamedTuple):
	success: bool
	error: str

apiKey = [
	"903810847",
	"890183781",
	"812321901",
	"328948027",
	"438028901",
	"432901890"
]

def readData(filename, key):

	try:
		f = open(filename)
		data = json.load(f)
	except:
		return Status(success=False, error="unable to load file")

	if key not in apiKey:
		return Status(success=False, error="Incorrect api Key")

	for device in data["devices"]:

		if device is None:
			return Status(success=False, error="No Device Info")

		if device["data"] is not list:
			return Status(success=False, error="No Data Found")

		if device["unit"] is None:
			return Status(success=False, error="unit not found")

	return Status(success=True, error="")
