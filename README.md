# house-price-predicitor
A Machine Learning web application built with Streamlit that predicts house prices based on user inputs like location, square footage, number of bedrooms, bathrooms, and balconies.

🚀 Features

Interactive Streamlit UI with background image

Input fields for location, sqft, bedrooms, bathrooms, balconies

Predicts house price using a trained ML model

Clean and styled result display

Uses pickle for model deployment

🛠 Tech Stack

Python

Pandas – Data processing

Scikit-learn – ML model

Streamlit – Web app framework

Pickle – Model serialization

📂 Project Structure
├── house_price_pridiction.pk1     # Saved ML model
├── cleaned_data.csv               # Dataset after preprocessing
├── app.py                         # Streamlit app code
├── requirements.txt               # Required Python libraries
└── README.md                      # Project documentation

⚡ How to Run

Clone the repo:

git clone https://github.com/<your-username>/house-price-predicitor.git
cd house-price-predicitor


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py


The app will open in your browser at:

http://localhost:8501

📊 Example Prediction

Input:

Location: Bangalore

Sqft: 1200

Bedrooms: 3

Bathrooms: 2

Balconies: 1

Output:

💰 Predicted Price: ₹ 75,00,000

# 🏡 House Price Predictor

![App Screenshot](images/Screenshot 2025-08-31 201401.png)


