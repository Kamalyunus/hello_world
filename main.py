import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    #url = 'http://api.ipstack.com/check?access_key=92fa815043bdad90aaaeb3b1ec112032'
    #req = requests.get(url)
    #response = req.json()
    #city = response["city"]
    #country = response["country_name"]
    city="Bentonville"
    country="USA"
    return render_template('index.html', city=city, country=country)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

