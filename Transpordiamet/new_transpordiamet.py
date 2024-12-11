from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure the path to chromedriver is configured if needed
wait = WebDriverWait(driver, 10)  # Explicit wait with a 10-second timeout

try:

    # Load the webpage
    driver.get("https://broneering.transpordiamet.ee/reservations/create")  # Replace with the actual URL
    time.sleep(random.uniform(8, 15))

    # Step 1: Check the radio button
    radio_button = wait.until(EC.element_to_be_clickable((By.ID, "3")))
    radio_button.click()
    time.sleep(random.uniform(2, 6))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(2, 6))

    # Step 2: Click the first "Edasi" button
    edasi_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(text(), "Edasi")]')))
    edasi_button.click()
    time.sleep(random.uniform(2, 6))


    # Step 3: Click the "Vali büroo" dropdown
    dropdown = wait.until(EC.element_to_be_clickable((By.ID, "mat-select-0")))
    dropdown.click()

    time.sleep(random.uniform(2, 6))

    # Step 4: Select "Haapsalu teenindusbüroo"
    haapsalu_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()=" Haapsalu teenindusbüroo "]')))
    haapsalu_option.click()
    time.sleep(random.uniform(2, 6))

    # Step 5: Click the second "Edasi" button
    edasi_button_2 = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit" and contains(text(), " Edasi ")]')))

    # Try clicking using JavaScript
    driver.execute_script("arguments[0].click();", edasi_button_2)

    # Wait for the page to transition
    wait.until(EC.url_changes(driver.current_url))
    print("Navigated to the next page.")

    time.sleep(3)
    print("success")

finally:
    time.sleep(1000)
    # Close the browser
    driver.quit()
