import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_partitioned_cookies(url):
    # Specify the path to the ChromeDriver executable
    chrome_driver_path = r"C:\Users\Noor\Downloads\chromedriver_win32\chromedriver.exe"

    # Launch the Chrome browser
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(url)

    try:
        # Accept cookies if required
        accept_cookies(driver)

        # Wait for the page to fully load
        time.sleep(5)  # Adjust this delay as needed

        # Get all cookies
        cookies = driver.get_cookies()
        print(f"Total Cookies Received for {url}: {len(cookies)}")

        # Print the received cookies
        for cookie in cookies:
            print(cookie)

    except Exception as e:
        print(f"Error occurred while scraping cookies: {e}")

    finally:
        # Close the browser
        driver.quit()

def accept_cookies(driver):
    try:
        # Check if cookie consent overlay exists
        overlay = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'sp_message_container')]"))
        )

        # If overlay exists, find and click on the accept button
        accept_button = overlay.find_element(By.XPATH, "//button[contains(@class, 'sp_message_accept')]")
        if accept_button:
            accept_button.click()
            print("Cookies accepted successfully.")

    except Exception as e:
        # No cookie consent overlay found or error occurred
        print("Error occurred while accepting cookies:", e)

if __name__ == "__main__":
    url = "https://www.bbc.co.uk/"  # Replace with your desired URL
    scrape_partitioned_cookies(url)
