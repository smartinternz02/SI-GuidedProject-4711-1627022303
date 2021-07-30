import numpy as np
from flask import Flask, request, jsonify, render_template
import random
app = Flask(__name__)
from tensorflow.keras.models import load_model
model=load_model("Engine_maintenance_keras.h5")


@app.route('/m_predict')
def predict():
    return render_template('manual.html')
@app.route('/s_predict')
def spredict():
    return render_template('sensor.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    ID=request.form["_id"]
    Cycle=request.form["cycles"]
    Settings1=request.form["set1"]
    Settings2=request.form["set2"]
    Settings3=request.form["set3"]
    S1=request.form["s1"]
    S2=request.form["s2"]  
    S3=request.form["s3"]
    S4=request.form["s4"]
    S5=request.form["s5"]
    S6=request.form["s6"]
    S7=request.form["s7"]
    S8=request.form["s8"] 
    S9=request.form["s9"]
    S10=request.form["s10"]
    S11=request.form["s11"]
    S12=request.form["s12"]
    S13=request.form["s13"]
    S14=request.form["s14"]
    S15=request.form["s15"]
    S16=request.form["s16"]
    S17=request.form["s17"]
    S18=request.form["s18"]
    S19=request.form["s19"]                   
    S20=request.form["s20"]
    S21=request.form["s21"]  
    x_test=np.array([[int(ID),int(Cycle),float(Settings1),float(Settings2),float(Settings3),float(S1),float(S2),float(S3),float(S4),float(S5),float(S6),float(S7),float(S8),float(S9),float(S10),float(S11),float(S12),float(S13),float(S14),float(S15),float(S16),float(S17),float(S18),float(S19),float(S20),float(S21)]])
    a = model.predict(x_test)
    pred = a>0.9
    if(pred == 0):
        pred = "No failure expected within 30 days."
    else:
        pred = "Maintenance Required!! Expected a failure within 30 days."
    
    return render_template('manual.html', prediction_text=pred)

@app.route('/sy_predict',methods=['POST'])

def sy_predict():
    inp1=[]
    inp1.append(random.randint(0,100))
    inp1.append(random.randint(0,365)) 
    for i in range(0,24):
        inp1.append(random.uniform(0,1))
   
    pred=model.predict(np.array([inp1]))>0.9
    if(pred == 0):
        pred = "No failure expected within 30 days."
    else:
        pred = "Maintenance Required!! Expected a failure within 30 days."
    return render_template('sensor.html', prediction_text=pred,data=inp1)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)






