from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import service as fs
from selenium.webdriver import DesiredCapabilities

class KoreanDict:
    def __init__(self):
        options = Options()
        
        # options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument("--remote-debugging-port=9222")
        self.driver = webdriver.Remote(
            command_executor="http://selenium:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.FIREFOX.copy()
            # options=options
        )
        # self.driver = webdriver.Chrome(executable_path='/opt/chrome/chromedriver', options=options)
        self.driver.implicitly_wait(10)

    def word_translate(self, word):
        self.driver.get("https://korean.dict.naver.com/kojadict/#/search?query=" + word)
        # wait until someid is clickable
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'row')))
        mean_elements = element.find_elements(By.CLASS_NAME, "mean")
        means = []
        for e in mean_elements:
            means.append(e.text)
        return {word: means}