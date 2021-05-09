import pandas as pd
from PIL import ImageColor


df = pd.read_csv('thecollector.csv')
# print(df)

#hexes = df['hexval']
# print(hexes)
#yelp = hexes[1].replace('\n','')
#print(yelp)
# print(len(yelp))

# print(yelp[0:7])
# newlist = []
# i = 1
# while i < len(yelp):
# 	newlist.append(yelp[i-1:i+6])
# 	i += 7

# print(newlist)
#print(len(hexes))


# ye = ImageColor.getrgb("#800800")
# print(ye)

def masshex(fivenum):
	newlist = []
	ilen = 1
	while ilen < len(fivenum):
		newlist.append(fivenum[ilen-1:ilen+6])
		ilen += 7

	retlist = []
	hue = 0
	while hue < 5:
		retlist.append(ImageColor.getrgb(str(newlist[hue])))
		hue += 1

	return retlist

def halfhex(singlenum):
	newlist = []
	ilen = 1
	while ilen < len(singlenum):
		newlist.append(singlenum[ilen-1:ilen+6])
		ilen += 7

	return newlist

halftest = halfhex(df['hexval'][0].replace('\n',''))
print(halftest)
#newone = masshex(yelp)
#print(newone, type(newone))

#print(df)
#print(len(df))

#trythis = masshex(yelp)
#print(trythis)
# na = df['name']
# art = df['artist']
# cid = df['colourid']
# colr = df['colour']
# cno = df['collectornum']
# exp = df['expansion']

# w = 0
# while w < len(df):
# 	cleandata = df.DataFrame([[][]],columns = ["name","artist","colourid","colour","collectornum","expansion","red_h","green_h","blue_h"])
# cleandict = {"name": [],"artist": [],"colourid": [],"colour": [],"collectornum": [],"expansion": [],"red_h": [],"green_h": [],"blue_h": []}
# w = 0

# while w < len(df):
# 	fivevals = hexes[w].replace('\n','')
# 	newcol = masshex(fivevals)
# 	cleandict.append()

#df.DataFrame([[],[],[],[]], columns = ["name","artist","colourid","colour","collectornum","expansion","red_h","green_h","blue_h"])
#it takes a list of lists! it should be easy to create lists
#.DataFrame( [[nameA, first colour],[nameA, second colour]etc.] , columns=["name","artist","colourid","colour","collectornum","expansion","red_h","green_h","blue_h"])
#print(len(df))
madlist = []
w = 0
while w < len(df):
	hexe = df['hexval']
	jelp = masshex(hexe[w].replace('\n',''))
	selp = halfhex(hexe[w].replace('\n',''))
	#print(len(jelp))
	colnum = 0
	while colnum < len(jelp):
		sublist = [df['name'][w],df['artist'][w],df['colourid'][w],df['colour'][w],df['collectornum'][w],df['expansion'][w],selp[colnum],jelp[colnum][0],jelp[colnum][1],jelp[colnum][2],f"{df['name'][w]}{df['expansion'][w]}{colnum + 1}"]
		madlist.append(sublist)
		colnum += 1
	#madlist.append(sublist)
	w += 1
	# madlist.append([df['name'][w]])
#print('ALL THE WAY DOWN')

# print(madlist)

print('length of unique sets:' + str(len(df)))
print(len(madlist))


collect = pd.DataFrame(madlist, columns = ["name","artist","colourid","colour","collectornum","expansion","hexval","red_h","green_h","blue_h","codename"])
collect.to_csv('truecollector.csv')