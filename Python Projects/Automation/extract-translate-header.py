

# Import necessary libraries
import requests 
from bs4 import BeautifulSoup
from googletrans import Translator

# Make a request to the webpage
url = '<url>'
req = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(req.text, 'html.parser')

# Extract all headers from the page
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Initialize the translator
translator = Translator()

# Translate the headers to Hindi
translated_headers = []
for header in headers:
    translated_headers.append(translator.translate(header.text, dest='hi').text)

# Create a HTML file
html_file = open('translated_headers.html', 'w')

# Write the translated headers to the HTML file
html_file.write('<html>\n')
for header in translated_headers:
    html_file.write('<p>' + header + '</p>\n')
html_file.write('</html>')

# Close the HTML file
html_file.close()