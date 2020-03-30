import importlib
import logging
import sys

from ..app import App

class PluginList:
    _plugins: list

    def __init__ (self, filename: str): 
        # @TODO Probably want to do some error handling here...
        with open(filename) as file_handle:
            self._plugins = file_handle.read().splitlines()

    async def activate(self, app: App):
        logging.debug("Activating plugins")

        for plugin_name in self._plugins:
            logging.debug("Importing plugin " + plugin_name)
            await self._activate_plugin(plugin_name, app)

    async def _activate_plugin(self, plugin_name: str, app: App):
        try:
            logging.debug("Activating plugin " + plugin_name)
            plugin = importlib.import_module(plugin_name)
            await plugin.activate(app)
        except ImportError as error:
            logging.error("Can not import plugin " + plugin_name + ", skipping... " + str(error))
