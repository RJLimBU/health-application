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

#### Web Module(restAPI)

The web module gets data from device module then display the data in html format. The APIs are deploy to 
Google Cloud Platform. 

There are three functions in the restAPI: get, post, delete

get: retrieve data 
post: output data retrieved from get
delete: this function will implement in the future, it will delete data that contain null

#### Chat Module

The chat module use document-database to store chat information

The module have input data with certain format feed to chat module and it return a dataset as output

The following section show formats for input data and output data

##### Input Data

```python
{
	user_id: int
	sender: str #username of current user
	recipient: str #id of recipient
	messageType: {text,voice,image,video}
	content: str

}
```

##### Output Data

output data have four types: text, voice, image, video

```python
#text message
{
	user_id: int	
	sender: str		#username of the sender
	recipient: str	#id of receiver
	date: str	# date of message sent
	time: str # time of message sent
	messageType: str # type of messages
	cotent: {
		msg: str	# content
		link: str	# for text message link will be empty
	}
}

#voice message
{
	user_id: int	
	sender: str		#username of the sender
	recipient: str	#id of receiver
	date: str	# date of message sent
	time: str # time of message sent
	messageType: str # type of messages
	cotent: {
		msg: str	# for voice message link is empty
		link: str	# link of voice
	}
}

#image message
{
	user_id: int	
	sender: str		#username of the sender
	recipient: str	#id of receiver
	date: str	# date of message sent
	time: str # time of message sent
	messageType: str # type of messages
	cotent: {
		msg: str	# for image message link is empty
		link: str	# link of image
	}
}
# video message
{
	user_id: int	
	sender: str		#username of the sender
	recipient: str	#id of receiver
	date: str	# date of message sent
	time: str # time of message sent
	messageType: str # type of messages
	cotent: {
		msg: str	# for video message link is empty
		link: str	# link of video
	}
}
```
