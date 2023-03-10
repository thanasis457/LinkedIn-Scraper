# LinkedIn Scraper
A project aiming to easily scrape profiles off of LinkedIn

![](https://imgur.com/jOoEu2h.png)

## Setup
### Download Project
```git clone https://github.com/thanasis457/LinkedIn-scraper LinkedIn_Scraper```  
```cd LinkedIn_Scraper```

### Backend
Navigate to directory: ```cd backend```  
Install dependencies: ```pip install -r requirements.txt```  
Start: ```python3 app.py```

### Frontend
Navigate to directory: ```cd frontend```  
Install dependencies: ```npm i```  
Start: ```npm start```


### Notes on the backend scraper
When starting the backend server, you will need to enter your LinkedIn credentials twice. You will first be prompted to enter them in the terminal. After that, a browser window should open and prompt you to login to LinkedIn directly from the website. The first is used for the API calls and the second for the scraper.

### Ports
The backend occupies port ```5600``` but you can also configure that manually in the code.  
The frontend occupies by default port ```3000```.

### Making GET requests
The backend is very barebones and only supports one request, namely scraping a profile.
If you want to test it or make external calls (ie. using Postman) the GET endpoint is ```/profile``` and the params should look like this:
```
{  
  profile: "Enter the profile url here",
  method: "Choose either 'scrape' or 'api'"
}
```

## How it works

### The scraper
The first option to fetch profiles is to scrape them. An automated browser visits the profile through an authenticated account and scrapes the data we want. The difficulty here is to wait enough time for LinkedIn to not suspect the account for scraping but not long enough that makes the response time unbearably long.

Inside the project there is also an unused implementation of automated authentication, taking advantage of an authentication post request we can observer from simply inspecting the LinkedIn page and selecting the values of some cookies to mask ourselves as a user in a normal browsing session. The downside is that if LinkedIn suspects us of abusing the platform it starts sending cookies with a name like "trk..." which are used for abuse prevention [as mentioned here](https://www.linkedin.com/legal/l/cookie-table). I have not found a way around them so this method is not reliable long term, which is why this project uses the traditional slow but safe manual UI login.

### The API
LinkedIn uses an API called Voyager. Access to it closed to authorised users but we can smartly pick the necessary cookies out of an existing LinkedIn session to gain access to the api. The majority of the functionality is handled by a 3rd party python module. The downside is that we might run into the same issue as with automated authentication, meaning LinkedIn could block us out. In addition, the current implementation of the python module does not return recommendations.


## Other Notes
Everything has been tested using Python 3.8 and I would not advise using any Python version >=3.10.

Conda has also been tested to work, but always ensure that the conda packages have the specified versions available or you should have to use pip.

