import requests
import pandas as pd

# 🔑 Replace YOUR_API_KEY below after signing up on data.gov.in
# Go to any dataset page → Click "Get API" → Copy your unique key

RAINFALL_API = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit=100"
CROP_API = "https://api.data.gov.in/resource/ab4b0db8-d8db-4b59-8e0b-b8b48d1455b2?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&limit=100"


def fetch_rainfall_data():
    """Fetch rainfall data from IMD dataset."""
    try:
        response = requests.get(RAINFALL_API)
        response.raise_for_status()
        data = response.json().get("records", [])
        if not data:
            return pd.DataFrame({"message": ["No rainfall data found."]})
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        return pd.DataFrame({"error": [f"Error fetching rainfall data: {e}"]})

def fetch_crop_data():
    """Fetch crop production data from Ministry of Agriculture dataset."""
    try:
        response = requests.get(CROP_API)
        response.raise_for_status()
        data = response.json().get("records", [])
        if not data:
            return pd.DataFrame({"message": ["No crop data found."]})
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        return pd.DataFrame({"error": [f"Error fetching crop data: {e}"]})
