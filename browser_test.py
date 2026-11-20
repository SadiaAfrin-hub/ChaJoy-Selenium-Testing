from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

print("Browser Title:", driver.title)

driver.quit()