import streamlit as st
import pickle
import numpy as np



def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

classification = data["model"]


def show_predict_page():
    st.markdown(
    '''
    <style>
    .stApp {
        background: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
        background-size: cover;
    }
    </style>
    ''', 
    unsafe_allow_html=True
    )
    
#title
    st.title("Liver Problem Prediction")
# sub-title
    st.write("""### please fill the details below""")

# user input
    age = st.slider("Select your age", 0, 100, 18)
    gender = st.selectbox("Select gender", ["Male", "Female"])
    tot_bilirubin = st.number_input("Enter total bilirubin", min_value=0.0, max_value=None, value=0.0)
    direct_bilirubin = st.number_input("Enter direct bilirubin", min_value=0.0, max_value=None, value=0.0)
    tot_proteins = st.number_input("Enter total proteins", min_value=0.0, max_value=None, value=0.0)
    albumin = st.number_input("Enter albumin", min_value=0.0, max_value=None, value=0.0)
    ag_ratio = st.number_input("Enter albumin/globulin ratio", min_value=0.0, max_value=None, value=0.0)
    sgpt = st.number_input("Enter SGPT (ALT)", min_value=0.0, max_value=None, value=0.0)
    sgot = st.number_input("Enter SGOT (AST)", min_value=0.0, max_value=None, value=0.0)
    alkphos = st.number_input("Enter alkaline phosphatase", min_value=0.0, max_value=None, value=0.0)

# gender convert to numeric
    gender_mapping = {"Male": 1, "Female": 0}
    gender_numeric = gender_mapping[gender]

# create predict button
    ok = st.button("Submit")
    if ok:
        x = np.array([[age, gender_numeric, tot_bilirubin, direct_bilirubin, tot_proteins, albumin, ag_ratio, sgpt, sgot, alkphos]])
        
        patient = classification.predict(x)
        result_mapping = {1: "Has liver problem", 2: "Patient is healthy"}
        result_label = result_mapping.get(int(patient), "Unknown result")

        # Display the result
        st.subheader(f"Prediction: {result_label}")


