import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

logging.debug('Этот лог уровня DEBUG')
logging.info('Этот лог уровня INFO')
logging.warning('Этот лог уровня WARNING')
logging.error('Этот лог уровня ERROR')
logging.critical('Этот лог уровня CRITICAL')

print(logger)