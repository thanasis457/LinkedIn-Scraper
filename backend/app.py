from flask import Flask, request, Response
from flask_cors import CORS
import re
from scraper import Scraper
app = Flask(__name__)
CORS(app)
scraper = None

busy = False

@app.route("/profile", methods = ['GET'])
def scrape_profile():
    global busy
    global scraper
    if(busy):
        return (Response("Busy handling previous request. Give it a few seconds to finish"), 503)
    busy = True
    profile = request.args.get("profile", default=None, type=str)
    print(request.args)
    if(profile == None):
        return (Response("No profile was specified"), 400)
    method = request.args.get("method", default="scrape", type=str)
    busy=False
    res= scraper.scrape_all(profileURL=profile, method = method)
    return res
    

@app.route("/", methods = ['GET'])
def status():
    return "<p>Hello!</p>"

if(__name__ == "__main__"):
    scraper = Scraper()
    app.run(host="localhost", port = 5600, debug=False)
    scraper.driver.quit()