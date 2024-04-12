from selenium import webdriver

# Launch Chrome browser
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.youtube.com/")

# Perform actions on the website
# ...

# Close the browser
driver.quit()
