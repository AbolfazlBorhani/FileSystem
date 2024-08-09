from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from getpass import getuser
from shutil import move
from PyQt5 import QtGui
from sys import argv
from os import listdir, getcwd, rename, remove, path, mkdir

class FileSystem(QMainWindow):
    allFile = []
    txt = []
    png = []
    jpg = []
    mp4 = []
    mkv = []
    mp3 = []
    etc = []

    path = ''
	
    def __init__(self):
        super(FileSystem, self).__init__()
        loadUi('UI\\Main.ui', self)
        
        app.processEvents()
        self.setWindowIcon(QtGui.QIcon(getcwd() + '\\Img\\WHI3PER.ico'))
        self.PATH.insert('C:\\Users\\' + getuser() + '\\Desktop')
        
        # ========================================================== #
        
        self.LIGHT.triggered.connect(self.lightMode)
        self.DARK.triggered.connect(self.darkMode)
        self.GRAY.triggered.connect(self.grayMode)
        self.PURPLE.triggered.connect(self.purpleMode)
        self.BLUE.triggered.connect(self.blueMode)
        self.ABOUT.triggered.connect(self.aboutMe)
        
        # ========================================================== #
        
        self.SHOW.clicked.connect(self.showDirectory)
        self.CATEGORIES.clicked.connect(self.categories)
        self.RENAME.clicked.connect(self.rename)
        self.DELETE.clicked.connect(self.delete)
        self.EXIT.clicked.connect(self.exitProgram)
        
    # ============================================================================================== #
    
    def lightMode(self):
        app.processEvents()
        self.setStyleSheet('QWidget { font: 10pt "Comic Sans MS"; }')
    
    # ============================================================================================== #
    
    def darkMode(self):
        app.processEvents()
        self.setStyleSheet('''
            QWidget {
                font: 10pt "Comic Sans MS";
                background-color: rgb(0, 0, 0);
                color: rgb(0, 255, 255);
            }
            QComboBox {
                background-color: rgb(46, 46, 46);
                color: rgb(0, 255, 255);
            }
            QPushButton {
                background-color: rgb(46, 46, 46);
                color: rgb(0, 255, 255);
            }
            QLabel { color: rgb(0, 255, 255); }
            QTextBrowser { color: rgb(0, 255, 255); }
                           ''')
        
    # ============================================================================================== #

    def grayMode(self):
        app.processEvents()
        self.setStyleSheet('''
            QWidget { 
                font: 10pt "Comic Sans MS"; 
                background-color: rgb(35, 35, 35);
                color: rgb(255, 255, 0);
            }

            QPushButton { background-color: rgb(55, 55, 55); }
            QComboBox {  background-color: rgb(55, 55, 55); color: rgb(85, 255, 127); }
            QTextBrowser { color: rgb(255, 255, 0); }
            QLabel { color: rgb(85, 255, 127); }
            QMenuBar { color: rgb(85, 255, 127); }
            ''')
    
    # ============================================================================================== #
    
    def purpleMode(self):
        app.processEvents()
        self.setStyleSheet('''
            QWidget {
                font: 10pt "Comic Sans MS";
                background-color: rgb(29, 26, 48);
                color: #FFFFFF;
            }
            QComboBox {
                background-color: rgb(240, 195, 142);
                color: rgb(29, 26, 48);
            }
            QPushButton {
                background-color: rgb(241, 170, 155);
                color: rgb(29, 26, 48);
            }
            QLineEdit {
                background-color: rgb(240, 195, 142);
	        color: rgb(29, 26, 48);
            }
            QLabel { color: rgb(241, 170, 155); }
            QTextBrowser { color: rgb(240, 195, 142); }
            ''')
    
    # ============================================================================================== #
    
    def blueMode(self):
        app.processEvents()
        self.setStyleSheet('''
            QWidget {
                font: 10pt "Comic Sans MS";
                background-color: rgb(29, 84, 132);
                color: #FFFFFF;
            }
            QComboBox {
                background-color: rgb(240, 195, 142);
                color: rgb(29, 26, 48);
            }
            QPushButton {
                background-color: rgb(159, 232, 250);
	            color: rgb(29, 26, 48);
            }
            QLineEdit {
                background-color: rgb(240, 195, 142);
                color: rgb(29, 26, 48);
            }
            QLabel { color: rgb(170, 255, 255); }
            QTextBrowser { color: rgb(240, 195, 142); }
            ''')
        
    # ============================================================================================== #

    def aboutMe(self):
        app.processEvents()
        loadUi('UI\\About Me.ui', self)
        self.LOGO_LABEL.setPixmap(QPixmap(getcwd() + '\\Img\\WHI3PER.png'))
        self.EMAIL.setPixmap(QPixmap(getcwd() + '\\Img\\Gmail.png'))
        self.GITHUB.setPixmap(QPixmap(getcwd() + '\\Img\\Github.png'))
        self.LINKDIN.setPixmap(QPixmap(getcwd() + '\\Img\\Linkdin.png'))
        self.TELEGRAM.setPixmap(QPixmap(getcwd() + '\\Img\\Telegram.png'))
        
    # ============================================================================================== #
    
    def clearVariables(self):
        app.processEvents()
        self.allFile.clear()
        self.txt.clear()
        self.png.clear()
        self.jpg.clear()
        self.mp4.clear()
        self.mkv.clear()
        self.mp3.clear()
        self.etc.clear()
    
        path = ''
        
    # ============================================================================================== #
        
    def saveFileNames(self):
        app.processEvents()
        self.clearVariables()
        self.path = self.PATH.text()
        
        if self.path[-2:] != '\\':
            self.path = self.path + '\\'

        listDirectory = listdir(self.path)

        for item in listDirectory:
            app.processEvents()
            if item[-4:] == '.cpp' or item[-4:] == '.txt' or item[-3:] == '.py':
                self.txt.append(item)
            elif item[-4:] == '.png' or item[-4:] == '.PNG':
                self.png.append(item)
            elif item[-4:] == '.jpg' or item[-4:] == '.JPG':
                self.jpg.append(item)
            elif item[-4:] == '.mp4' or item[-4:] == '.MP4':
                self.mp4.append(item)
            elif item[-4:] == '.mkv' or item[-4:] == '.MKV':
                self.mkv.append(item)
            elif item[-4:] == '.mp3' or item[-4:] == '.MP3':
                self.mp3.append(item)
            else:
                self.etc.append(item)

        self.allFile.append(self.txt)
        self.allFile.append(self.png)
        self.allFile.append(self.jpg)
        self.allFile.append(self.mp4)
        self.allFile.append(self.mkv)
        self.allFile.append(self.mp3)
        self.allFile.append(self.etc)
        
    # ============================================================================================== #

    def showDirectory(self):
        app.processEvents()
        self.LOGS.clear()
        self.LOGS.append('Show Directory:\n')
        
        self.saveFileNames()
        
        for type in [self.txt, self.png, self.jpg, self.mp4, self.mkv, self.mp3]:
            app.processEvents()
            if len(type) != 0:
                for file in type:
                    self.LOGS.append('> ' + file)
                self.LOGS.append('\n')
    
    # ============================================================================================== #

    def categories(self):
        app.processEvents()
        self.LOGS.clear()
        self.LOGS.append('Categories:\n')
        
        if self.txt: self.gotoCategories(self.txt, 'TXT')
        if self.png: self.gotoCategories(self.png, 'PNG')
        if self.jpg: self.gotoCategories(self.jpg, 'JPG')
        if self.mp4: self.gotoCategories(self.mp4, 'MP4')
        if self.mkv: self.gotoCategories(self.mkv, 'MKV')
        if self.mp3: self.gotoCategories(self.mp3, 'MP3')
        if self.etc: self.gotoCategories(self.etc, 'ETC')
    
    # ============================================================================================== #

    def gotoCategories(self, File, Format):
        self.LOGS.append('~ ' + Format)
        new_path = (self.path + '\\' + Format + '\\')
        
        if not path.exists(new_path):
            mkdir(new_path)
            
        for item in File:
            move((self.path + item), (new_path + item))

    # ============================================================================================== #
    
    def warning(self, Format: str):
        self.LOGS.append(f'Warning: There is no \'{Format}\' file or your request is invalid.')
        
    # ============================================================================================== #
        
    def rename(self):
        self.saveFileNames()
        app.processEvents()
        self.LOGS.clear()
        self.LOGS.append('Rename:\n')

        match(self.RENAME_COMBOBOX.currentText()):
            case 'TXT': self.gotoRename(self.txt, 'TXT')
            case 'PNG': self.gotoRename(self.png, 'PNG')
            case 'JPG': self.gotoRename(self.jpg, 'JPG')
            case 'MP4': self.gotoRename(self.mp4, 'MP4')
            case 'MKV': self.gotoRename(self.mkv, 'MKV')
            case 'MP3': self.gotoRename(self.mp3, 'MP3')
        
    # ============================================================================================== #

    def gotoRename(self, File, Format):
        self.LOGS.append('~ ' + Format)
        number = 1

        if File:
            for item in File:
                self.LOGS.append(item)
                rename((self.path + item), (self.path + str(number) + item[-4:]))
                number += 1
        else:
            self.warning(Format)
        
    # ============================================================================================== #
        
    def delete(self):
        self.saveFileNames()
        app.processEvents()
        self.LOGS.clear()
        self.LOGS.append('Delete:\n')
            
        match(self.DELETE_COMBOBOX.currentText()):
            case 'ALL':
                self.LOGS.append('~ ALL')
                
                for type in self.allFile:
                    if len(type) != 0:
                        for file in type:
                            self.LOGS.append(file)
                            remove(self.path + file)
            
            case 'TXT': self.gotoDelete(self.txt, 'TXT')
            case 'PNG': self.gotoDelete(self.png, 'PNG')
            case 'JPG': self.gotoDelete(self.jpg, 'JPG')
            case 'MP4': self.gotoDelete(self.mp4, 'MP4')
            case 'MKV': self.gotoDelete(self.mkv, 'MKV')
            case 'MP3': self.gotoDelete(self.Mp3, 'MP3')
            case 'ETC': self.gotoDelete(self.etc, 'ETC')
        
    # ============================================================================================== #

    def gotoDelete(self, File, Format):
        self.LOGS.append('~ ' + Format)
        if File:
            for item in File:
                self.LOGS.append(item)
                remove(self.path + item)
        else:
            self.warning(Format)

    # ============================================================================================== #

    def exitProgram(self):
        app.processEvents()
        exit()

    # =============================================================================================== #