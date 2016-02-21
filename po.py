import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = open("AA.html")
bsObj = BeautifulSoup(html)

table = bsObj.findAll("table", {"width":"556"})[0]
rows = table.findAll("tr")
cells = table.findAll("td")

csvFile = open("test.csv", 'wt')
writer = csv.writer(csvFile)

try:
	#for row in rows:
		for cell in cells:
			rowArray = []
			cellContent = (cell.get_text(",", strip=True))
			cellContent = cellContent.replace("", "")
			cellContent = cellContent.replace("\t", "").replace("\r", "").replace("\n", "")
			print(cellContent)
			rowArray.append(cellContent)
			writer.writerow(rowArray)

finally:
	csvFile.close()