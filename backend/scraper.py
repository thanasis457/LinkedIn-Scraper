from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from scrapers import profile, experience, recommendations, education
class Scraper:
    def __init__(self):
        self.options = FirefoxOptions()
        self.options.add_argument('--lang=en')
        # self.options.add_argument('--disable-blink-features=AutomationControlled')
        # self.service = ChromeService(executable_path=ChromeDriverManager().install())
        self.service = FirefoxService(executable_path=GeckoDriverManager().install())
        # self.driver = webdriver.Chrome(service=service)
        self.driver = webdriver.Firefox(service=self.service, options=self.options)
        self.profileScraped={
            'name':"",
            'titleDescription':"",
            'location': "",
            'about': "",
            'experiences': "",
            'education': "",
            'recommendations':"",
        }
        self.driver.get("https://www.linkedin.com/login/");
    
    def scrape_all(self, profileURL):
        self.profileScraped.update(profile.scrape(self.driver, profileURL))
        self.profileScraped.update(experience.scrape(self.driver, profileURL))
        self.profileScraped.update(education.scrape(self.driver, profileURL))
        self.profileScraped.update(recommendations.scrape(self.driver, profileURL))
        return self.profileScraped

