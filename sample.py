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

client = LINE("EMAIL", "PASSWORD") #USE_YOUR_EMAIL_AND_PASSWORD
client.log("Auth Token : " + str(client.authToken))

poll = OEPoll(client)
mobflex = Mobanzu(client)
loop = asyncio.get_event_loop()

def allow_liff():
    url = 'https://access.line.me/dialog/api/permissions'
    data = {'on': ['P', 'CM'], 'off': []}
    headers = {
        'X-Line-Access': client.authToken,
        'X-Line-Application': client.server.APP_NAME,
        'X-Line-ChannelId': 'CHANNEL_ID', #USE_YOUR_CHANNEL_ID
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

def sendFlex(to, alt, flex):
    data = {"type": "flex", "altText": alt, "contents": flex}
    sendTemplate(to, data)

async def clientBot(op):
    try:
        if op.type == 0:
#            print("[ 0 ] END OF OPERATION")
            return
        if op.type == 26:
            print("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            id = msg.id
            to = msg.to
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != client.getProfile().mid: to = sender
                    else: to = receiver
                if msg.toType == 1 or msg.toType == 2: to = msg.to
                if msg.contentType == 0:
                    if None == msg.text: return
                    cmd = msg.text.lower()
                    if cmd == "allowliff":
                        try: allow_liff(); client.sendReplyMessage(id, to, "Access Granted For Flex Message.")
                        except: client.sendReplyMessage(id, to, "line://app/LIFF_ID?type=text&text=Done") #USE_YOUR_LIFF_ID
                    try:
                        if cmd == "help":
                            contact = client.getContact(sender)
                            name = contact.displayName
                            status = contact.statusMessage if contact.statusMessage != '' else ' '
                            try: picture = "https://obs.line-scdn.net/" + contact.pictureStatus
                            except: picture = "https://i.ibb.co/tczXyp1/hlth-Img-Not-Found.jpg"
                            sendFlex(to, "Help Menu", mobflex.helpMenu(picture, name, status))
                        if cmd == "profile": sendFlex(to, "Profile Menu", mobflex.profileMenu())
                        if cmd == "group": sendFlex(to, "Group Menu", mobflex.groupMenu())
                        if cmd == "media": sendFlex(to, "Media Menu", mobflex.mediaMenu())
                        if cmd == "service": sendFlex(to, "Service Menu", mobflex.serviceMenu())
                        if cmd == "system": sendFlex(to, "System Menu", mobflex.systemMenu())
                        if cmd == "forum": sendFlex(to, "Forum Menu", mobflex.forumMenu())
                    except: client.sendReplyMessage(id, to, "Access LIFF Required\nPlease Type 'Allowliff' First.")
    except Exception as error: print(error)

def run():
    while True:
        try:
            ops = poll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                    loop.run_until_complete(clientBot(op))
                    poll.setRevision(op.revision)
        except Exception as error: print(error)

if __name__ == "__main__":
    run()
