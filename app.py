from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create DB if it doesn't exist
def init_db():
    conn = sqlite3.connect('reddit.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, content TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('reddit.db')
    c = conn.cursor()
    c.execute('SELECT * FROM posts ORDER BY id DESC')
    posts = c.fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = sqlite3.connect('reddit.db')
        c = conn.cursor()
        c.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('post.html')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
 
