import streamlit as st
import pickle
import numpy as np


with open('StudentsPrediction_Model', 'rb') as file:
    RFC_Model = pickle.load(file)


def show_predict_page():
    st.title("Students Grade Prediction")

    st.write("""#### Please fill this information to predict the grade""")

    Gender = (
        "Male",
        "Female",
    )

    Status = (
        "Single",
        "Married",
    )

    Job = (
        "Yes",
        "No",
    )

    Parent_Education = (
        "Uneducated",
        "High School",
        "College"
    )

    Family_income = (
        "Low",
        "Medium",
        "High",
    )

    Family_Problems = (
        "Very rare",
        "Just sometimes",
        "Most of the times",
    )

    Gender = st.selectbox("Gender", Gender)
    Age = st.slider("Your Age", 18, 35, 22)
    Status = st.selectbox("Status", Status)
    Job = st.selectbox("Job", Job)
    Parent_Education = st.selectbox("Parent Education", Parent_Education)
    Family_income = st.selectbox("Family income", Family_income)
    Family_Problems = st.selectbox("Family Problems", Family_Problems)

    ok = st.button("Predict")
    if ok:
        if Gender == "Male":
            Gender = 0
        else:
            Gender = 1

        if Status == "Single":
            Status = 0
        else:
            Status = 1

        if Job == "No":
            Job = 0
        else:
            Job = 1

        if Parent_Education == "Uneducated":
            Parent_Education = 0
        elif Parent_Education == "High School":
            Parent_Education = 1
        else:
            Parent_Education = 2

        if Family_income == "Low":
            Family_income = 0
        elif Family_income == "Medium":
            Family_income = 1
        else:
            Family_income = 2

        if Family_Problems == "Very rare":
            Family_Problems = 0
        elif Family_Problems == "Just sometimes":
            Family_Problems = 1
        else:
            Family_Problems = 2

        X = np.array(
            [[Gender, Age, Status, Job, Parent_Education, Family_income, Family_Problems]])
        Result = RFC_Model.predict(X)

        if Result >= 55:
            st.subheader(f"The Prediction Grade is: {Result[0]}")
            st.subheader("The Student is Expected to PASS")

        else:
            st.subheader(f"The Prediction Grade is: {Result[0]}")
            st.subheader("The Student is Expected to Fail")
