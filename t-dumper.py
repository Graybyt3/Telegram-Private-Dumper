import asyncio
import json
import os
from telegram import Bot

"""
Graybyt3 - Ex-Blackhat | Ex Super Mod of Team_CC.
Now securing systems as a Senior Security Expert.
I hack servers for fun, patch them to torture you.

"My life is a lie, and i'm living in this only truth.- Graybyt3"

WARNING: This code is for educational and ethical purposes only.
I am not responsible for any misuse or illegal activities.

WARNING: Steal my code, and I'll call you Pappu — there's no worse shame in this world than being called Pappu.
#FuCk_Pappu
"""

BOT_TOKEN = "YOUR_API_ID"

'''' Get YOUR_API_ID from https://t.me/BotFather '''

async def fetch_updates(file_name):
    bot = Bot(token=BOT_TOKEN)
    try:
        await bot.delete_webhook()
        updates = await bot.get_updates()
        data = [update.to_dict() for update in updates]
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        me = await bot.get_me()
        print("\n\033[32m[+] BOT NAME : " + me.username + "\033[0m")
        print("\033[32m[+] DATA SUCCESSFULLY DUMPED INTO : " + file_name + "\033[0m")
        print("\033[32m[+] NUMBER OF MESSAGES DUMPED : " + str(len(updates)) + "\033[0m")
        print("\033[32m[+] FILE DUMPED : " + os.path.abspath(file_name) + "\033[0m\n\n\033[31mThank You for Using Grabyte T-dumper\nIf My Code Ever Helped You, Then Say Out Loud FUCK PAPPU\033[0m\n")
    except Exception as e:
        print("\033[31m[-] FUCK PAPPU  " + str(e) + "\033[0m")

async def main():
    print("\n\n")  
    print("\033[36m█▀▀ █▀█ ▄▀█ █▄█ █▄▄ █▄█ ▀█▀ █▀▀   ▀█▀ ▄▄ █▀▄ █░█ █▀▄▀█ █▀█ █▀▀ █▀█")
    print("\033[35m█▄█ █▀▄ █▀█ ░█░ █▄█ ░█░ ░█░ ██▄   ░█░ ░░ █▄▀ █▄█ █░▀░█ █▀▀ ██▄ █▀▄\033[0m")
    print("\n\n")  

    file_name = input("\033[32mEnter the File Name to Save as\nLeave It Blank to Use Default Name : \033[0m")
    if not file_name:
        file_name = "graybyte-tdumper.txt"

    await fetch_updates(file_name)

if __name__ == "__main__":
    asyncio.run(main())
