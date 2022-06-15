import datetime

from dotenv import load_dotenv
from flask import Flask, render_template


load_dotenv()
app = Flask(__name__)


events = [
    {"title": "Teddybear hospital",
     "desc": "Leer over het ziekenhuis en laat je knuffel beter worden in het ziekenhuis.",
     "date": datetime.date(2020, 6, 26),
     "start": "9:00",
     "end": "11:00",
     "cars": 24,
     "needed": 27,
     },
    {"title": "Oud Valkeveen",
     "desc": "Ga mee met de draak of neem een duik.",
     "date": datetime.date(2020, 7, 31),
     "start": "9:00",
     "end": "14:15",
     "cars": 12,
     "needed": 27,
     }
]

def get_date_elements(date: datetime.date):

    return (date.strftime("%Y-%m-%d"), date.strftime("%d %B"))

@app.route('/')
def home():  # put application's code here

    for event in events:
        event["isodate"], event["shortdate"] = get_date_elements(event["date"])
    return render_template("home.html", title="Drive me", events=events)


@app.route('/register')
def register():

    return render_template("register.html", title="aanmelden", name="Emiel")

if __name__ == '__main__':
    app.run()
