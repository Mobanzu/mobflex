'''
┏━━━━━━━━━━━━━━━━━
┣ 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ.
┣ © 2020 ᴍᴏ-ʙᴀɴᴢᴜ
┗━━━━━━━━━━━━━━━━━
'''

from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
import requests, threading, json

class Mobanzu(threading.Thread):
    def __init__(self, client):
        self.client = client

    def sendTemplate(self, to, data):
        drex = LiffChatContext(to)
        mobz = LiffContext(chat=drex)
        view = LiffViewRequest('LIFF_ID', mobz) #USE_YOUR_LIFF_ID
        token = self.client.liff.issueLiffView(view)
        url = 'https://api.line.me/message/v3/share'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
        data = {"messages": [data]}
        requests.post(url, headers=headers, data=json.dumps(data))

    def helpMenu(self, to, picture, name, status):
        data = {
"type": "flex",
"altText": "Help Menu",
"contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": picture,
            "align": "center",
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "width": "70px",
        "height": "70px",
        "offsetStart": "50px",
        "offsetTop": "61px",
        "action": {
          "type": "uri",
          "label": "Profile",
          "uri": "line://nv/profilePopup/mid=u386d2ed45175a8d55b0f69db1d23e125"
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "P R O F I L E",
                  "uri": "line://app/LIFF_ID?type=text&text=profile" #USE_YOUR_LIFF_ID
                },
                "height": "sm",
                "style": "primary",
                "color": "#00ccff"
              }
            ],
            "height": "35px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "G R O U P",
                  "uri": "line://app/LIFF_ID?type=text&text=group" #USE_YOUR_LIFF_ID
                },
                "height": "sm",
                "style": "primary",
                "color": "#00ccff"
              }
            ],
            "height": "35px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "M E D I A",
                  "uri": "line://app/LIFF_ID?type=text&text=media" #USE_YOUR_LIFF_ID
                },
                "height": "sm",
                "style": "primary",
                "color": "#00ccff"
              }
            ],
            "height": "35px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "S E R V I C E",
                  "uri": "line://app/LIFF_ID?type=text&text=service" #USE_YOUR_LIFF_ID
                },
                "height": "sm",
                "style": "primary",
                "color": "#00ccff"
              }
            ],
            "height": "35px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "S Y S T E M",
                  "uri": "line://app/LIFF_ID?type=text&text=system" #USE_YOUR_LIFF_ID
                },
                "height": "sm",
                "style": "primary",
                "color": "#00ccff"
              }
            ],
            "height": "35px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "F O R U M",
                  "uri": "line://app/LIFF_ID?type=text&text=forum" #USE_YOUR_LIFF_ID
                },
                "height": "sm",
                "style": "primary",
                "color": "#00ccff"
              }
            ],
            "height": "35px"
          }
        ],
        "height": "230px",
        "width": "174px",
        "offsetStart": "62px",
        "spacing": "3.4px",
        "offsetTop": "81px"
      },
      {
        "type": "image",
        "url": "https://i.ibb.co/RN9p4z8/hlth-assault-menu.png",
        "align": "center",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1:1.5",
        "offsetBottom": "300.2px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": name,
                "weight": "bold",
                "align": "center",
                "size": "sm",
                "color": "#ffffff"
              }
            ],
            "height": "20px",
            "width": "114px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": status,
                "color": "#ffffff",
                "wrap": True,
                "size": "9px",
                "align": "center"
              }
            ],
            "width": "114px",
            "height": "24px",
            "offsetTop": "6px"
          }
        ],
        "height": "52px",
        "width": "114px",
        "offsetBottom": "665px",
        "offsetStart": "135px",
        "spacing": "2px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "height": "30px",
            "action": {
              "type": "uri",
              "label": "HELLTERHEAD Corp.",
              "uri": "line://nv/profilePopup/mid=u386d2ed45175a8d55b0f69db1d23e125"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "height": "30px",
            "margin": "110px",
            "action": {
              "type": "uri",
              "label": "Profile Button",
              "uri": "line://app/LIFF_ID?type=text&text=profile" #USE_YOUR_LIFF_ID
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "height": "30px",
            "margin": "8.2px",
            "action": {
              "type": "uri",
              "label": "Group Button",
              "uri": "line://app/LIFF_ID?type=text&text=group" #USE_YOUR_LIFF_ID
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "height": "30px",
            "margin": "8.2px",
            "action": {
              "type": "uri",
              "label": "Media Button",
              "uri": "line://app/LIFF_ID?type=text&text=media" #USE_YOUR_LIFF_ID
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "height": "30px",
            "margin": "8.2px",
            "action": {
              "type": "uri",
              "label": "Service Button",
              "uri": "line://app/LIFF_ID?type=text&text=service" #USE_YOUR_LIFF_ID
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "height": "30px",
            "margin": "8.2px",
            "action": {
              "type": "uri",
              "label": "System Button",
              "uri": "line://app/LIFF_ID?type=text&text=system" #USE_YOUR_LIFF_ID
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [],
            "height": "30px",
            "margin": "8.2px",
            "action": {
              "type": "uri",
              "label": "Forum Button",
              "uri": "line://app/LIFF_ID?type=text&text=forum" #USE_YOUR_LIFF_ID
            }
          }
        ],
        "height": "362px",
        "width": "175px",
        "offsetBottom": "780px",
        "offsetStart": "62px"
      }
    ],
    "paddingAll": "0px",
    "height": "434.2px"
  }
}}
        self.sendTemplate(to, data)

    def profileMenu(self, to):
        data = {
"type": "flex",
"altText": "Profile Menu",
"contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co/hFwjD39/hlth-background2nd.jpg",
        "align": "center",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1.4"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/vjsy27Y/hlth-2nd-Menu-top.png",
                "gravity": "top",
                "aspectMode": "fit",
                "size": "full",
                "aspectRatio": "4:1"
              }
            ],
            "height": "75px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "timeline",
                      "uri": "line://app/LIFF_ID?type=text&text=timeline" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "steal",
                      "uri": "line://app/LIFF_ID?type=text&text=steal" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "mymid",
                      "uri": "line://app/LIFF_ID?type=text&text=mymid" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "mybio",
                      "uri": "line://app/LIFF_ID?type=text&text=mybio" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "mypict",
                      "uri": "line://app/LIFF_ID?type=text&text=mypict" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "myvideo",
                      "uri": "line://app/LIFF_ID?type=text&text=myvideo" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "mycover",
                      "uri": "line://app/LIFF_ID?type=text&text=mycover" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "mycontact",
                      "uri": "line://app/LIFF_ID?type=text&text=mycontact" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "me",
                      "uri": "line://app/LIFF_ID?type=text&text=me" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "contact: <userid>",
                      "uri": "line://nv/profilePopup/mid=u386d2ed45175a8d55b0f69db1d23e125"
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "secondary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "spacer"
              }
            ],
            "backgroundColor": "#00ccff80",
            "width": "259.2px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/BfMJDDL/hlth-2nd-Menu-bottom.png",
                "gravity": "top",
                "aspectMode": "fit",
                "size": "full",
                "aspectRatio": "4:1"
              }
            ],
            "height": "75px"
          }
        ],
        "offsetBottom": "418px"
      }
    ],
    "paddingAll": "0px",
    "height": "418px"
  }
}}
        self.sendTemplate(to, data)

    def groupMenu(self, to):
        data = {
"type": "flex",
"altText": "Group Menu",
"contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co/hFwjD39/hlth-background2nd.jpg",
        "align": "center",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1.6"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/vjsy27Y/hlth-2nd-Menu-top.png",
                "gravity": "top",
                "aspectMode": "fit",
                "size": "full",
                "aspectRatio": "4:1"
              }
            ],
            "height": "75px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "mentionall",
                      "uri": "line://app/LIFF_ID?type=text&text=mentionall" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "gid",
                      "uri": "line://app/LIFF_ID?type=text&text=gid" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "gname",
                      "uri": "line://app/LIFF_ID?type=text&text=gname" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "gpict",
                      "uri": "line://app/LIFF_ID?type=text&text=gpict" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "getid",
                      "uri": "line://app/LIFF_ID?type=text&text=getid" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "memberlist",
                      "uri": "line://app/LIFF_ID?type=text&text=memberlist" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "pendinglist",
                      "uri": "line://app/LIFF_ID?type=text&text=pendinglist" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "getreader: <on|off>",
                      "uri": "line://nv/profilePopup/mid=u386d2ed45175a8d55b0f69db1d23e125"
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "secondary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "resendchat <on|off>",
                      "uri": "line://nv/profilePopup/mid=u386d2ed45175a8d55b0f69db1d23e125"
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "secondary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "spacer"
              }
            ],
            "backgroundColor": "#00ccff80",
            "width": "259.2px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/BfMJDDL/hlth-2nd-Menu-bottom.png",
                "gravity": "top",
                "aspectMode": "fit",
                "size": "full",
                "aspectRatio": "4:1"
              }
            ],
            "height": "75px"
          }
        ],
        "offsetBottom": "463px"
      }
    ],
    "paddingAll": "0px",
    "height": "463px"
  }
}}
        self.sendTemplate(to, data)

    def mediaMenu(self, to):
        data = {
"type": "flex",
"altText": "Media Menu",
"contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co/hFwjD39/hlth-background2nd.jpg",
        "align": "center",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1.3"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/vjsy27Y/hlth-2nd-Menu-top.png",
                "gravity": "top",
                "aspectMode": "fit",
                "size": "full",
                "aspectRatio": "4:1"
              }
            ],
            "height": "75px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "media:info",
                      "uri": "line://app/LIFF_ID?type=text&text=media:info" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "media:funny",
                      "uri": "line://app/LIFF_ID?type=text&text=media:funny" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "media:search",
                      "uri": "line://app/LIFF_ID?type=text&text=media:search" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "media:result",
                      "uri": "line://app/LIFF_ID?type=text&text=media:result" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "media:social",
                      "uri": "line://app/LIFF_ID?type=text&text=media:social" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "spacer"
              }
            ],
            "backgroundColor": "#00ccff80",
            "width": "259.2px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/BfMJDDL/hlth-2nd-Menu-bottom.png",
                "gravity": "top",
                "aspectMode": "fit",
                "size": "full",
                "aspectRatio": "4:1"
              }
            ],
            "height": "75px"
          }
        ],
        "offsetBottom": "375px"
      }
    ],
    "paddingAll": "0px",
    "height": "375px"
  }
}}
        self.sendTemplate(to, data)

    def serviceMenu(self, to):
        data = {
"type": "flex",
"altText": "Service Menu",
"contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co/hFwjD39/hlth-background2nd.jpg",
        "align": "center",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1.5:1"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/vjsy27Y/hlth-2nd-Menu-top.png",
                "gravity": "top",
                "aspectMode": "fit",
                "size": "full",
                "aspectRatio": "4:1"
              }
            ],
            "height": "75px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "token",
                      "uri": "line://app/LIFF_ID?type=text&text=token" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "broadcast",
                      "uri": "line://app/LIFF_ID?type=text&text=broadcast" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm"
              },
              {
                "type": "spacer"
              }
            ],
            "backgroundColor": "#00ccff80",
            "width": "259.2px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/BfMJDDL/hlth-2nd-Menu-bottom.png",
                "gravity": "top",
                "aspectMode": "fit",
                "size": "full",
                "aspectRatio": "4:1"
              }
            ],
            "height": "75px"
          }
        ],
        "offsetBottom": "198px"
      }
    ],
    "paddingAll": "0px",
    "height": "200px"
  }
}}
        self.sendTemplate(to, data)

    def systemMenu(self, to):
        data = {
"type": "flex",
"altText": "System Menu",
"contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co/hFwjD39/hlth-background2nd.jpg",
        "align": "center",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/vjsy27Y/hlth-2nd-Menu-top.png",
                "gravity": "top",
                "aspectMode": "fit",
                "size": "full",
                "aspectRatio": "4:1"
              }
            ],
            "height": "75px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "debug",
                      "uri": "line://app/LIFF_ID?type=text&text=debug" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "storage",
                      "uri": "line://app/LIFF_ID?type=text&text=storage" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "speed",
                      "uri": "line://app/LIFF_ID?type=text&text=speed" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "timeleft",
                      "uri": "line://app/LIFF_ID?type=text&text=timeleft" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "about",
                      "uri": "line://app/LIFF_ID?type=text&text=about" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "spacer"
              }
            ],
            "backgroundColor": "#00ccff80",
            "width": "259.2px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/BfMJDDL/hlth-2nd-Menu-bottom.png",
                "gravity": "top",
                "aspectMode": "fit",
                "size": "full",
                "aspectRatio": "4:1"
              }
            ],
            "height": "75px"
          }
        ],
        "offsetBottom": "287px"
      }
    ],
    "paddingAll": "0px",
    "height": "287px"
  }
}}
        self.sendTemplate(to, data)

    def forumMenu(self, to):
        data = {
"type": "flex",
"altText": "Forum Menu",
"contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co/hFwjD39/hlth-background2nd.jpg",
        "align": "center",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1.2:1"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/vjsy27Y/hlth-2nd-Menu-top.png",
                "gravity": "top",
                "aspectMode": "fit",
                "size": "full",
                "aspectRatio": "4:1"
              }
            ],
            "height": "75px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "info",
                      "uri": "line://app/LIFF_ID?type=text&text=info" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "creator",
                      "uri": "line://app/LIFF_ID?type=text&text=creator" #USE_YOUR_LIFF_ID
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "primary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "chatown: <text>",
                      "uri": "line://nv/profilePopup/mid=u386d2ed45175a8d55b0f69db1d23e125"
                    },
                    "height": "sm",
                    "color": "#0f222f60",
                    "style": "secondary"
                  }
                ],
                "width": "230px",
                "offsetStart": "14.5px",
                "spacing": "sm",
                "margin": "sm"
              },
              {
                "type": "spacer"
              }
            ],
            "backgroundColor": "#00ccff80",
            "width": "259.2px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/BfMJDDL/hlth-2nd-Menu-bottom.png",
                "gravity": "top",
                "aspectMode": "fit",
                "size": "full",
                "aspectRatio": "4:1"
              }
            ],
            "height": "75px"
          }
        ],
        "offsetBottom": "243px"
      }
    ],
    "paddingAll": "0px",
    "height": "243px"
  }
}}
        self.sendTemplate(to, data)
