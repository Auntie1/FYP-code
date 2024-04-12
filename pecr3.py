from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (assuming Chrome WebDriver is used)
driver = webdriver.Chrome()

# Function to check communication exemption cookie
def check_communication_exemption(url):
    try:
        driver.get(url)
        # Implement based on the cookies used for communication purposes
        communication_cookie = driver.find_element(By.ID, "communication_cookie")
        print("Communication exemption cookie found.")
    except:
        print("Communication exemption cookie not found.")

# Example usage:
URL_of_the_website = "https://example.com"
check_communication_exemption(URL_of_the_website)

# Close the WebDriver
driver.quit()
