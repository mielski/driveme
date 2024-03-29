import datetime
import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, session, redirect, url_for, abort

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

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


users = {"test": "test"}

# This is obsolete and eventually needs to be replaced with the users databse
app.selections = {"ae23": 'absent',
                  "ds3s": 'maybe',
                  }


@app.context_processor
def inject_name():
    return dict(name=session.get('name'))


def get_date_elements(date: datetime.date):

    return (date.strftime("%Y-%m-%d"), date.strftime("%d %B"))

def get_event_from_id(event_id):

    event_found = [e for e in events if e["event_id"] == event_id]
    if event_found:
        return event_found[0]
    else:
        return None


@app.route('/', methods=["GET", "POST"])
def home():  # put application's code here

    name = session.get('name')
    if not name in users:
        return redirect(url_for('login'))
    if request.method == "POST":
        form = request.form
        event_id = form.get("event_id")
        return redirect(url_for('join_event', event_id=event_id))

    for event in events:
        event["isodate"], event["shortdate"] = get_date_elements(event["date"])

    return render_template("home.html", title="Drive me", events=events, selections=app.selections)


@app.route('/join', methods=["GET", "POST"])
def join_event():
    event_id = request.args.get('event_id')
    if event := get_event_from_id(event_id):
        print(event)
        return render_template("register.html", event=event, title='join event')
    else:
        abort(400, "no event found, missing or wrong event_id provided in request")


@app.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')
        print(password, users.get(name), password == users.get(name))

        if not password == users.get(name):
            message = 'invalid username or password'
            return render_template("login.html", message=message)
        else:
            session['name'] = name
            return redirect(url_for('home'))
    return render_template("login.html", message='')

@app.route('/logout')
def logout():
    if session.get('name'):
        del session['name']

    return redirect(url_for("login"))


@app.route('/about')
def about():
    return "work in progress"
    flask.l

@app.route('/registreren', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')
        token = request.form.get('token')
        users[name] = password

        # check token
        if not token == os.environ.get('REGISTER_TOKEN'):
            return render_template('signup.html', title="aanmelden", message='illegal token')


        return redirect(url_for('login'))
    return render_template('signup.html', title="aanmelden")


if __name__ == '__main__':
    app.run()
