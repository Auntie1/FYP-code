import time  # Import time module for time-related operations
#import logging  # Import logging module for logging messages
from selenium import webdriver  # Import Selenium web automation library
from selenium.webdriver.common.by import By  # Import By class for locating elements
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for waiting for elements
from selenium.webdriver.support import expected_conditions as EC  # Import expected_conditions for defining wait conditions
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException  # Import specific exceptions from Selenium

# The class `AcceptCookies` handles the process of accepting cookies on web pages.
class AcceptCookies:
    def __init__(self, url):
        """
        Initialize AcceptCookies with the URL to scrape.

        Parameters:
        - url (str): The URL of the website to scrape.
        """
        self.url = url
        self.driver = webdriver.Chrome()  # Initialize a Chrome webdriver
        self.driver.maximize_window()  # Maximize the window for better visibility
    
    def scrape_cookie_data(self):
        """
        Scrape cookie data from the specified URL.
        """
        try:
            self.driver.get(self.url)  # Open the URL in the browser
            self.accept_cookies()  # Accept cookies if prompted
            self.print_cookie_data()  # Print received cookies
        except TimeoutException:
            print("Timeout: Page elements not found.")
        finally:
            self.driver.quit()  # Close the browser after scraping
    
    def accept_cookies(self):
        """
        Accept cookies if an accept button is found.
        """
        try:
            accept_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.get_xpath_for_accept_button()))
            )  # Wait for the accept button to be clickable
            accept_button.click()  # Click the accept button directly
            print("Cookies accepted.")
        except TimeoutException:
            print("Accept button not found or could not be clicked.")
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException: Element is not clickable at point. Trying scrolling and clicking again.")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", accept_button)  # Scroll to the accept button
            time.sleep(1)  # Give some time for the page to scroll
            accept_button.click()  # Click the accept button again
            print("Cookies accepted after scrolling.")

    def get_xpath_for_accept_button(self):
        """
        Generate XPath for accept button based on keywords.

        Returns:
        - str: XPath expression for finding the accept button.
        """
        # Keywords commonly used for accept buttons
        accept_button_keywords = ['accept', 'agree', 'ok', 'I agree', 'yes thats ok', 'accept all', 'yes I agree']
        # Construct XPath expression to find accept buttons containing any of the keywords
        accept_keywords_xpath = " or ".join(f"contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{keyword.lower()}')" for keyword in accept_button_keywords)
        return f"//button[{accept_keywords_xpath}]"

    def print_cookie_data(self):
        """
        Print received cookies along with their classification.
        """
        print("\nProcessing URL:", self.url)
        cookies = self.driver.get_cookies()  # Get all cookies received from the website
        if cookies:
            print("Received Cookies:")
            # Print each cookie's name, value, and classification
            for cookie in cookies:
                print(f"Cookie Name: {cookie['name']}, Cookie Value: {cookie['value']}, Classification: {self.classify_cookie(cookie)}")
            print(f"Total Cookies Received for {self.url}: {len(cookies)}")
        else:
            print("No cookies received.")

    @staticmethod
    def classify_cookie(cookie):
        """
        Classify cookies as session, 1st party, or 3rd party based on name and expiry.

        Parameters:
        - cookie (dict): Cookie object containing name, value, and expiry information.

        Returns:
        - str: Classification of the cookie.
        """
        # Check if the word 'session' is present in the cookie's name
        if 'session' in cookie['name'].lower():
            return "Session Cookie"
        # Check if the cookie has an expiry time, if not, it's a 1st party cookie
        elif cookie.get('expiry', 0) == 0:
            return "1st Party Cookie"
        else:
            return "3rd Party"

if __name__ == "__main__":
    # List of URLs to scrape
    urls = [
       "https://www.bbc.co.uk/news", "https://www.birminghammail.co.uk/", 
       "https://www.independent.co.uk/", "https://news.sky.com/uk", "https://www.ebay.co.uk/", "https://www.amazon.co.uk/",
       "https://www.shein.co.uk", "https://www.asos.com/", "https://www.facebook.com/login/", 
       "https://twitter.com/?lang=en", "https://www.instagram.com/", 
       "https://uk.linkedin.com/"
    ]
    
     # logger = setup_logger()  # Setup logger configuration
    # Iterate over each URL and scrape cookie data
    for url in urls:
        scraper = AcceptCookies(url) #logger)
        scraper.scrape_cookie_data()
