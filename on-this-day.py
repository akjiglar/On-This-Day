import requests
from bs4 import BeautifulSoup

date = input("Enter the date :- ")
month = input("Enter the month :- ")
url = 'https://www.onthisday.com/day/'+ month + '/' + date

r = requests.get(url)

html = r.text
soup = BeautifulSoup(html,'html.parser')

print(soup.title.text)


# Important Events

print()
print('Important Events')
print()

divs = soup.find_all('ul',class_='event-list event-list--with-advert')
for i in divs:
	print(i.text,end='')

# Famous birthdays

print()
print('Famous Birthdays')
print()

birthdays = soup.find('ul',class_='photo-list')
bdays = birthdays.find_all('li')
for i in bdays:
	print(i.text)

# This day in movies, music and sports

check = soup.find_all('section',class_='grid__item one-half--1024')
for i in check:
	print(i.text)


# Random fact on this day

did_you_know = soup.find('section',class_='section section--highlight section--did-you-know')
print(did_you_know.text)