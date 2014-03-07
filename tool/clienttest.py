﻿#coding:utf-8

import time

from socket import AF_INET,SOCK_STREAM,socket
from thread import start_new
import struct,json
HOST='127.0.0.1'
PORT=11009
BUFSIZE=1024
ADDR=(HOST , PORT)
client = socket(AF_INET,SOCK_STREAM)
client.connect(ADDR)

def sendData(sendstr,commandId):
    """78,37,38,48,9,0"""
    HEAD_0 = chr(78)
    HEAD_1 = chr(37)
    HEAD_2 = chr(38)
    HEAD_3 = chr(48)
    ProtoVersion = chr(9)
    ServerVersion = 0
    sendstr = sendstr
    data = struct.pack('!sssss3I',HEAD_0,HEAD_1,HEAD_2,\
                       HEAD_3,ProtoVersion,ServerVersion,\
                       len(sendstr)+4,commandId)
    senddata = data+sendstr
    return senddata

def resolveRecvdata(data):
    head = struct.unpack('!sssss3I',data[:17])
    lenght = head[6]
    data = data[17:17+lenght]
    return data


def login():#登录
    client.sendall(sendData(json.dumps({"username":"psyko","password":"7141283"}),101))
    print resolveRecvdata(client.recv(1024))

def create():#创角
    client.sendall(sendData(json.dumps({"userId":1926,"rolename":"chekwind"}),102))
    print resolveRecvdata(client.recv(1024))

def rolelogin():#角色登录
    client.sendall(sendData(json.dumps({"userId":1927,"characterId":1000012}),103))
    print resolveRecvdata(client.recv(1024))
    
def sendmail():#发邮件
    client.sendall(sendData(json.dumps({"pname":"chekwind","characterId":1000012,"title":"测试","content":"邮件测试"}),502))
    print resolveRecvdata(client.recv(1024))

def playerlist():#获取球员列表
    client.sendall(sendData(json.dumps({"characterId":1000012}),401))
    print resolveRecvdata(client.recv(1024))

def roleinfo():#获取角色信息
    client.sendall(sendData(json.dumps({"characterId":1000012}),105))
    print resolveRecvdata(client.recv(1024))

def playertraining():#球员训练
    client.sendall(sendData(json.dumps({"characterId":1000012,'playerid':17,'shoot':149,'dribbling':99,'speed':100,'pass':98,'tackle':72,'tackling':78,'save':53,'response':53,'trainpoint':100}),402))
    print resolveRecvdata(client.recv(1024))

def addplayerexp():#球员加经验
    client.sendall(sendData(json.dumps({"characterId":1000012,'playerid':1,'exp':100}),403))
    print resolveRecvdata(client.recv(1024))

def addplayer():#签约球员
    client.sendall(sendData(json.dumps({"characterId":1000012,'templateId':10003}),405))
    print resolveRecvdata(client.recv(1024))

def dropplayer():#解雇球员
    client.sendall(sendData(json.dumps({"characterId":1000012,'playerId':12}),406))
    print resolveRecvdata(client.recv(1024))

def upgrade():#球员升级
    client.sendall(sendData(json.dumps({"characterId":1000012,'playerid':1,'gamecoin':0,'itemid':0}),404))
    print resolveRecvdata(client.recv(1024))

def packageinfo():#获取背包信息
    client.sendall(sendData(json.dumps({"characterId":1000012}),201))
    print resolveRecvdata(client.recv(1024))

def playerinner():#获取球员寻找信息
    client.sendall(sendData(json.dumps({"characterId":1000012}),407))
    print resolveRecvdata(client.recv(1024))

def pickplayer():#挑选球员
    client.sendall(sendData(json.dumps({"characterId":1000012,'picktype':1,'costpoint':10,'leagueindex':5}),408))
    print resolveRecvdata(client.recv(1024))

def dissmissplayer():
    client.sendall(sendData(json.dumps({"characterId":1000012,'playerId':16}),409))
    print resolveRecvdata(client.recv(1024))

def rotateplayer():
    client.sendall(sendData(json.dumps({"characterId":1000012,'mainPlayerId':1,'benchPlayerId':17}),410))
    print resolveRecvdata(client.recv(1024))

def calpower():
    client.sendall(sendData(json.dumps({"characterId":1000012}),106))
    print resolveRecvdata(client.recv(1024))

def getshopinfo():
    client.sendall(sendData(json.dumps({"characterId":1000012,'shopCategory':1}),701))
    print resolveRecvdata(client.recv(1024))

def buyitem():
    client.sendall(sendData(json.dumps({"characterId":1000012,'shopCategory':1,'itemId':1101,'buyNum':1}),702))
    print resolveRecvdata(client.recv(1024))

def gettask():
    client.sendall(sendData(json.dumps({"characterId":1000012}),801))
    print resolveRecvdata(client.recv(2048))

def committask():
    client.sendall(sendData(json.dumps({"characterId":1000012,"taskId":1001}),802))
    print resolveRecvdata(client.recv(2048))

def gettrainbase():
    client.sendall(sendData(json.dumps({"characterId":1000012}),1001))
    print resolveRecvdata(client.recv(2048))
    
login()
#create()
rolelogin()
#playertraining()
#calpower()
#addplayerexp()
# addplayer()
#sendmail()
#upgrade()
#packageinfo()
#dropplayer()
#pickplayer()
#dissmissplayer()
#rotateplayer()
#getshopinfo()
#buyitem()
#committask()
gettrainbase()

#playerlist()