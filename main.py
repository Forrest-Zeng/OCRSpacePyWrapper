# this is only test stuff ignore it smh

from OCRSpacePyWrapper import OCRClient

client = OCRClient("e8557dc71a88957")

print(client.post(file="OCRSpacePyWrapper/test_pictures/this is illegal.jpeg")["ParsedResults"][0]["ParsedText"])