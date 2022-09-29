## Project Title: Lending Club – Interest Rate Predictor

**Author Name:** Rohit Singh - [GitHub](https://github.com/rohitsinghxyz) - [LinkedIn](https://www.linkedin.com/in/rohitsinghxyz)


1. Please download the ‘All Lending Club loan data’ data set from [Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club).

2. We are focussed only on the ‘accepted_2007_to_2018Q4.csv’ file.

3. The Anaconda environment used for the project can be installed by typing the following command in your terminal:

    conda create -n mynewenv --file Environment.txt
    
    You can pick your own environment name (mynewenv). Please make sure to enter the correct file path.

4. The Jupyter notebooks should be opened in this order:
    - 1_Preprocessing.ipynb
    - 2_Exploratory_Data_Analysis.ipynb
    - 3_Model_Prep.ipynb
    - 4_Model_Decision Tree.ipynb
    - 5_Model_Random Forest.ipynb
    - 6_Model_XG Boost.ipynb

**Interactive Interest Rate Predictor App**

There is a functional Streamlit app in this repo that allows a loan applicant to enter their details and the latest model will output their expected P2P loan interest rate (keeping in mind the RMSE error).

However, due to privacy concerns (Streamlit wants access to all your repos - public and private), I have decided not to deploy the app on Streamlit Cloud for now.

You can try out the app locally on your machine using the 'interest-rate-predictor-app' folder in the repo.
