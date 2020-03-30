import logging

import nanoinject
import yaml

from .bootstrap import Bootstrap

async def main():
    log_format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'

    logging.basicConfig(level=logging.INFO, format=log_format)
    logging.info("Starting nanobrew")

    bootstrap = Bootstrap()
    await bootstrap.initialize_plugins()
    await bootstrap.initialize_webserver()
    await bootstrap.activate_sensors()
