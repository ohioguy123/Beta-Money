import requests
import threading
import time
import json
import os

def print_logo():
    logo = """
    \033[93m▄▄███▄▄·███╗   ███╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗▄▄███▄▄·
    ██╔════╝████╗ ████║██╔═══██╗████╗  ██║██╔════╝╚██╗ ██╔╝██╔════╝
    ███████╗██╔████╔██║██║   ██║██╔██╗ ██║█████╗   ╚████╔╝ ███████╗
    ╚════██║██║╚██╔╝██║██║   ██║██║╚██╗██║██╔══╝    ╚██╔╝  ╚════██║
    ███████║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║███████╗   ██║   ███████║
    ╚═▀▀▀══╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═▀▀▀══╝
    \033[0m"""
    print(logo)

def make_request():
       Print(“told you bruv”)

def generate_credit_card():
    cookies = {
        "csrftoken": "8b56rI96TwUH0X7dOT86JmPMBbUVYEpX3EI7ZKp3ZXHWnrRySD9ORyNaAaRXnW7i",
        "_ga": "GA1.2.1579916434.1654760883",
        "_gid": "GA1.2.1410860416.1654760883",
        "_gads": "ID=d4f0fe2265535514-2243e178fad30069:T=1654760893:RT=1654760893:S=ALNI_MaIzJo5Kmg3rKoLXSuvDGnQkyW3uw",
        "_gpi": "UID=0000087f297f7f43:T=1654760893:RT=1654760893:S=ALNI_MbnajBnRWmSHW7vrpR-U1w2uMwyVw",
        'FCNEC': '[["AKsRol_6etCde6kaPNd_o13SF2anvKLy0qaXvN6Kz0O_d9YbYS_KOfZ-j0xDjsEXL_4Otx5R38juHOOwfg0JShy5DHGmgAw2R6ZN4KZyI3qGimMjR0mQ0SEgj2ncvV4jQ32pssYst9ml2ptS_Ip2XyPbrLivgKXjIQ=="],null,[]]'
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "content-type": "application/x-www-form-urlencoded",
        "x-csrftoken": "xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj",
        "x-requested-with": "XMLHttpRequest"
    }
    payload = {
        "brand": "VISA",
        "country": "UNITED STATES",
        "bank": "121 FINANCIAL C.U.",
        "cvv": "",
        "date": "",
        "year": "",
        "range": "500 - 1000",
        "amount": "10",
        "dataformat": "TEXT",
        "pin": "on",
        "ctoken": "xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj"
    }
    sitex = "https://www.vccgenerator.org/fetchdata/generate-home-credit-card/"
    rs = requests.post(sitex, headers=headers, cookies=cookies, data=payload)
    data = json.loads(rs.text)
    card = data['creditCard'][1]
    print(f"[-] Brand : {card['IssuingNetwork']}\n[-] Card Number : {card['CardNumber']}\n[-] Bank : {card['Bank']}\n[-] Name : {card['Name']}\n[-] Address : {card['Address']}\n[-] Country : {card['Country']}\n[-] Money Range : {card['MoneyRange']}\n[-] CVV : {card['CVV']}\n[-] Expiry : {card['Expiry']}\n[-] Pin : {card['Pin']}\n============================")

def hi():
    url = input("Bot Token: ")
    payload = input("Message: ")

    def function():
        requests.post(url, json={'content': payload})

    while True:
        function()
        time.sleep(1)
        print("Message Sent")

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    while True:
        clear_screen()
        print_logo()

        print("\nOptions:")
        print("1. Generate Discord Nitro PAID")
        print("2. Generate Credit Card")
        print("3. Discord Bot Spam")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                num_requests = int(input("Enter the number of requests to generate (press Enter to exit): "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if num_requests <= 0:
                print("Number of requests must be greater than 0.")
                continue

            for _ in range(num_requests):
                make_request()

            input("Press Enter to continue...")

        elif choice == '2':
            generate_credit_card()
            input("Press Enter to continue...")

        elif choice == '3':
            hi()
            input("Press Enter to continue...")

        elif choice == '4':
            print("Exiting the tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()
