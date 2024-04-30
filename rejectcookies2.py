import time  # Import time module for time-related operations
#import logging  # Import logging module for logging messages
from selenium import webdriver  # Import Selenium web automation library
from selenium.webdriver.common.by import By  # Import By class for locating elements
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for waiting for elements
from selenium.webdriver.support import expected_conditions as EC  # Import expected_conditions for defining wait conditions
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException  # Import specific exceptions from Selenium

# The class `RejectCookies` handles the process of rejecting cookies on web pages.
class RejectCookies:
    def __init__(self, url, logger):
        """
        Initialize RejectCookies with the URL to scrape and the logger.
        
        Args:
        - url (str): The URL to scrape for cookies.
        - logger (logging.Logger): The logger instance for logging messages.
        """
        self.url = url
        self.driver = webdriver.Chrome()  # Initialize a Chrome webdriver
        self.driver.maximize_window()  # Maximize the window for better visibility
        self.logger = logger

    def scrape_cookie_data(self):
        """
        Scrape cookie data from the specified URL.
        """
        try:
            self.driver.get(self.url)  # Open the URL in the browser
            self.reject_cookies()  # Reject cookies if a reject button is found
            self.print_cookie_data()  # Print received cookies along with their classification
        except TimeoutException:
            self.logger.error("Timeout: Page elements not found.")
        finally:
            self.driver.quit()  # Close the browser after scraping
    
    def reject_cookies(self):
        """
        Reject cookies if a reject button is found.
        """
        try:
            # Waiting for the reject button to be clickable
            reject_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.get_xpath_for_reject_button()))
            )
            reject_button.click()  # Click the reject button directly, no need for JavaScript executor
            self.logger.info("Cookies rejected.")
        except TimeoutException:
            self.logger.error("Reject button not found or could not be clicked.")
        except ElementClickInterceptedException:
            self.logger.error("ElementClickInterceptedException: Element is not clickable at point. Trying scrolling and clicking again.")
            # Scroll to the reject button and click again
            self.driver.execute_script("arguments[0].scrollIntoView(true);", reject_button)
            time.sleep(1)  # Give some time for the page to scroll
            reject_button.click()
            self.logger.info("Cookies rejected after scrolling.")

    def get_xpath_for_reject_button(self):
        """
        Generate XPath for reject button based on keywords.
        """
        # Keywords related to rejecting cookies
        reject_button_keywords = ['reject', 'deny', 'decline', 'no thanks', 'no thank you', 'decline all', 'deny all', 'refuse non-essential cookies', 'decline all cookies']
        # Generating XPath based on keywords
        reject_keywords_xpath = " or ".join(f"contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{keyword.lower()}')" for keyword in reject_button_keywords)
        return f"//button[{reject_keywords_xpath}]"

    def print_cookie_data(self):
        """
        Print received cookies along with their classification.
        """
        cookies = self.driver.get_cookies()
        printed_cookies = set()  # To keep track of printed cookies
        if cookies:
            self.logger.info(f"\nProcessing URL: {self.url}")
            self.logger.info("Received Cookies:")
            for cookie in cookies:
                # Constructing cookie information string
                cookie_str = f"Cookie Name: {cookie['name']}, Cookie Value: {cookie['value']}, Classification: {self.classify_cookie(cookie)}"
                # Print only if not already printed
                if cookie_str not in printed_cookies:
                    self.logger.info(cookie_str)
                    printed_cookies.add(cookie_str)
            self.logger.info(f"Total Cookies Received for {self.url}: {len(cookies)}")
        else:
            self.logger.info(f"\nProcessing URL: {self.url}\nNo cookies received.")

    @staticmethod
    def classify_cookie(cookie):
        """
        Classify cookies as session, 1st party, or 3rd party based on name and expiry.
        """
        if 'session' in cookie['name'].lower():
            return "Session Cookie"
        elif cookie.get('expiry', 0) == 0:
            return "1st Party Cookie"
        else:
            return "3rd Party"

# List of URLs to scrape for cookies
if __name__ == "__main__":
    urls = [
        "https://www.bbc.co.uk/news", "https://www.birminghammail.co.uk/", 
        "https://www.independent.co.uk/", "https://news.sky.com/uk", "https://www.ebay.co.uk/", "https://www.amazon.co.uk/",
        "https://www.shein.co.uk", "https://www.asos.com/", "https://www.facebook.com/login/", 
        "https://twitter.com/?lang=en", "https://www.instagram.com/", 
        "https://uk.linkedin.com/"
    ]
    
   # logger = setup_logger()  # Setup logger configuration
    # Iterate over each URL to scrape cookies
    for url in urls:
        scraper = RejectCookies(url) #logger)
        scraper.scrape_cookie_data()
