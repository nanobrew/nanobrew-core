import importlib
import logging
import sys

class PluginList:
    _plugins: list

    def __init__ (self, filename: str): 
        # @TODO Probably want to do some error handling here...
        with open(filename) as file_handle:
            self._plugins = file_handle.read().splitlines()

    async def activate(self, config, commands, events, queries):
        logging.debug("Activating plugins")

        for plugin_name in self._plugins:
            logging.debug("Importing plugin " + plugin_name)
            await self._activate_plugin(plugin_name, config, commands, events, queries)

    async def _activate_plugin(self, plugin_name: str, config, commands, events, queries):
        try:
            logging.debug("Activating plugin " + plugin_name)
            plugin = importlib.import_module(plugin_name)
            await plugin.activate(config=config, commands=commands, events=events, queries=queries)
        except ImportError as error:
            logging.error("Can not import plugin " + plugin_name + ", skipping... " + str(error))
