from pizzashare import db, models

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
