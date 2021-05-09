import csv
from PIL import ImageColor

# with open('thecollector.csv', 'r') as dataset:
# 	reader = csv.reader(dataset)
# 	for row in reader:
# 		print(row)

var = ImageColor.getcolor('#23a9dd', "RGB")
print(var)