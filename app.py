from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect('cadastro.db')
    return conn

def create_table():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL,
                 email TEXT NOT NULL,
                 senha TEXT NOT NULL,
                 crm TEXT,
                 cidade TEXT)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        crm = request.form['crm']
        cidade = request.form['cidade']

        conn = connect_db()
        c = conn.cursor()
        c.execute("INSERT INTO usuarios (nome, email, senha, crm, cidade) VALUES (?, ?, ?, ?, ?)", 
                  (nome, email, senha, crm, cidade))
        conn.commit()
        conn.close()

        return redirect(url_for('sucesso'))

    return render_template('index.html')

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

if __name__ == '__main__':
    create_table() 
    app.run(debug=True)
