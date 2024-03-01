import time
import asyncio
import requests
from telegram import Bot
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import config

print("Starting...")
BOT_TOKEN = config.BOT_TOKEN
CHAT_ID = config.CHAT_ID2


url_list = [
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=GqjPP2zRcEitEbsK4wsFXw',
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=QTpJ4JPuyk2TMdNpor368g',
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=cCSb7rnbxUuc8c-fFPza4A',
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=UIrAWbDNoUiM0jYwGPeT1g', 
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=IRCKUlg8SEm-QR85VmyJGQ', 
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=wq2mk2Rr-USjfTQOMih4VA', 
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=PivWTtBt20af-jjNHMn84Q', 
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=4cI9x9hRikuk3Eivye0liw',
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=FbQj0YAiVUWkAVvEVrI1zQ', 
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=r7EaVSiPLEeF82Oda_3RkA', 
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=h4JNMTB3uECSDmsGZkJc4g', 
    'https://broneering.transpordiamet.ee/make-reservation/select-time?ServiceId=vPK3ho0xI0-ucFWQOXF0Gw&BranchId=zYEtAFI_H0uAIfPAB0oEOw'
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
for url in url_list:

    def get_available_dates(url):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            available_dates = []

            clickable_days = soup.find_all('div', class_='day clickable')
            
            for day in clickable_days:
                date_text = day.get_text(strip=True)
                times = day['times'].split(';')
                available_times = [time.strip().split('|')[0] for time in times]
                date_number = int(date_text)

                if 8 <= date_number <= 11:
                    available_dates.append(f"UUED AJAD: {url}     September {date_text}: {'  ,  '.join(available_times)}")

                if available_dates:
                    break

            return available_dates
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return None

    async def main():
        bot = Bot(token=BOT_TOKEN)
        available_dates = get_available_dates(url)

        if available_dates:
            message = "\n".join(available_dates)
            await bot.send_message(chat_id=CHAT_ID, text=message)
            print("Dates sent")
        else:
            print("No available dates found")

    if __name__ == "__main__":
        asyncio.run(main())