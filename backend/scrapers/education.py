from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
import re

def scrape(driver, url):
    
    def scrape_education():
        education = []
        pastEducation = []
        try:
            pastEducation = edSoup.find_all('li', recursive=False)
        except:
            pass

        for current in pastEducation:
            school = {}
            try:
                school['name'] = current.div\
                    .div\
                    .find_all('div', recursive=False)[1]\
                    .div\
                    .a\
                    .div\
                    .span\
                    .span\
                    .text
            except:
                school['name'] = 'N/A'
            try:
                school['degree'] = current.div\
                    .div\
                    .find_all('div', recursive=False)[1]\
                    .div\
                    .a\
                    .find('span',class_="t-14 t-normal", recursive=False)\
                    .span\
                    .text
            except:
                school['degree'] = "N/A"

            try:
                school['dateRange'] = current.div\
                    .div\
                    .find_all('div', recursive=False)[1]\
                    .div\
                    .a\
                    .find('span', {'class': 't-black--light'}, recursive=False)\
                    .span\
                    .text
                
            except:
                school['dateRange'] = 'N/A'
                
            try:
                school['description'] = current.div\
                    .div\
                    .find_all('div', recursive=False)[1]\
                    .find_all('div', recursive=False)[1]\
                    .text\
                
                school['description'] = (re.sub(r'\n\s*\n', '\n\n', school['description'])).strip()
                
            except:
                school['description'] = 'N/A'
            
            education+=[school]

        print(education)
        return education
    
    driver.get(url+'details/education/')
    try:
        WebDriverWait(driver, timeout=7).until(lambda d: d.find_element(By.TAG_NAME,"ul") and d.find_element(By.CLASS_NAME,"pvs-list") and d.find_element(By.CLASS_NAME,"ivm-image-view-model"))
    except:
        pass
    edSoup = bs(driver.page_source, 'html.parser')
    edSoup = edSoup.find('ul', {'class':'pvs-list'})
    
    return {
        'education': scrape_education(),
    }