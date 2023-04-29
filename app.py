import streamlit as st
import joblib
import sklearn
import pandas as pd
import numpy as np

# Load the saved model
with open('model_kn.pkl', 'rb') as file:
    model = joblib.load(file)
    
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define a function to preprocess input data
def preprocess_data(df):
    # Apply any necessary preprocessing to the input dataframe
    # For example, label encoding the 'type' column as in the previous question
    le = LabelEncoder()
    df['type'] = le.fit_transform(df['type'])
    return df

# Define the Streamlit app
def app():
    # Set the page title
    st.set_page_config(page_title='Fraud Detection')

    # Define the app title and subtitle
    st.title('Fraud Detection')
    st.subheader('Detect fraudulent transactions')

    # Create a form for the user to input data
    st.sidebar.title('Input data')
    step = st.sidebar.number_input('Step', value=1)
    amount = st.sidebar.number_input('Amount', value=0.0)
    oldbalanceOrg = st.number_input('Old balance of sender account', value=0.0)
    newbalanceOrig = st.number_input('New balance of sender account', value=0.0)
    oldbalanceDest = st.number_input('Old balance of recipient account', value=0.0)
    newbalanceDest = st.number_input('New balance of recipient account', value=0.0)
    isFlaggedFraud = st.number_input('Is flagged as fraud', value=0)
    type = st.sidebar.selectbox('Transaction type', ['CASH_OUT', 'CASH_IN', 'TRANSFER', 'DEBIT', 'PAYMENT'])

    # Create a dataframe with the input data
    data = {
        'step': [step],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest],
        'isFlaggedFraud': [isFlaggedFraud],
        'type': [type]
    }
    df = pd.DataFrame(data)

    # Preprocess the input data
    df = preprocess_data(df)

    # Make predictions using the trained model
    predictions = model.predict(df)

    # Display the predictions to the user
    if predictions[0] == 0:
        st.success('This transaction is not fraudulent')
    else:
        st.error('This transaction is fraudulent')

# Run the Streamlit app
if __name__ == '__main__':
    app()


