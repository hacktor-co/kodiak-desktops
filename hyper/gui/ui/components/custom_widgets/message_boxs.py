"""
    - Created on Nov 9/2019 - hacktorco
    - All rights reserved for hacktor team

    - this package use for global message boxs
"""

from gui.common.styles.custom_widgets.message_boxs_styles import *

from PyQt5.QtWidgets import QMessageBox

def message_box_error(windows_title, title, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(title)
    msg.setInformativeText(text)
    msg.setWindowTitle(windows_title)
    msg.setAccessibleName(main_message_box_style[0])
    msg.setStyleSheet(main_message_box_style[1])
    msg.exec_()

def message_box_information(windows_title, title, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(title)
    msg.setInformativeText(text)
    msg.setWindowTitle(windows_title)
    msg.setAccessibleName(main_message_box_style[0])
    msg.setStyleSheet(main_message_box_style[1])
    msg.exec_()
