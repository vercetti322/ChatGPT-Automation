# library to send or recieve HTTP requests for OpenAI API
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help = "The prompt to send to OpenAI API")
parser.add_argument("file_name", help = "Nmae of the file to save Python scripts")
args = parser.parse_args()

# What is the endpoint (= specific location or URL to access a specific service)
# our API_endpoint is where our API_key will take us.
API_endpoint = "https://api.openai.com/v1/completions"
API_key = "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"

# Meta-Data
request_header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + API_key
}

# for 'temperature', value '0' is max creativity and '1' is abt being precise.
# Actual Data
request_data = {
  "model": "text-davinci-003",
  "prompt": f"Write python script for {args.prompt}. Provide only code, no text",
  "max_tokens": 1000,
  "temperature": 0.5
}

# we will send our key to endpoint via below function
response = requests.post(API_endpoint, headers = request_header, json = request_data)

# we send two informations in a request - Header (Meta-Data) & Body (actual)
if response.status_code == 200:
    response_text = (response.json()["choices"][0]["text"]) # first element of 'choices' object
    with open(args.file_name, "w") as file:
        file.write(response_text)
else:
    print(f"Request FAILED, here is the status code: {str(response.status_code)}")

