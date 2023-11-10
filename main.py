import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="👨‍💻", layout="wide")


with st.container():
    st.title("BMI Calculator")
    st.subheader("-By Aahlad Singh")
    st.write("A BMI calculator tells us whether a person is Underweight, Fit or Obese")
    st.write("The BMI calculation divides an adult's weight in kilograms (kg) by their height in metres (m) squared.")
    st.write("[Learn More about BMI ](https://en.wikipedia.org/wiki/Body_mass_index)")

    st.write("----------------------------------------------------------------------------------------------------------------------------")

st.subheader("Your Information ➡")
Height = st.slider('Your Height in Centimeter', 10, 230)
Weight = st.slider('Your Weight in Kilogram', 0, 150)

st.write("---")

st.subheader("BMI ➡ ")

bmi = (Weight / (Height / 100) ** 2)

RBmi = round(bmi, 2)

st.write("Your BMI is", RBmi, "Kg/m^2")
if RBmi < 18.5:
    st.write("You Are Underweight as your BMI is less than 18")
elif 24.9 > RBmi > 18.5:
    st.write("Your Weight is Normal")
elif RBmi > 25:
    st.write("You are Overweight as your BMI is more than 25")

st.write("---")

st.subheader("Thank You")
st.write("Class 10th Science Project")
st.write(" Aahlad Singh  Class 10 - A ")
st.write(" Kendriya Vidyalaya, Vasant Kunj, New Delhi ")




