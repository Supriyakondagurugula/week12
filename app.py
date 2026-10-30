from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    return render_template('success.html', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)