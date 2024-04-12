import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CookieScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()  # You can change this to your preferred browser driver
        self.urls = [
            #"https://www.ebay.co.uk/",
            "https://www.amazon.co.uk/",
           # "https://www.bbc.co.uk/news",
           # "https://news.sky.com/uk",
            #"https://www.asos.com/",
           # "https://www.bupa.co.uk/",
            #"https://www.nhs.uk/",
          #  "https://www.mytutor.co.uk/"
        ]

    def classify_cookie(self, url, cookie_domain, cookie_expires):
        if cookie_expires is None:
            return "Session Cookie"
        elif cookie_expires:
            return "3rd Party"
        domain = urlparse(cookie_domain).hostname
        if domain == urlparse(url).hostname:
            return "1st Party"
        else:
            return "3rd Party"

    def accept_cookies(self):
        try:
            accept_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept') or contains(text(), 'Agree') or contains(text(), 'OK') or contains(text(), 'Yes, I agree')]"))
            )
            # Scroll to the accept button to ensure it's in view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", accept_button)
            # Wait for the accept button to be visible
            WebDriverWait(self.driver, 10).until(EC.visibility_of(accept_button))
            accept_button.click()
            print("Cookies accepted.")
        except TimeoutException:
            print("No cookie consent mechanism found or could not accept cookies.")

    def scrape_cookie_data(self):
        for url in self.urls:
            try:
                # Visit the URL to capture cookies
                self.driver.get(url)
                
                # Accept cookies if there is a cookie consent mechanism
                self.accept_cookies()
                
                # Wait for the page to fully load
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
                
                # Introduce a delay to ensure all dynamic content is loaded, including cookies
                time.sleep(2)
                
                # Get the cookies from the browser
                browser_cookies = self.driver.get_cookies()

                # Print the received cookies for the current URL and their classification
                print(f"\nProcessing URL: {url}")
                print("Received Cookies:")
                cookie_counter = 0
                for cookie in browser_cookies:
                    cookie_counter += 1
                    cookie_name = cookie['name']
                    cookie_value = cookie['value']
                    cookie_domain = cookie['domain'] if 'domain' in cookie else ""
                    cookie_expires = cookie['expiry'] if 'expiry' in cookie else None
                    classification = self.classify_cookie(url, cookie_domain, cookie_expires)
                    print(f"Cookie Name: {cookie_name}, Cookie Value: {cookie_value}, Classification: {classification}")
                print(f"Total Cookies Received for {url}: {cookie_counter}")

            except TimeoutException:
                print(f"Timeout occurred while loading URL: {url}")

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    scraper = CookieScraper()
    scraper.scrape_cookie_data()
    scraper.close()
