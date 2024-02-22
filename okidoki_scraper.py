import time
import asyncio
import requests
from telegram import Bot
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import config


# Telegram bot setup
BOT_TOKEN = config.BOT_TOKEN
CHAT_ID = config.CHAT_ID

# Get time
current_time = datetime.now()
formatted_current_time = current_time.strftime('%H:%M')
print("Current time:", formatted_current_time)

one_hour_ago = current_time - timedelta(hours=1, minutes=5)
formatted_one_hour_ago = one_hour_ago.strftime('%H:%M')
print("One hour and five minutes ago:", formatted_one_hour_ago)

url = 'https://www.okidoki.ee/buy/1601/?sort=2'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

def make_request(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    elif response.status_code == 403:
        print("Access Denied. Waiting before making the next request...")
        time.sleep(10)  # Wait for a while before trying again
        return make_request(url)
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None

page_content = make_request(url)

async def send_listings(bot, links):
    if links:
        message = "\n".join(links)
        await bot.send_message(chat_id=CHAT_ID, text=message)

async def main():
    bot = Bot(token=BOT_TOKEN)
    links = []

    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        listings = soup.find_all('li', class_='classifieds__item')

        for listing in listings:
            top_tag = listing.find('span', class_='offer-label__text')
            if top_tag and top_tag.text.strip() == "TOP":
                continue  # Skip listings with "TOP" tag

            listing_time_str = listing.find('span', class_='horiz-offer-card__date').text.strip()

            # Handle time format
            if "Täna" in listing_time_str:
                hours, minutes = map(int, listing_time_str.split(',')[1].strip().split(':'))
                listing_time = current_time.replace(hour=hours, minute=minutes)
            else:
                # Try to parse with the first format
                try:
                    listing_time = datetime.strptime(listing_time_str, "%d.%m.%Y %H:%M")
                except ValueError:
                    # Handle other time formats
                    # print(f"Skipping listing with unexpected time format: {listing_time_str}")
                    continue

            if listing_time < one_hour_ago:
                continue  # Skip listings older than the desired time range

            # Process and print the listing
            # title = listing.find('h3', class_='horiz-offer-card__title').text.strip()
            # price = listing.find('span', class_='horiz-offer-card__price-value').text.strip()
            # price = price.replace("\n", "").strip()  # Remove newline characters and extra spaces
            # location = listing.find('span', class_='horiz-offer-card__location').text.strip()
            # specs = listing.find_all('li', class_='horiz-offer-card__specs-item')

            # mileage = specs[0].text.strip() if len(specs) > 0 else "N/A"
            # fuel_type = specs[1].text.strip() if len(specs) > 1 else "N/A"
            # transmission = specs[2].text.strip() if len(specs) > 2 else "N/A"
            # body_type = specs[3].text.strip() if len(specs) > 3 else "N/A"

            link = listing.find('a', class_='horiz-offer-card__image-link')['href']
            links.append(f"https://www.okidoki.ee{link}")
                      
    await send_listings(bot, links)  # Send the accumulated links

            
            # print(f"https://www.okidoki.ee{link}")  # Print the link
            # async def send_listings(bot):
            #     await bot.send_message(chat_id=CHAT_ID, text=f"https://www.okidoki.ee{link}")

            # async def main():
            #     bot = Bot(token=BOT_TOKEN)
            #     await send_listings(bot)

if __name__ == "__main__":
    asyncio.run(main())

