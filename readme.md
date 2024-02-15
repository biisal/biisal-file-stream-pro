![GitHub contributors](https://img.shields.io/github/contributors/biisal/biisal-file-stream-pro?style=flat&color=green)
![GitHub repo size](https://img.shields.io/github/repo-size/biisal/biisal-file-stream-pro?color=green)
![GitHub](https://img.shields.io/github/license/biisal/biisal-file-stream-pro?color=green)

### Demo Bot

Here is our Demo bot -

[![Click Here](https://img.shields.io/badge/Demo%20Bot-Click%20Here-blue?style=flat&logo=telegram&labelColor=white&link=https://t.me/Bisal_Files_Talk)](https://t.me/Bisal_File2Link_Bot)

### Need Deployment Support?

If you encounter any issues deploying the bot, feel free to seek assistance in our support group:

[![Join Support Group](https://img.shields.io/badge/Join%20Support%20Group-Click%20Here-blue?style=flat&logo=telegram&labelColor=white&link=https://t.me/Bisal_Files_Talk)](https://t.me/Bisal_Files_Talk)



<h1 align="center"></h1>
<p align="center"> 
  <img src="https://wallpapercave.com/wp/wp12026024.jpg" alt="Cover Image" width="650">
  </a>
  
 <p align="center">
    A Telegram bot to turn all media and documents files to instant direct download and stream link .
    <br />
   </strong></a>
    <br />
    <a href="https://github.com/biisal/biisal-file-stream-pro/issues">Report a Bug</a>
    |
    <a href="https://github.com/biisal/biisal-file-stream-pro/issues">Request Feature</a>
  </p>


<hr>

## Project Discontinuation Notice and Disclaimer

**Please Note**:

This project has been discontinued and is no longer actively maintained or updated. As a result, it may contain outdated dependencies or potential security vulnerabilities.

**Disclaimer:**

This code is provided as-is, for educational purposes only, with no support or warranty. The developer is not liable for any legal consequences, damages, or issues that may arise from its use.

By using this code, you accept these terms and conditions, agreeing that all risks and responsibilities lie with you, the end user. Ensure the code's suitability for your needs before proceeding.

Feel free to use the existing code for educational or reference purposes, but be aware that it may not be suitable for production use without significant updates and improvements.

Thank you for your interest in this project, and we appreciate your understanding regarding its discontinuation.

<hr>

## 🍁 About This Bot :

![streamingfilestreambot-professional-live_1](https://t3.ftcdn.net/jpg/05/97/92/78/240_F_597927853_iZIpn7Blgg3TPd1XEKgF1KhLRuqNxhiU.jpg)

</p>
<p align='center'>
    This bot will give you streamable download links for Telegram files without the need of waiting till the download completes.
</p>


<br>
<details>
  <summary><b>Features:</b></summary>
  
<p>

🚀Features<p>
💥Superfast⚡️ download and stream links.<br>
💥No ads in generated links.<br>
💥Superfast interface.<br>
💥Along with the links you also get file information like name,size ,etc.<br>
💥Updates channel Support.<br>
💥Mongodb database support for broadcasting.<br>
💥Password Protection.<br>
💥User DC Check.<br>
💥Custom Domain support. <br>
💥All unwanted code removed. <br>
💥A lot more tired of writing check out by deploying it. 
</details>
  <details>
      <summary><b>Deploy to Heroku<b></summary>
      Click the button below to deploy the bot on Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/biisal/biisal-file-stream-pro)

  </details>
  <details>
  <summary><b>Deploy on Windows or other plataform<b></summary>
  
  You should make sure you have Python 3.6+ installed on your PC, then clone this repo and run the following commands in a terminal:

```py
git clone https://github.com/biisal/biisal-file-stream-pro
cd filestreambot-pro
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 -m biisal
```



and to stop the whole bot,
 do <kbd>CTRL</kbd>+<kbd>C</kbd>

 </details>
</details>
<details>
  <summary><b>Vars and Details :</b></summary>

Go to a file named `Vars.py` in the `biisal` Named File and add all the variables there.
An example of `Vars.py` file:

```py
API_ID=12345
API_HASH=esx576f8738x883f3sfzx83
BOT_TOKEN=Your_Bot_Token
BIN_CHANNEL=-100
PORT=8080
FQDN=your_server_ip
OWNER_ID=your_user_id
DATABASE_URL=mongodb_uri
```
`API_ID` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`API_HASH` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.
  
`BOT_TOKEN` : Get the bot token from [@BotFather](https://telegram.dog/BotFather)

`BIN_CHANNEL` : Create a new channel (private/public), add [@missrose_bot](https://telegram.dog/MissRose_bot) as admin to the channel and type /id. Now copy paste the ID into this field.
  
`OWNER_USERNAME` : U should be knowing it afterall it's your username dont remember it? just go to settings!

`OWNER_ID` : Your Telegram User ID

`DATABASE_URL` : MongoDB URI for saving User IDs when they first Start the Bot. We will use that for Broadcasting to them. I will try to add more features related with Database. If you need help to get the URI you can click on logo below!

[![mongo](https://telegra.ph/file/fd68906852c71fdd68bef.jpg)](https://www.youtube.com/watch?v=HhHzCfrqsoE)

 Option Vars

`UPDATES_CHANNEL` : Put a Public Channel Username, so every user have to Join that channel to use the bot. Must add bot to channel as Admin to work properly.

`BANNED_CHANNELS` : Put IDs of Banned Channels where bot will not work. You can add multiple IDs & separate with <kbd>Space</kbd>.

`SLEEP_THRESHOLD` : Set a sleep threshold for flood wait exceptions happening globally in this telegram bot instance, below which any request that raises a flood wait will be automatically invoked again after sleeping for the required amount of time. Flood wait exceptions requiring higher waiting times will be raised. Defaults to 60 seconds.

`WORKERS` : Number of maximum concurrent workers for handling incoming updates. Defaults to `3`

`PORT` : The port that you want your webapp to be listened to. Defaults to `8080`

`WEB_SERVER_BIND_ADDRESS` : Your server bind adress. Defauls to `0.0.0.0`

`NO_PORT` : If you don't want your port to be displayed. You should point your `PORT` to `80` (http) or `443` (https) for the links to work. Ignore this if you're on Heroku.

`FQDN` :  A Fully Qualified Domain Name if present. Defaults to `WEB_SERVER_BIND_ADDRESS` </details>

<details>
  <summary><b>How to Use :</b></summary>

:warning: **Before using the  bot, don't forget to add the bot to the `BIN_CHANNEL` as an Admin**
 
`/start` : To check if the bot is alive or not.

To get an instant stream link, just forward any media to the bot and boom, its 🚀🚀.
  
![image](https://i.postimg.cc/7hbFzd7X/20231212-235124.jpg)


### Channel Support
Bot also Supported with Channels. Just add bot Channel as Admin. If any new file comes in Channel it will edit it with **Get Download Link** Button. </details>

### Credits : 

- [Me](https://github.com/biisal)
- [Adarsh](https://github.com/adarsh-goel)
- Everyone In This Journey !
