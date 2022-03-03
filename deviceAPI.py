# skeleton code of device API
from collections import namedtuple
from typing import NamedTuple
import json

class DeviceInfo(NamedTuple):
	name: str
	deviceType: str
	unit: str
	data: list

# class Status(NamedTuple):
# 	success: bool
# 	error: str

apiKey = [
	"903810847",
	"890183781",
	"812321901",
	"328948027",
	"438028901",
	"432901890"
]

checkUnit = {
	"thermometer": ("C", "F"),
	"pulse": ("bpm"),
	"blood_pressure": ("mmHg"),
	"glucometer": ("mg/dL", "mmol/L")
}

def readData(filename, key):

	try:
		f = open(filename)
		data = json.load(f)
	except:
		#return Status(success=False, error="unable to load file")
		return {'error': "unable to load file"}

	if key not in apiKey:
		#return Status(success=False, error="Incorrect api Key")
		return {'error': "Incorrect api Key"}

	for device in data["devices"]:
		if device is None:
			#return Status(success=False, error="No Device Info")
			return {'error': "No Device Info"}

		if type(device["data"]) is not list:
			#return Status(success=False, error="No Data Found")
			return {'error': "No Data Found"}

		if type(device["unit"]) is not str:
			#return Status(success=False, error="unit not found")
			return {'error': "unit not found"}

		if device["type"] == "thermometer":
			if device["unit"] not in checkUnit["thermometer"]:
				#return Status(success=False, error="Incorrect thermometer unit")
				return {'error': "Incorrect thermometer unit"}
		elif device["type"] == "pulse":
			if device["unit"] not in checkUnit["pulse"]:
				#return Status(success=False, error="Incorrect pulse unit")
				return {'error': "Incorrect pulse unit"}
		elif device["type"] == "blood_pressure":
			if device["unit"] not in checkUnit["blood_pressure"]:
				#return Status(success=False, error="Incorrect blood_pressure unit")
				return {'error': "Incorrect blood_pressure unit"}
		elif device["type"] == "glucometer":
			if device["unit"] not in checkUnit["glucometer"]:
				#return Status(success=False, error="Incorrect glucometer unit")
				return {'error': "Incorrect glucometer unit"}

	#return Status(success=True, error="")
	return data


# out = readData("deviceinfo.json", "903810847")
# print(out)
# print(type(out))
