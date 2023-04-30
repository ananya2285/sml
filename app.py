import streamlit as st
import joblib
import sklearn
import pandas as pd
import numpy as np

# Load the saved model
with open(r'model_rfc.pkl', 'rb') as file:
    model = joblib.load(file)


# Create the Streamlit app
def app():
    # Set app title and header
    st.set_page_config(page_title='Fraud Detection App', page_icon=':money_with_wings:',  page_bg_color='#87CEFA')
    st.title('Fraud Detection App')
    st.subheader('Detect fraudulent transactions')

    # Create input fields for user to enter data
    st.subheader('Enter transaction details:')
    step = st.number_input('Step', min_value=1)
    amount = st.number_input('Amount', min_value=0.0)
    oldbalanceOrg = st.number_input('Old Balance Org', min_value=0.0)
    newbalanceOrig = st.number_input('New Balance Orig', min_value=0.0)
    oldbalanceDest = st.number_input('Old Balance Dest', min_value=0.0)
    newbalanceDest = st.number_input('New Balance Dest', min_value=0.0)
    isFlaggedFraud = st.number_input('Is Flagged Fraud', min_value=0)
    type = st.selectbox('Type of payment', ['CASH_OUT', 'TRANSFER', 'DEBIT', 'PAYMENT'])

    # Create input array based on user input
    input_array = []
    input_array.append(step)
    input_array.append(amount)
    input_array.append(oldbalanceOrg)
    input_array.append(newbalanceOrig)
    input_array.append(oldbalanceDest)
    input_array.append(newbalanceDest)
    input_array.append(isFlaggedFraud)
    if (type == 'CASH_OUT'):
        input_array.append(1)
        input_array.append(0)
        input_array.append(0)
        input_array.append(0)
    elif (type == 'TRANSFER'):
        input_array.append(0)
        input_array.append(1)
        input_array.append(0)
        input_array.append(0)
    elif (type == 'DEBIT'):
        input_array.append(0)
        input_array.append(0)
        input_array.append(1)
        input_array.append(0)
    else:
        input_array.append(0)
        input_array.append(0)
        input_array.append(0)
        input_array.append(1)

    # When the user clicks the 'Predict' button, make a prediction
    if st.button('Predict'):
        # Preprocess the user input
        # input_array = preprocess_input(step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, isFlaggedFraud, type_PAYMENT)

        # Make a prediction
        prediction = model.predict([input_array])[0]

        # Display the prediction to the user
        if prediction == 0:
            st.success('This transaction is not fraudulent.')
        else:
            st.error('This transaction is fraudulent.')


app()

