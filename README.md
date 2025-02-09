# Credit Card Fraud Detection

## About the Project
This project provides a REST API to detect fraudulent credit card transactions. The API uses a trained machine learning model to receive input, process transactions, and return fraud predictions.

### Features:

- Fraud detection for credit card transactions
- Built with FastAPI
- Automated testing with pytest
- Deployment-ready with Docker
- Swagger API documentation (/docs)

## Dataset
This project uses the Credit Card Fraud Detection dataset from [Credit Card Fraud Detection on Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud), provided by Machine Learning Group - ULB which contains transactions made by credit cards in September 2013 by European cardholders.

### Dataset Overview:

- Contains 284,807 transactions, with 492 fraudulent cases (0.172%)
- Features are numerical, extracted using PCA (Principal Component Analysis)
- The dataset is highly imbalanced, requiring special handling in model training

### Usage:
- Used for training the fraud detection model
- Preprocessed and split into train/test datasets
- Handles class imbalance using oversampling/undersampling techniques


## Installation
Clone the repository and install dependencies:

    git clone https://github.com/ghsaberr/credit-card-fraud-detection.git
    cd credit-card-fraud-detection
    pip install -r requirements.txt

## Run the API

    uvicorn app:app --reload

Now the API is running at:
`http://127.0.0.1:8000/docs`

## Example Request
To send a test request, use:

{
  "features": [[0.1, -1.5, 2.3, 0.8, -0.6, 0.4, -2.1, 1.7, 0.3, -0.5, 
                0.9, -1.2, 1.8, 0.2, -0.8, 0.5, -0.3, 0.7, -0.1, 2.0, 
                -1.0, 1.5, 0.6, -1.7, 0.9, -0.4, 0.3, 0.1, -0.2, 0.5]]
}

## Running Tests
To run automated tests:
`pytest test_api.py -v`



