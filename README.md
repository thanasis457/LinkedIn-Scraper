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


## How it works

### Problem 1: Handling login
LinkedIn is notoriously difficult to scrape because of its many anti-abuse systems that prevent scrapers from runnning an unbounded nunmber of requests.  
How does that affect login? If LinkedIn detects that we abuse the system it will usually log us out and prompt us to log again or, most commonly, next time we leave the page we need to re-sign and solve some puzzle. Thus, automating the login is not advised as in the long run it is better to handle login through a slower yet more robust UI that enables to bypass puzzles and other 2FA techniques that a simple script could fail upon. The downside is that every time we start the server we need to manually enter our credentials at the LinkedIn login page.

For anyone interested, there is a way to automate login. If we inspect the network traffic durin login, there is a POST request being made. If we use that endpoint and send our email, password, and csrf token (JSESSIONID) then we can authenticate ourselves without any interaction.
However, as already stated, we cannot bypass 2FA security. After an unknown number of requests or unusually high traffic, LinkedIn will include some cookies with the name "trk...". These are used by LinkedIn for preventing abuse [as mentioned here](https://www.linkedin.com/legal/l/cookie-table). I have not found a way to get around them but when they appear you are forced to solve a puzzle or something similar, in addition to providing credentials.

### Problem 2: Scraping

Scraping basic profile features is easy. With a little patience and careful inspection of the DOM tree we can do a pretty good job at scraping. However, experience, education, and some other sections may overflow and thus not be shown in the main page. The solution to this problem is to navigate to ```/details/{section}``` where section could be "experience" and we get the full list of that profile's section. One other possible solution not present implementation is to make an signed out/anonymous visit to the profile. LinkedIn presents the full gamma of each profile for signed out users. This would inherently speed our scraping too since we need not render more than a single page. The big downside is that LinkedIn is pretty aggressive at putting an Auth wall once it notices even moderate traffic coming from the same device. Thus, unauthenticated requests work good on the short term but are too unreliable for stable use.


### Problem 3: Avoiding a ban

There is no single answer to this one but as a rule of thumb we should avoid repeated requests on short timescales, especially for new accounts, and making sure that our activity looks as 'human-like' as possible. This topic has been extensively studied about by more experienced developers. [Here is a good link to a blog about it](https://phantombuster.com/blog/guides/linkedin-automation-rate-limits-2021-edition-5pFlkXZFjtku79DltwBF0M).
This project is meant to be used by a single user, not by thousands of users looking to do hundreds of scrapes per day. A simple technique this project implements is waiting a small arbitrary amount of time between requests to simulate human behaviour.