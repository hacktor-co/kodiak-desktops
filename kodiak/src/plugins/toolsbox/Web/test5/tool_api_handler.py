"""
    - Created on Aug 1/2019 - mohammad javad ghasempour
    - email: topcodermc@gmail.com
    - tool for finding directory of web applications
"""

from .tool_api.dir_finder import main_handler

from datetime import datetime


def execute_tool(message_pack: dict):
    """
    :param message_pack: dictionary that contains all params that we need params are:
        ["Rhost"] => the target host url
    :return: yeild all result from target
    """
    rhost = message_pack["Rhost"]
    import_file_path = message_pack["ImportFilePath"] if len(message_pack["ImportFilePath"]) > 0 else None
    use_local_database = message_pack["UseLocalDatabase"]

    for item in main_handler(
            rhost, import_file_path=import_file_path,
            use_local_database=use_local_database
    ):
        yield (
            {
                "response": item,
                "timestamp": datetime.now()
            }
        )