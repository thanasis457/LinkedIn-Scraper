from bs4 import BeautifulSoup as bs
from pprint import pprint
from selenium.webdriver.support.ui import WebDriverWait 
import re

def scrape(driver, url):
    def document_initialised(driver):
        soup = bs(driver.page_source, 'html.parser')
        try:
            profileSection = soup.find('div', {'class':'mt2 relative'})
            aboutSection = soup.find('div', {'id':'about'})
            if(profileSection==None or aboutSection==None):
                raise Exception('None')
            return True
        except:
            return False
    def scrape_name():
        # Go to the fist ember (always the profile)
        # Go down the path for the profile name
        try:
            name = profileSoup.find('section', {'id': re.compile('ember.*')})\
                .find('div', {'class':'ph5'})\
                .find('div', {'class':'mt2 relative'})\
                .div\
                .div\
                .h1\
                .text
        except:
            return 'N/A'
        
        return name
    
    def scrape_location():
        try:
            location = profileSoup.find('section', {'id': re.compile('ember.*')})\
                .find('div', {'class':'ph5'})\
                .find('div', {'class':'mt2 relative'})\
                .find_all('div', recursive=False)[1]\
                .span\
                .text
        except:
            location = 'N/A'
        
        return location

    
    def scrape_title():
        # Go to the fist ember (always the profile)
        # Go down the path for the profile name
        try:
            titleDescription = profileSoup.find('section', {'id': re.compile('ember.*')})\
                .find('div', {'class':'ph5'})\
                .find('div', {'class':'mt2 relative'})\
                .div\
                .find_all('div', recursive=False)[1]\
                .text
        except:
            return 'N/A'
        return titleDescription
    
    def scrape_about():
        # Go to the ember with a child with id='about'
        # Go down the path for the description
        def aboutFilter(elem):
            # if(elem.find('div',{'id': 'about'})): pprint(elem)
            try:
                return elem.name=='section' and elem.find('div',{'id': 'about'})
            except:
                return False

        # profileSoup = bs(driver.page_source, "html.parser")

        # res = profileSoup.find('div', {'id':'about'})
        try:
            about = profileSoup.find(aboutFilter)\
                .find('div', {'class':'ph5'})\
                .div\
                .div\
                .div\
                .span\
                .text
        except:
            return 'N/A'
        
        return about
    
    driver.get(url)
    try:
        WebDriverWait(driver, timeout=5).until(document_initialised)
    except:
        pass
    profileSoup = bs(driver.page_source, "html.parser")
    
    return {
        'name': scrape_name(),
        'titleDescription': scrape_title(),
        'about': scrape_about(),
        'location': scrape_location()
    }
    
    
    