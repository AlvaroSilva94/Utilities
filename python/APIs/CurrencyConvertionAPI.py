from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/convert_currency', methods=['GET'])
def convert_currency():
    base_currency = request.args.get('base_currency')
    target_currency = request.args.get('target_currency')
    amount = float(request.args.get('amount'))

    exchange_rate_api_url = f'https://currency-converter-api2.p.rapidapi.com/convert_currency?base_currency={base_currency}&target_currency={target_currency}&amount={amount}'
    headers = {
        'x-rapidapi-key': '5e29971d8bmsh2d46a624dedb8ffp132725jsn0e7a350356fe',
        'x-rapidapi-host': 'currency-converter-api2.p.rapidapi.com'
    }
    response = requests.get(exchange_rate_api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'rates' in data and target_currency in data['rates']:
            exchange_rate = data['rates'][target_currency]
            converted_amount = round(amount * exchange_rate, 2)
            return f'{amount} {base_currency} is equivalent to {converted_amount} {target_currency}'

    return 'Unable to perform currency conversion.'

if __name__ == '__main__':
    app.run(debug=True)

# https://webcv.pythonanywhere.com/weather?city=Porto