from dotenv import load_dotenv
from flask import Flask, render_template


load_dotenv()
app = Flask(__name__)





@app.route('/')
def home():  # put application's code here

    return render_template("home.html", title="Drive me")


@app.route('/register')
def register():

    return render_template("register.html", title="aanmelden", name="Emiel")

if __name__ == '__main__':
    app.run()
