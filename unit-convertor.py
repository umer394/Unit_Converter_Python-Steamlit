import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered", initial_sidebar_state="expanded")
st.title("Unit Converter")
unit_list = ["Temperature", "Length", "Mass", "Volume"]
unit = st.selectbox("Select the type of conversion", unit_list, index=0)

factors = {
    "length":{
        "Kilometre": 0.001,       
        "Metre": 1,              
        "Centimetre": 100,       
        "Millimetre": 1000,       
        "Micrometre": 1e6,       
        "Nanometre": 1e9,        
        "Mile": 1 / 1609.34,      
        "Yard": 1.09361,         
        "Foot": 3.28084,         
        "Inch": 39.3701,         
        "Nautical mile": 1 / 1852 
    },
    "temperature":{
        "Fahrenheit": 32 ,
        "Kelvin": 273.15,
        "Celsius": 0  
    },
    "mass":{
        "Tonne": 0.001,        
        "Kilogram": 1,          
        "Gram": 1000,           
        "Milligram": 1e6,       
        "Microgram": 1e9,       
        "Imperial ton": 1 / 1016.047,  
        "US ton": 1 / 907.1847, 
        "Stone": 1 / 6.35029,   
        "Pound": 1 / 0.453592,  
        "Ounce": 1 / 0.0283495
    }

}

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

def length_conversion(value, from_unit, to_unit):
    return value * factors[to_unit] / factors[from_unit]

def mass_conversion(value, from_unit, to_unit):
    kg_value = value / factors[from_unit]
    return kg_value * factors[to_unit]


if unit == "Temperature":
    factors = factors["temperature"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("Select From unit", options=factors.keys(), index=1)
    with col2:
        to_unit = st.selectbox("Select To unit", options=factors.keys(), index=2)

    value = st.number_input("Enter the value to convert", min_value=0.0, key="from_value")

    if st.button("Convert"):
        result = temperature_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif unit == "Length":
    factors = factors["length"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("Select From unit", options=factors.keys(), index=1)
    with col2:
        to_unit = st.selectbox("Select To unit", options=factors.keys(), index=2)

    value = st.number_input("Enter the value to convert", min_value=0.0, key="from_value")

    if st.button("Convert"):
        result = length_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    
elif unit == "Mass":
    factors = factors["mass"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("Select From unit", options=factors.keys(), index=1)
    with col2:
        to_unit = st.selectbox("Select To unit", options=factors.keys(), index=2)

    value = st.number_input("Enter the value to convert", min_value=0.0, key="from_value")

    if st.button("Convert"):
        result = mass_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
