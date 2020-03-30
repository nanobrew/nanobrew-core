import asyncio
import logging
import sys

import nanoinject
import yaml

from .bootstrap import Bootstrap

async def main():
    logging.info("Starting nanobrew")

    bootstrap = Bootstrap()
    await bootstrap.initialize_plugins()
    await bootstrap.initialize_webserver()
    await bootstrap.activate_sensors()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()