# Author: Rohit Singh
# GitHub: https://github.com/rohitsinghxyz
# LinkedIn: https://www.linkedin.com/in/rohitsinghxyz
# Project: Lending Club - Interest Rate Predictor

import joblib
import streamlit as st
import pandas as pd
import numpy as np
from xgboost import XGBRegressor

st.markdown("""
<style>
.big-font {
    font-size:150px !important;  color:Red;
}
</style>
""", unsafe_allow_html=True)

st.title('''
Lending Club - Interest Rate Predictor
This app predicts P2P loan interest rate based on user inputs.
''')
st.write('---')

st.sidebar.header('Loan Applicant Information')

@st.cache(hash_funcs={XGBRegressor: id})
def load_model():
    model = joblib.load('data/xgb_fitgrid_best_estimator.pkl')
    return model

model = load_model()

# Numeric - Loan Amount
loan_amount = st.sidebar.number_input(
    'Loan Amount (Min $1000, Max $40,000)', min_value=1000, max_value=40000, step=1
)

# Categorical - Loan Term
loan_term = st.sidebar.radio(
    'Loan Term',
    ('36 months', '60 months')
)

# Categorical - Loan Purpose
loan_purpose = st.sidebar.selectbox(
    'Loan Purpose',
    ('debt_consolidation', 'small_business', 'home_improvement',
    'major_purchase', 'credit_card', 'other', 'house', 'car',
    'medical', 'vacation', 'moving', 'renewable_energy', 'wedding',
    'educational')
)

# Numeric - Annual Income
annual_income = st.sidebar.number_input(
    'Annual Income (Min $1900)', min_value=1900, max_value=110000000, step=1
)

# Numeric - FICO Score
fico = st.sidebar.number_input(
    'FICO score (Min 662, Max 850)', min_value=662, max_value=850, step=1
)

# Numeric - Mortgage Accounts
mortgage = st.sidebar.number_input(
    'Number of Mortgages (Min 0, Max 94)', min_value=0, max_value=94, step=1
)

# Categorical - Home Ownership
home_owner = st.sidebar.radio(
    'Home ownership status',
    ('OWN', 'RENT', 'MORTGAGE')
)

# Categorical - Disbursement Method
disbursement = st.sidebar.radio(
    'Disbursement Method',
    ('Cash', 'DirectPay')
)

# Categorical - Verification Status
verification = st.sidebar.radio(
    'Verification Status',
    ('Verified', 'Source Verified', 'Not Verified')
)
# Categorical - Bankruptcies
bankrupt = st.sidebar.radio(
    'Bankruptcies',
    ('pub_rec_bankruptcies_0', 'pub_rec_bankruptcies_1+')
)

# Categorical - Adverse Public Records
pub_records = st.sidebar.radio(
    'Adverse Public Records',
    ('pub_rec_0', 'pub_rec_1', 'pub_rec_2+')
)

# Categorical - Tax Liens
tax_lien = st.sidebar.radio(
    'Tax Liens',
    ('tax_liens_0', 'tax_liens_1+')
)

# Numeric - dti
dti = st.sidebar.number_input(
    'DTI', disabled=True
)

# Numeric - open_acc
open_acc = st.sidebar.number_input(
    'Open Accounts', disabled=True
)

# Numeric - num_bc_sats
num_bc_sats = st.sidebar.number_input(
    'Bankcard Accounts', disabled=True
)

user_df = pd.DataFrame(
    {'loan_amnt': [loan_amount],
    'term': [loan_term],
    'purpose': [loan_purpose],
    'annual_inc': [annual_income],
    'fico_range_avg': [fico],
    'home_ownership': [home_owner],
    'mort_acc': [mortgage],
    'disbursement_method': [disbursement],
    'verification_status': [verification],
    'pub_rec_bankruptcies_bin': [bankrupt],
    'pub_rec_bin': [pub_records],
    'tax_liens_bin': [tax_lien],
    'dti': [dti],
    'open_acc': [open_acc],
    'num_bc_sats': [num_bc_sats]}
)

int_rate = model.predict(user_df)

st.write("Your predicted P2P loan interest rate is:")
st.write(f'<p class="big-font">{np.around(int_rate, decimals=2)}%</p>', unsafe_allow_html=True)
