import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 1993868)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(715779594)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1421493830:AAHXOUsr13aU2UYJAx1RIhMGG5hpmZd5XdU"
    DATABASE_URL = "postgres://ckukrcziykaejp:54e9272421b670c8a9359b65eb12fb3bc4914864788ee214693f25b21854d67c@ec2-54-205-248-255.compute-1.amazonaws.com:5432/d64pfa0kvkh6km"
    APP_ID = "1993868"
    API_HASH = "dfe61c1ca61637ba00e2d3454d28d937"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(715779594)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Force Group Members To Join a Specific Channel Vefore Sending Messages In The Group.\nI Will Mute Members If They Not Joined Your Channel and Tell Them To Join The Channel and Unmute Themselves By Pressing a Button.__",
        
        "**Setup**\n__First Of All Add Me In The Group as Admin With Ban Users Permission and In The Channel as Admin.\nNote: Only Creator Of The Group Can Setup Me and I Will Leave The Chat If I am Not an Admin In The Chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To Get The Current Settings.\n/ForceSubscribe no/off/disable - To Turn Off ForceSubscribe.\n/ForceSubscribe {channel username} - To Turn on And Setup The Channel.\n/ForceSubscribe Clear - To Unmute all Members Who Muted By Me.\n\nNote: /FSub Is An Alias Of /ForceSubscribe__",
        
        "**Developed by @MortalViking | @Ishwaranrudhara**"
      ]

      START_MSG = "**Hi, [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
