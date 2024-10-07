import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_shopping_cart(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    time.sleep(10)

    assert (WebDriverWait(browser, 10)
     .until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary"))))