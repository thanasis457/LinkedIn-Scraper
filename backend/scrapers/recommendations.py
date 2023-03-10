from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
import re

def scrape(driver, url):
    
    def scrape_recommendations():
        recommendations = []
        pastRecommendations = recSoup.find_all('li', recursive=False)

        for rec in pastRecommendations:
            recLi = {}
            try:
                recLi['name'] = rec.div\
                    .div\
                    .find_all('div', recursive=False)[1]\
                    .div\
                    .a\
                    .div\
                    .span\
                    .span\
                    .text
            except:
                recLi['name'] = 'N/A'
            
            try:
                recLi['profile'] = rec.div\
                    .div\
                    .find_all('div', recursive=False)[1]\
                    .div\
                    .a\
                    .get('href')
            except:
                recLi['profile'] = 'N/A'

            try:
                subtitle = rec.div\
                    .div\
                    .find_all('div', recursive=False)[1]\
                    .div\
                    .a\
                    .find('span', attrs = {'class': 't-black--light'}, recursive=False)\
                    .span\
                    .text\
                    .split()
                
                recLi['date'] = ' '.join(subtitle[:3])
                recLi['relationship'] = ' '.join(subtitle[3:])
            except Exception as e:
                print(e)
                recLi['date'] = 'N/A'
                recLi['relationship'] = 'N/A'
            
            try:
                recLi['testimonial'] = rec.div\
                    .div\
                    .find_all('div', recursive=False)[1]\
                    .find_all('div', recursive=False)[1]\
                    .find('div', attrs={'class': 't-normal'})\
                    .span\
                    .text
            except:
                recLi['testimonial'] = 'N/A'
            
            recommendations+=[recLi]

        print(recommendations)
        return recommendations
    
    driver.get(url+'details/recommendations/')
    try:
        WebDriverWait(driver, timeout=7).until(lambda d: d.find_element(By.TAG_NAME,"ul") and d.find_element(By.CLASS_NAME,"pvs-list") and d.find_element(By.CLASS_NAME,"t-black--light"))
    except:
        pass
    recSoup = bs(driver.page_source, 'html.parser')
    recSoup = recSoup.find('ul', {'class':'pvs-list'})
    
    return {
        'recommendations': scrape_recommendations(),
    }