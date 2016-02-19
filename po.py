import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = open("AA.html")
bsObj = BeautifulSoup(html)
bsObj.prettify()

table = bsObj.findAll("table", {"width":"556"})[0]
rows = table.findAll("tr")
csvFile = open("test.csv", 'wt')
writer = csv.writer(csvFile)
try:
	for row in rows:
		csvRow = []
		for cell in row.findAll(['td', 'th']):
			csvRow.append(cell.get_text(",", strip=True))
			writer.writerow(csvRow)
finally:
	csvFile.close()