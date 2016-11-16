import sys

from sqlaskeleton.service.example import ExampleService
from sqlaskeleton import init
from sqlaskeleton.model import session_scope


def main(argv):
    init()

    import logging
    log = logging.getLogger(__name__)
    log.info(argv)

    with session_scope() as session:
        ex_svc = ExampleService(session)
        # ex_svc.create_tables()
        ex_svc.run_it()


if __name__ == '__main__':
    main(sys.argv)
