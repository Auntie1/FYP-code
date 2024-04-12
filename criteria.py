from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebsiteChecker:
    def __init__(self):
        self.driver = None

    def start_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Set implicit wait time to 10 seconds

    def stop_driver(self):
        if self.driver:
            self.driver.quit()

    def accept_cookies(self):
        # Accept cookies for website
        self.driver.get("https://www.bbc.co.uk/")  # Example URL
        try:
            WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='sp_message_iframe_547089']")))
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Accept']"))).click()
            self.driver.switch_to.default_content()
            print("Cookies accepted successfully.")
        except Exception as e:
            print("Error occurred while accepting cookies:", e)

    def check_strictly_necessary_criteria(self, websites):
        self.start_driver()
        try:
            self.accept_cookies()  # Accept cookies before checking strictly necessary criteria
            for website in websites:
                print("Checking compliance with 'strictly necessary' criteria for", website)
                self.driver.get(website)
                
                try:
                    # Wait for the page to be fully loaded
                    WebDriverWait(self.driver, 20).until(
                        EC.presence_of_element_located((By.TAG_NAME, 'body'))
                    )
                    
                    # Get the cookies received by the browser
                    cookies = self.driver.get_cookies()

                    # Check if there are any cookies received
                    if cookies:
                        strictly_necessary_cookies = [cookie for cookie in cookies if cookie.get('strictly_necessary')]
                        if strictly_necessary_cookies:
                            print("Cookies meet 'strictly necessary' criteria.")
                        else:
                            print("No 'strictly necessary' cookies found.")
                    else:
                        print("No cookies found.")
                except Exception as e:
                    print("Error occurred while checking compliance for", website, ":", e)
        finally:
            self.stop_driver()

# Example usage:
checker = WebsiteChecker()
checker.check_strictly_necessary_criteria(["https://www.bbc.co.uk/", "https://www.ebay.co.uk/", "https://pypi.org/project/requests/"])
