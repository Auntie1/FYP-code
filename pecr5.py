from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (assuming Chrome WebDriver is used)
driver = webdriver.Chrome()

# Function to check Information Society Services (ISS) cookies
def check_iss_cookies(url):
    try:
        driver.get(url)
        # Implement based on cookies used for Information Society Services
        iss_cookie = driver.find_element(By.ID, "iss_cookie")
        print("ISS cookie found.")
    except:
        print("ISS cookie not found.")

# Example usage:
URL_of_the_website = "https://example.com"
check_iss_cookies(URL_of_the_website)

# Close the WebDriver
driver.quit()
