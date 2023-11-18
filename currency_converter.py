# planning the program

# registeration in the currency convertion website
# obtain an API key
# start the game
# enter an intial currency
# enter a target currency
# enter the amount
# if the amount is lesser than zero > throw an error
# if the amount is bigger than zero > check if the request is success 
# if the request is success(request = 200) => show the conversion
# if the request is failure(request = 404) => print try again , exit the program

import requests

initial_curreny = input("enter the initial currency: ")
target_curreny = input("enter the target currency: ")

while True:
    try:
        amount_of_money = float(input("enter the amount of money: "))
    except:
        print("the amount must be a numberic amount")
        continue

    if amount_of_money == 0:
        print("the amount must be greater than zero")
        continue
    else:
        break


url = f"https://api.apilayer.com/currency_data/convert?to={target_curreny}&from={initial_curreny}&amount={amount_of_money}"

payload = {}
headers= {
    "apikey": "P0zTMFD4vMxrjipfaarZ3IUY3laLXA4z"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

if (status_code != 200):
    print("there was smth wrong , please try again later !")
    quit()

result = response.json()

print(result["result"])


