import numpy as np
import pickle
import json
import config

class Titanic_Prediction():
    def __init__(self,Pclass,Age,SibSp,Parch,Gender,Embarked):
        self.Pclass=Pclass
        self.Age=Age
        self.SibSp=SibSp
        self.Parch=Parch
        self.Gender=Gender
        self.Embarked=Embarked

    
    def __load_data(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model=pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data=json.load(f)

    def predict_survival(self):

        self.__load_data()
        Gender_name='Gender_'+self.Gender
        Embarked_name='Embarked_'+self.Embarked
        Gender_index=self.json_data['Column_list'].index(Gender_name)
        Embarked_index=self.json_data['Column_list'].index(Embarked_name)

        test_array=np.zeros([1,len(self.json_data['Column_list'])])
        test_array[0][0]=self.Pclass
        test_array[0][1]=self.Age
        test_array[0][2]=self.SibSp
        test_array[0][3]=self.Parch
        test_array[0][Gender_index]=1
        test_array[0][Embarked_index]=1

        pred_survival=self.model.predict(test_array)[0]

        
        return pred_survival