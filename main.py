from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/mars_explorer.db')
    app.run()

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


if __name__ == '__main__':
    main()
