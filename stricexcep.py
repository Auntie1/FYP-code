import logging  # Import the logging module for logging
from selenium import webdriver  # Import Selenium's webdriver module for browser automation
from selenium.webdriver.chrome.options import Options  # Import Options class to configure Chrome WebDriver
from selenium.webdriver.common.by import By  # Import By class for locating elements
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Import expected_conditions for defining expected conditions
from selenium.common.exceptions import TimeoutException, WebDriverException  # Import exceptions for error handling
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing
import time  # Import time module for delays
#Beautiful Soup works well in this code and without I get errors and am not able to pick up the keywords accuractly so this is why its been used here 

class StrictlyNecessaryCookiesChecker:
    def __init__(self):
        self.driver = self.create_driver()  # Initialize the Chrome WebDriver instance
        self.logger = self.setup_logger()  # Initialize the logger

    def create_driver(self):
        """
        Create a Chrome WebDriver instance.

        Returns:
        - driver: Chrome WebDriver instance.
        """
        try:
            options = Options()  # Create options object to customize Chrome WebDriver
            # Add '--ignore-certificate-errors' argument to ignore SSL certificate errors (optional)
            # options.add_argument("--ignore-certificate-errors")  
            driver = webdriver.Chrome(options=options)  # Create Chrome WebDriver instance
        except WebDriverException as e:
            print(f"Error: WebDriverException occurred while creating the driver: {str(e)}")
            return None
        else:
            return driver

    def check_cookie_exceptions(self, *website_urls):
        """
        Check for cookie exceptions on the provided list of website URLs.

        Parameters:
        - *website_urls (str): Variable-length list of website URLs to check.

        Returns:
        - None
        """
        if not self.driver:
            print("Error: WebDriver not initialized.")
            return

        for website_url in website_urls:
            print(f"Checking cookie exceptions for {website_url}")
            try:
                self.check_website_cookie_exception(website_url)  # Check cookie exceptions for each website URL
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        self.driver.quit()  # Quit the WebDriver after checking all websites

    def check_website_cookie_exception(self, website_url):
        """
        Check for cookie exemptions on a single website URL.

        Parameters:
        - website_url (str): The URL of the website to check.

        Returns:
        - None
        """
        self.driver.get(website_url)  # Open the website URL
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))  # Wait for the page to load
        time.sleep(2)  # Add a delay for page stabilization

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')  # Parse the HTML content of the page
        exemption_keywords = ['_ea_clicked', 'accessKey', 'align']  # Keywords indicating cookie exemptions
        exemption_classes = ['communication-exemption', 'necessary-exemption', 'analytics-exemption', 'personalization-exemption']  # Classes indicating cookie exemptions
        strictly_necessary_keywords = ["strictly necessary", "essential", "functional", "necessary cookie", "essential cookie", "essential cookies", "essential cookies only"]  # Keywords indicating strictly necessary cookies

        # Check for exemption keywords, classes, and strictly necessary keywords
        found_keywords = [keyword for keyword in exemption_keywords if soup.find(string=keyword)]
        found_classes = [class_name for class_name in exemption_classes if soup.find(class_=class_name)]
        found_strictly_necessary_keywords = [keyword for keyword in strictly_necessary_keywords if keyword in self.driver.page_source.lower()]

        # Print results based on findings
        if found_keywords or found_classes:
            print(f"Website {website_url} offers cookie exemptions.")
            if found_keywords:
                print(f"Exemption keywords found: {found_keywords}")
            if found_classes:
                print(f"Exemption classes found: {found_classes}")
        elif found_strictly_necessary_keywords:
            print(f"Website {website_url} offers strictly necessary cookies.")
        else:
            print("No cookie exemptions found.")

    def setup_logger(self):
        """
        Setup logger configuration.

        Returns:
        - logger: Logger instance.
        """
        logger = logging.getLogger("StrictlyNecessaryCookiesChecker")  # Create a logger instance
        logger.setLevel(logging.INFO)  # Set logger level to INFO

        formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')  # Define log message format

        ch = logging.StreamHandler()  # Create a StreamHandler to output log messages to console
        ch.setLevel(logging.INFO)  # Set log level for console output to INFO
        ch.setFormatter(formatter)  # Set log message format for console output

        logger.addHandler(ch)  # Add console handler to the logger

        return logger  # Return the logger instance

# Example usage:
checker = StrictlyNecessaryCookiesChecker()  # Create an instance of StrictlyNecessaryCookiesChecker
checker.check_cookie_exceptions(
    "https://www.bbc.co.uk/news",
    "https://www.birminghammail.co.uk/",
    "https://www.independent.co.uk/",
    "https://news.sky.com/uk",
    "https://www.ebay.co.uk/",
    "https://www.amazon.co.uk/",
    "https://www.shein.co.uk",
    "https://www.asos.com/",
    "https://www.facebook.com/login/",
    "https://twitter.com/?lang=en",
    "https://www.instagram.com/",
    "https://uk.linkedin.com/"
)
