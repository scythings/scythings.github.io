from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/discords')
def discords():
    return render_template('discords.html')

@app.route('/guilds')
def guilds():
    return render_template('guilds.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
