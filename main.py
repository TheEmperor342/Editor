from modules.ui_main import Ui_MainWindow
from modules.imports import *
from os import system, path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ==> MAKING UI
        # /////////////////////////////////////////////////

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # /////////////////////////////////////////////////

        # ==> REMOVING TITLE BAR
        # /////////////////////////////////////////////////

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui.titleBar.mouseMoveEvent = self.moveWindow
        self.ui.topBar.mouseMoveEvent = self.moveWindow

        # /////////////////////////////////////////////////

        # ==> CONNECTING BUTTONS
        # /////////////////////////////////////////////////

        self.ui.closeBtn.clicked.connect(self.close)
        self.ui.maxBtn.clicked.connect(self.maxMin)
        self.ui.minimizeBtn.clicked.connect(self.showMinimized)

        self.ui.saveFileBtn.clicked.connect(self.saveFile)
        self.ui.saveAsBtn.clicked.connect(self.saveAs)
        self.ui.openFileBtn.clicked.connect(self.openFile)
        self.ui.runFileBtn.clicked.connect(self.runFile)

        # /////////////////////////////////////////////////

        # ==> VARIABLES DEFINITIONS
        # /////////////////////////////////////////////////

        self.msg = QMessageBox()
        self.APP_STATE = False
        self.FILE_DATA = {"Path": None}

        # /////////////////////////////////////////////////

    # ==> RUN FILE                      -> CONNECTED TO 'self.ui.runFileBtn'
    # /////////////////////////////////////////////////

    def runFile(self) -> None:
        pathh = self.FILE_DATA["Path"]
        if pathh is not None and pathh.endswith(".py"):
            with open(f"temp/{path.basename(pathh)[:-3]}_run.py", 'w') as f:
                with open(pathh) as file2:
                    f.write(file2.read())
                    f.write("\n\n\ninput('Press ENTER to Exit')")
                system(f'start python "temp/{path.basename(pathh)[:-3]}_run.py"')
        else:
            self.msg.setWindowTitle("Warning")
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Either The File Type is not Python or the file isn't saved.")
            self.msg.exec_()

    # /////////////////////////////////////////////////

    # ==> OPEN FILE                     -> CONNECTED TO 'self.ui.openFileBtn'
    # /////////////////////////////////////////////////

    def openFile(self) -> None:
        saveLocation = QFileDialog.getOpenFileName(
            self,
            "Location of the File to be Opened",
            "/",
            filter = "Python File (*.py) ;; All Files (*.*)"
        )
        with open(saveLocation[0], 'r') as f:
            self.ui.textEdit.setText(f.read())
            self.FILE_DATA["Path"] = str(saveLocation[0])

    # /////////////////////////////////////////////////

    # ==> SAVE AS                       -> CONNECTED TO 'self.ui.saveAsBtn'
    # /////////////////////////////////////////////////

    def saveAs(self) -> None:
        saveLocation = QFileDialog.getSaveFileName(
            self,
            "Location to Save the File",
            "/",
            filter = "Python File (*.py) ;; All Files (*.*)"
        )
        try:
            with open(saveLocation[0], 'w') as f:
                f.write(self.ui.textEdit.toPlainText())
                self.FILE_DATA["Path"] = str(saveLocation[0])

        except Exception as e:
            self.msg.setWindowTitle("Error")
            self.msg.setText(f"An Exception occured whilst trying to save that file:\n\t{e}")

            self.msg.setIcon(QMessageBox.Critical)
            self.msg.exec_()

    # /////////////////////////////////////////////////

    # ==> TO SAVE THE FILE              -> CONNECTED TO 'self.ui.saveFileBtn'
    # /////////////////////////////////////////////////

    def saveFile(self) -> None:
        if self.FILE_DATA["Path"] is None:
            saveLocation = QFileDialog.getSaveFileName(
                self,
                "Location to Save the File",
                "/",
                filter = "Python File (*.py) ;; All Files (*.*)"
            )
            try:
                with open(saveLocation[0], 'w') as f:
                    f.write(self.ui.textEdit.toPlainText())
                    self.FILE_DATA["Path"] = str(saveLocation[0])

            except Exception as e:
                self.msg.setWindowTitle("Error")
                self.msg.setText(f"An Exception occured whilst trying to save that file:\n\t{e}")

                self.msg.setIcon(QMessageBox.Critical)
                self.msg.exec_()

        else:
            try:
                with open(self.FILE_DATA["Path"], 'w') as f:
                    f.write(self.ui.textEdit.toPlainText())

            except Exception as e:
                self.msg.setWindowTitle("Error")
                self.msg.setText(f"An Exception occured whilst trying to save that file:\n\t{e}")

                self.msg.setIcon(QMessageBox.Critical)
                self.msg.exec_()

    # /////////////////////////////////////////////////

    # ==> TO MAXIMIZE/NORMALIZE WINDOW  -> CONNECTED TO 'self.ui.maxBtn'
    # /////////////////////////////////////////////////

    def maxMin(self) -> None:
        if not self.APP_STATE:
            self.showMaximized()
            self.APP_STATE = True
            self.ui.maxBtn.setIcon(
                QIcon(u":/Icons/img/icons/cil-window-restore.png")
            )
            self.ui.maxBtn.setToolTip("Restore")
        else:
            self.showNormal()
            self.APP_STATE = False
            self.ui.maxBtn.setIcon(
                QIcon(u":/Icons/img/icons/cil-window-maximize.png")
            )
            self.ui.maxBtn.setToolTip("Maximize")

    # /////////////////////////////////////////////////

    # ==> MOVE WINDOW WHEN TITLE BAR PRESSED
    # /////////////////////////////////////////////////

    def moveWindow(self, event) -> None:
        if event.buttons() == Qt.LeftButton and not self.APP_STATE:
            self.move(self.pos()+event.globalPos()-self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event): self.dragPos = event.globalPos()

    # /////////////////////////////////////////////////


if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec_()
