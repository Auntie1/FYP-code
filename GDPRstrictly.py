from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# CHECK WHY ERROR WAS OCCURING AND IF THE COOKIE "ESSENTIAL COOKIES EXIST MANUALLY AND IF NOT SHOWING UP TRY TO FIND OUT WHY


class WebsiteChecker:
    def __init__(self):
        self.driver = None

    def start_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Set implicit wait time to 10 seconds

    def stop_driver(self):
        if self.driver:
            self.driver.quit()

    def accept_cookies(self, website):
        try:
            self.driver.get(website)
            # Wait for the cookie consent popup iframe to be available and switch to it
            WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@title, 'sp_message_iframe')]")))
            # Wait for the accept button to be clickable and click it
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]"))).click()
            # Switch back to the default content
            self.driver.switch_to.default_content()
            print("Cookies accepted successfully for", website)
        except NoSuchElementException as e:
            print("Cookie consent popup iframe not found for", website)
        except TimeoutException as e:
            print("Timed out waiting for cookie consent popup for", website)
        except Exception as e:
            print("Error occurred while accepting cookies for", website, ":", e)





    def check_strictly_necessary_criteria(self, websites):
        strictly_necessary_keywords = ["strictly necessary", "essential cookie", "functional cookie"]
        
        self.start_driver()
        try:
            for website in websites:
                print("Checking compliance with 'strictly necessary' criteria for", website)
                self.accept_cookies(website)  # Accept cookies before checking strictly necessary criteria
                
                try:
                    self.driver.get(website)
                    
                    # Wait for the page to be fully loaded
                    WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
                    
                    # Get the cookies received by the browser
                    cookies = self.driver.get_cookies()

                    # Check if there are any cookies received
                    if cookies:
                        strictly_necessary_cookies = [cookie for cookie in cookies if cookie.get('strictly_necessary')]
                        if strictly_necessary_cookies:
                            print("Cookies meet 'strictly necessary' criteria.")
                            continue  # Move to the next website
                        else:
                            print("No 'strictly necessary' cookies found.")
                    
                    # Search for keywords in the page source
                    page_source = self.driver.page_source.lower()
                    for keyword in strictly_necessary_keywords:
                        if keyword in page_source:
                            print("Keyword indicating 'strictly necessary' cookies found:", keyword)
                            break  # Move to the next website
                    else:
                        print("No keywords indicating 'strictly necessary' cookies found.")
                    
                except Exception as e:
                    print("Error occurred while checking compliance for", website, ":", e)
        finally:
            self.stop_driver()

# Example usage:
checker = WebsiteChecker()
checker.check_strictly_necessary_criteria(["https://www.bbc.co.uk/", "https://www.ebay.co.uk/", "https://pypi.org/project/requests/", "https://www.gov.uk/log-in-register-hmrc-online-services"])
