from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -------------------- SETUP --------------------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 30)

# -------------------- OPEN WEBSITE --------------------
driver.get("https://d6tnkcljxvlqk.cloudfront.net/login")

# -------------------- LOGIN --------------------
try:
    wait.until(EC.presence_of_element_located((By.ID, "inputEmail"))).send_keys("support@yelowsoft.com")
    driver.find_element(By.ID, "inputPassword").send_keys("YSDev@1510")

    driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/app-login/div/form/div/div[2]/button'
    ).click()

    wait.until(EC.url_contains("/company"))
    print("✅ LOGIN SUCCESSFUL")

except Exception as e:
    print("❌ LOGIN FAILED:", e)
    driver.quit()
    exit()

# -------------------- OPEN COMPANY DROPDOWN --------------------
try:
    company_menu = wait.until(EC.presence_of_element_located((
        By.XPATH,
        '//*[@id="app"]/app-sidebar-layout/aside/div/nav/app-no-company-header/ul/li[1]/a'
    )))
    driver.execute_script("arguments[0].click();", company_menu)

    wait.until(EC.presence_of_element_located((By.XPATH, "//bs-dropdown-container")))
    print("✅ Company dropdown opened")

except Exception as e:
    print("❌ Company dropdown failed:", e)
    driver.quit()
    exit()

# -------------------- CLICK YELOWCAB --------------------
try:
    yelowcab = wait.until(EC.presence_of_element_located((
        By.XPATH,
        "//bs-dropdown-container//span[normalize-space()='YelowCab']/ancestor::a"
    )))
    driver.execute_script("arguments[0].click();", yelowcab)

    wait.until(EC.url_contains("/company/service"))
    print("✅ YelowCab opened")

except Exception as e:
    print("❌ YelowCab open failed:", e)
    driver.quit()
    exit()

# -------------------- OPEN FIRST COMPANY --------------------
try:
    first_company = wait.until(EC.presence_of_element_located((
        By.XPATH,
        '//*[@id="app"]/div[1]/app-company/div[1]/section/div/div[2]/div/div/table/tbody/tr[1]/td[2]/div/div/h5/a'
    )))
    driver.execute_script("arguments[0].click();", first_company)

    wait.until(EC.url_contains("/dashboard"))
    print("✅ Company dashboard opened")

except Exception as e:
    print("❌ Company dashboard failed:", e)
    driver.quit()
    exit()

# -------------------- OPEN DISPATCH BOOKING --------------------
try:
    book_ride_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="app"]/div[1]/app-yelowcab-dashboard/div/header/div/div[1]/a'
    )))
    driver.execute_script("arguments[0].click();", book_ride_btn)

    wait.until(EC.url_contains("/yelowcab/ride/add"))
    print("✅ Dispatch Booking opened")

except Exception as e:
    print("❌ Dispatch page failed:", e)
    driver.quit()
    exit()

# -------------------- ENTER SOURCE ADDRESS --------------------
try:
    source = wait.until(EC.presence_of_element_located((
        By.XPATH,
        '//*[@id="app"]/div[1]/cab-booking/div[1]/section/div[2]/div/div/form/div/div[1]/div[1]/div/div[1]/div/div/div[2]/div[1]/div/app-search-box-google/ng-select/div/div/div[2]/input'
    )))
    source.send_keys("Yelowsoft, Sarkhej - Gandhinagar Highway, nr. Adani CNG Station, Makarba, Ahmedabad, Gujarat, India")
    time.sleep(5)
    source.send_keys("\n")   # select first suggestion
    print("✅ Source entered")

except Exception as e:
    print("❌ Source failed:", e)
    driver.quit()
    exit()

# -------------------- ENTER DESTINATION ADDRESS --------------------
try:
    destination = wait.until(EC.presence_of_element_located((
        By.XPATH,
        '//*[@id="app"]/div[1]/cab-booking/div[1]/section/div[2]/div/div/form/div/div[1]/div[1]/div/div[1]/div/div/div[2]/div[3]/div/div/app-search-box-google/ng-select/div/div/div[2]/input'
    )))
    destination.send_keys("Sardar Vallabhbhai Patel International Airport (AMD), Hansol, Ahmedabad, Gujarat, India")
    time.sleep(5)
    destination.send_keys("\n")
    print("✅ Destination entered")

except Exception as e:
    print("❌ Destination failed:", e)
    driver.quit()
    exit()

# -------------------- CLICK BOOK NOW --------------------
try:
    book_now = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="app"]/div[1]/cab-booking/div[1]/section/div[2]/div/div/form/div/div[1]/div[2]/div/div[2]/div/button'
    )))
    driver.execute_script("arguments[0].click();", book_now)

    print("✅ BOOK NOW clicked — Ride booking triggered")

except Exception as e:
    print("❌ Booking failed:", e)
    driver.quit()
    exit()

# -------------------- HOLD BROWSER --------------------
time.sleep(8)
driver.quit()
