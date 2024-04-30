import re  # Import the re module for regular expressions
import logging  # Import the logging module for logging
from selenium import webdriver  # Import Selenium's webdriver module for browser automation
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException  # Import exceptions for error handling
from selenium.webdriver.common.by import By  # Import By class for locating elements
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Import expected_conditions for defining expected conditions
from selenium.webdriver.chrome.options import Options  # Import Options class to configure Chrome WebDriver
#There is no difference in result when using Beautiful Soup in this code therefore I removed it as it was uneccesary

class CookiePolicyAnalyzer:
    """
    A class for analyzing the cookie policy of websites.

    Attributes:
    - driver: Chrome WebDriver instance.
    - logger: Logger instance for logging messages.
    - processed_cookies: Set to store processed cookies.
    """

    def __init__(self):
        """
        Initialize the CookiePolicyAnalyzer class.
        """
        self.driver = None
        self.logger = self.setup_logger()  # Initialize logger
        self.processed_cookies = set()

    def setup_logger(self):
        """
        Setup logger configuration.

        Returns:
        - logger: Logger instance.
        """
        logger = logging.getLogger(__name__)  # Create logger instance
        logger.setLevel(logging.INFO)  # Set logging level to INFO

        formatter = logging.Formatter('%(message)s')  # Define logging format
        ch = logging.StreamHandler()  # Create stream handler
        ch.setFormatter(formatter)  # Set formatter for stream handler
        logger.addHandler(ch)  # Add stream handler to logger

        return logger  # Return logger instance

    def create_driver(self):
        """
        Create a Chrome WebDriver instance with specified options.

        Returns:
        - driver: Chrome WebDriver instance.
        """
        try:
            chrome_options = Options()
            # chrome_options.add_argument('--ignore-certificate-errors')  # Removed ignore SSL certificate errors
            driver = webdriver.Chrome(options=chrome_options)  # Create Chrome WebDriver instance
            driver.implicitly_wait(10)  # Set implicit wait time to 10 seconds
            return driver  # Return Chrome WebDriver instance
        except WebDriverException as e:
            self.logger.error(f"Error: WebDriverException occurred while creating the driver: {e}")
            return None

    def analyze_cookie_policy(self, website_urls):
        """
        Analyze the cookie policy for a list of website URLs.

        Parameters:
        - website_urls (list): List of website URLs to analyze.

        Returns:
        - None
        """
        self.driver = self.create_driver()  # Create WebDriver instance
        if not self.driver:
            self.logger.error("Error: WebDriver not initialized.")  # Log error if WebDriver is not initialized
            return

        try:
            for website_url in website_urls:
                self.logger.info(f"Analyzing cookie policy for: {website_url}")  # Log analysis for each website URL
                self.driver.get(website_url)  # Open the website URL

                # Wait for the page to be fully loaded
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'body'))
                )

                # Search for keywords related to cookie policies
                page_source = self.driver.page_source.lower()  # Get lowercased page source
                keyword_found = self.search_cookie_keywords(page_source)  # Search for cookie-related keywords
                if keyword_found:
                    self.logger.info(f"Keyword related to cookie policy found: {keyword_found}")  # Log if keyword related to cookie policy is found
                else:
                    self.logger.info("No keyword related to cookie policy found.")  # Log if no keyword related to cookie policy is found

        except TimeoutException:
            self.logger.error("Timeout occurred while loading the page.")  # Log timeout error
        except NoSuchElementException as e:
            self.logger.error(f"Element not found on the page: {e}")  # Log element not found error
        except WebDriverException as e:
            self.logger.error(f"WebDriver error: {e}")  # Log WebDriver error
        except Exception as e:
            self.logger.error(f"Error occurred while analyzing cookie policy: {e}")  # Log any other error
        finally:
            self.close_driver()  # Close WebDriver instance

    def search_cookie_keywords(self, text):
        """
        Search for cookie-related keywords in the text.

        Parameters:
        - text (str): Text to search for keywords.

        Returns:
        - keyword (str): Keyword related to cookie policy if found, None otherwise.
        """
        # Define patterns to search for cookie-related keywords
        patterns = {
            "cookie policy": r"cookie\s*policy",
            "cookie notice": r"cookie\s*notice",
            "cookie consent": r"cookie\s*consent",
            "privacy policy": r"privacy\s*policy",
        }

        # Search for patterns in the text
        for keyword, pattern in patterns.items():
            if re.search(pattern, text, re.IGNORECASE):  # Search for keyword ignoring case sensitivity
                return keyword  # Return keyword if found

        return None  # Return None if no keyword is found

    def close_driver(self):
        """
        Close the WebDriver instance.
        """
        if self.driver:
            self.driver.quit()  # Quit WebDriver instance

# Example usage:
if __name__ == "__main__":
    website_urls = [
        "https://www.bbc.co.uk/news", "https://www.birminghammail.co.uk/", 
       "https://www.independent.co.uk/", "https://news.sky.com/uk", "https://www.ebay.co.uk/", "https://www.amazon.co.uk/",
       "https://www.shein.co.uk", "https://www.asos.com/", "https://www.facebook.com/login/", 
       "https://twitter.com/?lang=en", "https://www.instagram.com/", 
       "https://uk.linkedin.com/"
    ]  # List of websites to check for cookie policy
    analyzer = CookiePolicyAnalyzer()  # Create instance of CookiePolicyAnalyzer
    analyzer.analyze_cookie_policy(website_urls)  # Analyze cookie policy for each website URL
