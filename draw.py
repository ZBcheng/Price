from getInfo import GetInfo
import matplotlib.pyplot as plt

if __name__ == "__main__":
	item = GetInfo("xian")

	info = []
	for each in item.get():
		list = []
		area = each['area'].split('m')
		price = each['price'].split('万')
		list.append(float(area[0]))
		list.append(float(price[0]))
		info.append(list)

	for each in info:
		plt.scatter(each[0], each[1], color = 'blue', alpha = 0.5)
		plt.xlabel('area')
		plt.ylabel('price')

	plt.show()
