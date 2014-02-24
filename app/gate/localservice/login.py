#coding:utf8
'''
Created on 2014-1-17

@author: CC
'''

from app.gate.appinterface import login
import json
from app.gate.gateservice import localserviceHandle
from twisted.python import log


@localserviceHandle
def registerToServer_100(key,dynamicId,request_proto):
	'''账号注册'''
	argument=json.loads(request_proto)
	dynamicId=dynamicId
	username=argument.get('username')
	password=argument.get('password')
	data=login.registerToServer(dynamicId,username,password)
	return json.dumps(data)

@localserviceHandle
def loginToServer_101(key,dynamicId,request_proto):
	'''账号登录'''
	argument=json.loads(request_proto)
	dynamicId=dynamicId
	username=argument.get('username')
	password=argument.get('password')
	data=login.loginToServer(dynamicId,username,password)
	response={}
	_data=data.get('data')
	response['result']=data.get('result',False)
	responsedata={}
	response['data']=responsedata
	if _data:
		responsedata['userId']=_data.get('userId',0)
		responsedata['hasRole']=_data.get('hasRole',False)
		responsedata['characterId']=_data.get('defaultId',False)
	return json.dumps(response)

@localserviceHandle
def activeNewGamer_102(key,dynamicId,request_proto):
	'''创建角色'''
	argument=json.loads(request_proto)
	userId=argument.get('userId')
	nickName=argument.get('rolename')
	data=login.activeNewGamer(dynamicId,userId,nickName)
	return json.dumps(data)

def SerializePartialEnterScene(result,response):
	'''序列化进入场景的返回消息'''
	return json.dumps(result)

@localserviceHandle
def roleLogin_103(key,dynamicId,request_proto):
	'''角色登陆'''
	argument=json.loads(request_proto)
	userId=argument.get('userId')
	characterId=argument.get('characterId')
	data=login.roleLogin(dynamicId,userId,characterId)
	if not data.get('result'):
		return json.dumps(data)
	placeId=data['data'].get('placeId',1000)
	response={}
	dd=login.enterScene(dynamicId,characterId,placeId,True)
	if not dd:
		return
	dd.addCallback(SerializePartialEnterScene,response)
	return dd