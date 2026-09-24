# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client
from pyrogram.types import BotCommand
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION, LOGIN_SYSTEM

if STRING_SESSION is not None and LOGIN_SYSTEM == False:
	TechVJUser = Client("TechVJ", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
	TechVJUser.start()
else:
    TechVJUser = None

class Bot(Client):

    def __init__(self):
        super().__init__(
            "techvj login",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="TechVJ"),
            workers=150,
            sleep_threshold=5
        )


	async def start(self):
    await super().start()

    await self.set_bot_commands([
        BotCommand("start", "CHECK I'M ALIVE"),
        BotCommand("help", "HELP MENU"),
        BotCommand("batch", "DOWNLOAD MULTIPLE POST AT A TIME"),
        BotCommand("settings", "CUSTOMIZE YOUR SETTINGS"),
        BotCommand("login", "LOGIN YOUR ACCOUNT"),
        BotCommand("logout", "LOGOUT YOUR ACCOUNT"),
        BotCommand("set_thumb", "SET YOUR THUMBNAIL"),
        BotCommand("view_thumb", "VIEW YOUR THUMBNAIL"),
        BotCommand("del_thumb", "DELETE YOUR THUMBNAIL"),
        BotCommand("set_caption", "SET CUSTOM CAPTION"),
        BotCommand("see_caption", "SEE CUSTOM CAPTION"),
        BotCommand("del_caption", "DELETE CUSTOM CAPTION"),
        BotCommand("setchat", "SET YOUR CHANNEL"),
        BotCommand("remchat", "DELETE YOUR CHANNEL"),
        BotCommand("cancel", "CANCEL ONGOING TASK"),
        BotCommand("broadcast", "BROADCAST MESSAGE (OWNER ONLY)")
    ])

    print("Bot Started Powered By @VJ_Bots")
    

    async def stop(self, *args):

        await super().stop()
        print('Bot Stopped Bye')

if __name__ == "__main__":
    bot = Bot()
    bot.run()

# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
