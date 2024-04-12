from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

class WebsiteChecker:
    def __init__(self, ignore_ssl_errors=False):
        self.driver = self.create_driver(ignore_ssl_errors)

    def create_driver(self, ignore_ssl_errors=False):
        chrome_options = Options()
        if ignore_ssl_errors:
            chrome_options.add_argument('--ignore-certificate-errors')

        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def check_exemptions(self, *website_urls):
        for website_url in website_urls:
            print("Checking exemptions for", website_url)
            
            try:
                self.driver.get(website_url)
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
                
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                
                exemption_keywords = ['_ea_clicked', 'accessKey', 'align']
                for keyword in exemption_keywords:
                    if soup.find(string=keyword):
                        print("Exemption keyword '{}' found.".format(keyword))
                
                exemption_classes = ['communication-exemption', 'necessary-exemption', 'analytics-exemption', 'personalization-exemption']
                for class_name in exemption_classes:
                    if soup.find(class_=class_name):
                        print("Exemption class '{}' found.".format(class_name))
                
                if not (any(soup.find(string=keyword) for keyword in exemption_keywords) or
                        any(soup.find(class_=class_name) for class_name in exemption_classes)):
                    print("No exemptions found.")
            except TimeoutException as te:
                print("Timeout occurred while loading the page:", str(te))
            except Exception as e:
                print("An error occurred:", str(e))
        
        self.driver.quit()

# Create an instance of the WebsiteChecker class
checker = WebsiteChecker(ignore_ssl_errors=False)  # Set ignore_ssl_errors to True to bypass SSL errors

# Call the check_exemptions method with the website URLs
checker.check_exemptions("https://www.ebay.co.uk/", "https://www.amazon.co.uk/", "https://www.etsy.com/")
