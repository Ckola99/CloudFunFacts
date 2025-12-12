import requests
import json


API_ENDPOINT = "https://o20rdj2sdi.execute-api.eu-north-1.amazonaws.com/funfact"

def test_fun_fact_endpoint():
    print(f"Testing API Endpoint: {API_ENDPOINT}")
    print("---------------------------------------")

    try:
        # Send the GET request
        response = requests.get(API_ENDPOINT)

        # Check if the request was successful (HTTP 200)
        if response.status_code == 200:
            print("✅ SUCCESS: API returned status 200 (OK).")

            # The .json() method automatically parses the JSON body
            data = response.json()

            print(f"Response Status: {response.status_code}")
            print("Response Body:")
            print(json.dumps(data, indent=4))

            # Additional check: Verify the expected key exists
            if 'fact' in data:
                print(f"Fact retrieved: {data['fact']}")
            else:
                print("FAILURE: Response body does not contain the 'fact' key.")

        else:
            print(f"FAILURE: API returned status {response.status_code}")
            print(f"Error Body: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"CONNECTION ERROR: Could not connect to the API endpoint. Details: {e}")

if __name__ == "__main__":
    test_fun_fact_endpoint()
