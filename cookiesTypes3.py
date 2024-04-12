import requests
from http.cookies import SimpleCookie
from urllib.parse import urlparse, unquote

def classify_cookie(url, cookie_domain, cookie_expires):
    if cookie_expires:
        return "3rd Party"
    domain = urlparse(cookie_domain).hostname
    if domain == urlparse(url).hostname:
        return "1st Party"
    else:
        return "3rd Party"

url = "https://www.ebay.co.uk/"

# Remove the 'cookies' parameter from the request
response = requests.get(url)

# Print the entire response headers
print("Response Headers:")
print(response.headers)

# Check the cookies in the response
received_cookies = SimpleCookie()
received_cookies.load(response.headers.get('Set-Cookie', ''))

# Print the number of received cookies
num_received_cookies = len(received_cookies)
print(f"\nNumber of Received Cookies: {num_received_cookies}")

# Print the received cookies and their classification
print("\nReceived Cookies:")
for cookie_name, cookie_value in received_cookies.items():
    cookie_domain = unquote(cookie_value['domain']) if 'domain' in cookie_value else ""
    cookie_expires = cookie_value['expires'] if 'expires' in cookie_value else ""
    classification = classify_cookie(url, cookie_domain, cookie_expires)
    print(f"Cookie Name: {cookie_name}, Cookie Value: {cookie_value.value}, Classification: {classification}")
