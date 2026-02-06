from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/blog")
def blog():
    context = {
        'title': 'Post 1',
        'content': 'Texto del post',
    }
    return render_template('blog.html', **context)

@app.route("/blog-posts")
def blog_posts():
    context = {
        'post': [
            {
                'title': 'Primer post',
                'content': 'Contenido del primer post'
            },
            {
                'title': 'Segundo post',
                'content': 'Contenido del segundo post'
            },
            {
                'title': 'Tercer post',
                'content': 'Contenido del tercer post'
            }
        ]
    }
    return render_template('blogtarea2.html', **context)

@app.route("/mi-blog")
def mi_blog():
    return render_template('blogtarea2.html')

if __name__ == '__main__':
    app.run(debug=True)
