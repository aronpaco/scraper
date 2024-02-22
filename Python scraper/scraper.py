import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    job_listings = soup.find_all('div', class_='card')

    for job in job_listings:
        title = job.find('h2', class_='title').text
        company = job.find('h3', class_='company').text
        location = job.find('p', class_='location').text
        print(f"Title: {title}\nCompany: {company}\nLocation: {location}\n{'='*20}")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
