import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371},
        "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
        "Temperature": {"Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15}
    }
    
    for category, units in conversion_factors.items():
        if from_unit in units and to_unit in units:
            if callable(units[from_unit]):
                return units[to_unit](units[from_unit](value))
            else:
                return value * (units[to_unit] / units[from_unit])
    return None

# Set page config and style
st.set_page_config(page_title="Unit Converter", page_icon="⚖️", layout="centered")
st.markdown("""
    <style>
        body {
            background-color:#E6E6FA;
            color: #4a4a4a;
            font-family: Arial, sans-serif;
        }
        .stApp {
            background-color:#77DD77 ;
        }
        .stSelectbox, .stNumber_input, .stButton > button {
            background-color: #dfe6e9;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Unit Converter By Aleena Amir")

categories = {"Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile"],
              "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
              "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]}

category = st.selectbox("Select Category", list(categories.keys()))
from_unit = st.selectbox("From Unit", categories[category])
to_unit = st.selectbox("To Unit", categories[category])
value = st.number_input("Enter Value", min_value=0.0, step=0.1)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    if result is not None:
        st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
    else:
        st.error("Invalid conversion")
