import csv
import numpy as np

style, name, size, color, quantity, price, cost = np.loadtxt('test-csv.csv', delimiter=',', unpack=True, dtype='str')

x=0
saveFile = open('test-replace.csv', 'w')

for eachStyle in style:
	saveLine = eachStyle[1:].strip("\'") + '_' + color[x][1:].strip("\'") + '_' + size[x][1:].strip("\'") + ',' + quantity[x][1:].strip("\'") + '\n'
	x = x + 1
	print(saveLine)
	saveFile.write(saveLine)