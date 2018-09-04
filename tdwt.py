import pandas as pd

df = pd.read_csv("tandd.csv")

print(df)

iteml = []		#Creating lists for items and locations
locl = []		#Creating lists for locations
sumt = 0
itemc = 0

for index, row in df.iterrows():
	if row['item'] not in iteml:
		iteml.append(row['item'])
	if row['location'] not in locl:
		locl.append(row['location'])

print(locl)
print(iteml)

tweights = []		#Store t weight
dweights = []		#Store d weight
	
for i in range(len(iteml)):
	for j in range(len(locl)):
		sumt = 0
		items = 0
		for index, row in df.iterrows():
			if(row['item'] == iteml[i]):
				sumt = sumt + row['count']
			if(row['item'] == iteml[i] and row['location'] == locl[j]):
				itemc = row['count']
		dweights.append(float(itemc)/sumt)
		sumt = 0
		items = 0
		for index, row in df.iterrows():
			if(row['location'] == locl[j]):
				sumt = sumt + row['count']
			if(row['location'] == locl[j] and row['item'] == iteml[i]):
				itemc = row['count']
		tweights.append(float(itemc)/sumt)


i = 0
for k in range(len(iteml)):
	for j in range(len(locl)):
		print("T weight for ",locl[j]," and ",iteml[k]," is ",tweights[i])
		print("D weight for ",locl[j]," and ",iteml[k]," is ",dweights[i])
		i = i + 1
		
sumip = 0		
for i in tweights:
	sumip = sumip + i
print(sumip)
sumip = 0
for i in dweights:
	sumip = sumip + i
print(sumip)
