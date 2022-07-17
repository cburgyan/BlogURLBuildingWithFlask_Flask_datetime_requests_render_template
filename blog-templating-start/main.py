from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

url = 'https://api.npoint.io/ec84679d2403beee8160'
blog_posts_json = requests.get(url=url).json()
post_list = []
for post in blog_posts_json:
    post_list.append(Post(id=post["id"], title=post["title"], subtitle=post["subtitle"], body=post["body"]))


@app.route('/')
def home():
    return render_template("index.html", posts=blog_posts_json)


@app.route('/post/<blog_id>')
def post_page(blog_id):
    title = ""
    subtitle = ""
    body = ""
    for post in post_list:
        if post.id == int(blog_id):
            title = post.title
            subtitle = post.subtitle
            body = post.body
            break
    return render_template('post.html', title=title, subtitle=subtitle, body=body)

if __name__ == "__main__":
    app.run(debug=True)
