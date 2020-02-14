from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost:27017/mars_app'
mongo=PyMongo(app)

# ​Route to render index.html template using data from Mongo
@app.route("/")

def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# ​Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
# ​ Update the Mongo database using update and upsert=True
    mars.update({}, mars_data, upsert=True)
    print('Scrapping Successful!')
    return redirect("/", code=302)
if __name__ == "__main__":
    app.run(debug=True)