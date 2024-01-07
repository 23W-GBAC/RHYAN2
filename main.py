from flask import Flask, render_template
import requests
import os
app = Flask(__name__)

NEWS_API_KEY = 'API_KEY'

@app.route('/')
def home():
    # Fetch news about cancer advancements from the News API
    api_url = f'https://newsapi.org/v2/everything?q=cancer&apiKey={NEWS_API_KEY}'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        return render_template('index.html', articles=articles)
    else:
        return f"Error fetching news from the API: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5000)




