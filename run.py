import asyncio
import sys

from nanobrew.core.main import main

try:
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
except KeyboardInterrupt:
    print("Exiting nanobrew...")
    sys.exit(0)
