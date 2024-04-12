from selenium import webdriver
from http.cookies import SimpleCookie
from urllib.parse import urlparse

def classify_cookie(cookie_domain, cookie_value):
    # Check if the cookie is a session cookie
    if not cookie_value:
        return "Session Cookie"
    
    # Extract the domain from the cookie_domain
    domain = urlparse(cookie_domain).hostname

    # Check if the cookie domain matches the request domain
    if domain == urlparse(url).hostname:
        return "1st Party Cookie"
    else:
        return "3rd Party Cookie"

# Set the URL
url = "https://www.ebay.co.uk/"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)

# Get all cookies from the browser session
browser_cookies = driver.get_cookies()

# Print the received cookies and their classification
print("\nReceived Cookies:")
cookie_count = 0
for cookie in browser_cookies:
    # Get the cookie name, value, and domain
    cookie_name = cookie['name']
    cookie_value = cookie['value']
    cookie_domain = cookie['domain']

    # Classify the cookie
    classification = classify_cookie(cookie_domain, cookie_value)

    print(f"Cookie Name: {cookie_name}, Cookie Value: {cookie_value}, Classification: {classification}")
    cookie_count += 1

# Print the count of received cookies
print(f"\nTotal Cookies Received: {cookie_count}")

# Quit the WebDriver session
driver.quit()
