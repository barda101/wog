import requests
from random import randint


def api_func():
    # Replace 'YOUR_ACCESS_KEY' with your actual API key from exchangeratesapi.io
    api_key = '86413429eaa8a4c958ef8a0e'

    # Specify the base currency (USD) and the target currency (NIS)
    base_currency = 'USD'
    target_currency = 'ILS'

    # API endpoint URL
    url = f'https://open.er-api.com/v6/latest/{base_currency}?apikey={api_key}'

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Get the exchange rate for USD to NIS
        exchange_rate = data['rates'][target_currency]

        # Print the exchange rate
        #print(f'The current exchange rate from {base_currency} to {target_currency} is: {exchange_rate}')
        return exchange_rate
    else:
        # Print an error message if the request was unsuccessful
        print(f'Error: Unable to retrieve exchange rates. Status code: {response.status_code}')


def get_money_interval(value, difficulty):
    usd_ils_rate = api_func()
    d = difficulty
    t = value
    interval = (t - (5 - d), t + (5 - d))
    return interval


def guess_from_user(num):
    return float(input(f"Guess how much ${num} is worth in ILS: "))


def play(diff):
    gen_num = randint(1, 100)
    rate = api_func()
    value = gen_num * rate
    interval = get_money_interval(value, diff)
    user_guess = guess_from_user(gen_num)
    if interval[0] <= user_guess <= interval[1]:
        return True
    else:
        return False




