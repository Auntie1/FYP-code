from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (assuming Chrome WebDriver is used)
driver = webdriver.Chrome()

# Function to check consent mechanism
def check_consent_mechanism(url):
    try:
        driver.get(url)
        consent_banner = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cookie-consent-banner"))
        )
        print("Consent mechanism found.")
    except:
        print("Consent mechanism not found.")

# Example usage:
URL_of_the_website = "https://example.com"
check_consent_mechanism(URL_of_the_website)

# Close the WebDriver
driver.quit()
