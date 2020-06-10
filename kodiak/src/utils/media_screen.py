"""
this class Create By mr.robot-ag at june (6/7/2020)
this class have all screen-size
"""

from typing import List, Tuple

from PyQt5.QtWidgets import QDesktopWidget


class MediaScreen:
    def __init__(self):
        super(MediaScreen, self).__init__()
        self.screen_width: int = int(QDesktopWidget().width())
        self.screen_height: int = int(QDesktopWidget().height())

    def __get_small_screen__(self) -> bool:
        """
        this is a private method
        this method check this screen size is small or not

        medium Screen Sizes
        320x569, 360x640, 480x854

        return: boolean
        """
        __width_dpi__: List = [320, 360, 480, 800]  # px
        __height_dpi__: List = [569, 640, 854, 600]  # px
        for width in __width_dpi__:
            if self.screen_width == width:
                for height in __height_dpi__:
                    if self.screen_height == height:
                        # is a small Screen
                        return True
        # is'nt a small Screen
        return False

    def __get_medium_screen__(self) -> bool:
        """
        this is a private method
        this method check this screen size is medium or not

        medium Screen Sizes
        960x540

        return: boolean
        """
        __width_mdpi__: int = 960  # px
        __height_mdpi__: int = 540  # px
        if (self.screen_width >= __width_mdpi__) and (self.screen_width <= __width_mdpi__):
            if self.screen_height <= __height_mdpi__:
                # is a medium Screen
                return True
        return False

    def __get_large_screen__(self) -> bool:
        """
        this is a private method
        this method check this screen size is large or not

        Large Screen Sizes
        1024x640, 1280x1024,1366x768

        return: boolean
        """
        __width_hdpi__: List = [1024, 1280, 1366]  # px
        __height_hdpi__: List = [640, 1024, 768]  # px
        for width in __width_hdpi__:
            if self.screen_width == width:
                for height in __height_hdpi__:
                    if self.screen_height == height:
                        # is a large  Screen
                        return True
        # is'nt a large Screen
        return False

    def __get_extra_large_screen__(self) -> bool:
        """
        this is a private method
        this method check this screen size is extralarge or not

        extraLarge Screen Sizes
        1600x900, 1680x1050,1920x1080

        return: boolean
        """

        __width_hdpi__: List = [1600, 1680, 1920]  # px
        __height_hdpi__: List = [900, 1050, 1080]  # px
        for width in __width_hdpi__:
            if self.screen_width == width:
                for height in __height_hdpi__:
                    if self.screen_height == height:
                        # is a large  Screen
                        return True
        # is'nt a large Screen
        return False

    def is_small(self) -> Tuple[bool, int, int]:
        """
        return: boolean
        """
        if self.__get_small_screen__():
            return True, self.screen_width, self.screen_height
        return False, self.screen_width, self.screen_height

    def is_medium(self) -> Tuple[bool, int, int]:
        """
        return: boolean
        """
        if self.__get_medium_screen__():
            return True, self.screen_width, self.screen_height
        return False, self.screen_width, self.screen_height

    def is_large(self) -> Tuple[bool, int, int]:
        """
        return: boolean
        """
        if self.__get_large_screen__():
            return True, self.screen_width, self.screen_height
        return False, self.screen_width, self.screen_height

    def is_extra_large(self) -> Tuple[bool, int, int]:
        """
        return: boolean
        """
        if self.__get_extra_large_screen__():
            return True, self.screen_width, self.screen_height
        return False, self.screen_width, self.screen_height
