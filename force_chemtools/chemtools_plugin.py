from force_bdss.api import BaseExtensionPlugin, plugin_id

PLUGIN_VERSION = 0


class ChemtoolsPlugin(BaseExtensionPlugin):
    """This plugin provides useful classes and DatsSource subclasses
    for creating and running chemtools.
    """

    id = plugin_id("chemtools", "wrapper", PLUGIN_VERSION)

    def get_name(self):
        return "Chemtools Plugin"

    def get_description(self):
        return (
            "A plugin containing useful chemical objects"
        )

    def get_version(self):
        return PLUGIN_VERSION

    #: Define the factory classes that you want to export to this list.
    def get_factory_classes(self):
        return []

