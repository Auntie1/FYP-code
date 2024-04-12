import requests
from http.cookies import SimpleCookie
from urllib.parse import urlparse, unquote

def classify_cookie(cookie_domain, cookie_expires):
    # Check if the cookie has an expiration time
    if cookie_expires:
        return "3rd Party"  # If it has an expiration, it's likely a 3rd party cookie

    # Extract the domain from the URL of the cookie
    domain = urlparse(cookie_domain).hostname

    # Check if the cookie domain matches the request domain
    if domain == urlparse(url).hostname:
        return "1st Party"
    else:
        return "3rd Party"

url = "https://www.google.co.uk/webhp?hl=en&ictx=2&sa=X&ved=0ahUKEwi1urK7loqEAxUsWkEAHTn7CPIQPQhr"
cookies = {'cookie_name': 'cookie_value'}  # Replace with your actual cookies

response = requests.get(url, cookies=cookies)

# Check the cookies in the response
received_cookies = SimpleCookie()
received_cookies.load(response.headers.get('Set-Cookie', ''))

# Print the number of received cookies
num_received_cookies = len(received_cookies)
print(f"Number of Received Cookies: {num_received_cookies}")

# Print the received cookies and their classification
print("\nReceived Cookies:")
for cookie_name, cookie_value in received_cookies.items():
    cookie_domain = unquote(cookie_value['domain']) if 'domain' in cookie_value else ""
    cookie_expires = cookie_value['expires'] if 'expires' in cookie_value else ""

    # Classify the cookie
    classification = classify_cookie(cookie_domain, cookie_expires)

    print(f"Cookie Name: {cookie_name}, Cookie Value: {cookie_value.value}, Classification: {classification}")
