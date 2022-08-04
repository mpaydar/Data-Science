import pandas as pd

# reading the csv
headers=["Price"," Maintenancecost","#ofdoors","#ofpassengers","Luggagecap",'Safetyrating',"VehicleClass"]
df=pd.read_csv("https://raw.githubusercontent.com/mpaydar/CS381/main/HW1/cars-sample35.csv",names=headers)
price=[]
maintenance=[]
doors=[]
passengers=[]
luggage=[]
safetyRating=[]
vehicle=[]

# print(df)

price=df['Price'].tolist()
maintenance=df[' Maintenancecost'].tolist()
doors=df['#ofdoors'].tolist()
passengers=df['#ofpassengers'].tolist()
luggage=df['Luggagecap'].tolist()
safetyRating=df['Safetyrating'].tolist()
vehicles=df['VehicleClass'].tolist()


#3
med_price=[]
for i in range(len(price)): 
    if price[i]=='med':
        med_price.append(i)
print(med_price)


#4
passN=[]
for i in range(len(price)): 
    if price[i]=='med':
        passN.append(passengers[i])
print(passN)


#5
NotEffAuto=[]
for i in range(len(price)): 
    if price[i]=='high' and maintenance[i]!='low':
        NotEffAuto.append(i)
print(NotEffAuto)



#6
priceIndexes = [p for p in range(len(price)) if price[p]=='med']
print(priceIndexes)



# 7 using list comprehension 
targetPassNum=[passengers[passNum] for passNum in priceIndexes]
print(targetPassNum)

#8 
effecientAuto=[(p) for p in range(len(price)) if (price[p]=='high' and maintenance[p]!='low')]
print(effecientAuto)





#Nested List Comprehension:
nlist = [[1, 2, 3], ['A', 'B', 'C'], [4, 5], ['D', 'E'] ]
newList= [ n for sublist in nlist for n in sublist]
print(newList)