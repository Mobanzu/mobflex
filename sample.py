'''
┏━━━━━━━━━━━━━━━━━
┣ 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ.
┣ © 2020 ᴍᴏ-ʙᴀɴᴢᴜ
┗━━━━━━━━━━━━━━━━━
'''

from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from mobanzu import Mobanzu
import requests, uvloop, json, threading, asyncio, livejson

client = LINE("YOUR_EMAIL", "YOUR_PASSWORD")
client.log("Auth Token : " + str(client.authToken))

clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = OEPoll(client)
mobflex = Mobanzu(client)
clientMID = client.getProfile().mid
loop = asyncio.get_event_loop()

def allow_liff():
	url = 'https://access.line.me/dialog/api/permissions'
	data = {'on': ['P', 'CM'], 'off': []}
	headers = {
	    'X-Line-Access': client.authToken,
	    'X-Line-Application': client.server.APP_NAME,
	    'X-Line-ChannelId': 'CHANNEL_LIFF_ID', #USE_YOUR_CHANNEL_LIFF_ID
	    'Content-Type': 'application/json'
	}
	requests.post(url, json=data, headers=headers)

def sendTemplate(to, data):
    drex = LiffChatContext(to)
    mobz = LiffContext(chat=drex)
    view = LiffViewRequest('LIFF_ID', mobz) #USE_YOUR_LIFF_ID
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages": [data]}
    requests.post(url, headers=headers, data=json.dumps(data))

async def clientBot(op):
    try:
        if op.type == 0:
#            print ("[ 0 ] END OF OPERATION")
            return
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            id = msg.id
            to = msg.to
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != clientMID: to = sender
                    else: to = receiver
                if msg.toType == 1 or msg.toType == 2: to = msg.to
                if msg.contentType == 0:
                    if None == msg.text: return
                    cmd = msg.text.lower()
                    if cmd == "allowliff":
                        try:
                            allow_liff()
                            client.sendReplyMessage(id, to, "Access Granted For Flex Message.")
                        except: client.sendReplyMessage(id, to, "line://app/LIFF_ID?type=text&text=Done") #USE_YOUR_LIFF_ID
                    try:
                        if cmd == "help":
                            contact = client.getContact(sender)
                            name = contact.displayName
                            status = contact.statusMessage if contact.statusMessage != '' else 'Unknown'
                            try: picture = "https://obs.line-scdn.net/" + contact.pictureStatus
                            except: picture = "https://i.ibb.co/tczXyp1/hlth-Img-Not-Found.jpg"
                            mobflex.helpMenu(to, picture, name, status)
                        if cmd == "profile": mobflex.profileMenu(to)
                        if cmd == "group": mobflex.groupMenu(to)
                        if cmd == "media": mobflex.mediaMenu(to)
                        if cmd == "service": mobflex.serviceMenu(to)
                        if cmd == "system": mobflex.systemMenu(to)
                        if cmd == "forum": mobflex.forumMenu(to)
                    except: client.sendReplyMessage(id, to, "Access LIFF Required\nPlease Type 'Allowliff' First.")
    except Exception as error: print(error)

def run():
    while True:
        try:
            ops = clientPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                    loop.run_until_complete(clientBot(op))
                    clientPoll.setRevision(op.revision)
        except Exception as error: print(error)

if __name__ == "__main__":
    run()
