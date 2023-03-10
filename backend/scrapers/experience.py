from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import copy


def scrape(driver, url):
    def scrape_experience():
        experience = []
        pastExperience = []
        try:
            pastExperience = expSoup.find_all('li', recursive=False)
        except:
            pass

        for exp in pastExperience:
            job = {}
            subjobs=[]
            try:
                subjobs = exp.div.div.find_all('div', recursive=False)[1].find_all('div', recursive=False)[1].ul.li.div.div.div.ul.find_all('li', recursive=False)
            except:
                pass
            # pprint(subjobs[0])
            if(len(subjobs)!=0):
                for sj in subjobs:
                    job={}
                    try:
                        job['company'] = exp.div\
                                    .div\
                                    .find_all('div', recursive=False)[1]\
                                    .div\
                                    .a\
                                    .div\
                                    .span\
                                    .span\
                                    .text
                    except:
                        job['company'] = 'N/A'
                    
                    try:
                        job['location'] = exp.div\
                                    .div\
                                    .find_all('div', recursive=False)[1]\
                                    .div\
                                    .a\
                                    .find('span', recursive=False, attrs={'class': 't-black--light'})\
                                    .span\
                                    .text
                    except:
                        try:
                            job['location'] = sj.div\
                                .div\
                                .find_all('div', recursive=False)[1]\
                                .div\
                                .a\
                                .find_all('span', recursive=False, attrs={'class': 't-black--light'})[1]\
                                .span\
                                .text
                        except:
                            job['location'] = 'N/A'
                    
                    try:
                        job['position'] = sj.div\
                            .div\
                            .find_all('div', recursive=False)[1]\
                            .div\
                            .a\
                            .div\
                            .span\
                            .span\
                            .text
                    except:
                        job['position'] = 'N/A'
                    
                    try:
                        job['dateRange'] = sj.div\
                            .div\
                            .find_all('div', recursive=False)[1]\
                            .div\
                            .a\
                            .find('span', recursive=False, attrs={'class': 't-black--light'})\
                            .span\
                            .text
                    except:
                        job['dateRange'] = 'N/A'
                    
                    try:
                        job['description'] = sj.div\
                            .div\
                            .find_all('div', recursive=False)[1]\
                            .find_all('div', recursive=False)[1]\
                            .ul\
                            .li\
                            .text\
                            .strip()
                    except:
                        job['description'] = 'N/A'
                        
                    experience+=[copy.deepcopy(job)]

                continue
                    
                
            try:
                job['position'] = exp.div\
                    .div\
                    .find_all('div', recursive=False)[1]\
                    .div\
                    .div\
                    .div\
                    .span\
                    .span\
                    .text
            except:
                job['position'] = 'N/A'
            try:
                job['company'] = exp.div\
                    .div\
                    .find_all('div', recursive=False)[1]\
                    .div\
                    .div\
                    .find('span', recursive=False)\
                    .span\
                    .text\
                    .split('·')[0]
            except:
                job['company'] = 'N/A'
            
            try:
                job['job'] = exp.div\
                    .div\
                    .find_all('div', recursive=False)[1]\
                    .div\
                    .div\
                    .find('span', recursive=False)\
                    .span\
                    .text\
                    .split('·')[1]
            except:
                job['job'] = 'N/A'
            
            try:
                job['dateRange'] = exp.div\
                    .div\
                    .find_all('div', recursive=False)[1]\
                    .div\
                    .div\
                    .find_all('span', recursive=False)[1]\
                    .span\
                    .text
            except:
                job['dateRange'] = 'N/A'
                    
            try:
                job['location'] = exp.div\
                    .div\
                    .find_all('div', recursive=False)[1]\
                    .div\
                    .div\
                    .find_all('span', recursive=False)[2]\
                    .span\
                    .text
            except:
                job['location'] = 'N/A'

            try:
                job['description'] = exp.div\
                    .div\
                    .find_all('div', recursive=False)[1]\
                    .find_all('div', recursive=False)[1]\
                    .ul\
                    .li\
                    .div\
                    .ul\
                    .li\
                    .div\
                    .div\
                    .div\
                    .span\
                    .text
            except:
                job['description'] = 'N/A'
                    
            experience+=[job]
        return experience
    
    # def experience_initialised(driver):
    driver.get(url+'details/experience/')
    try:
        WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.TAG_NAME,"ul") and d.find_element(By.CLASS_NAME,"pvs-list"))
    except:
        pass
    expSoup = bs(driver.page_source, 'html.parser')
    expSoup = expSoup.find('ul', {'class':'pvs-list'})
    
    return {
        'experiences': scrape_experience(),
    }