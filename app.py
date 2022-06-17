import datetime

from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)


events = [
    {"event_id": "ae23",
     "title": "Teddybear hospital",
     "desc": "Leer over het ziekenhuis en laat je knuffel beter worden in het ziekenhuis.",
     "date": datetime.date(2020, 6, 26),
     "start": "9:00",
     "end": "11:00",
     "cars": 24,
     "needed": 27,
     },
    {"event_id": "ds3s",
     "title": "Oud Valkeveen",
     "desc": "Ga mee met de draak of neem een duik.",
     "date": datetime.date(2020, 7, 31),
     "start": "9:00",
     "end": "14:15",
     "cars": 12,
     "needed": 27,
     }
]

NO, MAYBE, YES = range(3)

userdata = dict(id=1,
              kids=3,
              status={
                  "ds3s": "absent",
                  "ae23": "present",
              })
app.userdata = userdata


def get_date_elements(date: datetime.date):

    return (date.strftime("%Y-%m-%d"), date.strftime("%d %B"))


@app.route('/', methods=["GET", "POST"])
def home():  # put application's code here

    if request.method == "POST":
        form = request.form
        event_id = form.get("event_id")
        new_status = form.get("submit")
        app.userdata["status"][event_id] = new_status


    for event in events:
        event["isodate"], event["shortdate"] = get_date_elements(event["date"])

    return render_template("home.html", title="Drive me", events=events, selections=app.userdata["status"])


@app.route('/register')
def register():

    return render_template("register.html", title="aanmelden", name="Emiel")


if __name__ == '__main__':
    app.run()
