from flask import Flask, render_template, request
from weather import get_forecast

app = Flask(__name__)


@app.route("/")
def index():
    address = request.values.get('address')
    forecast = None
    print(address)
    if address:
        forecast = get_forecast(address).decode()
        print(forecast)
    return render_template('index.html', forecast=forecast)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run()
