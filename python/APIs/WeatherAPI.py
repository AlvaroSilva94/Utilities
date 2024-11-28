from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    api_key = '8555c38230c044a8a40152819231606'
    base_url = 'https://api.weatherapi.com/v1/current.json'

    city = request.args.get('city')
    if not city:
        return 'City parameter is missing.', 400

    params = {
        'key': api_key,
        'q': city,
        'aqi': 'no',
        'lang': 'en'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data['current']['temp_c']
        description = data['current']['condition']['text']
        result = {
            'city': city,
            'temperature': temperature,
            'description': description
        }
        return result

    return 'Unable to fetch weather data.', 500

if __name__ == '__main__':
    app.run(debug=True)
