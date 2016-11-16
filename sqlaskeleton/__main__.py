import logging
import sys

from sqlaskeleton.service.example import ExampleService
from sqlaskeleton import init
from sqlaskeleton.model import session_scope

log = logging.getLogger(__name__)


def main():

    init()

    args = sys.argv[1:]
    log.info(args)

    with session_scope() as session:
        ex_svc = ExampleService(session)
        # ex_svc.create_tables()
        ex_svc.run_it()


if __name__ == '__main__':
    main()
