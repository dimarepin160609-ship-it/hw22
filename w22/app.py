from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from forms import LoginForm, MessageForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-random-key' # Обов'язково для токенів
csrf = CSRFProtect(app) # Вмикаємо захист для всього додатку

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return "Вхід успішний!"
    return render_template('index.html', form=form, title="Вхід")

@app.route('/message', methods=['GET', 'POST'])
def send_message():
    form = MessageForm()
    if form.validate_on_submit():
        return "Повідомлення відправлено!"
    return render_template('index.html', form=form, title="Повідомлення")

if __name__ == '__main__':
    app.run(debug=True)