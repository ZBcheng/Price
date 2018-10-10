from getInfo import GetInfo
import matplotlib.pyplot as plt

if __name__ == "__main__":
	Xian = GetInfo("xian")

	info = []
	for item in Xian.get():
		list = []
		area = item['area'].split('m')
		price = item['price'].split('万')
		list.append(float(area[0]))
		list.append(float(price[0]))
		info.append(list)

	for item in info:
		plt.scatter(item[0], item[1], color = 'blue', alpha=0.5)
		plt.xlabel('area')
		plt.ylabel('price')

	plt.show()
