import os
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        #add a title
        self.setWindowTitle("First Window")

        #set vertical window
        self.setLayout(qtw.QVBoxLayout())

        #create label
        my_label = qtw.QLabel("Lets get started, whats your IP address?")
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        #create entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("IP_address")
        my_entry.setText("Enter IP address here")
        my_entry.setFont(qtg.QFont('Helvetica', 10))
        self.layout().addWidget(my_entry)

        #create button
        my_button = qtw.QPushButton("Press Me",
            clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        def press_it():
            #add name to label
            my_label.setText(f"hello {my_entry.text()}")
            #clear the entry box
            my_entry.setText("")
            #var2 = str(input('What would you like to search for. Spaces must be +: '))
            #os.system('chromium https://duckduckgo.com/?q='+var2+' ')


        #show the app
        self.show()

app = qtw.QApplication([])
mw = MainWindow()


#run app
app.exec_()
