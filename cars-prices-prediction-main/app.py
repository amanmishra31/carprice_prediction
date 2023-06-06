import numpy as np
from flask import Flask,render_template
import joblib
from flask import request



app = Flask(__name__)
model = joblib.load("car_prices_prediction.pkl")


@app.route('/')
def prem():
    return render_template('index.html')

@app.route('/',methods=["POST"])
def home1():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4_Petrol = request.form['d']
    if(data4_Petrol=='Petrol'):
        data4_Petrol=1
        data4_Diesel=0
    elif(data4_Petrol=='Diesel'):
        data4_Petrol=0
        data4_Diesel=1
    else:
        data4_Petrol=0
        data4_Diesel=0 
    data5_Individual = request.form['e']
    if(data5_Individual=='Individual'):
        data5_Individual=1
    else:
        data5_Individual=0
    data6_Mannual = request.form['f']
    if(data6_Mannual=='Mannual'):
        data6_Mannual=1
    else:
        data6_Mannual=0
    data7 = request.form['g']
    arr = np.array([[data1,data2,data3,data4_Petrol,data5_Individual,data6_Mannual,data7]],dtype= float)
    
    pred = model.predict(arr)
    output = np.round_(pred,2)
    price = ' '.join(map(str, output))
    # print(price) 
    return render_template('index.html',prediction_text = f" {price} Lakh")

    # return render_template('index.html',prediction_text = f"The Suggested Crop for Given Climatic Codition is :{pred}")

if __name__ == "__main__":
    app.run(debug=True)