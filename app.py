import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("co2_rf_model.pkl")

st.title("🌍 Carbon Emissions Prediction App")
st.write("Predict CO₂ emissions using Machine Learning")

st.sidebar.header("Input Parameters")

year = st.sidebar.number_input("Year", 1950, 2050, 2030)
population = st.sidebar.number_input("Population", 1_000_000, 8_000_000)
gdp = st.sidebar.number_input("GDP (USD)", 1_000_000_000, 10_000_000_000)

if st.sidebar.button("Predict CO₂ Emissions"):
    input_df = pd.DataFrame({
        "year": [year],
        "population": [population],
        "gdp": [gdp]
    })

    prediction = model.predict(input_df)[0]
    st.success(f"🌱 Predicted CO₂ Emissions: {prediction:.2f}")

# Load dataset for visualization
df = pd.read_csv("owid-co2-data.csv")
df = df[['year', 'co2']].dropna()

st.subheader("📈 Historical CO₂ Emissions Trend")

fig, ax = plt.subplots()
ax.plot(df['year'], df['co2'], label="Historical CO₂")
ax.set_xlabel("Year")
ax.set_ylabel("CO₂ Emissions")
ax.legend()

st.pyplot(fig)
