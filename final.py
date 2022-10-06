# scraping the data from locally stored json file
import pandas as pd
import json 

with open("temp_js.json", 'r') as file:
    temp = json.load(file)

# print (temp['jobDetails'][0])

Job_Details = temp['jobDetails']
# print(Job_Details[1])

# converting everything in Dataframe 
JD_DF= pd.DataFrame(Job_Details)
print(JD_DF)

## checking head and tail of dataframe with 2 entries

print(JD_DF.head(2))
print(JD_DF.tail(2))

# #to verifiy the colums we can also get information by converting the data into csv, 
# JD_DF= pd.DataFrame(Job_Details).head(2)
print(JD_DF.to_csv('list.csv'))

# it will give only 2 rows data 
JD_DF= pd.DataFrame(Job_Details).head(2)[['title', 'footerPlaceholderLabel', 'companyName', 'tagsAndSkills', 'jobDescription']]

# it will give all rows data 
JD_DF= pd.DataFrame(Job_Details)[['title', 'footerPlaceholderLabel', 'companyName', 'tagsAndSkills', 'jobDescription']]
print(JD_DF.to_csv('final.csv'))

