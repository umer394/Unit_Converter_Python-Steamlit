import streamlit as st

def convert_length(value, from_unit, to_unit):
    length_units = {
        "Metre": 1,
        "Centimetre": 100,
        "Millimetre": 1000,
        "Kilometre": 0.001,
        "Inch": 39.3701,
        "Foot": 3.28084,
        "Yard": 1.09361,
        "Mile": 0.000621371
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_mass(value, from_unit, to_unit):
    mass_units = {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1_000_000,
        "Tonne": 0.001,
        "Pound": 2.20462,
        "Ounce": 35.274
    }
    return value * (mass_units[to_unit] / mass_units[from_unit])

st.title("Unit Converter")

category = st.selectbox("Select Category", ["Length", "Mass"])

if category == "Length":
    from_unit = st.selectbox("From", ["Metre", "Centimetre", "Millimetre", "Kilometre", "Inch", "Foot", "Yard", "Mile"], index=0)
    to_unit = st.selectbox("To", ["Metre", "Centimetre", "Millimetre", "Kilometre", "Inch", "Foot", "Yard", "Mile"], index=1)
    value = st.number_input("Enter Value", min_value=0.0, format="%.4f")
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Mass":
    from_unit = st.selectbox("From", ["Kilogram", "Gram", "Milligram", "Tonne", "Pound", "Ounce"], index=0)
    to_unit = st.selectbox("To", ["Kilogram", "Gram", "Milligram", "Tonne", "Pound", "Ounce"], index=1)
    value = st.number_input("Enter Value", min_value=0.0, format="%.4f")
    if st.button("Convert"):
        result = convert_mass(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
