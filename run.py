from app import app, db
from app.models import User, Bucketlist


@app.shell_context_processor
def make_shell_context():
    '''conteext when flask shell runs to avoid cimbersome imports'''
    return {'db': db, 'User': User, 'Bucketlist': Bucketlist}
