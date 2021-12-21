import hashlib
import hmac



def option_1():
    key = input("Enter the key :")
    message = input("Enter the message :")
    hmac1 = hmac.new(key=key.encode(), msg=message.encode(), digestmod="sha1")
    message_digest1 = hmac1.digest()
    message_digest2 = hmac1.hexdigest()
    print("Digest Value:", message_digest1)
    print("Digest Value in hex:", message_digest2)


def option_2():
    myfile = input("Enter file name :")
    key = input("Enter the key :")
    with open(myfile, 'rb') as f:
        body = f.read(-1)
        hash = hmac.new(key=key.encode(), msg=body, digestmod="sha1")
        message_digest1 = hash.digest()
        message_digest2 = hash.hexdigest()
        print("Digest Value:", message_digest1)
        print("Digest Value in hex:", message_digest2)

def menu():
    print("[1] Option 1 for Hash Function implementation using string.")
    print("[2] Option 2 for Hash Function implementation using text file.")
    print("[0] Option 0 to exit")


def display():
    print(" _  _            _            __                  _    _            ")
    print("| || | __ _  ___| |_         / _| _  _  _ _   __ | |_ (_) ___  _ _  ")
    print("| __ |/ _` |(_-/|   \       |  _|| || || ' \ / _||  _|| |/ _ \| ' \ ")
    print("|_||_|\__/_|/__/|_||_|      |_|   \_._||_||_|\__| \__||_|\___/|_||_|")


display()
menu()
option = int(input("Enter your option :"))
while option != 0:
    if option == 1:
        print("Hash function using string")
        option_1()
    elif option == 2:
        print("Hash function using text file")
        option_2()
    else:
        print("Invalid option !")

    print()
    menu()
    option = int(input("Enter your option :"))
print("Thanks for using :>")
