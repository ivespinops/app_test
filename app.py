from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

CSV_FILE = "users.csv"

# Función para leer los usuarios desde el archivo CSV
def read_users():
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)

# Función para agregar un nuevo usuario al archivo CSV
def add_user(name, email):
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email])

# Ruta de inicio
@app.route('/')
def home():
    users = read_users()
    return render_template('home.html', users=users)

# Ruta sobre nosotros
@app.route('/about')
def about():
    return render_template('about.html')

# Ruta para el formulario de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        add_user(name, email)
        return redirect(url_for('home'))
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)