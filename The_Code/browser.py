# IMPORTS
import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# WEB ENGINE( pip install PyQtWebEngine)
from PyQt5.QtWebEngineWidgets import *

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # ADD WINDOW ELEMENTS
        # ADD TAB WIGDETS TO DISPLAY WEB TABS
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.setCentralWidget(self.tabs)

        # ADD DOUBLE CLICK EVENT LISTENER
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        # ADD TAB CLOSE EVENT LISTENER
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        # ADD ACTIVE TAB CHANGE EVENT LISTENER
        self.tabs.currentChanged.connect(self.current_tab_changed)


        # ADD NAVIGATION TOOLBAR
        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)

        # ADD BUTTONS TO NAVIGATION TOOLBAR
        # PREVIOUS WEB PAGE BUTTON
        back_btn = QAction(QIcon(os.path.join('icons', 'cil-arrow-circle-left.png')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        navtb.addAction(back_btn)
        # NAVIGATE TO PREVIOUS PAGE
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())




        # NEXT WEB PAGE BUTTON
        next_btn = QAction(QIcon(os.path.join('icons', 'cil-arrow-circle-right.png')), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        navtb.addAction(next_btn)
        # NAVIGATE TO NEXT WEB PAGE
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())




        # REFRESH WEB PAGE BUTTON
        reload_btn = QAction(QIcon(os.path.join('icons', 'cil-reload.png')), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        navtb.addAction(reload_btn)
        # RELOAD WEB PAGE
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())




        # HOME PAGE BUTTON
        home_btn = QAction(QIcon(os.path.join('icons', 'cil-home.png')), "Home", self)
        home_btn.setStatusTip("Go home")
        navtb.addAction(home_btn)
        # NAVIGATE TO DEFAULT HOME PAGE
        home_btn.triggered.connect(self.navigate_home)



        # ADD SEPARATOR TO NAVIGATION BUTTONS
        navtb.addSeparator()

        # ADD LABEL ICON TO SHOW THE SECURITY STATUS OF THE LOADED URL
        self.httpsicon = QLabel()  
        self.httpsicon.setPixmap(QPixmap(os.path.join('icons', 'cil-lock-unlocked.png')))
        navtb.addWidget(self.httpsicon)

        # ADD LINE EDIT TO SHOW AND EDIT URLS
        self.urlbar = QLineEdit()
        navtb.addWidget(self.urlbar)
        # LOAD URL WHEN ENTER BUTTON IS PRESSED
        self.urlbar.returnPressed.connect(self.navigate_to_url)



        # ADD STOP BUTTON TO STOP URL LOADING
        stop_btn = QAction(QIcon(os.path.join('icons', 'cil-media-stop.png')), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        navtb.addAction(stop_btn)
        # STOP URL LOADING
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())


        # ADD TOP MENU
        # File menu
        file_menu = self.menuBar().addMenu("&File")
        # ADD FILE MENU ACTIONS
        new_tab_action = QAction(QIcon(os.path.join('icons', 'cil-library-add.png')), "New Tab", self)
        new_tab_action.setStatusTip("Open a new tab")
        file_menu.addAction(new_tab_action)
        # ADD NEW TAB
        new_tab_action.triggered.connect(lambda _: self.add_new_tab())


        # Help menu
        help_menu = self.menuBar().addMenu("&Help")
        # ADD HELP MENU ACTIONS
        navigate_home_action = QAction(QIcon(os.path.join('icons', 'cil-exit-to-app.png')),
                                            "Homepage", self)
        navigate_home_action.setStatusTip("Go to Spinn Design Homepage")
        help_menu.addAction(navigate_home_action)
        # NAVIGATE TO DEVELOPER WEBSITE
        navigate_home_action.triggered.connect(self.navigate_home)



        # SET WINDOW TITTLE AND ICON
        self.setWindowTitle("Spinn Browser")
        self.setWindowIcon(QIcon(os.path.join('icons', 'cil-screen-desktop.png')))


        # ADD STYLESHEET TO CUSTOMIZE YOUR WINDOWS
        # STYLESHEET (DARK MODE)
        self.setStyleSheet("""QWidget{
           background-color: rgb(48, 48, 48);
           color: rgb(255, 255, 255);
        }
        QTabWidget::pane { /* The tab widget frame */
            border-top: 2px solid rgb(90, 90, 90);
            position: absolute;
            top: -0.5em;
            color: rgb(255, 255, 255);
            padding: 5px;
        }

        QTabWidget::tab-bar {
            alignment: left;
        }

        /* Style the tab using the tab sub-control. Note that
            it reads QTabBar _not_ QTabWidget */
        QLabel, QToolButton, QTabBar::tab {
            background: rgb(90, 90, 90);
            border: 2px solid rgb(90, 90, 90);
            /*border-bottom-color: #C2C7CB; /* same as the pane color */
            border-radius: 10px;
            min-width: 8ex;
            padding: 5px;
            margin-right: 2px;
            color: rgb(255, 255, 255);
        }

        QLabel:hover, QToolButton::hover, QTabBar::tab:selected, QTabBar::tab:hover {
            background: rgb(49, 49, 49);
            border: 2px solid rgb(0, 36, 36);
            background-color: rgb(0, 36, 36);
        }

        QLineEdit {
            border: 2px solid rgb(0, 36, 36);
            border-radius: 10px;
            padding: 5px;
            background-color: rgb(0, 36, 36);
            color: rgb(255, 255, 255);
        }
        QLineEdit:hover {
            border: 2px solid rgb(0, 66, 124);
        }
        QLineEdit:focus{
            border: 2px solid rgb(0, 136, 255);
            color: rgb(200, 200, 200);
        }
        QPushButton{
            background: rgb(49, 49, 49);
            border: 2px solid rgb(0, 36, 36);
            background-color: rgb(0, 36, 36);
            padding: 5px;
            border-radius: 10px;
        }""")



        # LOAD DEFAULT HOME PAGE (GOOLE.COM)
        #url = http://www.duckduckgo.com,
        #label = Homepage
        self.add_new_tab(QUrl('http://www.duckduckgo.com'), 'Homepage')

        # SHOW MAIN WINDOW
        self.show()

    # ############################################
    # FUNCTIONS
    ##############################################
    # ADD NEW WEB TAB
    def add_new_tab(self, qurl=None, label="Blank"):
        # Check if url value is blank
        if qurl is None:
            qurl = QUrl('https://duckduckgo.com')#pass empty string to url

        # Load the passed url
        browser = QWebEngineView()
        browser.setUrl(qurl)

        # ADD THE WEB PAGE TAB
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        # ADD BROWSER EVENT LISTENERS
        # On URL change
        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))
        # On loadfinished
        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))


    # ADD NEW TAB ON DOUBLE CLICK ON TABS
    def tab_open_doubleclick(self, i):
        if i == -1:  # No tab under the click
            self.add_new_tab()

    # CLOSE TABS 
    def close_current_tab(self, i):
        if self.tabs.count() < 2: #Only close if there is more than one tab open
            return

        self.tabs.removeTab(i)


    # UPDATE URL TEXT WHEN ACTIVE TAB IS CHANGED
    def update_urlbar(self, q, browser=None):
        #q = QURL
        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return
        # URL Schema
        if q.scheme() == 'https':
            # If schema is https change icon to locked padlock to show that the webpage is secure
            self.httpsicon.setPixmap(QPixmap(os.path.join('icons', 'cil-lock-locked.png')))

        else:
            # If schema is not https change icon to locked padlock to show that the webpage is unsecure
            self.httpsicon.setPixmap(QPixmap(os.path.join('icons', 'cil-lock-unlocked.png')))

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)



    # ACTIVE TAB CHANGE ACTIONS
    def current_tab_changed(self, i):
        # i = tab index
        # GET CURRENT TAB URL
        qurl = self.tabs.currentWidget().url()
        # UPDATE URL TEXT
        self.update_urlbar(qurl, self.tabs.currentWidget())
        # UPDATE WINDOWS TITTLE
        self.update_title(self.tabs.currentWidget())


    # UPDATE WINDOWS TITTLE
    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            # If this signal is not from the current ACTIVE tab, ignore
            return

        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle(title)


    # NAVIGATE TO PASSED URL
    def navigate_to_url(self):  # Does not receive the Url
        # GET URL TEXT
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            # pass http as default url schema
            q.setScheme("http")

        self.tabs.currentWidget().setUrl(q)


    # NAVIGATE TO DEFAULT HOME PAGE
    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl("https://duckduckgo.com"))








app = QApplication(sys.argv)
# APPLICATION NAME
app.setApplicationName("Tytans Browser")
# APPLICATION COMPANY NAME
app.setOrganizationName("Tytans Browser")
# APPLICATION COMPANY ORGANISATION
app.setOrganizationDomain("semanticpaint.com")


window = MainWindow()
app.exec_()