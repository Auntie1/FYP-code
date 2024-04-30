import logging  # Import the logging module for logging
from selenium import webdriver  # Import Selenium's webdriver module for browser automation
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException  # Import exceptions for error handling
from selenium.webdriver.common.by import By  # Import By class for locating elements
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Import expected_conditions for defining expected conditions
from selenium.webdriver.chrome.options import Options  # Import Options class to configure Chrome WebDriver
#More accurate result comes from not using Beautiful Soup in this code 

class Granular:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Initialize Chrome WebDriver instance
        self.driver.implicitly_wait(10)  # Set implicit wait time to 10 seconds
        self.page_load_timeout = 30  # Set timeout for page loading to 30 seconds
        self.keywords = [
            "granular consent", "specific consent", "individual consent",
            "opt-in preferences", "select cookies", "customise preferences",
            "manage cookies", "cookie settings", "cookie preferences",
            "cookie options", "privacy settings", "privacy preferences",
            "cookie policy", "cookie choices", "customise my choices"
        ]  # Keywords indicating granular consent

    def check_granular_consent(self, websites):
        """
        Check for granular consent on the provided list of websites.

        Parameters:
        - websites (list): List of website URLs to check.

        Returns:
        - None
        """
        for website in websites:
            print("Checking granular consent for", website)
            try:
                self.driver.get(website)  # Open the website URL
                
                # Wait for the page to be fully loaded
                WebDriverWait(self.driver, self.page_load_timeout).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'body'))
                )
                
                # Search for keywords indicating granular consent
                granular_consent_found = any(keyword in self.driver.page_source.lower() for keyword in self.keywords)
                
                # Print results based on findings
                if granular_consent_found:
                    print("Granular consent is provided.")
                else:
                    print("Granular consent is not provided or indicated.")
            except TimeoutException:
                print("Timeout occurred while loading the page.")
            except NoSuchElementException:
                print("Element not found on the page.")
            except WebDriverException as e:
                print("WebDriver error:", e)
            except Exception as e:
                print("Error occurred:", e)
            finally:
                self.driver.delete_all_cookies()  # Clear cookies after each website check

# Example usage:
if __name__ == "__main__":
    checker = Granular()  # Create an instance of Granular
    websites_to_check = [
        "https://www.bbc.co.uk/news", "https://www.birminghammail.co.uk/", 
       "https://www.independent.co.uk/", "https://news.sky.com/uk", "https://www.ebay.co.uk/", "https://www.amazon.co.uk/",
       "https://www.shein.co.uk", "https://www.asos.com/", "https://www.facebook.com/login/", 
       "https://twitter.com/?lang=en", "https://www.instagram.com/", 
       "https://uk.linkedin.com/"
    ]  # List of websites to check for granular consent
    checker.check_granular_consent(websites_to_check)
