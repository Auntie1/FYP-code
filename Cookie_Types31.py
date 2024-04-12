import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # Add this import statement
from urllib.parse import urlparse
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def classify_cookie(url, cookie_domain, cookie_expires):
    if cookie_expires:
        return "3rd Party"
    domain = urlparse(cookie_domain).hostname
    if domain == urlparse(url).hostname:
        return "1st Party"
    else:
        return "3rd Party"

# List of URLs to check
urls = [ "https://www.amazon.co.uk/"]

# Initialize WebDriver (assuming Chrome WebDriver is used)
driver = webdriver.Chrome()

for url in urls:
    try:
        # Visit the URL to capture cookies
        driver.get(url)
        
        # Wait for the page to fully load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        
        # Introduce a delay to ensure all dynamic content is loaded, including cookies
        time.sleep(2)
        
        # Get the cookies from the browser
        browser_cookies = driver.get_cookies()

        # Print the received cookies for the current URL and their classification
        print(f"\nProcessing URL: {url}")
        print("Received Cookies:")
        for cookie in browser_cookies:
            cookie_name = cookie['name']
            cookie_value = cookie['value']
            cookie_domain = cookie['domain'] if 'domain' in cookie else ""
            cookie_expires = cookie['expiry'] if 'expiry' in cookie else ""
            classification = classify_cookie(url, cookie_domain, cookie_expires)
            print(f"Cookie Name: {cookie_name}, Cookie Value: {cookie_value}, Classification: {classification}")

    except TimeoutException:
        print(f"Timeout occurred while loading URL: {url}")

# Close the WebDriver after processing all URLs
driver.quit()
