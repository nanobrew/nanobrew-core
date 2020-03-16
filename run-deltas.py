import sys
import asyncio
import logging
import aiosqlite

from nanobrew.delta import DeltaLog
from nanobrew.delta import DeltaFinder
from nanobrew.delta import DeltaRunner

async def run_deltas():
    try:
        db = await aiosqlite.connect('nanobrew.db')
        db.row_factory = aiosqlite.Row

        log = await DeltaLog.create(db)
        runner = DeltaRunner(db, log)
        finder = DeltaFinder("dev/deltas")
        
        latest = await log.get_latest()
        deltas = await finder.find_newer(latest)

        if len(deltas) == 0:
            logging.info("No new deltas found")

        for delta in deltas.values():
            logging.info("Running delta " + delta.get_name())
            await runner.run(delta)

        await db.close()
    finally:
        await db.close()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

asyncio.run(run_deltas())