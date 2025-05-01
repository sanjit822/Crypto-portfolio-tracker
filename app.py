from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Prices Page
@app.route('/prices')
def prices():
    try:
        response = requests.get('https://api.coingecko.com/api/v3/coins/markets', 
                                 params={'vs_currency': 'usd', 'order': 'market_cap_desc', 'per_page': 10, 'page': 1})
        cryptos = response.json()
    except Exception as e:
        cryptos = []
        print(f"Error fetching crypto prices: {e}")
    return render_template('prices.html', cryptos=cryptos)

# Portfolio Page
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if name and email and message:
            flash('Thank you, your message has been received!', 'success')
        else:
            flash('Please fill out all fields.', 'error')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
