from selenium import webdriver

class WebsiteChecker:
    def __init__(self, website):
        self.website = website

    def check_consent_mechanism(self):
        print(f"Checking cookie consent mechanism for {self.website}...")
        # Initialize Chrome browser
        driver = webdriver.Chrome()
        driver.get(self.website)
        # Add further code to interact with the webpage as needed

# Example usage:
checker = WebsiteChecker("https://www.ebay.co.uk/")
checker.check_consent_mechanism()
