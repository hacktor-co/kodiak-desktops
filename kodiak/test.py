from plugins.toolsbox.WebTools.tools.DirectoryFinder.tool_api_handler import execute_tool


for item in execute_tool(message_pack={
    "Rhost": "http://hacktor.co",
    "ImportFilePath": "/Users/topcoder/Home/Projects/Corps/HackTor/projects/FHack/test/1.txt",
    "UseLocalDatabase": False
}):
    print(item)