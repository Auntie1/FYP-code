from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (assuming Chrome WebDriver is used)
driver = webdriver.Chrome()

# Function to check cookie policy information
def check_cookie_information(url):
    try:
        driver.get(url)
        cookie_policy_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Cookie Policy"))
        )
        cookie_policy_link.click()
        print("Cookie policy information found and accessed.")
    except:
        print("Cookie policy information not found.")

# Example usage:
URL_of_the_website = "https://www.google.co.uk/"
check_cookie_information(URL_of_the_website)

# Close the WebDriver
driver.quit()
