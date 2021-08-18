from db import init_db

if __name__ == "__main__":
    init_db()
    from db import db_session
    from models import User
    # u = User('admin', 'admin@localhost')
    # db_session.add(u)
    # db_session.commit()
    print(User.query.all())

