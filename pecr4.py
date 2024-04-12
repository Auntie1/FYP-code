from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (assuming Chrome WebDriver is used)
driver = webdriver.Chrome()

# Function to check strictly necessary exemption cookie
def check_strictly_necessary_exemption(url):
    try:
        driver.get(url)
        # Implement based on the cookies considered strictly necessary
        strictly_necessary_cookie = driver.find_element(By.ID, "strictly_necessary_cookie")
        print("Strictly necessary exemption cookie found.")
    except:
        print("Strictly necessary exemption cookie not found.")

# Example usage:
URL_of_the_website = "https://example.com"
check_strictly_necessary_exemption(URL_of_the_website)

# Close the WebDriver
driver.quit()
