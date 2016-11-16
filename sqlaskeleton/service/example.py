import logging

from sqlaskeleton.model import Base
from sqlaskeleton.model.example import Example

log = logging.getLogger(__name__)


class ExampleService(object):

    def __init__(self, db_session):
        self.db_session = db_session

    def run_it(self):
        log.info('Starting run_it()')

        q = self.db_session.query(Example)

        for r in q.all():
            log.info(r)

    def create_tables(self):
        # import pdb; pdb.set_trace()
        # from sqlalchemy.schema import CreateSchema
        # self.db_session.bind.execute(CreateSchema('sqlaskeleton'))

        Base.metadata.create_all(self.db_session.bind)
        log.info('Finished createing tables.')
