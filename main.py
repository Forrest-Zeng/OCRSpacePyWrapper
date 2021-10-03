from __init__ import *

client = OCRClient("e8557dc71a88957")

print(client.post(file="this is illegal.jpeg")["ParsedResults"][0]["ParsedText"])