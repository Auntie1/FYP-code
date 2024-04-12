import requests
from http.cookies import SimpleCookie
from urllib.parse import urlparse, unquote

def classify_cookie(cookie_domain, cookie_value):
    # Check if the cookie is a session cookie
    if not cookie_value:
        return "Session Cookie"

    # Extract the domain from the URL of the cookie
    domain = urlparse(cookie_domain).hostname

    # Check if the cookie domain matches the request domain
    if domain == urlparse(url).hostname:
        return "1st Party Cookie"
    else:
        return "3rd Party Cookie"

url = "https://www.ebay.co.uk/"
cookies = {'cookie_name': 'cookie_value'}  # Replace with your actual cookies

response = requests.get(url, cookies=cookies)

# Check the cookies in the response
received_cookies = SimpleCookie()
received_cookies.load(response.headers.get('Set-Cookie', ''))

# Print the received cookies and their classification
print("\nReceived Cookies:")
cookie_count = 0
for cookie_name, cookie_value in received_cookies.items():
    # Set cookie_domain to an empty string for simplicity
    cookie_domain = ""

    # Classify the cookie
    classification = classify_cookie(cookie_domain, cookie_value.value)

    print(f"Cookie Name: {cookie_name}, Cookie Value: {cookie_value.value}, Classification: {classification}")
    cookie_count += 1

# Print the count of received cookies
print(f"\nTotal Cookies Received: {cookie_count}")
