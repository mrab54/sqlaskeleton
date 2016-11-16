import logging.config
from os import path

from settings import DB_ENGINE_URL
from sqlaskeleton.model import DBSession
from sqlalchemy import create_engine

base_dir = path.split(path.dirname(__file__))[0]
log_file_name = 'logging.ini'
log_path = path.abspath(path.join(base_dir, log_file_name))
log = logging.getLogger(__name__)


def init_db():
    log.info('Initializing databse engine and session')
    engine = create_engine(DB_ENGINE_URL)
    DBSession.configure(bind=engine)


def init():
    logging.config.fileConfig(log_path)

    init_db()
