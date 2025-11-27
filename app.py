# import streamlit as st
# import pandas as pd
# import numpy as np
# import pickle

# model = pickle.load(open("rf_model.pkl",'rb'))
# scaler = pickle.load(open('scaler.pkl', 'rb'))

# st.title("Cost Predictor")
# st.write("Predict your medical cost for breakthrough in life")


# age = st.number_input("Enter Age", min_value=0, max_value=100, step=1)
# sex = st.selectbox("Select Gender", ["male", "female"])
# bmi = st.number_input("Enter BMI", min_value=10.0, max_value=60.0, step=0.1)
# children = st.number_input("Number of Children", min_value=0, max_value=10, step=1)
# smoker = st.selectbox("Do you smoke?", ["yes", "no"])
# region = st.selectbox("Select Region", ["northeast", "northwest", "southeast", "southwest"])

# if st.button("Predict Insurance Cost"):
#     # Step 1: Create input DataFrame with same column names used during training
#     input_df = pd.DataFrame({
#         "age": [age],
#         "sex": [sex],
#         "bmi": [bmi],
#         "children": [children],
#         "smoker": [smoker],
#         "region": [region]
#     })

#     # Step 2: Encode categorical columns 
#     input_df['sex'] = input_df['sex'].map({'male':1, 'female':0})
#     input_df['smoker'] = input_df['smoker'].map({"yes":1,'no':0})
#     input_df['region'] = input_df['region'].map({'southeast':0,"southwest":1,'northwest':2,"northeast":3})


#     # Step 3: Scale the entire dataset
#     num_cols = ['age','bmi','children']
#     input_df[num_cols] = scaler.transform(input_df[num_cols])

#     # Step 4: Predict using the trained model
#     prediction = model.predict(input_df)

#     # Step 5: Display result
#     st.success(f"💰 Estimated Annual Insurance Charge: **${prediction[0]:,.2f}**")


import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Optional: Page setup
st.set_page_config(page_title="Medical Cost Predictor", layout="centered")

# Load model and scaler
model = pickle.load(open("rf_model.pkl",'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# ---- Add Background Image ----
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1605379399642-870262d3d051");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# ---- App UI ----
st.title("Medical Cost Predictor")
st.write("Predict your medical cost for better financial planning ")

age = st.number_input("Enter Age", min_value=0, max_value=100, step=1)
sex = st.selectbox("Select Gender", ["male", "female"])
bmi = st.number_input("Enter BMI", min_value=10.0, max_value=60.0, step=0.1)
children = st.number_input("Number of Children", min_value=0, max_value=10, step=1)
smoker = st.selectbox("Do you smoke?", ["yes", "no"])
region = st.selectbox("Select Region", ["northeast", "northwest", "southeast", "southwest"])

if st.button("Predict Insurance Cost"):
    input_df = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region]
    })

    input_df['sex'] = input_df['sex'].map({'male': 1, 'female': 0})
    input_df['smoker'] = input_df['smoker'].map({'yes': 1, 'no': 0})
    input_df['region'] = input_df['region'].map({'southeast': 0, 'southwest': 1, 'northwest': 2, 'northeast': 3})

    num_cols = ['age', 'bmi', 'children']
    input_df[num_cols] = scaler.transform(input_df[num_cols])

    prediction = model.predict(input_df)
    st.success(f"💰 Estimated Annual Insurance Charge: **${prediction[0]:,.2f}**")
