# this is only test stuff ignore it please

from ocr-space-py import OCRClient
import os

client = OCRClient(os.environ['KEY'])



# print(client.post(file="OCRSpacePyWrapper/test_pictures/hehehe differentiation.png")["ParsedResults"][0]["ParsedText"])
# print(client.post(file="OCRSpacePyWrapper/test_pictures/lmao imaginary numbers .png")["ParsedResults"][0]["ParsedText"])
# print(client.post(file="OCRSpacePyWrapper/test_pictures/secant and cosecant are losers.png")["ParsedResults"][0]["ParsedText"])
# print(client.post(file="OCRSpacePyWrapper/test_pictures/THIS IS BEST MEME.jpeg")["ParsedResults"][0]["ParsedText"])
# print(client.post(file="OCRSpacePyWrapper/test_pictures/this is illegal.jpeg")["ParsedResults"][0]["ParsedText"])

# print(client.get(url="https://irvinecoding.club/assets/images/YDRC-Workshop.png")["ParsedResults"][0]["ParsedText"])