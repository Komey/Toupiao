from django.shortcuts import render
from django.http import HttpResponse
from API.models import games as GAMES,users as USERS,rounds as ROUNDS
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def returnCode(code):

    val = {
        1001:'Unknow username',
        1002:'worng password',
        1003:'User name excepted',
        1004:'missing some part',
        2000:'Success',
    }
    msg = {}
    msg['error'] = code
    msg['message'] = val[code]
    return json.dumps(msg)
def returnMsg(msg):

    val = {}
    val['error'] = 2000
    val['message'] = msg
    return json.dumps(val)

#########username & password
@csrf_exempt
def login(request):

    UserName = request.REQUEST.get('username','')
    PassWord = request.REQUEST.get('password','')
    if UserName =='' or PassWord =='':
        return HttpResponse(returnCode(1004))#"{'error':1004,'message':'missing some part'}")
    try:
        info = USERS.objects.get(username = UserName)
        if info.password != PassWord:
            return HttpResponse(returnCode(1002))#"{'error':1002,'message':'worng password'}")
        else:
            UserInfo = info.user_info
            UserID = info.id
            val = {}
            
            data = {
                'userid':UserID,
                'userinfo':UserInfo,
            }
            
            return  HttpResponse(returnMsg(data))
    except:
        return HttpResponse(returnCode(1001))#"{'error':1001,'message':'Unknow username'}")

#########username password userinfo
@csrf_exempt
def signup(request):
    UserName = request.REQUEST.get('username','')
    PassWord = request.REQUEST.get('password','')
    UserInfo = request.REQUEST.get('userinfo','')
    if UserName =='' or PassWord =='':
        return HttpResponse(returnCode(1004))#"{'error':1004,'message':'missing some part'}")
    try:
        user = USERS.objects.get(username = UserName)
        return HttpResponse(returnCode(1003))#"{'error':1003,'message':'User name excepted'}")
    except:
        new_user = USERS(username = UserName,password = PassWord,user_info = UserInfo)
        new_user.save()
        return HttpResponse(returnCode(2000))#"{'error':2000,'message':'Success!'}")

######## userid userinfo
@csrf_exempt
def updateuserinfo(request):
    UserID = request.REQUEST.get('userid','')
    UserInfo = request.REQUEST.get('userinfo','')
    if UserID =='' or UserInfo =='':
        return HttpResponse(returnCode(1004))#"{'error':1004,'message':'missing some part'}")
    try:
        info = USERS.objects.get(id = int(UserID))
        info.user_info = UserInfo
        info.save()
        return HttpResponse(returnCode(2000))#"{'error':2000,'message':'Success!'}")
    except:
        return HttpResponse(returnCode(1001))#"{'error':1001,'message':'Unknow userid'}")

@csrf_exempt
def getuserinfo(request):
    UserID = request.REQUEST.get('userid','')
    if UserID =='':
        return HttpResponse(returnCode(1004))#"{'error':1004,'message':'missing some part'}")
    try:
        user = USERS.objects.get(id = int(UserID))
        return HttpResponse(returnMsg(user.user_info))#"{'error':2000,'message':'"+user.user_info+"'}")
    except:
        return HttpResponse(returnCode(1001))#"{'error':1001,'message':'Unknow userid'}")

######## userid password newpassword
@csrf_exempt
def changepassword(request):
    UserID = request.REQUEST.get('userid','')
    PassWord = request.REQUEST.get('password','')
    NewPassWord = request.REQUEST.get('newpassword','')
    if UserID =='' or PassWord =='' or NewPassWord == '':
        return HttpResponse(returnCode(1004))#"{'error':1004,'message':'missing some part'}")
    try:
        info = USERS.objects.get(id = int(UserID))
        if info.password != PassWord:
            return HttpResponse(returnCode(1002))#"{'error':1002,'message':'worng password'}")
        else:
            info.password = NewPassWord
            info.save()
            return HttpResponse(returnCode(2000))#"{'error':2000,'message':'Success!'}")
    except:
        return HttpResponse(returnCode(1001))#"{'error':1001,'message':'Unknow userid'}")

######## creategame?userid=1&gamename=&gameinfo=
@csrf_exempt
def creategame(request):
    UserID = request.REQUEST.get('userid','')
    GameName = request.REQUEST.get('gamename','')
    GameInfo = request.REQUEST.get('gameinfo','')
    if UserID ==''or GameName ==''or GameInfo =='':
        return HttpResponse("{'error':1004,'message':'missing some part'}")
    Game = GAMES(user_id = UserID,game_name = GameName,game_info = GameInfo)
    Game.save()
    return HttpResponse(returnCode(2000))#"{'error':2000,'message':'Success!'}")

######## deletegame?gameid=2
@csrf_exempt
def deletegame(request):
    GameID = request.REQUEST.get('gameid','')

    if GameID =='':
        return HttpResponse(returnCode(1004))#"{'error':1004,'message':'missing some part'}")
    try:
        Game = GAMES.objects.get(id = int(GameID))
        Game.delete()
        return HttpResponse(returnCode(2000))#"{'error':2000,'message':'Success!'}")
    except:
        return HttpResponse(returnCode(1000))#"{'error':1001,'message':'Unknow gameid'}")

######## getgames?userid=1
@csrf_exempt
def getgames(request):
    UserID = request.REQUEST.get('userid','')

    if UserID =='':
        return HttpResponse(returnCode(1004))#"{'error':1004,'message':'missing some part'}")
    try:
        Games = GAMES.objects.filter(user_id = UserID)
        
        game_list = []
        for g in Games:
            data = {
                'game_id':g.id,
                'game_name':g.game_name,
                'game_date':g.game_date.strftime('%Y-%m-%d %H:%M:%S'),
                'game_info':g.game_info
            }
            game_list.append(data)
        
        return HttpResponse(returnMsg(game_list))#json.dumps(val))
    except:
        return HttpResponse(returnCode(1001))#"{'error':1001,'message':'Unknow userid'}")

######## updategame?gameid=1&gamename=Hi&gameinfo=Test
@csrf_exempt
def updategame(request):
    GameID = request.REQUEST.get('gameid','')
    GameName = request.REQUEST.get('gamename','')
    GameInfo = request.REQUEST.get('gameinfo','')
    if GameID ==''or GameName ==''or GameInfo =='':
        return HttpResponse(returnCode(1004))#"{'error':1004,'message':'missing some part'}")
    try:
        Game = GAMES.objects.get(id = int(GameID))
        Game.game_info = GameInfo
        Game.game_name = GameName
        Game.save()
        return HttpResponse(returnCode(2000))#"{'error':2000,'message':'Success!'}")
    except:
        return HttpResponse(returnCode(1001))#"{'error':1001,'message':'Unknow gameid'}")

####### createround?gameid=1&roundname=first&roundinfo=nicai
@csrf_exempt
def createround(request):
    GameID = request.REQUEST.get('gameid','')
    RoundName = request.REQUEST.get('roundname','')
    RoundInfo = request.REQUEST.get('roundinfo','')
    if GameID ==''or RoundName ==''or RoundInfo =='':
        return HttpResponse(returnCode(1004))#"{'error':1004,'message':'missing some part'}")
    Round = ROUNDS(game_id = GameID,round_name = RoundName,round_info = RoundInfo)
    Round.save()
    return HttpResponse(returnCode(2000))#"{'error':2000,'message':'Success!'}")

###### deleteround?roundid=1
@csrf_exempt
def deleteround(request):
    RoundID = request.REQUEST.get('roundid','')

    if RoundID =='':
        return HttpResponse(returnCode(1004))#"{'error':1004,'message':'missing some part'}")
    try:
        Round = ROUNDS.objects.get(id = int(RoundID))
        Round.delete()
        return HttpResponse(returnCode(2000))#"{'error':2000,'message':'Success!'}")
    except:
        return HttpResponse(returnCode(1001))#"{'error':1001,'message':'Unknow gameid'}")

###### getrounds?gameid=1
@csrf_exempt
def getrounds(request):
    GameID = request.REQUEST.get('gameid','')

    if GameID =='':
        return HttpResponse(returnCode(1004))#"{'error':1004,'message':'missing some part'}")
    try:
        Rounds = ROUNDS.objects.filter(game_id = GameID)
        
        round_list = []
        for Round in Rounds:
            data = {
                'round_id':Round.id,
                'round_name':Round.round_name,
                'round_date':Round.round_date.strftime('%Y-%m-%d %H:%M:%S'),
                'round_info':Round.round_info
            }
            round_list.append(data)
        
        return HttpResponse(returnMsg(round_list))#json.dumps(val))
    except:
        return HttpResponse(returnCode(1001))#"{'error':1001,'message':'Unknow gameid'}")

##### updateround?roundid=1&roundname=HiFirst&roundinfo=this is first
@csrf_exempt
def updateround(request):
    RoundID = request.REQUEST.get('roundid','')
    RoundName = request.REQUEST.get('roundname','')
    RoundInfo = request.REQUEST.get('roundinfo','')
    if RoundID ==''or RoundName ==''or RoundInfo =='':
        return HttpResponse(returnCode(1004))#"{'error':1004,'message':'missing some part'}")
    try:
        Round = ROUNDS.objects.get(id = int(RoundID))
        Round.round_info = RoundInfo
        Round.round_name = RoundName
        Round.save()
        return HttpResponse(returnCode(2000))#"{'error':2000,'message':'Success!'}")
    except:
        return HttpResponse(returnCode(1001))#"{'error':1001,'message':'Unknow gameid'}")

import paho.mqtt.publish as publish
Hostname = "publish-lmh5257.myalauda.cn"
Port = 39664
######### sendmessage?topic=komey&message=hello
@csrf_exempt
def sendmessage(request):
    Topic = request.REQUEST.get('topic','')
    Message = request.REQUEST.get('message','')
    if Topic =='' or Message =='':
        return HttpResponse(returnCode(1004))#"{'error':1004,'message':'missing some part'}")
    publish.single(Topic, Message,qos=2, hostname=Hostname,port=Port)
    return HttpResponse(returnCode(2000))#"{'error':2000,'message':'Success!'}")


