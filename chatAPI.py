import datetime
import json

def readMessage(content, mtype, user_id, sender, receiver):
	curtime = str(datetime.datetime.now())

	chatMessage = {
	'user_id': user_id, 
	'sender': sender, 
	'receiver': receiver, 
	'messageType': mtype,
	'time': curtime,
	'content': content
	}

	jstr = json.dumps(chatMessage, indent=4)

	return jstr


out = readMessage("Hello", "text", 1, "jack", "bob")
print(out)
print(type(out))
