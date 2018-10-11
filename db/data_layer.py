from db.base import DbManager
from db.models import System_app, System_config
from pprint import pprint


db = DbManager()

def create_data(table, data_obj):
    try:
        if table == 'system_app':
            data = System_app()
        elif table == 'system_config':
            data = System_config()

        data.parse_json(data_obj, 'create')
        return db.save(data)
    except:
        pass

    return None

def read_data(table, id):
    try:
        if table == 'system_app':
            data_obj = db.open().query(System_app).filter(System_app.id == id).one()
            return System_app().read_data(data_obj)
        elif table == 'system_config':
            data_obj = db.open().query(System_config).filter(System_config.id == id).one()
            return System_config().read_data(data_obj)

    except:
        pass

    return None        


# def read_data_all():
#     return db.open().query(System_app).all()


def update_data(table, id, data_obj):
    try:
        if table == 'system_app':
            data = db.open().query(System_app).filter(System_app.id == id).one()
        elif table == 'system_config':
            data = db.open().query(System_config).filter(System_config.id == id).one()

        data.parse_json(data_obj, 'update')
        return db.save(data)
    except:
        pass
    
    return None

def delete_data(table, id):
    try:
        if table == 'system_app':
            data = db.open().query(System_app).filter(System_app.id == id).one()
        elif table == 'system_config':
            data = db.open().query(System_config).filter(System_config.id == id).one()

        db.delete(data)
        return True
    except:
        pass
    
    return False

 