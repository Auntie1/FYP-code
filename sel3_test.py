from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebsiteChecker:
    def __init__(self, websites):
        self.websites = websites
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Set implicit wait

    def check_clear_comprehensive_info(self):
        for website in self.websites:
            print(f"Checking clear and comprehensive information about cookies for {website}...")
            self.driver.get(website)
            try:
                # Check for elements containing common keywords related to privacy policy and cookie consent
                keywords = ['cookie', 'consent', 'privacy']
                xpath = f'//*[contains(text(), "{keywords[0]}") or contains(text(), "{keywords[1]}") or contains(text(), "{keywords[2]}")]'
                elements = self.driver.find_elements(By.XPATH, xpath)
                if elements:
                    print("Clear and comprehensive information about cookies found.")
                else:
                    print("Clear and comprehensive information about cookies not found.")
            except NoSuchElementException:
                print("Clear and comprehensive information about cookies not found.")

    def __del__(self):
        self.driver.quit()

# Example usage:
urls = [
    "https://www.youtube.com/",
    "https://www.google.com/",
    "https://www.amazon.com/",
    "https://pypi.org/project/requests/"
]

checker = WebsiteChecker(urls)
checker.check_clear_comprehensive_info()
