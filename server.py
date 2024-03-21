import os

from flask import Flask, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
from flask import render_template
from flask_login import LoginManager, login_user
from data.fogin_form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init('db/mars_explorer.db')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # user = User()
    # user.surname = 'Scott'
    # user.name = 'Ridley'
    # user.age = 21
    # user.position = 'captain'
    # user.speciality = 'research engineer'
    # user.address = 'module_1'
    # user.email = 'scott_chief@mars.org'
    # session.commit()
    #
    # user_1 = User()
    # user_1.surname = 'Scott_1'
    # user_1.name = 'Ridley'
    # user_1.age = 21
    # user_1.position = 'capitan'
    # user_1.speciality = 'research engineer'
    # user_1.address = 'module_1'
    # user_1.email = 'scott_chief_1@mars.org'
    #
    # user_2 = User()
    # user_2.surname = 'Scott_2'
    # user_2.name = 'Ridley'
    # user_2.age = 21
    # user_2.position = 'capitan'
    # user_2.speciality = 'research engineer'
    # user_2.address = 'module_1'
    # user_2.email = 'scott_chief_2@mars.org'
    #
    # user_3 = User()
    # user_3.surname = 'Scott_3'
    # user_3.name = 'Ridley'
    # user_3.age = 21
    # user_3.position = 'capitan'
    # user_3.speciality = 'research engineer'
    # user_3.address = 'module_1'
    # user_3.email = 'scott_chief_3@mars.org'
    #
    # session.add(user)
    # session.add(user_1)
    # session.commit()


@app.route('/')
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    for user in session.query(User).all():
        print(user)
    users = session.query(User).all()
    names = {name.id: (name.surname, name.name) for name in users}
    print(names)
    return render_template('index.html', jobs=jobs, names=names)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


if __name__ == '__main__':
    main()
