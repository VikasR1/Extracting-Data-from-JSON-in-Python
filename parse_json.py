import json

dect = '{"name":"Vikas", "Skills":["Python, Project Management, Scrum"]}'

det_dict = json.loads(dect)

# To Output the full details
print(det_dict)

# To Output only the programming languages information
print(det_dict['Skills'])