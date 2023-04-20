from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(
    ChromeDriverManager().install())


browser.get("https://google.com")

search_bar = browser.find_element(By.CLASS_NAME, "gLFyf")
search_bar.send_keys("pycon")
search_bar.send_keys(Keys.ENTER)

search_results = browser.find_elements(By.CLASS_NAME, "g")

for search_result in search_results:
    try:
        search_result_title = search_result.find_element(By.TAG_NAME, "h3")
        print(search_result_title.text)
    except Exception as error:
        print(error)


browser.close()
