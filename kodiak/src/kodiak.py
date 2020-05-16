"""
    - Created on May 13/2020 - hacktorco
    - All rights reserved for hacktor team

    - This package handle kodiak application that user select which kind of
        application want to run, gui base or console base

    - [mjghasempour, abolfazl]
"""

if __name__ == '__main__':

    from core.startup import StartUp

    # start application from this below class
    StartUp().start_app()
