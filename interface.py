from flask import Flask,request,render_template,jsonify
from utils import Titanic_Prediction
import config

app=Flask(__name__)

@app.route('/Titanic_model')
def home():
    #return jsonify({'Result':'Successful'})
    return render_template('Titanic_prediction.html')

@app.route('/Titanic_pred',methods=['GET','POST'])
def predict_status():
    if request.method=='GET':
        data=request.args.get
        Pclass=int(data('Pclass'))
        Age=float(data('Age'))
        SibSp=int(data('SibSp'))
        Parch=int(data('Parch'))
        Gender=data('Gender')
        Embarked=data('Embarked')

        obj=Titanic_Prediction(Pclass,Age,SibSp,Parch,Gender,Embarked)
        status=obj.predict_survival()
        if status==0:
            survival_status='Not Survived'
        else:
            survival_status='Survived'
        #return jsonify({'Result':f'Passanger is {status}'})
        return render_template('Titanic_prediction.html',prediction=survival_status)
    
    elif request.method=='POST':
        data=request.form
        Pclass=int(data['Pclass'])
        Age=float(data['Age'])
        SibSp=int(data['SibSp'])
        Parch=int(data['Parch'])
        Gender=data['Gender']
        Embarked=data['Embarked']

        obj=Titanic_Prediction(Pclass,Age,SibSp,Parch,Gender,Embarked)
        status=obj.predict_survival()
        if status==0:
            survival_status='Not Survived'
        else:
            survival_status='Survived'
        #return jsonify({'Result':f'Passanger is {survival_status}'})
        return render_template('Titanic_prediction.html',prediction=survival_status)
    
if __name__=='__main__':
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)
    


