from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By  # Import the By module
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebsiteChecker:
    def __init__(self, website):
        self.website = website
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Set implicit wait

    def check_consent_mechanism(self):
        print(f"Checking cookie consent mechanism for {self.website}...")
        self.driver.get(self.website)
        try:
            # Search for elements containing common classes, IDs, or attributes related to cookie consent
            cookie_consent_selectors = [
                '.cookie-consent', '#cookie-banner', '.privacy-policy-banner',
                '[id*="cookie"]', '[id*="consent"]', '[class*="cookie"]', '[class*="consent"]',
                '[data-cookie]', '[data-consent]', '[data-privacy-policy]',
                'div:-soup-contains("cookie")', 'div:-soup-contains("consent")', 'div:-soup-contains("privacy policy")',
                'span:-soup-contains("cookie")', 'span:-soup-contains("consent")', 'span:-soup-contains("privacy policy")',
                'p:-soup-contains("cookie")', 'p:-soup-contains("consent")', 'p:-soup-contains("privacy policy")'
            ]
            for selector in cookie_consent_selectors:
                if self.driver.find_elements(By.CSS_SELECTOR, selector):
                    print("Cookie consent mechanism found.")
                    return
            print("Cookie consent mechanism not found.")
        except TimeoutException:
            print("Timed out waiting for cookie consent mechanism.")
        finally:
            self.driver.quit()

# Example usage:
checker = WebsiteChecker("https://www.youtube.com/")
checker.check_consent_mechanism()
