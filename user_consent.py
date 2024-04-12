from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebsiteChecker:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Set implicit wait time to 10 seconds

    def provide_consent(self, websites):
        for website in websites:
            print("Providing consent for", website)
            try:
                self.driver.get(website)

                # Wait for the page to be fully loaded
                WebDriverWait(self.driver, 120).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'body'))
                )
                # Scroll to the bottom of the page to ensure all content is loaded
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # Check for consent button outside iframes
                try:
                    consent_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept")]'))
                    )
                    print("Consent button found.")
                    print("Please manually click the consent button.")
                except TimeoutException:
                    print("Consent button not found outside iframes.")

                # Check for consent indicator
                try:
                    consent_indicator = WebDriverWait(self.driver, 20).until(
                        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "cookie consent")]'))
                    )
                    print("Consent provided successfully.")
                except TimeoutException:
                    print("Unable to confirm consent.")
            except NoSuchElementException:
                print("Unable to provide consent for", website)
            finally:
                self.driver.quit()

# Example usage:
checker = WebsiteChecker()
checker.provide_consent(["https://www.ebay.co.uk/", "https://www.amazon.co.uk/"])
