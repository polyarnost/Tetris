from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction, QInputDialog
from PyQt5.QtGui import QResizeEvent

from Board import Board


class Tetris(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)

        self.tboard.start()

        self.resize(380, 580)
        self.center()
        self.setWindowTitle('Tetris')

        restart_action = QAction("Restart", self)
        restart_action.triggered.connect(self.tboard.restartGame)

        change_rows_columns_action = QAction("Change Rows/Columns", self)
        change_rows_columns_action.triggered.connect(self.changeRowsColumns)

        change_window_size_action = QAction("Change Window Size", self)
        change_window_size_action.triggered.connect(self.changeWindowSize)


        toolbar = self.addToolBar("Options")
        toolbar.addAction(change_rows_columns_action)
        toolbar.addAction(change_window_size_action)
        toolbar.addAction(restart_action)

        self.show()


    def center(self):

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())//2,
            (screen.height()-size.height())//2)

    def changeRowsColumns(self):
        rows, ok1 = QInputDialog.getInt(self, "Rows/Columns", "Enter the number of rows:",
                                        value=Board.BoardHeight, min=10, max=30)
        cols, ok2 = QInputDialog.getInt(self, "Rows/Columns", "Enter the number of columns:",
                                        value=Board.BoardWidth, min=10, max=30)
        if ok1 and ok2:
            Board.BoardHeight = rows
            Board.BoardWidth = cols
            self.tboard.clearBoard()
            self.resizeEvent(QResizeEvent(self.size(), self.size()))

    def changeWindowSize(self):
        width, ok1 = QInputDialog.getInt(self, "Window Size", "Enter the width of the window:",
                                         value=self.width(), min=200, max=1000)
        height, ok2 = QInputDialog.getInt(self, "Window Size", "Enter the height of the window:",
                                          value=self.height(), min=200, max=1000)
        if ok1 and ok2:
            self.resize(width, height)