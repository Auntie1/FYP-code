
import requests
from http.cookies import SimpleCookie

def classify_cookie(cookie):
    expires = cookie.get("expires")
    if expires is not None:
        return "Persistent"
    elif cookie.get("httponly"):
        return "HttpOnly Session"
    else:
        return "Session"

url = "https://www.google.co.uk/"
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
for cookie_name, cookie in received_cookies.items():
    classification = classify_cookie(cookie)
    print(f"Cookie Name: {cookie_name}, Classification: {classification}, Cookie Value: {cookie.value}")
