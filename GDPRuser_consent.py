from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

class WebsiteChecker:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)  # Set implicit wait time to 10 seconds

    def provide_consent(self, websites):
        for website in websites:
            print("Providing consent for", website)
            try:
                self.driver.get(website)
                
                # Wait for the page to be fully loaded
                WebDriverWait(self.driver, 300).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'body'))
                )
                
                # Capture the number of cookies before checking consent
                cookies_before = len(self.driver.get_cookies())

                # Scroll to the bottom of the page to ensure all content is loaded
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
                # Add a delay before clicking the consent button
                time.sleep(5)

                # Attempt to click the consent button
                try:
                    consent_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept")]'))
                    )
                    print("Consent button found. Clicking...")
                    consent_button.click()
                    
                    # Wait for some time to allow changes to take effect
                    WebDriverWait(self.driver, 10).until(EC.staleness_of(consent_button))

                    # Capture the number of cookies after clicking consent button
                    cookies_after = len(self.driver.get_cookies())

                    # Check if the number of cookies has increased
                    if cookies_after > cookies_before:
                        print("Consent provided successfully.")
                        continue  # Move to the next website
                except NoSuchElementException:
                    print("Consent button not found.")

                # If consent button not found, try to detect consent using keywords
                keywords = ["consent", "accept all", "consent all"]

                # Search for keywords in the page source
                page_source = self.driver.page_source.lower()
                for keyword in keywords:
                    if keyword in page_source:
                        print("Consent indicated by keyword:", keyword)
                        break  # Move to the next website

                # If no consent indication is found, print a message
                print("Unable to confirm consent.")
            except TimeoutException:
                print("Timeout occurred while loading the page.")
            except NoSuchElementException:
                print("Element not found on the page.")
            except WebDriverException as e:
                print("WebDriver error:", e)
            except Exception as e:
                print("Error occurred while providing consent:", e)
            finally:
                self.driver.delete_all_cookies()

# Example usage:
checker = WebsiteChecker()
checker.provide_consent(["https://www.ebay.co.uk/", "https://www.google.com/", "https://www.bupa.co.uk/", "https://www.amazon.co.uk/"])
