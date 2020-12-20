"""
    - Created on 06/24/2020 by mjghasempour - hacktorco
    - All rights reserved for hacktor team

    - This package create tool page for each categories of toolsbox
"""

from .components.registered_part.registered import Registered
from .components.unregistered_part.unregistered import UnRegistered
from utils.dir_manager import DirManager

from importlib import import_module
from typing import List


class ToolPageMaker:

    def __init__(self, parent, form_base_layout, scroll_area_contents_page_containers, tool_box: str):
        super(ToolPageMaker, self).__init__()
        self.parent = parent
        self.scroll_area_contents_page_containers = scroll_area_contents_page_containers
        self.form_base_layout = form_base_layout
        self.tool_box: str = tool_box

        self.registered_tool: List = list()
        self.unregistered_tool: List = list()

    def make_page(self):
        self.__load_tool_plugins__()

        Registered(self.form_base_layout).setup_ui(
            containers=self.scroll_area_contents_page_containers, plugins=self.registered_tool
        )
        UnRegistered(self.form_base_layout).setup_ui(
            containers=self.scroll_area_contents_page_containers, plugins=self.unregistered_tool
        )

    def __load_tool_plugins__(self):
        dir_manager = DirManager()

        tools_list_name = [
            tool for tool in dir_manager.get_all_directory(
                f"{dir_manager.current_dir}/plugins/toolsbox/{self.tool_box}"
            )
        ]

        self.registered_tool.clear()

        for tool_name in tools_list_name:
            plugin_module_path = f"plugins.toolsbox.{self.tool_box}.{tool_name}.gui_handler"
            plugin_module = import_module(plugin_module_path)
            plugin = plugin_module.GUIHandler()

            plugin_mainico: str = \
                f"{dir_manager.current_dir}/plugins/toolsbox/{self.tool_box}/{tool_name}/assets/mainico.svg"
            plugin_item_collection: tuple = (plugin, plugin_mainico, tool_name)

            self.registered_tool.append(plugin_item_collection)

        del dir_manager
