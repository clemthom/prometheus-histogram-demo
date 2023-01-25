from flask import Flask
from prometheus_client import Histogram, generate_latest
import random

app = Flask(__name__)
request_time = Histogram('request_time','Request time')

@app.route('/timer')
def timer_func():
    dummy_time = random.uniform(0,0.9)
    request_time.observe(dummy_time)
    return "Timer endpoint took {} seconds".format(dummy_time)

@app.route('/metrics')
def metrics():
    return generate_latest()

app.run(host='0.0.0.0', port=8080)
