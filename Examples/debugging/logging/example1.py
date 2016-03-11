import logging
import worker

format='%(asctime)s %(message)s'

logging.basicConfig(filename='example.log', format=format, level=logging.DEBUG)


logging.debug("debug level message")
logging.warning("debug level message")

worker.worker()

logging.info("test complete")
