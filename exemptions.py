from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By

class WebsiteChecker:
    def __init__(self, websites):
        self.websites = websites
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Set implicit wait

    def check_exemptions(self):
        for website in self.websites:
            print(f"Checking exemptions to cookie rules for {website}...")
            try:
                self.driver.get(website)
                # Get the body element to search for exemption-related text
                body_element = self.driver.find_element(By.TAG_NAME, 'body')
                # Check if the body text contains any exemption-related keywords
                exemption_keywords = ['exemption', 'Exception', 'exempt', 'Exempt']
                exemption_detected = any(keyword in body_element.text for keyword in exemption_keywords)
                if exemption_detected:
                    print("Exemptions to cookie rules detected.")
                else:
                    print("No exemptions to cookie rules apply.")
            except NoSuchElementException:
                print("Error: Body element not found on the page. Skipping...")
                continue
            except WebDriverException as e:
                print(f"Error occurred while processing {website}: {e}")
                continue

        self.driver.quit()

# Example usage:
websites = ["https://www.youtube.com/", "https://www.google.com/", "https://www.amazon.com/", "https://pypi.org/project/requests/", "https://www.gov.uk/","https://www.bbc.com/", 
            "https://www.nhs.uk/", "https://www.cdc.gov/"]
checker = WebsiteChecker(websites)
checker.check_exemptions()
