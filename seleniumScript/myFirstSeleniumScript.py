from selenium import webdriver;
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install());

driver.get("http://www.google.com")
driver.set_page_load_timeout(30)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("page.png")
driver.close()
driver.quit()
