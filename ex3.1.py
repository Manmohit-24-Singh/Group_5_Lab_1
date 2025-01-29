import json #importing json library
import matplotlib.pyplot as plt #importing matplot library

with open("internetdata.json", "r") as internet: #Opening json file in reading mode
    dtls = json.load(internet) #Loading the json file content in a variable



rich_country = [] #Creating an empty list
poor_country = [] #Creating an empty list

for i in dtls: #Iterating in dtls
    if i["incomeperperson"] != None: #Filtering null incomeperperson values
        if i["incomeperperson"] > 10000: #Filtering if the income is above 10000
            rich_country.append(i) #If income is above 10000 then append the entire dictionary to rich_country list
        else: #Else statement
            poor_country.append(i) #If income is not above 10000 then append the entire dictionary to rich_country list

rich_internet = [j['internetuserate'] for j in rich_country if j['internetuserate']!= None] #Storing the internet usage for rich countries in a variable using list comprehension
poor_internet = [k['internetuserate'] for k in poor_country if k['internetuserate']!= None] #Storing the internet usage for poor countries in a variable using list comprehension


plt.figure(figsize=(10, 10)) #Setting figsize for plot
plt.hist(rich_internet, color="blue") #Using rich_internet for the histogram and giving the colour
plt.title("Internet Usage Distribution for Rich Countries (Income > $10,000)") #Histogram title
plt.xlabel("Internet Usage Rate") #Histogram x-axis label
plt.ylabel("Frequency") #Histogram y-axis label
plt.savefig("hist1.png") #Saving the histogram as a png file

plt.figure(figsize=(10, 10)) #Setting figsize for plot
plt.hist(poor_internet, color="red") #Using poor_internet for the histogram and giving the colour
plt.title("Internet Usage Distribution for Poor Countries (Income < $10,000)") #Histogram title
plt.xlabel("Internet Usage Rate") #Histogram x-axis label
plt.ylabel("Frequency") #Histogram y-axis label
plt.savefig("hist2.png") #Saving the histogram as a png file

