from flask import Flask, render_template
import requests

app = Flask(__name__)

res = requests.get('https://api.npoint.io/813b4d1a4390656ce640').json()


@app.route('/')
def home():
    return render_template("index.html", posts=res)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:idx>')
def post(idx):
    requested_post = None
    for blog_post in res:
        if blog_post["id"] == idx:
            requested_post = blog_post
    
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
