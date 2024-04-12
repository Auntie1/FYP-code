import requests
from http.cookiejar import CookieJar

# Create a session to persist cookies across requests
session = requests.Session()

# Send a request and store the cookies in the cookie jar
response = session.get('https://www.amazon.co.uk/')

# Print the received cookies
print("Initial Cookies:", session.cookies)  # Explanation: Prints the cookies stored in the session after the first request.

# Make another request using the same session to include the cookies
response = session.get('https://www.amazon.co.uk/')

# Print the updated cookies
print("Updated Cookies:", session.cookies)  # Explanation: Prints the cookies stored in the session after the second request.

# Purpose: The purpose of using a session is to persist cookies across multiple requests.
# This is useful for scenarios where you want to maintain a session state, such as staying logged in on a website or carrying other session-specific information.
# The CookieJar within the session automatically manages the cookies for subsequent requests, simplifying the process of handling cookies.
