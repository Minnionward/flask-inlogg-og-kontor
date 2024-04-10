from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Brukerkontoer (brukernavn og passord)
USER_CREDENTIALS = {'minion': '123QWEr'}

# Liste over kontorer som er leid ut dette ser du i dashboardet. jeg bruker lister som midlertidig løsning for å teste at ting fungerer
rented_offices = []

# Funksjon for å sjekke om brukernavn og passord er gyldige
def check_credentials(username, password):
    return username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password

# Innloggingsside hvor brukere blir sendt til dashboard etter vellykket innlogging
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_credentials(username, password):
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', message='Invalid username or password')
    return render_template('login.html', message=None)

# Dashboard htmlen som du blir sent til etter inlogging
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', rented_offices=rented_offices)

# Legg til et kontor hvor du kan se kontorer som er lagret og også slette de lagrede kontorene via dette dashboardet
@app.route('/add_office', methods=['POST'])
def add_office():
    office_name = request.form['office_name']
    rented_offices.append(office_name)
    return redirect(url_for('dashboard'))

# Slett et kontor fra listen med alle kontorene 
@app.route('/delete_office/<office_name>', methods=['POST'])
def delete_office(office_name):
    rented_offices.remove(office_name)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
