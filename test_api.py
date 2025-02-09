import requests

# Define the API URL
BASE_URL = "http://127.0.0.1:8000"

def test_health_check():
    """Checks if the API is running"""
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200

    expected_message = "Welcome to the Fraud Detection API! Use /predict/ to make predictions."
    assert response.json() == {"message": expected_message}


def test_prediction():
    """Checks that the API returns a valid response for prediction"""
    sample_data = {
  "features": [[0.1, -1.5, 2.3, 0.8, -0.6, 0.4, -2.1, 1.7, 0.3, -0.5, 0.9, -1.2, 1.8, 0.2, -0.8, 0.5, -0.3, 0.7, -0.1, 2.0, -1.0, 1.5, 0.6, -1.7, 0.9, -0.4, 0.3, 0.1, -0.2, 0.5]]
}

    response = requests.post(f"{BASE_URL}/predict/", json=sample_data)
    
    assert response.status_code == 200
    assert "fraud_predictions" in response.json() # Must have a prediction value