from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Andrei',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date': 'April 22 2020'
    },
    {
        'author': 'Stink',
        'title': 'Blog Post 2',
        'content': 'first post content',
        'date': 'April 24 2020'
    }

]
# route: what we type into browser to get to pages
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

if __name__ == '__main__':
    app.run(debug = True)