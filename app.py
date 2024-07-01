from flask import Flask, render_template, request
import pickle 
import numpy as np
app = Flask(__name__)

model = pickle.load(open('model_pl.pkl', 'rb'))
@app.route('/')
def hello_world():
    return render_template("weather.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    day_info = [np.array(float_features)]
    prediction =  model.predict(day_info)

    if prediction[0] == 0:
        return render_template('weather.html', pred='Rainy')
    elif prediction[0] == 1:
        return render_template('weather.html', pred='Cloudy')
    elif prediction[0] == 1:
        return render_template('weather.html', pred='Sunny')
    else:
        return render_template('weather.html', pred='Snowy')


if __name__ == '__main__':
    app.run()