import requests

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter the amount of money: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount
        except ValueError:
            print("Please enter a numeric amount.")

def get_currency_input(prompt):
    return input(prompt).strip().upper()  # Convert to uppercase for consistency

def main():
    initial_currency = get_currency_input("Enter the initial currency: ")
    target_currency = get_currency_input("Enter the target currency: ")
    
    amount_of_money = get_valid_amount()

    url = f"https://api.apilayer.com/currency_data/convert?to={target_currency}&from={initial_currency}&amount={amount_of_money}"

    headers = {
        "apikey": "P0zTMFD4vMxrjipfaarZ3IUY3laLXA4z"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            result = response.json()
            converted_amount = result.get("result")
            print(f"Converted amount: {converted_amount}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
