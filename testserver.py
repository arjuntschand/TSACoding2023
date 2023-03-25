from flask import Flask, request, jsonify # Imports the flask library modules
import pandas as pd
import numpy as np # linear algebra
from datetime import datetime, timedelta
import requests
import json
import datetime
import math

app = Flask(__name__)
print("hi")
@app.route('/')



def home():
    return "hi"

if __name__ == '__main__':
    # run app in debug mode on port 5000
    #app.run(debug=True, host="192.168.87.250", port=5000)
    app.run(debug=True, host="192.168.86.27", port=5000)

print("hi")