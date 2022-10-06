import json
 
data = '{"name":"Vikas", "Designation": "Scrum Master", "Skills":"Python, Project Management, Scrum"}'

# # step 1 : converting the python string in temp json object and storing that data in json file

temp_file = json.dumps(data)

with open("my_file.json", 'w') as file:
    file.write(temp_file)


# # step 2: obtain data from json file

# with open("my_file.json", "r") as file:
#     temp = json.load(file)

# print(temp)