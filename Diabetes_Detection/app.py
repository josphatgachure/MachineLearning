import joblib
import streamlit as st

with open('random_model.pkl','rb') as model:
     Classifier = joblib.load(model)
def predictor(Pregnancies,Glucose,BMI,Age):
    global Classifier
    prediction =Classifier.predict([[Pregnancies,Glucose,BMI,Age]])
    if prediction == 0:
        return "Not Diabetic"
    elif prediction == 1:
        return "Diabetic"
    else:
        return "You're wrong"

def main():
    st.title("INDIAN DIABETIC PREDICTION APP")
    Pregnancies = st.number_input("Pregnancies")
    Glucose   = st.number_input("Glucose")
    BMI = st.number_input("BMI")
    Age = st.number_input("Age")

    if st.button("Predict"):
       prediction = predictor(Pregnancies,Glucose,BMI,Age)
       st.success(f'This patient is {prediction}')


if __name__ == '__main__':
     main()