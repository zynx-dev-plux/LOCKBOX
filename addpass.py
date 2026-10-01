from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidget,QTableWidgetItem
from pickle import load,dump
def save():
    error = QMessageBox()
    usern=w.usern.text()
    passwd=w.passwd.text()
    webn=w.webn.text()
    if usern=="" or passwd=="" or webn=="":
        error.setWindowTitle("error")
        error.setText("please make sure that you filled all the inputs")
        error.setIcon(QMessageBox.Icon.Critical)
        error.setStyleSheet("""
        QMessageBox {
        background-color: white;
        }

        QMessageBox QLabel {
        color: black;
        font-size: 16px;
        }
        QMessageBox QPushButton {
        background-color: green;
        color: white;
        border: 0px;
        padding: 8px 20px;
        border-radius: 5px;
        }
        }""")
        error.exec()
    else:
        f=open("data.dat","ab")
        e=dict()
        e["username"]=w.usern.text()
        e["password"]=w.passwd.text()
        e["website"]=w.webn.text()
        dump(e,f)
        msg = QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText("Your data was saved successfully!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStyleSheet("""
          QMessageBox {
           background-color: white;
          }
          QMessageBox QLabel {
           color: black;
           font-size: 16px;}
         QMessageBox QPushButton {
           background-color: green;
           color: white;
           border: 0px;
           padding: 8px 20px;
           border-radius: 5px;}}""")
        msg.exec()
        f.close()

app = QApplication([])
w = loadUi ("addPass.ui")
w.show()
w.save.clicked.connect (save)
app.exec_()