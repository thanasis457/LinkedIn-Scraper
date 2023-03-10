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
When starting the backend server, a window should open up prompting you to login to your LinkedIn. Sign in as this will be the account used for accessing and scraping other accounts

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
