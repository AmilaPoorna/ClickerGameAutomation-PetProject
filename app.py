import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = uc.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "langSelect-EN"))
).click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

end_time = time.time() + 300
while time.time() < end_time:
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()

    upgrades = driver.find_elements(By.CSS_SELECTOR, ".upgrade.enabled")
    for upgrade in upgrades:
        try:
            upgrade.click()
        except:
            pass

    products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    for product in products:
        try:
           product.click()
        except:
            pass

driver.quit()
