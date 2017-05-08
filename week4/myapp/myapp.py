import os
from flask import Flask, render_template, request
from weather import get_forecast, get_map

app = Flask(__name__)


@app.route("/")
def index():
    address = request.values.get('address')
    forecast = None
    map_src = None
    if address:
        forecast = get_forecast(address)
        map_src = get_map(address)
    return render_template('index.html', forecast=forecast, map_src=map_src)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
