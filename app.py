from flask import Flask , render_template ,request
import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
    print(request.headers)
    return render_template('index.html' , data=request.headers)

if __name__ == "__main__":
    app.run(debug=True)