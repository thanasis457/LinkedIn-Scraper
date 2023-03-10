from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from scrapers import profile as profileScraper,\
    experience as experienceScraper, recommendations as recommendationsScraper,\
        education as educationScraper, api as apiScraper
from time import sleep, time
import random

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
    
    def scrape_all(self, profileURL, method):
        try:
            if(method == 'scrape'):
                self.profileScraped.update(profileScraper.scrape(self.driver, profileURL))
                sleep(random.randint(1, 4))
                self.profileScraped.update(experienceScraper.scrape(self.driver, profileURL))
                sleep(random.randint(1, 4))
                self.profileScraped.update(educationScraper.scrape(self.driver, profileURL))
                sleep(random.randint(1, 4))
                self.profileScraped.update(recommendationsScraper.scrape(self.driver, profileURL))
                return self.profileScraped
            else: # api
                profile = apiScraper.get_profile(profileURL)
                
                self.profileScraped = {
                    'name': ' '.join((profile.get('firstName', ''), profile.get('lastName', ''))),
                    'titleDescription': profile.get('headline', 'N/A'),
                    'location': ', '.join((profile.get('geoLocationName', ''), profile.get('geoCountryName', ''))),
                    'about': profile.get('summary', 'N/A'),
                }
                self.profileScraped['experiences'] = []
                for experience in profile['experience']:
                    newExp = {
                        'position': experience.get('title', 'N/A'),
                        'company': experience.get('companyName', 'N/A'),
                        'dateRange': str(experience.get('timePeriod', {}).get('startDate', {}).get('year', 'N/A'))+' - '+ str(experience.get('timePeriod', {}).get('endDate', {}).get('year', 'Present')),
                        'location': experience.get('geoLocationName', 'N/A'),
                        'description': experience.get('description', 'N/A'),
                    }
                    self.profileScraped['experiences']+=[newExp]
                self.profileScraped['education'] = []
                for ed in profile['education']:
                    newEd = {
                        'school': ed.get('school', {}).get('schoolName', 'N/A'),
                        'degree': ed.get('degreeName', 'N/A'),
                        'dateRange': str(ed.get('timePeriod', {}).get('startDate', {}).get('year', 'N/A'))+' - '+ str(ed.get('timePeriod', {}).get('endDate', {}).get('year', 'Present')),
                        'description': '\n'.join((ed.get('activities', ''), ed.get('description', ''))).strip(),
                    }
                    self.profileScraped['education']+=[newExp]
                
                self.profileScraped['recommendations'] = []
                
                return self.profileScraped
                
        except Exception as e:
            return (e, 500)
            

