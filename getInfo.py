import requests
from bs4 import BeautifulSoup
import time

class GetInfo:

	def __init__(self, city_name):
		self.city_name = city_name

	def get(self):
		for i in range(1, 50):
			link = 'https://' + self.city_name + '.anjuke.com/sale/p' + str(i)
			print("第%s页" % (i))
			headers = {
				'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
				'cookie': 'aQQ_ajkguid = B82CD8F3 - 8203 - 2DD7 - B034 - 4215E7360E73;twe = 2;sessid = 73FB6C0A - DCDA - 8D40 - 7F6B - 85CB51CCCD44;_ga = GA1.2.198050355.1520347278;58tj_uuid = 3c2dd2d0 - c288 - 431b - 8a63 - 5c032c4c39fb;als = 0;ctid = 31;new_uv = 3;__xsptplus8 = 8.3.1520507634.1520507634.1 % 234 % 7C % 7C % 7C % 7C % 7C % 23 % 23NwR64eIUCj5ZWiEBB0qBm7U_KmmQerQu % 23'

			}

			r = requests.get(link, headers = headers)

			soup = BeautifulSoup(r.text, "html.parser")
			house_list = soup.find_all('li', class_="list-item")

			list = []

			for house in house_list:
				name = house.find('div', class_='house-title').a.text.strip()
				price = house.find('span', class_='price-det').text.strip()
				price_area = house.find('span', class_='unit-price').text.strip()

				no_room = house.find('div', class_='details-item').span.text
				area = house.find('div', class_='details-item').contents[3].text
				floor = house.find('div', class_='details-item').contents[5].text
				year = house.find('div', class_='details-item').contents[7].text
				broker = house.find('span', class_='brokername').text
				broker = broker[1:]
				address = house.find('span', class_='comm-address').text.strip()
				address = address.replace('\xa0\xa0\n           ', '  ')
				tag_list = house.find_all('span', class_='item-tags')
				tags = [i.text for i in tag_list]


				print(name, price, price_area, no_room, area, floor, year, broker, address, tags)
				dict = {'name': name, 'price': price, 'no_room': no_room, 'area': area, 'floor': floor, 'year': year, 'broker': broker, 'address': address, 'tags': tags}

				list.append(dict)

		time.sleep(5)

		return list