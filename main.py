# this is only test stuff ignore it smh

from OCRSpacePyWrapper import OCRClient
import os

client = OCRClient(os.environ['KEY'])

print(client.post(file="OCRSpacePyWrapper/test_pictures/lmao imaginary numbers .png")["ParsedResults"][0]["ParsedText"])