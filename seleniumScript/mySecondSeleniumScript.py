from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install());

driver.get("http://www.facebook.com")
driver.set_page_load_timeout(30)
driver.maximize_window()
driver.implicitly_wait(20)
print(driver.title)
assert "Facebook" in driver.title
driver.get_screenshot_as_file("C:\\Users\\sonij\\Desktop\\Personal\\pythonWB\\Screenshot\\page.png")
driver.find_element_by_id("email").send_keys("SeleniumWebdriver")
driver.find_element_by_name("pass").send_keys("Phython")
driver.find_element_by_id("loginbutton").click()
driver.get_screenshot_as_file("C:\\Users\\sonij\\Desktop\\Personal\\pythonWB\\Screenshot\\page1.png")
driver.close()
driver.quit()
