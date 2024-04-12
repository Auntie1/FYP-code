from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class WebsiteChecker:
    def __init__(self):
        self.driver = webdriver.Chrome()  # You can change this to your preferred browser driver

    def check_exemptions(self, website_url):
        print("Checking exemptions for", website_url)
        
        try:
            # Make a request to the website
            self.driver.get(website_url)
            
            # Wait for the page to load
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            
            # Parse HTML content
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            
            # Search for exemption keywords
            exemption_keywords = ['_ea_clicked', 'accessKey', 'align']
            for keyword in exemption_keywords:
                if soup.find(string=keyword):
                    print("Exemption keyword '{}' found.".format(keyword))
            
            # Search for exemption classes
            exemption_classes = ['communication-exemption', 'necessary-exemption', 'analytics-exemption', 'personalization-exemption']
            for class_name in exemption_classes:
                if soup.find(class_=class_name):
                    print("Exemption class '{}' found.".format(class_name))
            
            # If no exemptions found, print a message
            if not (any(soup.find(string=keyword) for keyword in exemption_keywords) or
                    any(soup.find(class_=class_name) for class_name in exemption_classes)):
                print("No exemptions found.")
        except Exception as e:
            print("An error occurred:", str(e))
        finally:
            # Quit the driver after processing
            self.driver.quit()

# Create an instance of the WebsiteChecker class
checker = WebsiteChecker()

# Call the check_exemptions method with the website URL
checker.check_exemptions("https://www.ebay.co.uk/gdpr")
