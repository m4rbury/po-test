import csv
import numpy as np

style, name, size, color, quantity, price, cost = np.loadtxt('test-csv.csv', delimiter=',', unpack=True, dtype='str')

x=0
saveFile = open('test-replace.csv', 'w')

for eachStyle in style:
	saveLine = eachStyle[1:] + '_' + color[x][1:] + '_' + size[x][1:] + '\n'
	x = x + 1
	print(saveLine)
	saveFile.write(saveLine)