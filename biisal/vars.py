# (c) adarsh-goel (c) @biisal
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = "Bɪɪsᴀʟ Fɪʟᴇ2Lɪɴᴋ Bᴏᴛ"
bisal_channel = "https://telegram.me/bisal_files"
bisal_grp = "https://t.me/+PA8OPL2Zglk3MDM1"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', 'YOUR_API_ID'))
    API_HASH = str(getenv('API_HASH', 'YOUR_API_HASH'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , 'YOUR_BOT_TOKEN'))
    name = str(getenv('name', 'bisal_file2link_bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', 'A PRIVATE CHANNEL ID'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', 'A PRIVATE CHANNEL ID TO GET NEW USERS NOTIF.'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "YOUR ID").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'YOUR_USERNAME WITHOUT @'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'YOUR MONGO DB URL'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'YOUR PUBLIC CHANNEL USERNAME WITHOUT @')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "THE CHANNEL ID THAT YOU WANT TO BAN")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "SAME AS BANNED CHANNELS")).split()))   
    