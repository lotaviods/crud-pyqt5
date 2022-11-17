import logging
import sys
from PyQt5 import QtWidgets
from controller.product_controller import ProductController
from ui.product.product_ui_dialog import ProductUiDialog
logger = logging.getLogger()


def configureLogger():
    # Create a handler and set logging level for the handler
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.NOTSET)
    logging.root.setLevel(logging.NOTSET)

    # link handler to logger
    logger.addHandler(c_handler)

if __name__ == '__main__':
    configureLogger()

    logger.log(msg='🚀 Running 🚀 ', level=logging.INFO)

    app = QtWidgets.QApplication(sys.argv)

    dialog = QtWidgets.QDialog()
    ui = ProductUiDialog(controller=ProductController())
    ui.setupUi(dialog)
    dialog.show()

    try:
        app.exec_()
    except:
        logger.error(msg='\n Something went wrong 😭')
    finally:
        logger.log(msg='\n Bye!!', level=logging.INFO)
