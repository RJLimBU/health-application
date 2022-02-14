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
deviceInfo data:
name                      type              description
deviceInfo.name           string      describes name of the input device
deviceInfo.deviceType     string      describes type of the input device
deviceInfo.data           list        stores parameters of measurements

device key:
name        type              descritopn <br />
key         string          key for the patient's account <br />
```
##### Output data

```python
status data:
name                      type              description <br />
status.success            boolean           return ture if read data successfully otherwise return false <br />
status.error              string            description of the error <br />
```

##### Example
```python
#Input:

deviceInfo.name = "bloodPressureMachine"
deviceInfo.type = "blood_pressure_device"
deviceInfo.data = [120]
key = "feh27889#"

readData(deviceInfo, key) <br />

#Output:

status.success = True <br />
status.error = "" <br />
```



