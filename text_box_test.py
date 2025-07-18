from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver (make sure chromedriver is in the same folder or in PATH)
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

# Fill the form fields
driver.find_element(By.ID, "userName").send_keys("Lucia Codjia")
driver.find_element(By.ID, "userEmail").send_keys("lucia@example.com")
driver.find_element(By.ID, "currentAddress").send_keys("Cotonou, Bénin")
driver.find_element(By.ID, "permanentAddress").send_keys("1234 Dev Street")

# Scroll to the submit button to avoid ad iframe blocking the click)
submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
time.sleep(1)   # Scroll to the submit button to avoid ad iframe blocking the click

# Click the submit button
submit_button.click()

# Wait for the result to appear
time.sleep(2)

# Validate result
output_name = driver.find_element(By.ID, "name").text
output_email = driver.find_element(By.ID, "email").text

# Basic verification
if "Lucia Codjia" in output_name and "lucia@example.com" in output_email:
    print("✅ Test passed: Form submitted and output verified.")
else:
    print("❌ Test failed: Output not as expected.")

# Close browser
driver.quit()
