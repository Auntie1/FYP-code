import requests
from http.cookiejar import CookieJar

# Create a session to persist cookies across requests
session = requests.Session()

# Send a request and store the cookies in the cookie jar
response = session.get('https://www.ebay.co.uk/')

# Print the response headers
print("Initial Response Headers:", response.headers)

# Print the received cookies
print("Initial Cookies:", session.cookies)

# Make another request using the same session to include the cookies
response = session.get('https://www.ebay.co.uk/')

# Print the response headers
print("Updated Response Headers:", response.headers)

# Print the updated cookies
print("Updated Cookies:", session.cookies)
