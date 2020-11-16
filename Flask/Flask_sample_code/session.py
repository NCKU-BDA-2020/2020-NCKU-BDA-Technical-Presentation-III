from flask import Flask, session, redirect, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "pisnai"

@app.route('/')
def hello():
    return redirect(url_for("visits"))
    
@app.route('/visits-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
        session.permanet = True
        session.permanent_session_lifetime = timedelta(hours = 1)
    return "Total visits: {}".format(session.get('visits'))

@app.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None) # delete visits
    return 'Visits deleted'

if __name__ == "__main__":
	app.run(debug=True)
    
