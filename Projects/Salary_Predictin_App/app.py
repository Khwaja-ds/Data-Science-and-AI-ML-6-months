import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt
import random


with open("salary_model.pkl", "rb") as f:
    model = pickle.load(f)


st.set_page_config(page_title="Salary Predictor", page_icon="", layout="wide")


st.title(" Salary Predictor")
st.write("Wondering how much you *might* earn with your experience? Let's find out!")

st.markdown("---")

# SIDEBAR
st.sidebar.header("Model Overview")
st.sidebar.write("This app uses a simple Linear Regression model trained on salary data.")
st.sidebar.code("Model: salary = β0 + β1 × experience")

# Bonus added by me
quotes = [
    "“The only way to do great work is to love what you do.” – Steve Jobs",
    "“Don't watch the clock; do what it does. Keep going.” – Sam Levenson",
    "“Your future is created by what you do today, not tomorrow.” – Robert Kiyosaki"
]
st.sidebar.markdown(f" **Tip:** {random.choice(quotes)}")

# INPUT 
st.subheader(" Enter Your Experience")

col1, col2 = st.columns(2)

with col1:
    exp_input = st.number_input("Type your experience (in years)", min_value=0.0, max_value=50.0, value=1.0, step=0.1)

with col2:
    exp_slider = st.slider("Or use the slider", min_value=0.0, max_value=50.0, value=1.0, step=0.1)

# Sync both inputs
experience = exp_input if exp_input != 1.0 else exp_slider

#  PREDICTION 
if st.button(" Predict My Salary"):
    salary = model.predict(np.array([[experience]]))[0]
    st.success(f"Estimated Salary for {experience:.1f} years of experience: ₹ {salary:,.2f}")

# VISUALIZATION
st.markdown("---")
st.subheader(" Salary Trend")

years = np.arange(0, 21, 0.5).reshape(-1, 1)
predicted_salaries = model.predict(years)

fig, ax = plt.subplots()
ax.plot(years, predicted_salaries, color="teal", linewidth=2)
ax.set_title("Experience vs Predicted Salary")
ax.set_xlabel("Years of Experience")
ax.set_ylabel("Salary (in ₹)")
st.pyplot(fig)


st.markdown("---")
st.caption("")
