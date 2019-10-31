import urllib.request

response = urllib.request.urlopen('https://cfmodelserver.herokuapp.com/model')

print(response.read())


# print("I just hit the server, waaaaaapahh")
# print(f'''There are {x} Surfers at Venice''')