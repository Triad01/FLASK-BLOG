from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        "author": "Triad",
        "title": "Blog post 1",
        "content": "First Blog conetent",
        "date_posted": "March 22, 2024"
    },
     {
        "author": "Goodluck",
        "title": "Blog post 2",
        "content": "Second Blog conetent",
        "date_posted": "March 22, 2024"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)