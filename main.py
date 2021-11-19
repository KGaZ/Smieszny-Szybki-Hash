from random import random, randint
import requests
import mechanize

dlugosc = 5

znaki = []

for i in range(65, 91):
    znaki.append(chr(i))

for i in range(97, 123):
    znaki.append(chr(i))

for i in range(0, 10):
    znaki.append(str(i))

print(znaki)


def generateEnd(before, left):
    if left == 1:

        for i in range(0, len(znaki)):
            print(before + znaki[i])

    else:

        for i in range(0, len(znaki)):
            generateEnd(before + znaki[i], left - 1)


#generateEnd("", int(input("Podaj dlugosc: ")))

data = {"LoginName":"jgalgan@sbs.sniadek.pl",
        "Password":input("Podaj hasło: ")}

url = "https://cufs.vulcan.net.pl/kielce/Account/LogOn"

response = requests.post(url, params=data)

print(response.text)