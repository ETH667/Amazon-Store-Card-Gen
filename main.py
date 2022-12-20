import random
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

class validator():

    def __init__(self):
        self.cardNumber = None
        self.Brand = None

    def __findBrand(self):
        if self.cardNumber[:2] in ['34', '37']:
            self.Brand = 'American Express'
        elif self.cardNumber[:3] in ['300', '301', '302', '303', '304', '305']:
            self.Brand = 'Diners Club - Carte Blanche'
        elif self.cardNumber[:2] in ['36']:
            self.Brand = 'Diners Club - International'
        elif self.cardNumber[:2] in ['54']:
            self.Brand = 'Diners Club - USA & Canada'
        elif self.cardNumber[:4] in ['6011'] or self.cardNumber[0:3] in ['644', '645', '646', '647', '648',
                                                                         '649'] or self.cardNumber[0:2] in [
            '65'] or self.cardNumber[0:6] in [str(x) for x in range(622126, 622926)]:
            self.Brand = 'Discover'
        elif self.cardNumber[:3] in ['637', '638', '639']:
            self.Brand = 'InstaPayment'
        elif self.cardNumber[:4] in [str(x) for x in range(3528, 3590)]:
            self.Brand = 'JCB'
        elif self.cardNumber[:4] in ['5018', '5020', '5038', '5893', '6304', '6759', '6761', '6762', '6763']:
            self.Brand = 'Maestro'
        elif self.cardNumber[:2] in ['51', '52', '53', '54', '55'] or self.cardNumber[:6] in [str(x) for x in
                                                                                              range(222100, 272100)]:
            self.Brand = 'MasterCard'
        elif self.cardNumber[:4] in ['4026', '4508', '4844', '4913', '4917'] or self.cardNumber[:6] == '417500':
            self.Brand = 'VISA Electron'
        elif self.cardNumber[0] in ['4']:
            self.Brand = 'VISA'
        else:
            self.Brand = 'Unknown Brand'

    def validate(self, number):
        """
        number: str or int credit card number
        """
        if number is None: return 'Not a valid Credit Card Number'
        if number is bool: return 'Not a valid Credit Card Number'
        if number is float: return 'Not a valid Credit Card Number'
        number = ''.join(x for x in str(number).strip().split())
        if number.isdigit() and 13 <= len(number) <= 19:
            # Identify Brand
            self.cardNumber = number
            self.__findBrand()
            # Luhn's Algorithm
            lastDigit = int(number[-1])
            base = [int(x) for x in reversed(number[:-1])]
            base = [x if i % 2 != 0 else 2 * x for i, x in enumerate(base)]
            base = [x if x <= 9 else x - 9 for x in base]
            base = sum(base)
            base = (base * 9) % 10
            if base == lastDigit:
                print(Fore.GREEN)
                return f'[✰] {self.cardNumber} Valid Card'
                file = open("cards.txt", "w")
                number = repr(number)
                file.write(number)
                file.close()
            else:
                print(Fore.RED)
                return f'[✰] {self.cardNumber} Invalid Card'
        else:
            return 'Not a valid Credit Card Number'


print("Amazon Store Card Gen By ETH")

                                                            
print("Join https://discord.gg/Rc4cTD83Ev to learn how to order with these cards")
print("Join https://discord.gg/Rc4cTD83Ev to get aged amazon accounts")
print(" ") 
print(Fore.RED + " ")
print("Cards & Balance List:")
print("0.  Random Amazon Storecard")
print("1.  $1000 Amazon Storecard")
print("2.  $2000 Amazon Storecard")
print("3.  $5000 Amazon Storecard")
print("4.  $7000 Amazon Storecard")
print('5.  $10.000 Amazon Storecard')
print("6.  $20.000 Amazon Storecard")
print("7.  $40.000 Amazon Storecard")
print("8.  $100.000 Amazon Storecard ")
print(" ")
whatcard = input("[✰] Yo bg tu veut combien de thunes sur ta carte : ")
print(" ")
whatcard = int(whatcard)
randomnums = "0123456789"

if whatcard == 1:
    howmany = input("[✰] Et t'en veut combien : ")
    time.sleep(0.8)
    print("[/] Je lance sa... ")
    time.sleep(0.8)
    howmany = int(howmany)

    for x in range(howmany):
        bin = "60457811427"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
        print(validator().validate(int(cc)))

if whatcard == 2:
    howmany = input("[✰] Et t'en veut combien : ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "604578112"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)+str(ff7)
        print(validator().validate(int(cc)))

if whatcard == 3:
    howmany = input("[✰]  Et t'en veut combien : ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "604578116"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)+str(ff7)
        print(validator().validate(int(cc)))

if whatcard == 4:
    howmany = input("[✰] Et t'en veut combien : ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "604578118493"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)
        print(validator().validate(int(cc)))

if whatcard == 5:
    howmany = input("[✰] Et t'en veut combien : ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "6045781156"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)
        print(validator().validate(int(cc)))

if whatcard == 6:
    howmany = input("[✰] Et t'en veut combien : ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "60457811453"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)
        print(validator().validate(int(cc)))
		
if whatcard == 7:
    howmany = input("[✰] Et t'en veut combien : ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "60457811947"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)
        print(validator().validate(int(cc)))
		
if whatcard == 8:
    howmany = input("[✰] Et t'en veut combien : ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "60457811859"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)
        print(validator().validate(int(cc)))
		
if whatcard == 0:
    howmany = input("[✰] Et t'en veut combien : ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "604578112735"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)
        print(validator().validate(int(cc)))
        

print(" ")
print(" ")
print(Fore.RED + "if the cards dont mf work try it again retard")
print(" ")
input('Press ENTER to exit')
