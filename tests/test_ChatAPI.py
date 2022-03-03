from chatAPI import *
import json

def test_chatAPI1():
	user_id = 1
	sender = "joe"
	recipient = "doctor1"
	messageType = "text"
	content = "hello"
	data = readMessage(user_id, sender, recipient, messageType, content)
	chk = data.get('user_id',0)
	if chk:
		assert data['user_id'] == 1
		assert data['sender'] == "joe"
		assert data['recipient'] == "doctor1"
		assert data['messageType'] == "text"
		assert data['content']['msg'] == "hello"
		assert data['content']['link'] == None
	else:
		assert False

def test_chatAPI2():
	user_id = "1"
	sender = "joe"
	recipient = "doctor1"
	messageType = "text"
	content = "hello"
	data = readMessage(user_id, sender, recipient, messageType, content)
	chk = data.get('user_id', 0)
	if chk:
		assert False
	else:
		assert data['error'] == "incorrect user id format"

def test_chatAPI3():
	user_id = 2
	sender = "sam"
	recipient = "nurse"
	messageType = "test"
	content = "hello"
	data = readMessage(user_id, sender, recipient, messageType, content)
	chk = data.get('user_id', 0)
	if chk:
		assert False
	else:
		assert data['error'] == "message type must be text/voice/image/video"

def test_chatAPI3():
	user_id = 2
	sender = "sam"
	recipient = "nurse"
	messageType = "image"
	content = "/home/image.png"
	data = readMessage(user_id, sender, recipient, messageType, content)
	chk = data.get('user_id', 0)
	if chk:
		assert data['user_id'] == 2
		assert data['sender'] == "sam"
		assert data['recipient'] == "nurse"
		assert data['messageType'] == "image"
		assert data['content']['msg'] == None
		assert data['content']['link'] == "/home/image.png"
	else:
		assert False
