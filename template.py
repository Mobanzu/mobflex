'''
┏━━━━━━━━━━━━━━━━━
┣ 𐀀 HΞLLTΞRHΞΛD ᴄᴏʀᴘ.
┣ © 2020 ᴍᴏ-ʙᴀɴᴢᴜ
┗━━━━━━━━━━━━━━━━━
'''

class Mobanzu(object):
    def __init__(self, client):
        self.client = client

    def helpMenu(self, picture, name, status):
        data = {
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
                  "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=profile"
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
                  "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=group"
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
                  "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=media"
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
                  "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=service"
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
                  "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=system"
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
                  "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=forum"
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
              "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=profile"
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
              "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=group"
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
              "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=media"
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
              "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=service"
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
              "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=system"
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
              "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=forum"
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
}
        return data

    def profileMenu(self):
        data = {
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=timeline"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=steal"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=mymid"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=mybio"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=mypict"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=myvideo"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=mycover"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=mycontact"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=me"
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
}
        return data

    def groupMenu(self):
        data = {
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=mentionall"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=gid"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=gname"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=gpict"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=getid"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=memberlist"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=pendinglist"
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
}
        return data

    def mediaMenu(self):
        data = {
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=media:info"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=media:funny"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=media:search"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=media:result"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=media:social"
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
}
        return data

    def serviceMenu(self):
        data = {
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=token"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=broadcast"
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
}
        return data

    def systemMenu(self):
        data = {
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=debug"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=storage"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=speed"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=timeleft"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=about"
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
}
        return data

    def forumMenu(self):
        data = {
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=info"
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
                      "uri": "line://app/1655425084-3OQ8Mn9J?type=text&text=creator"
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
}
        return data
