from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtNetwork import QLocalServer, QLocalSocket
from sys import argv, exit
from lib.mainwindow4 import MainWindow


if __name__ == '__main__':
    app = QApplication(argv)
    win = MainWindow()
    serverName = 'ldy'
    socket = QLocalSocket()
    socket.connectToServer(serverName)
    # 如果连接成功，表明server已经存在，当前已有实例在运行
    if socket.waitForConnected(500):
        QMessageBox.warning(win, '警告', '该程序已经启动')
        app.quit()
    else:
        localServer = QLocalServer()  # 没有实例运行，创建服务器
        localServer.listen(serverName)
        win.show()
        exit(app.exec())
