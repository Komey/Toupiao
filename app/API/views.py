from django.shortcuts import render
from django.http import HttpResponse
from API.models import games as GAMES,users as USERS,rounds as ROUNDS
import json
# Create your views here.

#########username & password
def login(request):

    UserName = request.REQUEST.get('username','')
    PassWord = request.REQUEST.get('password','')
    if UserName =='' or PassWord =='':
        return HttpResponse('{error:1004,maeeage:missing some part}')
    try:
        info = USERS.objects.get(username = UserName)
        if info.password != PassWord:
            return HttpResponse('{error:1002,maeeage:worng password}')
        else:
            UserInfo = info.user_info
            UserID = info.id
            val = {}
            val['error'] = 2000

            data = {
                'userid':UserID,
                'userinfo':UserInfo,
            }
            val['message'] = data
            return  HttpResponse(json.dumps(val))
    except:
        return HttpResponse('{error:1001,maeeage:Unknow username}')

#########username password userinfo
def signup(request):
    UserName = request.REQUEST.get('username','')
    PassWord = request.REQUEST.get('password','')
    UserInfo = request.REQUEST.get('userinfo','')
    if UserName =='' or PassWord =='':
        return HttpResponse('{error:1004,maeeage:missing some part}')
    try:
        user = USERS.objects.get(username = UserName)
        return HttpResponse('{error:1003,message:User name excepted}')
    except:
        new_user = USERS(username = UserName,password = PassWord,user_info = UserInfo)
        new_user.save()
        return HttpResponse('{error:2000,message:Success!}')

######## userid userinfo
def updateuserinfo(request):
    UserID = request.REQUEST.get('userid','')
    UserInfo = request.REQUEST.get('userinfo','')
    if UserID =='' or UserInfo =='':
        return HttpResponse('{error:1004,maeeage:missing some part}')
    try:
        info = USERS.objects.get(id = int(UserID))
        info.user_info = UserInfo
        info.save()
        return HttpResponse('{error:2000,message:Success!}')
    except:
        return HttpResponse('{error:1001,maeeage:Unknow userid}')

######## userid password newpassword
def changepassword(request):
    UserID = request.REQUEST.get('userid','')
    PassWord = request.REQUEST.get('password','')
    NewPassWord = request.REQUEST.get('newpassword','')
    if UserID =='' or PassWord =='' or NewPassWord == '':
        return HttpResponse('{error:1004,maeeage:missing some part}')
    try:
        info = USERS.objects.get(id = int(UserID))
        if info.password != PassWord:
            return HttpResponse('{error:1002,maeeage:worng password}')
        else:
            info.password = NewPassWord
            info.save()
            return HttpResponse('{error:2000,message:Success!}')
    except:
        return HttpResponse('{error:1001,maeeage:Unknow userid}')

######## creategame?userid=1&gamename=&gameinfo=
def creategame(request):
    UserID = request.REQUEST.get('userid','')
    GameName = request.REQUEST.get('gamename','')
    GameInfo = request.REQUEST.get('gameinfo','')
    if UserID ==''or GameName ==''or GameInfo =='':
        return HttpResponse('{error:1004,maeeage:missing some part}')
    Game = GAMES(user_id = UserID,game_name = GameName,game_info = GameInfo)
    Game.save()
    return HttpResponse('{error:2000,message:Success!}')

######## deletegame?gameid=2
def deletegame(request):
    GameID = request.REQUEST.get('gameid','')

    if GameID =='':
        return HttpResponse('{error:1004,maeeage:missing some part}')
    try:
        Game = GAMES.objects.get(id = int(GameID))
        Game.delete()
        return HttpResponse('{error:2000,message:Success!}')
    except:
        return HttpResponse('{error:1001,maeeage:Unknow gameid}')

######## getgames?userid=1
def getgames(request):
    UserID = request.REQUEST.get('userid','')

    if UserID =='':
        return HttpResponse('{error:1004,maeeage:missing some part}')
    try:
        Games = GAMES.objects.filter(user_id = UserID)
        val = {}
        val['error'] = 2000
        game_list = []
        for g in Games:
            data = {
                'game_id':g.id,
                'game_name':g.game_name,
                'game_date':g.game_date.strftime('%Y-%m-%d %H:%M:%S'),
                'game_info':g.game_info
            }
            game_list.append(data)
        val['message'] = game_list
        return HttpResponse(json.dumps(val))
    except:
        return HttpResponse('{error:1001,maeeage:Unknow userid}')

######## updategame?gameid=1&gamename=Hi&gameinfo=Test
def updategame(request):
    GameID = request.REQUEST.get('gameid','')
    GameName = request.REQUEST.get('gamename','')
    GameInfo = request.REQUEST.get('gameinfo','')
    if GameID ==''or GameName ==''or GameInfo =='':
        return HttpResponse('{error:1004,maeeage:missing some part}')
    try:
        Game = GAMES.objects.get(id = int(GameID))
        Game.game_info = GameInfo
        Game.game_name = GameName
        Game.save()
        return HttpResponse('{error:2000,message:Success!}')
    except:
        return HttpResponse('{error:1001,maeeage:Unknow gameid}')

####### createround?gameid=1&roundname=first&roundinfo=nicai
def createround(request):
    GameID = request.REQUEST.get('gameid','')
    RoundName = request.REQUEST.get('roundname','')
    RoundInfo = request.REQUEST.get('roundinfo','')
    if GameID ==''or RoundName ==''or RoundInfo =='':
        return HttpResponse('{error:1004,maeeage:missing some part}')
    Round = ROUNDS(game_id = GameID,round_name = RoundName,round_info = RoundInfo)
    Round.save()
    return HttpResponse('{error:2000,message:Success!}')

###### deleteround?roundid=1
def deleteround(request):
    RoundID = request.REQUEST.get('roundid','')

    if RoundID =='':
        return HttpResponse('{error:1004,maeeage:missing some part}')
    try:
        Round = ROUNDS.objects.get(id = int(RoundID))
        Round.delete()
        return HttpResponse('{error:2000,message:Success!}')
    except:
        return HttpResponse('{error:1001,maeeage:Unknow gameid}')

###### getrounds?gameid=1
def getrounds(request):
    GameID = request.REQUEST.get('gameid','')

    if GameID =='':
        return HttpResponse('{error:1004,maeeage:missing some part}')
    try:
        Rounds = ROUNDS.objects.filter(game_id = GameID)
        val = {}
        val['error'] = 2000
        round_list = []
        for Round in Rounds:
            data = {
                'round_id':Round.id,
                'round_name':Round.round_name,
                'round_date':Round.round_date.strftime('%Y-%m-%d %H:%M:%S'),
                'round_info':Round.round_info
            }
            round_list.append(data)
        val['message'] = round_list
        return HttpResponse(json.dumps(val))
    except:
        return HttpResponse('{error:1001,maeeage:Unknow gameid}')

##### updateround?roundid=1&roundname=HiFirst&roundinfo=this is first
def updateround(request):
    RoundID = request.REQUEST.get('roundid','')
    RoundName = request.REQUEST.get('roundname','')
    RoundInfo = request.REQUEST.get('roundinfo','')
    if RoundID ==''or RoundName ==''or RoundInfo =='':
        return HttpResponse('{error:1004,maeeage:missing some part}')
    try:
        Round = ROUNDS.objects.get(id = int(RoundID))
        Round.round_info = RoundInfo
        Round.round_name = RoundName
        Round.save()
        return HttpResponse('{error:2000,message:Success!}')
    except:
        return HttpResponse('{error:1001,maeeage:Unknow gameid}')

import paho.mqtt.publish as publish
Hostname = "mqtt-lmh5257.myalauda.cn"
Port = 10078
######### sendmessage?topic=komey&message=hello
def sendmessage(request):
    Topic = request.REQUEST.get('topic','')
    Message = request.REQUEST.get('message','')
    if Topic =='' or Message =='':
        return HttpResponse('{error:1004,maeeage:missing some part}')
    publish.single(Topic, Message,qos=2, hostname=Hostname,port=Port)
    return HttpResponse('{error:2000,message:Success!}')


