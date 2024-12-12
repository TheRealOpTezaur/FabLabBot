import asyncio
import telegram

TOKEN = "7059496794:AAEBw5L60f6uM_dMtAGAt5M3SgSZiCHQK30"
chat_id = '-4784110072'

# Channel ID Sample: -1001829542722

bot = telegram.Bot(token=TOKEN)

async def send_message(text, chat_id):
    async with bot:
        await bot.send_message(text=text, chat_id=chat_id)

async def main():
    # Sending a message
    await send_message(text='Meaun la cabinet', chat_id=chat_id)

if __name__ == '__main__':
    asyncio.run(main())