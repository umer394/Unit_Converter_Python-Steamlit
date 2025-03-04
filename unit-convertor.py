import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered", initial_sidebar_state="expanded")
st.title("Unit Converter")
unit_list = ["Temperature", "Length", "Mass", "Volume","Area","Energy","Frequency","Speed","Pressure","Time","Plane Angle","Fuel Economy"]
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
    },
    "volume":{
        "Cubic meter": 1 / 1000,            
        "Liter": 1,                        
        "Milliliter": 1000,                  
        "US liquid gallon": 1 / 3.78541,     
        "US liquid quart": 1 / 0.946353,     
        "US liquid pint": 1 / 0.473176,      
        "US legal cup": 1 / 0.24,            
        "US fluid ounce": 1 / 0.0295735,     
        "US tablespoon": 1 / 0.0147868,      
        "US teaspoon": 1 / 0.00492892,       
        "Imperial gallon": 1 / 4.54609,      
        "Imperial quart": 1 / 1.13652,       
        "Imperial pint": 1 / 0.568261,       
        "Imperial cup": 1 / 0.284131,        
        "Imperial fluid ounce": 1 / 0.0284131, 
        "Imperial tablespoon": 1 / 0.0177582,  
        "Imperial teaspoon": 1 / 0.00591939, 
        "Cubic foot": 1 / 28.3168,           
        "Cubic inch": 1 / 0.0163871 
    },
    "area":{
        "Square kilometre": 1 / 1_000_000,   
        "Square metre": 1,                   
        "Square mile": 1 / 2_589_988,        
        "Square yard": 1 / 0.836127,          
        "Square foot": 1 / 0.092903,          
        "Square inch": 1 / 0.00064516,        
        "Hectare": 1 / 10_000,                
        "Acre": 1 / 4_046.86
    },
    "energy":{
        "Joule": 1,                       
        "Kilojoule": 1 / 1000,              
        "Gram calorie": 1 / 4.184,          
        "Kilocalorie": 1 / 4184,           
        "Watt hour": 1 / 3600,              
        "Kilowatt-hour": 1 / 3.6e6,         
        "Electronvolt": 1 / 1.60218e-19,    
        "British thermal unit": 1 / 1055.06,
        "US therm": 1 / 1.055e8,            
        "Foot-pound": 1 / 1.35582 
    },
    "frequency":{
        "Hertz": 1,             
        "Kilohertz": 1 / 1e3,   
        "Megahertz": 1 / 1e6,   
        "Gigahertz": 1 / 1e9
    },
    "pressure":{
        "Pascal": 1,                   
        "Bar": 1e-5,                   
        "Pound per square inch": 1 / 6894.757,  
        "Standard atmosphere": 1 / 101325,  
        "Torr": 1 / 133.322 
    },
    "speed":{
        "Metre per second": 1,                   
        "Kilometre per hour": 3.6,               
        "Mile per hour": 2.23694,                
        "Foot per second": 3.28084,              
        "Knot": 1.94384
    },
    "time":{
        "Nanosecond": 1e9,           
        "Microsecond": 1e6,          
        "Millisecond": 1e3,          
        "Second": 1,                 
        "Minute": 1/60,              
        "Hour": 1/3600,              
        "Day": 1/86400,              
        "Week": 1/604800,            
        "Month": 1/2.628e6,          
        "Calendar year": 1/3.154e7, 
        "Decade": 1/3.154e8,         
        "Century": 1/3.154e9
    },
    "plane_angle":{
        "Arcsecond": 3600,           
        "Minute of arc": 60,         
        "Degree": 1,                 
        "Radian": 1 / 57.2958,       
        "Gradian": 10 / 9,           
        "Milliradian": 1000 / 57.2958
    },
    "fuel_economy":{
        "Kilometre per liter (km/L)": 1,              
        "Mile per US gallon (mpg US)": 2.35215,        
        "Mile per Imperial gallon (mpg UK)": 2.82481,  
        "Litre per 100 kilometres (L/100km)": 100,
    }

}

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9 / 5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            return value

    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5 / 9
        elif to_unit == "Kelvin":
            return (value - 32) * 5 / 9 + 273.15
        else:
            return value

    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9 / 5 + 32
        else:
            return value

def length_conversion(value, from_unit, to_unit):
    return value * factors[to_unit] / factors[from_unit]

def mass_conversion(value, from_unit, to_unit):
    kg_value = value / factors[from_unit]
    return kg_value * factors[to_unit]

def volume_conversion(value,from_unit,to_unit):
    liter_value = value / factors[from_unit]
    return liter_value * factors[to_unit]

def area_conversion(value,from_unit,to_unit):
    sqm_value = value / factors[from_unit]
    return sqm_value * factors[to_unit]


def energy_conversion(value,from_unit,to_unit):
    joule_value = value / factors[from_unit]
    return joule_value * factors[to_unit]

def frquency_conversion(value,from_unit,to_unit):
    hertz_value = value / factors[from_unit]
    return hertz_value * factors[to_unit]

def pressure_conversion(value,from_unit,to_unit):
    pascal_value = value / factors[from_unit]
    return pascal_value * factors[to_unit]

def speed_conversion(value,from_unit,to_unit):
    mps_value = value / factors[from_unit]
    return mps_value * factors[to_unit]

def time_conversion(value,from_unit,to_unit):
    seconds_value = value / factors[from_unit]
    return seconds_value * factors[to_unit]


def plane_angle_conversion(value,from_unit,to_unit):
    degree_value = value / factors[from_unit]
    return degree_value * factors[to_unit]

def fuel_economy_conversion(value,from_unit,to_unit):
    km_per_liter_value = value / factors[from_unit]
    return km_per_liter_value * factors[to_unit]

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
        st.success(f"{value} {from_unit} = {result} {to_unit}")

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
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    
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
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif unit == "Volume":
    factors = factors["volume"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("Select From unit", options=factors.keys(), index=1)
    with col2:
        to_unit = st.selectbox("Select To unit", options=factors.keys(), index=2)

    value = st.number_input("Enter the value to convert", min_value=0.0, key="from_value")

    if st.button("Convert"):
        result = volume_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")


elif unit == "Area":
    factors = factors["area"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("Select From unit", options=factors.keys(), index=1)
    with col2:
        to_unit = st.selectbox("Select To unit", options=factors.keys(), index=2)

    value = st.number_input("Enter the value to convert", min_value=0.0, key="from_value")

    if st.button("Convert"):
        result = area_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")


elif unit == "Frequency":
    factors = factors["frequency"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("Select From unit", options=factors.keys(), index=1)
    with col2:
        to_unit = st.selectbox("Select To unit", options=factors.keys(), index=2)

    value = st.number_input("Enter the value to convert", min_value=0.0, key="from_value")

    if st.button("Convert"):
        result = frquency_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif unit == "Energy":
    factors = factors["energy"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("Select From unit", options=factors.keys(), index=1)
    with col2:
        to_unit = st.selectbox("Select To unit", options=factors.keys(), index=2)

    value = st.number_input("Enter the value to convert", min_value=0.0, key="from_value")

    if st.button("Convert"):
        result = energy_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")


elif unit == "Pressure":
    factors = factors["pressure"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("Select From unit", options=factors.keys(), index=1)
    with col2:
        to_unit = st.selectbox("Select To unit", options=factors.keys(), index=2)

    value = st.number_input("Enter the value to convert", min_value=0.0, key="from_value")

    if st.button("Convert"):
        result = pressure_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif unit == "Speed":
    factors = factors["speed"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("Select From unit", options=factors.keys(), index=1)
    with col2:
        to_unit = st.selectbox("Select To unit", options=factors.keys(), index=2)

    value = st.number_input("Enter the value to convert", min_value=0.0, key="from_value")

    if st.button("Convert"):
        result = speed_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif unit == "Time":
    factors = factors["time"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("Select From unit", options=factors.keys(), index=1)
    with col2:
        to_unit = st.selectbox("Select To unit", options=factors.keys(), index=2)

    value = st.number_input("Enter the value to convert", min_value=0.0, key="from_value")

    if st.button("Convert"):
        result = time_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif unit == "Plane Angle":
    factors = factors["plane_angle"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("Select From unit", options=factors.keys(), index=1)
    with col2:
        to_unit = st.selectbox("Select To unit", options=factors.keys(), index=2)

    value = st.number_input("Enter the value to convert", min_value=0.0, key="from_value")

    if st.button("Convert"):
        result = plane_angle_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif unit == "Fuel Economy":
    factors = factors["fuel_economy"]
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("Select From unit", options=factors.keys(), index=1)
    with col2:
        to_unit = st.selectbox("Select To unit", options=factors.keys(), index=2)

    value = st.number_input("Enter the value to convert", min_value=0.0, key="from_value")

    if st.button("Convert"):
        result = fuel_economy_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")