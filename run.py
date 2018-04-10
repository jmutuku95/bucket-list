import os
from app import db, create_app
from app.models import User, Bucketlist

config_name = os.getenv('APP_SETTINGS')  # config_name = "development"
app = create_app(config_name)


@app.shell_context_processor
def make_shell_context():
    '''conteext when flask shell runs to avoid cimbersome imports'''
    return {'db': db, 'User': User, 'Bucketlist': Bucketlist}


