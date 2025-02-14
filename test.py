from dotenv import load_dotenv
import os
import requests

load_dotenv()
print(os.getenv("YOUTUBE_API_KEY"))

print("hello world")


# Define the API endpoint
url = "https://official-joke-api.appspot.com/random_joke"  # Example API

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Convert response to JSON
    print("Response Data:", data)
else:
    print("Error:", response.status_code, response.text)


# https://developers.google.com/youtube/reporting/v1/code_samples/python 

# might be super helfpul...

# Could we get this? - https://research.youtube/how-it-works/