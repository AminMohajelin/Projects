from PyQt5 import QtCore, QtGui, QtWidgets, uic , QtPrintSupport
from PyQt5.QtWidgets import  QDialog, QApplication,QMessageBox,QTableWidget,QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import sqlite3
from datetime import datetime

class newReturn(QtWidgets.QDialog):
    def __init__(self):
        super(newReturn,self).__init__()
        uic.loadUi('newReturn.ui',self)
        self.returnBtn.clicked.connect(self.returnB)
        self.cancelBtn.clicked.connect(self.close)

    def returnB(self):
        
        try:
            bookId = int(self.bookIdTxt.text())
            userCode = int(self.userCodeTxt.text())
            returnDate = self.returnDateTxt.text()
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            cur.execute(f"update tableLending set status = 1 , returnDate = '{returnDate}' where bookId = {bookId} and userCode = {userCode}")
            sqliteConnection.commit()
            msg = QMessageBox(self)
            msg.setText(f'Book returned successfully')
            msg.setWindowTitle('Return')
            msg.exec()
            self.bookIdTxt.setText('')
            self.userCodeTxt.setText('')
            self.returnDateTxt.setText('')

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class returnBook(QtWidgets.QDialog):
    def __init__(self):
        super(returnBook,self).__init__()
        uic.loadUi('returnBook.ui',self)
        self.titleTxt.textChanged.connect(self.filterTitle)
        self.newReturnBtn.clicked.connect(self.showNewReturn)
        self.tableReturn.setColumnWidth(0,200)
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute("select title, isbn, publisher, tableBooks.bookId, tableLending.userCode,firstName, lastName, lendDate, dueDate, returnDate from tableLending join tableBooks on tableLending.bookId = tableBooks.bookId join tableUser on tableLending.userCode = tableUser.userCode join tablePerson on tableUser.nationalCode = tablePerson.nationalCode where status = 1")
            
            for rowNumber, rowData in enumerate(result):
                self.tableReturn.insertRow(rowNumber)
                for columnNumber, columnData in enumerate(rowData):
                    item = str(columnData)
                    self.tableReturn.setItem(rowNumber,columnNumber,QtWidgets.QTableWidgetItem(item))
            cur.close()
            sqliteConnection.close()
            
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

    def showNewReturn(self):
        self.snr = newReturn()
        self.snr.setModal(True)
        self.snr.show()

    def filterTitle(self):
        self.tableReturn.model().removeRows(0,self.tableReturn.rowCount())
        t = self.titleTxt.text().lower()
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute(f"select title, isbn, publisher, tableBooks.bookId, tableLending.userCode,firstName, lastName, lendDate, dueDate,returnDate from tableLending join tableBooks on tableLending.bookId = tableBooks.bookId join tableUser on tableLending.userCode = tableUser.userCode join tablePerson on tableUser.nationalCode = tablePerson.nationalCode where status = 1")
            self.tableReturn.setEditTriggers(QTableWidget.NoEditTriggers)
            i = 0
            for fields in result:
                if fields[0].lower().startswith(t):
                    self.tableReturn.insertRow(i)
                    self.tableReturn.setItem(i,0,QTableWidgetItem(fields[0]))
                    self.tableReturn.setItem(i,1,QTableWidgetItem(str(fields[1])))
                    self.tableReturn.setItem(i,2,QTableWidgetItem(fields[2]))
                    self.tableReturn.setItem(i,3,QTableWidgetItem(str(fields[3])))
                    self.tableReturn.setItem(i,4,QTableWidgetItem(str(fields[4])))
                    self.tableReturn.setItem(i,5,QTableWidgetItem(fields[5]))
                    self.tableReturn.setItem(i,6,QTableWidgetItem(fields[6]))
                    self.tableReturn.setItem(i,7,QTableWidgetItem(fields[7]))
                    self.tableReturn.setItem(i,8,QTableWidgetItem(fields[8]))
                    self.tableReturn.setItem(i,9,QTableWidgetItem(fields[9]))
                    i = i + 1
            cur.close()
            sqliteConnection.close()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class newLend(QtWidgets.QDialog):
    def __init__(self):
        super(newLend,self).__init__()
        uic.loadUi('newLend.ui',self)
        self.lendBtn.clicked.connect(self.lend)
        self.cancelBtn.clicked.connect(self.close)

    def lend(self):
        
        try:
            bookId = int(self.bookIdTxt.text())
            userCode = int(self.userCodeTxt.text())
            dueDate = self.dueDateTxt.text()
            lendDate = datetime.today().strftime('%d/%m/%Y')
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            avl = cur.execute(f"SELECT (tableBooks.copyCount - count( * ) ) as a FROM tableLending join tableBooks on tableLending.bookId = tableBooks.bookId WHERE status = 0 and tableLending.bookId = {bookId}")
            for i in avl:
                a = i[0]

            if a == 0:
                msg = QMessageBox(self)
                msg.setText(f'this book is not available right now')
                msg.setWindowTitle('Error')
                msg.exec()
                return

            else:
                cur.execute(f"insert into tableLending (bookId, userCode, status, lendDate, dueDate) values ({bookId}, {userCode}, {0}, '{lendDate}', '{dueDate}')")
                sqliteConnection.commit()
                msg = QMessageBox(self)
                msg.setText(f'Book lended to the user successfully')
                msg.setWindowTitle('Lending')
                msg.exec()

            cur.close()
            sqliteConnection.close()
            self.bookIdTxt.setText('')
            self.userCodeTxt.setText('')
            self.dueDateTxt.setText('')
        
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class lending(QtWidgets.QDialog):
    def __init__(self):
        super(lending,self).__init__()
        uic.loadUi('lending.ui', self)
        self.titleTxt.textChanged.connect(self.filterTitle)
        self.newLendBtn.clicked.connect(self.showNewLend)
        self.tableLending.setColumnWidth(0,300)
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute("select title, isbn, publisher, tableBooks.bookId, tableLending.userCode,firstName, lastName, lendDate, dueDate from tableLending join tableBooks on tableLending.bookId = tableBooks.bookId join tableUser on tableLending.userCode = tableUser.userCode join tablePerson on tableUser.nationalCode = tablePerson.nationalCode where status = 0")
            
            for rowNumber, rowData in enumerate(result):
                self.tableLending.insertRow(rowNumber)
                for columnNumber, columnData in enumerate(rowData):
                    item = str(columnData)
                    self.tableLending.setItem(rowNumber,columnNumber,QtWidgets.QTableWidgetItem(item))
            cur.close()
            sqliteConnection.close()
            
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

    def showNewLend(self):
        self.snl = newLend()
        self.snl.setModal(True)
        self.snl.show()

    def filterTitle(self):
        self.tableLending.model().removeRows(0,self.tableLending.rowCount())
        t = self.titleTxt.text().lower()
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute(f"select title, isbn, publisher, tableBooks.bookId, tableLending.userCode,firstName, lastName, lendDate, dueDate from tableLending join tableBooks on tableLending.bookId = tableBooks.bookId join tableUser on tableLending.userCode = tableUser.userCode join tablePerson on tableUser.nationalCode = tablePerson.nationalCode where status = 0")
            self.tableLending.setEditTriggers(QTableWidget.NoEditTriggers)
            i = 0
            for fields in result:
                if fields[0].lower().startswith(t):
                    self.tableLending.insertRow(i)
                    self.tableLending.setItem(i,0,QTableWidgetItem(fields[0]))
                    self.tableLending.setItem(i,1,QTableWidgetItem(str(fields[1])))
                    self.tableLending.setItem(i,2,QTableWidgetItem(fields[2]))
                    self.tableLending.setItem(i,3,QTableWidgetItem(str(fields[3])))
                    self.tableLending.setItem(i,4,QTableWidgetItem(str(fields[4])))
                    self.tableLending.setItem(i,5,QTableWidgetItem(fields[5]))
                    self.tableLending.setItem(i,6,QTableWidgetItem(fields[6]))
                    self.tableLending.setItem(i,7,QTableWidgetItem(fields[7]))
                    self.tableLending.setItem(i,8,QTableWidgetItem(fields[8]))
                    i = i + 1
            cur.close()
            sqliteConnection.close()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class removeLibrarian(QtWidgets.QDialog):
    def __init__(self):
        super(removeLibrarian,self).__init__()
        uic.loadUi('removeLibrarian.ui',self)
        self.deleteBtn.clicked.connect(self.delete)

    def delete(self):
        
        try:
            nC = int(self.nationalCodeTxt.text())
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            lC = cur.execute(f"select librarianCode from tableLibrarian where nationalCode = {nC}")
            for i in lC:
                lc = i[0]
            cur.execute(f"delete from tableLibrarianLogIn where librarianCode = {lc}")
            sqliteConnection.commit()
            cur.execute(f"delete from tableLibrarian where nationalCode = {nC}")
            sqliteConnection.commit()
            cur.execute(f"delete from tablePerson where nationalCode = {nC}")
            sqliteConnection.commit()
            msg = QMessageBox(self)
            msg.setText(f'librarian Deleted successfully.')
            msg.setWindowTitle('Delete')
            msg.exec()
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class editLibrarianForm(QtWidgets.QDialog):
    def __init__(self):
        super(editLibrarianForm,self).__init__()
        uic.loadUi('librarianRegistration.ui',self)
        self.photoBtn.clicked.connect(self.profilePhoto)
        self.cancelBtn.clicked.connect(self.close)
    
    def profilePhoto(self):
        photoFile, _ = QFileDialog.getOpenFileName(self, 'Open file','' ,"Image files (*.jpg)")
        global ti
        ti = open(photoFile ,'rb')  
        global pc
        pc = 1      
        image = QImage(photoFile)
        self.imagePreviewLabel.setPixmap(QPixmap.fromImage(image))
        self.imagePreviewLabel.setScaledContents(True)
        self.registerBtn.setEnabled(True)

class findLibrarianForm(QtWidgets.QDialog):
    def __init__(self):
        super(findLibrarianForm,self).__init__()
        uic.loadUi('findLibrarianForm.ui',self)
        self.findBtn.clicked.connect(self.showLibrarianForm)

    def showLibrarianForm(self):
        
        try:
            self.nC = int(self.nationalCodeTxt.text())
            self.srlf = editLibrarianForm()
            self.srlf.setModal(True)
            self.srlf.show()
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute(f"select photo, firstName, lastName, tablePerson.nationalCode, birthDate, phone, city, street, alley, postalCode, librarianCode from tablePerson join tableLibrarian on tablePerson.nationalCode = tableLibrarian.nationalCode where tablePerson.nationalCode = {self.nC}")
            for i in result:
                self.srlf.firstNameTxt.setText(str(i[1]))
                self.srlf.lastNameTxt.setText(str(i[2]))
                self.srlf.nationalCodeTxt.setText(str(i[3]))
                self.srlf.birthDateTxt.setText(str(i[4]))
                self.srlf.phoneTxt.setText(str(i[5]))
                self.srlf.cityTxt.setText(str(i[6]))
                self.srlf.streetTxt.setText(str(i[7]))
                self.srlf.alleyTxt.setText(str(i[8]))
                self.srlf.postalCodeTxt.setText(str(i[9]))
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(i[0],'jpg')
                self.srlf.imagePreviewLabel.setPixmap(pixmap)
                self.srlf.imagePreviewLabel.setScaledContents(True)
                global pc
                pc = 0
                self.srlf.photoBtn.clicked.connect(self.srlf.profilePhoto)
                self.srlf.registerBtn.clicked.connect(self.editLibrarian)
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

    def editLibrarian(self):
        
        try:
            firstName = self.srlf.firstNameTxt.text()
            lastName = self.srlf.lastNameTxt.text()
            nationalCode = int(self.srlf.nationalCodeTxt.text())
            birthDate = self.srlf.birthDateTxt.text()
            phone = int(self.srlf.phoneTxt.text())
            city = self.srlf.cityTxt.text()
            street = self.srlf.streetTxt.text()
            alley = self.srlf.alleyTxt.text()
            postalCode = int(self.srlf.postalCodeTxt.text())
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            cur.execute(f"update tablePerson set firstName = '{firstName}', lastName = '{lastName}', nationalCode = {nationalCode}, birthDate = '{birthDate}', phone = {phone}, city = '{city}', street = '{street}', alley ='{alley}', postalCode = {postalCode} where nationalCode = {self.nC} ")
            sqliteConnection.commit()
            if pc == 1:
                cur.execute(f'update tablePerson set photo = null where nationalCode = {self.nC}')
                sqliteConnection.commit()
                cur.execute(f"insert into tablePerson(id, photo) values(0,?)", [sqlite3.Binary(ti.read())])
                sqliteConnection.commit()
                cur.execute(f'update tablePerson set photo = (select photo from tablePerson where id = 0) where nationalCode = {self.nC}')
                sqliteConnection.commit()
                cur.execute(f"delete from tablePerson where id = 0 ")
                sqliteConnection.commit()

            msg = QMessageBox(self)
            msg.setText(f'librarian Edited successfully.')
            msg.setWindowTitle('Edit')
            msg.exec()
            self.srlf.firstNameTxt.setText('')
            self.srlf.lastNameTxt.setText('')
            self.srlf.nationalCodeTxt.setText('')
            self.srlf.birthDateTxt.setText('')
            self.srlf.phoneTxt.setText('')
            self.srlf.cityTxt.setText('')
            self.srlf.streetTxt.setText('')
            self.srlf.alleyTxt.setText('')
            self.srlf.postalCodeTxt.setText('')
            self.srlf.imagePreviewLabel.clear()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class librarians(QtWidgets.QDialog):
    def __init__(self):
        super(librarians,self).__init__()
        uic.loadUi('librarians.ui',self)
        self.lastNameTxt.textChanged.connect(self.filterLastName)
        self.librarianEditBtn.clicked.connect(self.showFindLibrarianForm)
        self.librarianDeleteBtn.clicked.connect(self.showRemoveLibrarian)
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute("select photo, firstName, lastName, librarianCode, tablePerson.nationalCode, birthDate, phone, city, street, alley, postalCode from tablePerson join tableLibrarian on tablePerson.nationalCode = tableLibrarian.nationalCode")
            
            for rowNumber, rowData in enumerate(result):
                self.tableLibrarians.insertRow(rowNumber)
                for columnNumber, columnData in enumerate(rowData):
                    item = str(columnData)
                    if(columnNumber == 0):
                        item = self.getImageLabel(columnData)
                        self.tableLibrarians.setCellWidget(rowNumber,columnNumber,item)
                    else:
                        self.tableLibrarians.setItem(rowNumber,columnNumber,QtWidgets.QTableWidgetItem(item))
            self.tableLibrarians.verticalHeader().setDefaultSectionSize(135)
            cur.close()
            sqliteConnection.close()
            
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)
        
    def showRemoveLibrarian(self):
        self.srl = removeLibrarian()
        self.srl.setModal(True)
        self.srl.show()

    def showFindLibrarianForm(self):
        self.sflf = findLibrarianForm()
        self.sflf.setModal(True)
        self.sflf.show()

    def filterLastName(self):
        self.tableLibrarians.model().removeRows(0,self.tableLibrarians.rowCount())
        ln = self.lastNameTxt.text().lower()
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute("select photo, firstName, lastName, librarianCode, tablePerson.nationalCode, birthDate, phone, city, street, alley, postalCode from tablePerson join tableLibrarian on tablePerson.nationalCode = tableLibrarian.nationalCode")
            self.tableLibrarians.setEditTriggers(QTableWidget.NoEditTriggers)
            i = 0
            for fields in result:
                if fields[2].lower().startswith(ln):
                    self.tableLibrarians.insertRow(i)
                    self.tableLibrarians.setCellWidget(i,0,self.getImageLabel(fields[0]))
                    self.tableLibrarians.setItem(i,1,QTableWidgetItem(fields[1]))
                    self.tableLibrarians.setItem(i,2,QTableWidgetItem(fields[2]))
                    self.tableLibrarians.setItem(i,3,QTableWidgetItem(str(fields[3])))
                    self.tableLibrarians.setItem(i,4,QTableWidgetItem(str(fields[4])))
                    self.tableLibrarians.setItem(i,5,QTableWidgetItem(fields[5]))
                    self.tableLibrarians.setItem(i,6,QTableWidgetItem(str(fields[6])))
                    self.tableLibrarians.setItem(i,7,QTableWidgetItem(fields[7]))
                    self.tableLibrarians.setItem(i,8,QTableWidgetItem(fields[8]))
                    self.tableLibrarians.setItem(i,9,QTableWidgetItem(fields[9]))
                    self.tableLibrarians.setItem(i,10,QTableWidgetItem(str(fields[10])))
                    i = i + 1

            self.tableLibrarians.verticalHeader().setDefaultSectionSize(135)
            cur.close()
            sqliteConnection.close()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

    def getImageLabel(self,image):
        imageLabel = QtWidgets.QLabel()
        imageLabel.setText("")
        imageLabel.setScaledContents(True)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image,'jpg')
        imageLabel.setPixmap(pixmap)
        return imageLabel

class regBookForm(QtWidgets.QDialog):
    def __init__(self):
        super(regBookForm,self).__init__()
        uic.loadUi('bookRegistration.ui',self)
        self.registerBtn.clicked.connect(self.registration)
        self.cancelBtn.clicked.connect(self.terminate)
    
    def registration(self):
        
        try:
            title = self.titleTxt.text()
            isbn = self.isbnTxt.text()
            publisher = self.publisherTxt.text()
            bookId = int(self.bookIdTxt.text())
            price = int(self.priceTxt.text())
            publicationYear = int(self.publicationYearTxt.text())
            copyCount = int(self.copyCountTxt.text())
            edition = int(self.editionTxt.text())
            authorId = self.authorIdTxt.text()

            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            cur.execute(f"insert into tableBooks (title, ISBN, publisher, bookId, price, publicationYear, copyCount, edition) values ('{title}','{isbn}','{publisher}',{bookId},{price},{publicationYear},{copyCount},{edition})")
            sqliteConnection.commit()
            aid = authorId.split(',')
            for i in aid:
                cur.execute(f"insert  into tableAuthorBooks (authorId, bookId) values ({int(i)},{bookId})")
                sqliteConnection.commit()

            cur.close()
            sqliteConnection.close()
            msg = QMessageBox(self)
            msg.setText(f'Book added successfully.')
            msg.setWindowTitle('Registration')
            msg.exec()
            self.titleTxt.setText('')
            self.isbnTxt.setText('')
            self.publisherTxt.setText('')
            self.bookIdTxt.setText('')
            self.priceTxt.setText('')
            self.publicationYearTxt.setText('')
            self.copyCountTxt.setText('')
            self.editionTxt.setText('')
            self.authorIdTxt.setText('')

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

    def terminate(self):
        self.close()

class removeBook(QtWidgets.QDialog):
    def __init__(self):
        super(removeBook,self).__init__()
        uic.loadUi('removeBook.ui',self)
        self.deleteBtn.clicked.connect(self.delete)

    def delete(self):
        
        try:
            bi = int(self.bookIdTxt.text())
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            cur.execute(f"delete from tableBooks where BookId = {bi}")
            sqliteConnection.commit()
            msg = QMessageBox(self)
            msg.setText(f'Book Deleted successfully.')
            msg.setWindowTitle('Delete')
            msg.exec()
            self.bookIdTxt.setText('')
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class editBookForm(QtWidgets.QDialog):
    def __init__(self):
        super(editBookForm,self).__init__()
        uic.loadUi('bookRegistration.ui',self)
        self.cancelBtn.clicked.connect(self.close)
        self.label_12.setText('')
        self.label_11.setText('Author Id')

class findBookForm(QtWidgets.QDialog):
    def __init__(self):
        super(findBookForm,self).__init__()
        uic.loadUi('findBookForm.ui',self)
        self.findBtn.clicked.connect(self.showBookForm)

    def showBookForm(self):
        
        try:
            self.bi = int(self.bookIdTxt.text())
            self.sbf = editBookForm()
            self.sbf.setModal(True)
            self.sbf.show()
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute(f"select title, ISBN, publisher, tableBooks.bookId, price, publicationYear, copyCount, edition, authorId from tableBooks join tableAuthorBooks on tableBooks.bookId = tableAuthorBooks.bookId where tableBooks.bookId = {self.bi}")
            for i in result:
                self.sbf.titleTxt.setText(str(i[0]))
                self.sbf.isbnTxt.setText(str(i[1]))
                self.sbf.publisherTxt.setText(str(i[2]))
                self.sbf.bookIdTxt.setText(str(i[3]))
                self.sbf.priceTxt.setText(str(i[4]))
                self.sbf.publicationYearTxt.setText(str(i[5]))
                self.sbf.copyCountTxt.setText(str(i[6]))
                self.sbf.editionTxt.setText(str(i[7]))
                self.sbf.authorIdTxt.setText(str(i[8]))
                self.sbf.registerBtn.clicked.connect(self.editBook)

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

    def editBook(self):
        
        try:
            title = self.sbf.titleTxt.text()
            isbn = self.sbf.isbnTxt.text()
            publisher = self.sbf.publisherTxt.text()
            bookId = int(self.sbf.bookIdTxt.text())
            price = int(self.sbf.priceTxt.text())
            publicationYear = int(self.sbf.publicationYearTxt.text())
            copyCount = int(self.sbf.copyCountTxt.text())
            edition = int(self.sbf.editionTxt.text())
            authorId = int(self.sbf.authorIdTxt.text())
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            cur.execute(f"update tableBooks set title = '{title}', isbn = '{isbn}', publisher = '{publisher}', bookId = {bookId}, price = {price}, publicationYear = {publicationYear}, copyCount = {copyCount}, edition ={edition} where bookId = {self.bi} ")
            sqliteConnection.commit()
            cur.execute(f"update tableAuthorBooks set authorId = {authorId} where bookId = {bookId}")
            sqliteConnection.commit()
            msg = QMessageBox(self)
            msg.setText(f'Book Edited successfully.')
            msg.setWindowTitle('Edit')
            msg.exec()
            self.sbf.titleTxt.setText('')
            self.sbf.isbnTxt.setText('')
            self.sbf.publisherTxt.setText('')
            self.sbf.bookIdTxt.setText('')
            self.sbf.priceTxt.setText('')
            self.sbf.publicationYearTxt.setText('')
            self.sbf.copyCountTxt.setText('')
            self.sbf.editionTxt.setText('')
            self.sbf.authorIdTxt.setText('')

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class books(QtWidgets.QDialog):
    def __init__(self):
        super(books,self).__init__()
        uic.loadUi('books.ui',self)
        self.titleTxt.textChanged.connect(self.filterTitle)
        self.bookEditBtn.clicked.connect(self.showFindBookForm)
        self.bookDeleteBtn.clicked.connect(self.showRemoveBook)
        self.tableBooks.setColumnWidth(0,200)
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute("select title, isbn, publisher, tableBooks.bookId, price, publicationYear, copyCount, edition, firstName, LastName FROM tablebooks left JOIN tableAuthorBooks ON tableBooks.bookId = tableAuthorBooks.bookId left join tableAuthor on tableAuthor.authorId = tableAuthorBooks.authorId group by title")
            
            for rowNumber, rowData in enumerate(result):
                self.tableBooks.insertRow(rowNumber)
                for columnNumber, columnData in enumerate(rowData):
                    item = str(columnData)
                    self.tableBooks.setItem(rowNumber,columnNumber,QtWidgets.QTableWidgetItem(item))
            cur.close()
            sqliteConnection.close()
            
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)
        
    def showRemoveBook(self):
        self.srb = removeBook()
        self.srb.setModal(True)
        self.srb.show()

    def showFindBookForm(self):
        self.sfbf = findBookForm()
        self.sfbf.setModal(True)
        self.sfbf.show()

    def filterTitle(self):
        self.tableBooks.model().removeRows(0,self.tableBooks.rowCount())
        t = self.titleTxt.text().lower()
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute("select title, isbn, publisher, tableBooks.bookId, price, publicationYear, copyCount, edition, firstName, LastName FROM tablebooks left JOIN tableAuthorBooks ON tableBooks.bookId = tableAuthorBooks.bookId left join tableAuthor on tableAuthor.authorId = tableAuthorBooks.authorId group by title")
            self.tableBooks.setEditTriggers(QTableWidget.NoEditTriggers)
            i = 0
            for fields in result:
                if fields[0].lower().startswith(t):
                    self.tableBooks.insertRow(i)
                    self.tableBooks.setItem(i,0,QTableWidgetItem(fields[0]))
                    self.tableBooks.setItem(i,1,QTableWidgetItem(str(fields[1])))
                    self.tableBooks.setItem(i,2,QTableWidgetItem(fields[2]))
                    self.tableBooks.setItem(i,3,QTableWidgetItem(str(fields[3])))
                    self.tableBooks.setItem(i,4,QTableWidgetItem(str(fields[4])))
                    self.tableBooks.setItem(i,5,QTableWidgetItem(str(fields[5])))
                    self.tableBooks.setItem(i,6,QTableWidgetItem(str(fields[6])))
                    self.tableBooks.setItem(i,7,QTableWidgetItem(str(fields[7])))
                    self.tableBooks.setItem(i,8,QTableWidgetItem(fields[8]))
                    self.tableBooks.setItem(i,9,QTableWidgetItem(fields[9]))
                    i = i + 1
            cur.close()
            sqliteConnection.close()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class booksForm(QtWidgets.QDialog):
    def __init__(self):
        super(booksForm,self).__init__()
        uic.loadUi('booksForm.ui',self)
        self.registerABookBtn.clicked.connect(self.showRegBookForm)
        self.existingBooksBtn.clicked.connect(self.showBooks)

    def showBooks(self):
        self.sb = books()
        self.sb.setModal(True)
        self.sb.show()

    def showRegBookForm(self):
        self.srbf = regBookForm()
        self.srbf.setModal(True)
        self.srbf.show()

class removeAuthor(QtWidgets.QDialog):
    def __init__(self):
        super(removeAuthor,self).__init__()
        uic.loadUi('removeAuthor.ui',self)
        self.deleteBtn.clicked.connect(self.delete)

    def delete(self):
        
        try:
            ai = int(self.authorIdTxt.text())
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            cur.execute(f"delete from tableAuthor where authorId = {ai}")
            sqliteConnection.commit()
            msg = QMessageBox(self)
            msg.setText(f'author Deleted successfully.')
            msg.setWindowTitle('Delete')
            msg.exec()
            self.authorIdTxt.setText('')
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class editAuthorForm(QtWidgets.QDialog):
    def __init__(self):
        super(editAuthorForm,self).__init__()
        uic.loadUi('AuthorRegistration.ui',self)
        self.cancelBtn.clicked.connect(self.close)

class findAuthorForm(QtWidgets.QDialog):
    def __init__(self):
        super(findAuthorForm,self).__init__()
        uic.loadUi('findAuthorForm.ui',self)
        self.findBtn.clicked.connect(self.showAuthorForm)

    def showAuthorForm(self):
        
        try:
            self.ai = int(self.authorIdTxt.text())
            self.saf = editAuthorForm()
            self.saf.setModal(True)
            self.saf.show()
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute(f"select firstName, lastName, authorId, birthDate, passDate from tableAuthor where authorId = {self.ai}")
            for i in result:
                self.saf.firstNameTxt.setText(str(i[0]))
                self.saf.lastNameTxt.setText(str(i[1]))
                self.saf.authorIdTxt.setText(str(i[2]))
                self.saf.birthDateTxt.setText(str(i[3]))
                self.saf.passDateTxt.setText(str(i[4]))
                self.saf.registerBtn.clicked.connect(self.editAuthor)
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

    def editAuthor(self):
        
        try:
            firstName = self.saf.firstNameTxt.text()
            lastName = self.saf.lastNameTxt.text()
            authorId = int(self.saf.authorIdTxt.text())
            birthDate = self.saf.birthDateTxt.text()
            passDate = self.saf.passDateTxt.text()
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            cur.execute(f"update tableAuthor set firstName = '{firstName}', lastName = '{lastName}', authorId = {authorId}, birthDate = '{birthDate}', passDate = '{passDate}' where authorId = {self.ai} ")
            sqliteConnection.commit()
            msg = QMessageBox(self)
            msg.setText(f'َAuthor Edited successfully.')
            msg.setWindowTitle('Edit')
            msg.exec()
            self.saf.firstNameTxt.setText('')
            self.saf.lastNameTxt.setText('')
            self.saf.authorIdTxt.setText('')
            self.saf.birthDateTxt.setText('')
            self.saf.passDateTxt.setText('')

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class authors(QtWidgets.QDialog):
    def __init__(self):
        super(authors,self).__init__()
        uic.loadUi('authors.ui',self)
        self.lastNameTxt.textChanged.connect(self.filterLastName)
        self.authorEditBtn.clicked.connect(self.showFindAuthorForm)
        self.authorDeleteBtn.clicked.connect(self.showRemoveAuthor)
        self.tableAuthors.setColumnWidth(0,300)
        self.tableAuthors.setColumnWidth(1,500)
        self.tableAuthors.setColumnWidth(2,100)
        self.tableAuthors.setColumnWidth(3,100)
        self.tableAuthors.setColumnWidth(4,100)
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute("select firstName, lastName, birthDate, passDate, authorId from tableAuthor")
            
            for rowNumber, rowData in enumerate(result):
                self.tableAuthors.insertRow(rowNumber)
                for columnNumber, columnData in enumerate(rowData):
                    item = str(columnData)
                    self.tableAuthors.setItem(rowNumber,columnNumber,QtWidgets.QTableWidgetItem(item))
            cur.close()
            sqliteConnection.close()
            
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)
        
    def showRemoveAuthor(self):
        #
        self.sra = removeAuthor()
        self.sra.setModal(True)
        self.sra.show()

    def showFindAuthorForm(self):
        #
        self.sfaf = findAuthorForm()
        self.sfaf.setModal(True)
        self.sfaf.show()

    def filterLastName(self):
        self.tableAuthors.model().removeRows(0,self.tableAuthors.rowCount())
        ln = self.lastNameTxt.text().lower()
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute("select firstName, lastName, birthDate, passDate, authorId from tableAuthor")
            self.tableAuthors.setEditTriggers(QTableWidget.NoEditTriggers)
            i = 0
            for fields in result:
                if fields[1].lower().startswith(ln):
                    self.tableAuthors.insertRow(i)
                    self.tableAuthors.setItem(i,0,QTableWidgetItem(fields[0]))
                    self.tableAuthors.setItem(i,1,QTableWidgetItem(fields[1]))
                    self.tableAuthors.setItem(i,2,QTableWidgetItem(fields[2]))
                    self.tableAuthors.setItem(i,3,QTableWidgetItem(fields[3]))
                    self.tableAuthors.setItem(i,4,QTableWidgetItem(str(fields[4])))
                    i = i + 1
            cur.close()
            sqliteConnection.close()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class authorsForm(QtWidgets.QDialog):
    def __init__(self):
        super(authorsForm,self).__init__()
        uic.loadUi('authorsForm.ui',self)
        self.registerAnAuthorBtn.clicked.connect(self.showRegAuthorForm)
        self.existingAuthorsBtn.clicked.connect(self.showAuthors)

    def showAuthors(self):
        self.sa = authors()
        self.sa.setModal(True)
        self.sa.show()

    def showRegAuthorForm(self):
        self.sraf = regAuthorForm()
        self.sraf.setModal(True)
        self.sraf.show()

class regAuthorForm(QtWidgets.QDialog):
    def __init__(self):
        super(regAuthorForm,self).__init__()
        uic.loadUi('authorRegistration.ui',self)    
        self.registerBtn.clicked.connect(self.registration)
        self.cancelBtn.clicked.connect(self.close)

    def registration(self):
        
        try:
            firstName = self.firstNameTxt.text()
            lastName = self.lastNameTxt.text()
            authorId = int(self.authorIdTxt.text())
            birthDate = self.birthDateTxt.text()
            passDate = self.passDateTxt.text()
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            cur.execute(f"insert into tableAuthor (authorId, firstName, lastName, birthDate, passDate) values ({authorId}, '{firstName}','{lastName}','{birthDate}','{passDate}')")
            sqliteConnection.commit()
            cur.close()
            sqliteConnection.close()
            msg = QMessageBox(self)
            msg.setText(f'Author added successfully.')
            msg.setWindowTitle('Registration')
            msg.exec()
            self.firstNameTxt.setText('')
            self.lastNameTxt.setText('')
            self.authorIdTxt.setText('')
            self.birthDateTxt.setText('')
            self.passDateTxt.setText('')

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class removeUser(QtWidgets.QDialog):
    def __init__(self):
        super(removeUser,self).__init__()
        uic.loadUi('removeUser.ui',self)
        self.deleteBtn.clicked.connect(self.delete)

    def delete(self):
        
        try:
            nC = int(self.nationalCodeTxt.text())
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            uC = cur.execute(f"select userCode from tableUser where nationalCode = {nC}")
            for i in uC:
                uc = i[0]
            cur.execute(f"delete from tableUserLogIn where userCode = {uc}")
            sqliteConnection.commit()
            cur.execute(f"delete from tableUser where nationalCode = {nC}")
            sqliteConnection.commit()
            cur.execute(f"delete from tablePerson where nationalCode = {nC}")
            sqliteConnection.commit()
            msg = QMessageBox(self)
            msg.setText(f'User Deleted successfully.')
            msg.setWindowTitle('Delete')
            msg.exec()
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class editUserForm(QtWidgets.QDialog):
    def __init__(self):
        super(editUserForm,self).__init__()
        uic.loadUi('UserRegistration.ui',self)
        self.photoBtn.clicked.connect(self.profilePhoto)
        self.cancelBtn.clicked.connect(self.close)
    
    def profilePhoto(self):
        photoFile, _ = QFileDialog.getOpenFileName(self, 'Open file','' ,"Image files (*.jpg)")
        global uti
        uti = open(photoFile ,'rb')  
        global pc
        pc = 1      
        image = QImage(photoFile)
        self.imagePreviewLabel.setPixmap(QPixmap.fromImage(image))
        self.imagePreviewLabel.setScaledContents(True)
        self.registerBtn.setEnabled(True)

class findUserForm(QtWidgets.QDialog):
    def __init__(self):
        super(findUserForm,self).__init__()
        uic.loadUi('findUserForm.ui',self)
        self.findBtn.clicked.connect(self.showUserForm)

    def showUserForm(self):
        
        try:
            self.nC = int(self.nationalCodeTxt.text())
            self.sruf = editUserForm()
            self.sruf.setModal(True)
            self.sruf.show()
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute(f"select photo, firstName, lastName, tablePerson.nationalCode, birthDate, phone, city, street, alley, postalCode, userCode from tablePerson join tableUser on tablePerson.nationalCode = tableUser.nationalCode where tablePerson.nationalCode = {self.nC}")
            for i in result:
                self.sruf.firstNameTxt.setText(str(i[1]))
                self.sruf.lastNameTxt.setText(str(i[2]))
                self.sruf.nationalCodeTxt.setText(str(i[3]))
                self.sruf.birthDateTxt.setText(str(i[4]))
                self.sruf.phoneTxt.setText(str(i[5]))
                self.sruf.cityTxt.setText(str(i[6]))
                self.sruf.streetTxt.setText(str(i[7]))
                self.sruf.alleyTxt.setText(str(i[8]))
                self.sruf.postalCodeTxt.setText(str(i[9]))
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(i[0],'jpg')
                self.sruf.imagePreviewLabel.setPixmap(pixmap)
                self.sruf.imagePreviewLabel.setScaledContents(True)
                global pc
                pc = 0
                self.sruf.photoBtn.clicked.connect(self.sruf.profilePhoto)
                self.sruf.registerBtn.clicked.connect(self.editUser)
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

    def editUser(self):
        
        try:
            firstName = self.sruf.firstNameTxt.text()
            lastName = self.sruf.lastNameTxt.text()
            nationalCode = int(self.sruf.nationalCodeTxt.text())
            birthDate = self.sruf.birthDateTxt.text()
            phone = int(self.sruf.phoneTxt.text())
            city = self.sruf.cityTxt.text()
            street = self.sruf.streetTxt.text()
            alley = self.sruf.alleyTxt.text()
            postalCode = int(self.sruf.postalCodeTxt.text())
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            cur.execute(f"update tablePerson set firstName = '{firstName}', lastName = '{lastName}', nationalCode = {nationalCode}, birthDate = '{birthDate}', phone = {phone}, city = '{city}', street = '{street}', alley ='{alley}', postalCode = {postalCode} where nationalCode = {self.nC} ")
            sqliteConnection.commit()
            if pc == 1:
                cur.execute(f'update tablePerson set photo = null where nationalCode = {self.nC}')
                sqliteConnection.commit()
                cur.execute(f"insert into tablePerson(id, photo) values(0,?)", [sqlite3.Binary(uti.read())])
                sqliteConnection.commit()
                cur.execute(f'update tablePerson set photo = (select photo from tablePerson where id = 0) where nationalCode = {self.nC}')
                sqliteConnection.commit()
                cur.execute(f"delete from tablePerson where id = 0 ")
                sqliteConnection.commit()

            msg = QMessageBox(self)
            msg.setText(f'User Edited successfully.')
            msg.setWindowTitle('Edit')
            msg.exec()
            self.sruf.firstNameTxt.setText('')
            self.sruf.lastNameTxt.setText('')
            self.sruf.nationalCodeTxt.setText('')
            self.sruf.birthDateTxt.setText('')
            self.sruf.phoneTxt.setText('')
            self.sruf.cityTxt.setText('')
            self.sruf.streetTxt.setText('')
            self.sruf.alleyTxt.setText('')
            self.sruf.postalCodeTxt.setText('')
            self.sruf.imagePreviewLabel.clear()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class users(QtWidgets.QDialog):
    def __init__(self):
        super(users,self).__init__()
        uic.loadUi('users.ui',self)
        self.lastNameTxt.textChanged.connect(self.filterLastName)
        self.userEditBtn.clicked.connect(self.showFindUserForm)
        self.userDeleteBtn.clicked.connect(self.showRemoveUser)
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute("select photo, firstName, lastName, userCode, tablePerson.nationalCode, birthDate, phone, city, street, alley, postalCode from tablePerson join tableUser on tablePerson.nationalCode = tableUser.nationalCode")
            
            for rowNumber, rowData in enumerate(result):
                self.tableUsers.insertRow(rowNumber)
                for columnNumber, columnData in enumerate(rowData):
                    item = str(columnData)
                    if(columnNumber == 0):
                        item = self.getImageLabel(columnData)
                        self.tableUsers.setCellWidget(rowNumber,columnNumber,item)
                    else:
                        self.tableUsers.setItem(rowNumber,columnNumber,QtWidgets.QTableWidgetItem(item))
            self.tableUsers.verticalHeader().setDefaultSectionSize(135)
            cur.close()
            sqliteConnection.close()
            
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)
        
    def showRemoveUser(self):
        self.sru = removeUser()
        self.sru.setModal(True)
        self.sru.show()

    def showFindUserForm(self):
        self.sfuf = findUserForm()
        self.sfuf.setModal(True)
        self.sfuf.show()

    def filterLastName(self):
        self.tableUsers.model().removeRows(0,self.tableUsers.rowCount())
        ln = self.lastNameTxt.text().lower()
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            result = cur.execute("select photo, firstName, lastName, userCode, tablePerson.nationalCode, birthDate, phone, city, street, alley, postalCode from tablePerson join tableUser on tablePerson.nationalCode = tableUser.nationalCode")
            self.tableUsers.setEditTriggers(QTableWidget.NoEditTriggers)
            i = 0
            for fields in result:
                if fields[2].lower().startswith(ln):
                    self.tableUsers.insertRow(i)
                    self.tableUsers.setCellWidget(i,0,self.getImageLabel(fields[0]))
                    self.tableUsers.setItem(i,1,QTableWidgetItem(fields[1]))
                    self.tableUsers.setItem(i,2,QTableWidgetItem(fields[2]))
                    self.tableUsers.setItem(i,3,QTableWidgetItem(str(fields[3])))
                    self.tableUsers.setItem(i,4,QTableWidgetItem(str(fields[4])))
                    self.tableUsers.setItem(i,5,QTableWidgetItem(fields[5]))
                    self.tableUsers.setItem(i,6,QTableWidgetItem(str(fields[6])))
                    self.tableUsers.setItem(i,7,QTableWidgetItem(fields[7]))
                    self.tableUsers.setItem(i,8,QTableWidgetItem(fields[8]))
                    self.tableUsers.setItem(i,9,QTableWidgetItem(fields[9]))
                    self.tableUsers.setItem(i,10,QTableWidgetItem(str(fields[10])))
                    i = i + 1

            self.tableUsers.verticalHeader().setDefaultSectionSize(135)
            cur.close()
            sqliteConnection.close()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText(f'Something went wrong')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

    def getImageLabel(self,image):
        imageLabel = QtWidgets.QLabel()
        imageLabel.setText("")
        imageLabel.setScaledContents(True)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image,'jpg')
        imageLabel.setPixmap(pixmap)
        return imageLabel

class usersForm(QtWidgets.QDialog):
    def __init__(self):
        super(usersForm,self).__init__()
        uic.loadUi('usersForm.ui',self)
        self.registerAUserBtn.clicked.connect(self.showRegUserForm)
        self.existingUsersBtn.clicked.connect(self.showUsers)

    def showUsers(self):
        self.su = users()
        self.su.setModal(True)
        self.su.show()

    def showRegUserForm(self):
        self.sruf = regUserForm()
        self.sruf.setModal(True)
        self.sruf.show()

class regUserForm(QtWidgets.QDialog):
    def __init__(self):
        super(regUserForm,self).__init__()
        uic.loadUi('userRegistration.ui',self)
        self.registerBtn.setEnabled(False)
        self.photoBtn.clicked.connect(self.profilePhoto)
        self.registerBtn.clicked.connect(self.registration)
        self.cancelBtn.clicked.connect(self.close)

    def registration(self):
        
        try:
            firstName = self.firstNameTxt.text()
            lastName = self.lastNameTxt.text()
            nationalCode = int(self.nationalCodeTxt.text())
            birthDate = self.birthDateTxt.text()
            phone = int(self.phoneTxt.text())
            city = self.cityTxt.text()
            street = self.streetTxt.text()
            alley = self.alleyTxt.text()
            postalCode = int(self.postalCodeTxt.text())
            userCode = nationalCode * 2
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            cur.execute(f"insert into tablePerson(nationalCode, firstName, lastName, phone, birthDate, city, street, alley, postalCode, photo) values('{nationalCode}', '{firstName}', '{lastName}', '{phone}', '{birthDate}', '{city}', '{street}', '{alley}', '{postalCode}', ? )", [sqlite3.Binary(uti.read())])
            sqliteConnection.commit()
            cur.execute(f"insert into tableUser (userCode, nationalCode) values ('{userCode}','{nationalCode}')")
            sqliteConnection.commit()
            cur.execute(f"insert into tableUserLogIn (userCode, userPassword) values ('{userCode}','{nationalCode}')")
            sqliteConnection.commit()
            cur.close()
            sqliteConnection.close()
            msg = QMessageBox(self)
            msg.setText(f'User added successfully. their user code is {userCode} and their password is their national code, please remind them to chage the password at first log in.')
            msg.setWindowTitle('Registration')
            msg.exec()
            self.firstNameTxt.setText('')
            self.lastNameTxt.setText('')
            self.nationalCodeTxt.setText('')
            self.birthDateTxt.setText('')
            self.phoneTxt.setText('')
            self.cityTxt.setText('')
            self.streetTxt.setText('')
            self.alleyTxt.setText('')
            self.postalCodeTxt.setText('')
            self.imagePreviewLabel.clear()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText('something went wrong.')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

    def profilePhoto(self):
        photoFile, _ = QFileDialog.getOpenFileName(self, 'Open file','' ,"Image files (*.jpg)")
        global uti
        uti = open(photoFile ,'rb')        
        image = QImage(photoFile)
        self.imagePreviewLabel.setPixmap(QPixmap.fromImage(image))
        self.imagePreviewLabel.setScaledContents(True)
        self.registerBtn.setEnabled(True)

class regLibrarianForm(QtWidgets.QDialog):
    def __init__(self):
        super(regLibrarianForm,self).__init__()
        uic.loadUi('librarianRegistration.ui',self)
        self.registerBtn.setEnabled(False)
        self.photoBtn.clicked.connect(self.profilePhoto)
        self.registerBtn.clicked.connect(self.registration)
        self.cancelBtn.clicked.connect(self.close)

    def registration(self):
       
        try:
            firstName = self.firstNameTxt.text()
            lastName = self.lastNameTxt.text()
            nationalCode = int(self.nationalCodeTxt.text())
            birthDate = self.birthDateTxt.text()
            phone = int(self.phoneTxt.text())
            city = self.cityTxt.text()
            street = self.streetTxt.text()
            alley = self.alleyTxt.text()
            postalCode = int(self.postalCodeTxt.text())
            librarianCode = nationalCode * 2
            
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            cur.execute(f"insert into tablePerson(nationalCode, firstName, lastName, phone, birthDate, city, street, alley, postalCode, photo) values('{nationalCode}', '{firstName}', '{lastName}', '{phone}', '{birthDate}', '{city}', '{street}', '{alley}', '{postalCode}', ? )", [sqlite3.Binary(ti.read())])
            sqliteConnection.commit()
            cur.execute(f"insert into tableLibrarian (librarianCode, nationalCode) values ('{librarianCode}','{nationalCode}')")
            sqliteConnection.commit()
            cur.execute(f"insert into tableLibrarianLogIn (librarianCode, librarianPassword) values ('{librarianCode}','{nationalCode}')")
            sqliteConnection.commit()
            cur.close()
            sqliteConnection.close()
            msg = QMessageBox(self)
            msg.setText(f'Librarian added successfully. their librarian code is {librarianCode} and their password is their national code, please remind them to chage the password at first log in.')
            msg.setWindowTitle('Registration')
            msg.exec()
            self.firstNameTxt.setText('')
            self.lastNameTxt.setText('')
            self.nationalCodeTxt.setText('')
            self.birthDateTxt.setText('')
            self.phoneTxt.setText('')
            self.cityTxt.setText('')
            self.streetTxt.setText('')
            self.alleyTxt.setText('')
            self.postalCodeTxt.setText('')
            self.imagePreviewLabel.clear()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText('something went wrong.')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

    def profilePhoto(self):
        photoFile, _ = QFileDialog.getOpenFileName(self, 'Open file','' ,"Image files (*.jpg )")
        global ti
        ti = open(photoFile ,'rb')  
        global pc
        pc = 1      
        image = QImage(photoFile)
        self.imagePreviewLabel.setPixmap(QPixmap.fromImage(image))
        self.imagePreviewLabel.setScaledContents(True)
        self.registerBtn.setEnabled(True)
        
class librariansForm(QtWidgets.QDialog):
    def __init__(self):
        super(librariansForm,self).__init__()
        uic.loadUi('librariansForm.ui',self)
        self.registerALibrarianBtn.clicked.connect(self.showRegLibrarianForm)
        self.existingLibrariansBtn.clicked.connect(self.showLibrarians)

    def showLibrarians(self):
        self.sl = librarians()
        self.sl.setModal(True)
        self.sl.show()
    
    def showRegLibrarianForm(self):
        self.srlf = regLibrarianForm()
        self.srlf.setModal(True)
        self.srlf.show()

class librarianChangePassword(QtWidgets.QDialog):
    def __init__(self):
        super(librarianChangePassword,self).__init__()
        uic.loadUi('changePassword.ui',self)
        self.changeBtn.clicked.connect(self.change)

    def change(self):
        try:
            newPass = self.passwordTxt.text()
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            cur.execute(f"update tableLibrarianLogIn set librarianPassword = '{newPass}' where librarianCode = {lc}")
            sqliteConnection.commit()
            cur.close()
            msg = QMessageBox(self)
            msg.setText('Password changed successfully.')
            msg.setWindowTitle('passWord')
            msg.exec()
            self.passwordTxt.setText('')

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText('something went wrong.')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class userChangePassword(QtWidgets.QDialog):
    def __init__(self):
        super(userChangePassword,self).__init__()
        uic.loadUi('changePassword.ui',self)
        self.changeBtn.clicked.connect(self.change)

    def change(self):
        try:
            newPass = self.passwordTxt.text()
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            cur.execute(f"update tableUserLogIn set userPassword = '{newPass}' where userCode = {uc}")
            sqliteConnection.commit()
            cur.close()
            msg = QMessageBox(self)
            msg.setText('Password changed successfully.')
            msg.setWindowTitle('passWord')
            msg.exec()
            self.passwordTxt.setText('')

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText('something went wrong.')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class profileLibrarian(QtWidgets.QDialog):
    def __init__(self):
        super(profileLibrarian,self).__init__()
        uic.loadUi('profileLibrarian.ui',self)
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            rec = cur.execute(f"select firstName, lastName, photo , librarianCode from tablePerson join tableLibrarian on tablePerson.nationalCode = tableLibrarian.nationalCode where librarianCode = {lc} ")
            for data in rec:
                firstName = data[0]
                lastName = data[1]
                image = data[2]
                code = str(data[3])

            self.labelFName.setText(firstName)
            self.labelLName.setText(lastName)
            self.labelCode.setText(code)
            self.labelRole.setText("Librarian")
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(image,'jpg')
            self.photoLabel.setPixmap(pixmap)
            self.photoLabel.setScaledContents(True) 
            cur.close()
            sqliteConnection.close()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText('something went wrong.')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)
        
        self.usersBtn.clicked.connect(self.showUsersForm)
        self.authorsBtn.clicked.connect(self.showAuthorsForm)
        self.booksBtn.clicked.connect(self.showBooksForm)
        self.lendABookBtn.clicked.connect(self.showLending)
        self.returnABookBtn.clicked.connect(self.showReturnBook)
        self.changePasswordBtn.clicked.connect(self.showChangePassword)
        self.exitBtn.clicked.connect(self.terminate)

    def showReturnBook(self):
        self.srb = returnBook()
        self.srb.setModal(True)
        self.srb.show()

    def showLending(self):
        self.sl = lending()
        self.sl.setModal(True)
        self.sl.show()

    def showBooksForm(self):
        self.sbf = booksForm()
        self.sbf.setModal(True)
        self.sbf.show()

    def showAuthorsForm(self):
        self.saf = authorsForm()
        self.saf.setModal(True)
        self.saf.show()

    def showUsersForm(self):
        self.suf = usersForm()
        self.suf.setModal(True)
        self.suf.show()
            

    def showChangePassword(self):
        self.scp = librarianChangePassword()
        self.scp.setModal(True)
        self.scp.show()


    def terminate(self):
        self.close()

class profileUser(QtWidgets.QDialog):
    def __init__(self):
        super(profileUser,self).__init__()
        uic.loadUi('profileUser.ui',self)
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            rec = cur.execute(f"select firstName, lastName, photo , userCode from tablePerson join tableUser on tablePerson.nationalCode = tableUser.nationalCode where userCode = {uc} ")
            for data in rec:
                firstName = data[0]
                lastName = data[1]
                image = data[2]
                code = str(data[3])

            self.labelFName.setText(firstName)
            self.labelLName.setText(lastName)
            self.labelCode.setText(code)
            self.labelRole.setText("user")
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(image,'jpg')
            self.photoLabel.setPixmap(pixmap)
            self.photoLabel.setScaledContents(True) 
            cur.close()
            sqliteConnection.close()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText('something went wrong.')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)
        
        self.booksBtn.clicked.connect(self.showBooks)
        self.changePasswordBtn.clicked.connect(self.showChangePassword)
        self.exitBtn.clicked.connect(self.terminate)

    def showBooks(self):
        self.sb = books()
        self.sb.setModal(True)
        self.sb.show()
        self.sb.bookEditBtn.setEnabled(False)
        self.sb.bookDeleteBtn.setEnabled(False)

    def showChangePassword(self):
        self.scp = userChangePassword()
        self.scp.setModal(True)
        self.scp.show()


    def terminate(self):
        self.close()

class profileAdmin(QtWidgets.QDialog):
    def __init__(self):
        super(profileAdmin,self).__init__()
        uic.loadUi('profileAdmin.ui',self)
        try:
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            rec = cur.execute(f"select firstName, lastName, photo from tablePerson where id = 1 ")
            for data in rec:
                firstName = data[0]
                lastName = data[1]
                image = data[2]

            self.labelFName.setText(firstName)
            self.labelLName.setText(lastName)
            self.labelCode.setText("1")
            self.labelRole.setText("system adminstrator")
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(image,'jpg')
            self.photoLabel.setPixmap(pixmap)
            self.photoLabel.setScaledContents(True) 
            cur.close()
            sqliteConnection.close()

        except Exception as e:
            msg = QMessageBox(self)
            msg.setText('something went wrong.')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)
        
        self.librarianBtn.clicked.connect(self.showLibrariansForm)
        self.usersBtn.clicked.connect(self.showUsersForm)
        self.authorsBtn.clicked.connect(self.showAuthorsForm)
        self.booksBtn.clicked.connect(self.showBooksForm)
        self.lendABookBtn.clicked.connect(self.showLending)
        self.returnABookBtn.clicked.connect(self.showReturnBook)
        self.exitBtn.clicked.connect(self.terminate)

    def showReturnBook(self):
        self.srb = returnBook()
        self.srb.setModal(True)
        self.srb.show()

    def showLending(self):
        self.sl = lending()
        self.sl.setModal(True)
        self.sl.show()

    def showBooksForm(self):
        self.sbf = booksForm()
        self.sbf.setModal(True)
        self.sbf.show()

    def showAuthorsForm(self):
        self.saf = authorsForm()
        self.saf.setModal(True)
        self.saf.show()

    def showUsersForm(self):
        self.suf = usersForm()
        self.suf.setModal(True)
        self.suf.show()

    def showLibrariansForm(self):
        self.slf = librariansForm()
        self.slf.setModal(True)
        self.slf.show()
            
    def terminate(self):
        self.close()
        
class librarianLogInForm(QtWidgets.QDialog):
    def __init__(self):
        super(librarianLogInForm,self).__init__()
        uic.loadUi('librarianLogIn.ui',self)
        self.librarianLogInBtn.clicked.connect(self.librarianLogIn)

    def librarianLogIn(self):
        try:
            global lc
            lc = int(self.librarianCodeTxt.text())
            lp = self.librarianPasswordTxt.text()
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            info = cur.execute(f"select librarianCode, librarianPassword from tableLibrarianLogIn where librarianCode = {lc}")
            for i in info:
                passWord = i[1]

            if lp == passWord:
                self.lli = profileLibrarian()
                self.lli.setModal(True)
                self.lli.show()
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText('Wrong log in information')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class userLogInForm(QtWidgets.QDialog):
    def __init__(self):
        super(userLogInForm,self).__init__()
        uic.loadUi('userLogIn.ui',self)
        self.userLogInBtn.clicked.connect(self.userLogIn)

    def userLogIn(self):
        try:
            global uc
            uc = int(self.userCodeTxt.text())
            up = self.userPasswordTxt.text()
            sqliteConnection = sqlite3.connect("library.db")
            cur = sqliteConnection.cursor()
            info = cur.execute(f"select userCode, userPassword from tableUserLogIn where userCode = {uc}")
            for i in info:
                passWord = i[1]

            if up == passWord:
                self.uli = profileUser()
                self.uli.setModal(True)
                self.uli.show()
        except Exception as e:
            msg = QMessageBox(self)
            msg.setText('Wrong log in information')
            msg.setWindowTitle('Error')
            msg.exec()
            print(e)

class showAdminLogInForm(QtWidgets.QDialog):
    def __init__(self):
        super(showAdminLogInForm,self).__init__()
        uic.loadUi('adminLogIn.ui',self)
        self.adminLogInBtn.clicked.connect(self.adminLogIn)

    def adminLogIn(self):
        if self.adminLogInCode.text().lower() == 'admin' and self.adminPassword.text().lower() == 'admin':
            self.ali = profileAdmin()
            self.ali.setModal(True)
            self.ali.show()

        else:
            msg = QMessageBox(self)
            msg.setText('Wrong log in information')
            msg.setWindowTitle('Error')
            msg.exec()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('mainWindow.ui',self)
        self.exitBtn.clicked.connect(self.terminate)
        self.librarianLogInBtn.clicked.connect(self.showLibrarianLogInForm)
        self.userLogInBtn.clicked.connect(self.showUserLogInForm)
        self.adminBtn.clicked.connect(self.showAdminLogInForm)
        self.guestBtn.clicked.connect(self.showBooks)

    def showBooks(self):
        self.sb = books()
        self.sb.setModal(True)
        self.sb.show()
        self.sb.bookEditBtn.setEnabled(False)
        self.sb.bookDeleteBtn.setEnabled(False)
        

    def showLibrarianLogInForm(self):
        self.sllif = librarianLogInForm()
        self.sllif.setModal(True)
        self.sllif.show()
        
    def showUserLogInForm(self):
        self.sulif = userLogInForm()
        self.sulif.setModal(True)
        self.sulif.show()

    def showAdminLogInForm(self):
        self.salif = showAdminLogInForm()
        self.salif.setModal(True)
        self.salif.show()

    def terminate(self):
        self.close()

app = QApplication([])
mW = MainWindow()
mW.show()
app.exec()