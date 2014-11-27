# -*- coding: utf-8 -*-
import sip
import sys
import random
import easygui
#import os
#import unicodedata
import sqlite3 as lite
from PyQt4 import QtCore, QtGui, uic



class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        uic.loadUi('TWh.ui', self)

        self.pushButton_2.clicked.connect(self.View1_Click)
        self.pushButton_3.clicked.connect(self.Add1_Click)
        self.pushButton_Change.clicked.connect(self.Change1_Click)
        self.pushButton_5.clicked.connect(self.Delete1_Click)

        
        

    def View1_Click(self):
        print "View1_Click called" 
        con = lite.connect('warehouse.db')
        with con:
            cur = con.cursor()               
            cur.execute(u'SELECT * FROM tovar') 
            col_names = [cn[0] for cn in cur.description]
            rows = cur.fetchall()
            i=0
            while i<(len(rows)):
                for row in rows: 
                    tovar_id = str(row[0]).zfill(5)
                    tovar_name = (row[1])
                    tovar_type = (row[2])
                    tovar_size  = str(row[3])
                    tovar_colour  = str(row[4])
                    tovar_matherials  = (row[5])
                    tovar_kolvo  = str(row[6])                 

                    id_item = QtGui.QTableWidgetItem(str(tovar_id))
                    self.table1_Products.setItem(i, 0, id_item)
                    id_item.setTextAlignment(QtCore.Qt.AlignCenter)
                    
                    name_item = QtGui.QTableWidgetItem(tovar_name)
                    self.table1_Products.setItem(i, 1, name_item)
                    name_item.setTextAlignment(QtCore.Qt.AlignCenter)

                    type_item = QtGui.QTableWidgetItem(tovar_type)
                    self.table1_Products.setItem(i, 2, type_item)
                    type_item.setTextAlignment(QtCore.Qt.AlignCenter)

                    size_item = QtGui.QTableWidgetItem(str(tovar_size))
                    self.table1_Products.setItem(i, 3, size_item)
                    size_item.setTextAlignment(QtCore.Qt.AlignCenter)
                    
                    colour_item = QtGui.QTableWidgetItem(tovar_colour)
                    self.table1_Products.setItem(i, 4, colour_item)
                    colour_item.setTextAlignment(QtCore.Qt.AlignCenter)

                    matherials_item = QtGui.QTableWidgetItem(tovar_matherials)
                    self.table1_Products.setItem(i, 5, matherials_item)
                    matherials_item.setTextAlignment(QtCore.Qt.AlignCenter)

                    kolvo_item = QtGui.QTableWidgetItem(tovar_kolvo)
                    self.table1_Products.setItem(i, 6, kolvo_item)
                    kolvo_item.setTextAlignment(QtCore.Qt.AlignCenter)
                    
                    i += 1

                    

    def Add1_Click(self):
        print "Add1_Click called" 
        try:
            tovar_id = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 0).text().toUtf8(), "utf-8")
            tovar_name = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 1).text().toUtf8(), "utf-8")
            tovar_type = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 2).text().toUtf8(), "utf-8")
            tovar_size  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 3).text().toUtf8(), "utf-8")
            tovar_colour  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 4).text().toUtf8(), "utf-8")
            tovar_matherials  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 5).text().toUtf8(), "utf-8")
            tovar_kolvo  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 6).text().toUtf8(), "utf-8")            
            
        except:
            msgBox1 = QtGui.QMessageBox()
            msgBox1.setWindowTitle(u"Уведомление")
            msgBox1.setText(u"Заполните все поля")
            msgBox1.exec_()
        con = lite.connect('warehouse.db')
        with con:
            cur = con.cursor()               
            cur.execute(u"""INSERT INTO tovar (tovar_id, name, type, size, colour, matherials, kolvo)
                        VALUES(?,?,?,?,?,?,?)""",(int(tovar_id), tovar_name, tovar_type, tovar_size, int(tovar_colour), tovar_matherials, int(tovar_kolvo)))
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle(u"Уведомление")
            msgBox.setText((u"Товар (id='%s') успешно добавлен")%((tovar_id)))
            msgBox.exec_()
        con.close()
        self.table1_Products.clearContents()
        return



    def Change1_Click(self):
        print "Change1_Click called" 
        try:
            tovar_id = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 0).text().toUtf8(), "utf-8")
            tovar_name = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 1).text().toUtf8(), "utf-8")
            tovar_type = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 2).text().toUtf8(), "utf-8")
            tovar_size  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 3).text().toUtf8(), "utf-8")
            tovar_colour  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 4).text().toUtf8(), "utf-8")
            tovar_matherials  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 5).text().toUtf8(), "utf-8")
            tovar_kolvo  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 6).text().toUtf8(), "utf-8")            
            
        except:
            msgBox1 = QtGui.QMessageBox()
            msgBox1.setWindowTitle(u"Уведомление")
            msgBox1.setText(u"Заполните все поля")
            msgBox1.exec_()
        con = lite.connect('warehouse.db')
        with con:
            cur = con.cursor()               
            cur.execute(u"""UPDATE tovar SET tovar_id=?, name=?, type=?, size=?, colour=?, matherials=?, kolvo=?
                        WHERE tovar_id=?""",(int(tovar_id), tovar_name, tovar_type, tovar_size, int(tovar_colour), tovar_matherials, int(tovar_kolvo), int(tovar_id)))
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle(u"Уведомление")
            msgBox.setText((u"Информация о товаре (id='%s') успешно изменена")%((tovar_id)))
            msgBox.exec_()
        con.close()
        self.table1_Products.clearContents()
        return



    def Delete1_Click(self):
        print "Delete1_Click called" 
        try:
            tovar_id = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 0).text().toUtf8(), "utf-8")
        except:
            msgBox1 = QtGui.QMessageBox()
            msgBox1.setWindowTitle(u"Уведомление")
            msgBox1.setText(u"Укажите id товара который хотите удалить")
            msgBox1.exec_()
        con = lite.connect('warehouse.db')
        with con:
            cur = con.cursor()               
            cur.execute(u"DELETE from tovar where tovar_id='%s'" % tovar_id)
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle(u"Уведомление")
            msgBox.setText((u"Информация о товаре(id='%s') успешно удалена")%((tovar_id)))
            msgBox.exec_()
        con.close()
        self.table1_Products.clearContents()
        return

                    

        

app = QtGui.QApplication(sys.argv)
a = MainWindow()
a.show()
sys.exit(app.exec_())
