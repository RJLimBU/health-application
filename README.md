# Health Application

### Description

The health application monitor patients remotely. There are four types of users in <br />
the app: patients, medical professionals, administrators and developers. <br />



### Branch

main: This branch has the working verion of the program, <br />
code that is tested will merge to the main branch. <br />

testBranch: This branch has code that is still in the testing process, <br />
I will use this branch to experiment changes to the code. <br />

### Modules

#### Device Module

The device module will read data from different devices. (e.g. blood pressure, <br />
thermometer, pulse, etc.) 

##### Input data
```python
#device information (.json) 
#variable_name          type              description
#name           	string      	describes name of the input device
#type     		string      	describes type of the input device
#unit			string			specifiy unit of measurement
#data           	list        	stores parameters of measurements

#api key:
#variable_name        type              descritopn
#key         		string          key for the device api
```
##### Output data
```python
#status data(NamedTuple):
#name                      type              description 
#status.success            boolean           return ture if read data successfully otherwise return false
#status.error              string            description of the error
```

##### Example
```python
#Input:
{
	"devices" : [
	{
		"name": "bloodPressureMachine",
		"type": "blood_pressure_device",
		"unit": "mmHg",
		"data": [120]
	}
	]
}

readData(filename, key)

#Output:
{
	"devices" : [
	{
		"name": "bloodPressureMachine",
		"type": "blood_pressure_device",
		"unit": "mmHg",
		"data": [120]
	}
	]
}
```

##### Error condition
- unable to load json file
```python
status.success=False
status.error="unable to load file"
```
- No device information
```python
status.success=False
status.error = "No Device Info"
```
- Incorrect key information
```python
status.success=False
status.error = "Incorrect api Key"
```
- incorrect device data
```python
status.success=False
status.error = "No Data Found"
```
- No unit of measurement
```python
status.success=False
status.error = "unit not found"
```
- Incorrect unit
```python
status.success=False
status.error = "Incorrect unit"
```

#### Chat Module

The chat module use document-database to store chat messages and sql-database to store user ID.

```python
Chat database
{
user_id
message_id
sender
recipient
messageType:{text,voice,image,video}
time
file
text
}
```
