
from .registered_part.registered import Registered
from .unregistered_part.unregistered import UnRegistered
from utils.dir_manager import DirManager

from importlib import import_module


class ToolPageMaker:

    def __init__(self, parent, form_base_layout, scroll_area_contents_page_containers, tool_box: str):
        super(ToolPageMaker, self).__init__()
        self.parent = parent
        self.scroll_area_contents_page_containers = scroll_area_contents_page_containers
        self.form_base_layout = form_base_layout
        self.tool_box: str = tool_box

    def make_page(self):
        self.__load_tool_plugins__()

        Registered(self.form_base_layout).setup_ui(containers=self.scroll_area_contents_page_containers)
        UnRegistered(self.form_base_layout).setup_ui(containers=self.scroll_area_contents_page_containers)

    def __load_tool_plugins__(self):
        dir_manager = DirManager()

        tools_list_name = [
            tool for tool in dir_manager.get_all_directory(
                f"{dir_manager.current_dir}/plugins/toolsbox/{self.tool_box}"
            )
        ]

        # TODO: Error on loading plugins

        # for tool_name in tools_list_name:
        plugin_module_path = f"plugins.toolsbox.{self.tool_box}.UrlFuzzer.gui_handler"
        plugin_module = import_module(plugin_module_path)
        plugin = plugin_module.GUIHandler()
        plugin.execute_app()

        del dir_manager
