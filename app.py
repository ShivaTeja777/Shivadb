from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def registration_page():
    return render_template('registration.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    username = request.form['username']
    password = request.form['password']
    return redirect(url_for('display_info', username=username, password=password))

@app.route('/display_info/<username>/<password>')
def display_info(username, password):
    return render_template('display_info.html', username=username, password=password)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
