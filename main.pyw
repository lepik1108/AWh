# -*- coding: cp1251 -*-
import sip
import sys
import random
import easygui
#import os
#import unicodedata
import sqlite3 as lite
from PyQt4 import QtCore, QtGui, uic

import imaplib
import email

from datetime import datetime

from multiprocessing import Process, Pipe
import time







        
class PB_Window(QtGui.QMainWindow):
    def __init__(ui, parent=None):
        QtGui.QMainWindow.__init__(ui, parent)
        uic.loadUi('PB_Window.ui', ui)
        ui.setAttribute(QtCore.Qt.WA_DeleteOnClose)





class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        uic.loadUi('TWh.ui', self)

        self.pushButton_2.clicked.connect(self.View1_Click)
        self.pushButton_3.clicked.connect(self.Add1_Click)
        self.pushButton_Change.clicked.connect(self.Change1_Click)
        self.pushButton_5.clicked.connect(self.Delete1_Click)
        
        self.pushButton_CheckMail.clicked.connect(self.CheckMail_Click)

        self.pushButton_7.clicked.connect(self.Approve2_Click)
        self.pushButton_8.clicked.connect(self.View2_Click)
        


      
        

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
            tovar_id = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 0).text().toUtf8(), "cp1251")
            tovar_name = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 1).text().toUtf8(), "cp1251")
            tovar_type = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 2).text().toUtf8(), "cp1251")
            tovar_size  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 3).text().toUtf8(), "cp1251")
            tovar_colour  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 4).text().toUtf8(), "cp1251")
            tovar_matherials  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 5).text().toUtf8(), "cp1251")
            tovar_kolvo  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 6).text().toUtf8(), "cp1251")            
            
        except:
            msgBox1 = QtGui.QMessageBox()
            msgBox1.setWindowTitle(u"Уведомление")
            msgBox1.setText(u"Заполните все поля")
            msgBox1.exec_()
        con = lite.connect('warehouse.db')
        with con:
            cur = con.cursor()               
            cur.execute(u"""INSERT INTO tovar (tovar_id, name, type, size, colour, matherials, kolvo)
                        VALUES(?,?,?,?,?,?,?)""",(int(tovar_id), tovar_name, tovar_type, tovar_size, int(tovar_colour), tovar_matherials, int(tovar_kol)))
        con.close()
        self.table1_Products.clearContents()
        return



    def Change1_Click(self):
        print "Change1_Click called"       
        try:
            tovar_id = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 0).text().toUtf8(), "cp1251")
            tovar_name = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 1).text().toUtf8(), "cp1251")
            tovar_type = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 2).text().toUtf8(), "cp1251")
            tovar_size  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 3).text().toUtf8(), "cp1251")
            tovar_colour  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 4).text().toUtf8(), "cp1251")
            tovar_matherials  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 5).text().toUtf8(), "cp1251")
            tovar_kolvo  = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 6).text().toUtf8(), "cp1251")            
            
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
            tovar_id = unicode(self.table1_Products.item(self.table1_Products.currentRow(), 0).text().toUtf8(), "cp1251")
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



    def CheckMail_Click(self):

        print "CheckMail_Click called"
        ui_date = self.calendarWidget.selectedDate().toPyDate()
        
        # gmail account
        m_user = 'testxstar@gmail.com'  # gmail address
        m_pass = 'vdblnsgdjllamdxb'  # application secret key, allowed in your gmail account

        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle(u"Уведомление")
        msgBox.setText(u"Сейчас будет проверена почта, дождитесь уведомления о завершении проверки.")
        msgBox.exec_()

        self.hide()

        #pb = PB_Window()
        #pb.show()
        
        
        conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        conn.login(m_user, m_pass)
        conn.select()
        typ, data = conn.search(None, 'ALL') # 'UNSEEN' 
        i = 0
        
        for num in data[0].split():
            typ, data = conn.fetch(num, '(RFC822)')

            msg = email.message_from_string(data[0][1])
            #print type(msg['Date'])
            
            text = ""
            if msg.is_multipart():
                html = None
                for part in msg.get_payload():
                    #print "%s, %s" % (part.get_content_type(), part.get_content_charset())
         
                    if part.get_content_charset() is None:
                        # We cannot know the character set, so return decoded "something"
                        text = part.get_payload(decode=True)
                        continue
         
                    charset = part.get_content_charset()
         
                    if part.get_content_type() == 'text/plain':
                        text = unicode(part.get_payload(decode=True), str(charset), "ignore").encode('cp1251', 'replace')
         
                if text != '':
                    try:
                        print '--------------------------------------------------------------------------------'
                        print text

                        #print 'Raw Date:', msg['Date'][5:25]
                        #print "day = ", str(int(msg['Date'][5:7])).zfill(2)
                        #print (str(int(msg['Date'][5:7])).zfill(2)+ msg['Date'][7:25])
                        if msg['Date'][6] == ' ':
                            date_object = datetime.strptime((str(int(msg['Date'][5:7])).zfill(2)+' '+ msg['Date'][7:24]), '%d %b %Y %H:%M:%S')    
                        else:
                            date_object = datetime.strptime(msg['Date'][5:24], '%d %b %Y %H:%M:%S')
                        print date_object.date()
                        print (ui_date)
                        
                        if  date_object.date() == ui_date :
                            print '111111111111'
                
                            
                            date_item = QtGui.QTableWidgetItem(date_object.strftime('%d %b %Y %H:%M:%S'))
                            self.tableWidget_Orders.setItem(i, 0, date_item)
                            date_item.setTextAlignment(QtCore.Qt.AlignCenter)

                            msg_item = QtGui.QTableWidgetItem(unicode(text, "cp1251"))
                            self.tableWidget_Orders.setItem(i, 1, msg_item)
                            msg_item.setTextAlignment(QtCore.Qt.AlignCenter)
                            
                            i+=1
                            self.tableWidget_Orders.insertRow(i)
                            print i
                            
                    except:
                        print 'exception'                      
                
        conn.close()
        conn.logout()
        #pb.close()
        self.tableWidget_Orders.removeRow(i)
        self.show()
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle(u"Уведомление")
        msgBox.setText(u"Письма, по выбранной Вами дате успешно загружены")
        msgBox.exec_()



    def View2_Click(self):
        print "View2_Click called"
        self.tableWidget_ord.clearContents()
        con = lite.connect('warehouse.db')
        with con:
            cur = con.cursor()               
            cur.execute(u'SELECT * FROM submitted_orders') 
            col_names = [cn[0] for cn in cur.description]
            rows = cur.fetchall()
            i=0
            while i<(len(rows)):
                for row in rows:
                    order_id = (row[0])#.zfill(5)
                    tovar_id = (row[1])#.zfill(5)
                    
                    tovar_name = cur.execute(u'SELECT name FROM tovar WHERE tovar_id=%s'%int(tovar_id)).fetchone()[0]
                    tovar_type = cur.execute(u'SELECT type FROM tovar WHERE tovar_id=%s'%int(tovar_id)).fetchone()[0]
                    
                    order_colour  = str(row[2])
                    order_size  = str(row[3])
                    order_kolvo  = str(row[4])
                    order_date = (row[5])
                    print order_id, tovar_id, (tovar_name[0]), (tovar_type[0]), order_size, order_colour, order_kolvo, order_date
###
###
                    order_id_item = QtGui.QTableWidgetItem(str(order_id).zfill(5))
                    self.tableWidget_ord.setItem(i, 0, order_id_item)
                    order_id_item.setTextAlignment(QtCore.Qt.AlignCenter)

                    tovar_id_item = QtGui.QTableWidgetItem(str(tovar_id).zfill(5))
                    self.tableWidget_ord.setItem(i, 1, tovar_id_item)
                    tovar_id_item.setTextAlignment(QtCore.Qt.AlignCenter)
                    
                    name_item = QtGui.QTableWidgetItem(tovar_name)
                    self.tableWidget_ord.setItem(i, 2, name_item)
                    name_item.setTextAlignment(QtCore.Qt.AlignCenter)

                    type_item = QtGui.QTableWidgetItem(tovar_type)
                    self.tableWidget_ord.setItem(i, 3, type_item)
                    type_item.setTextAlignment(QtCore.Qt.AlignCenter)

                    size_item = QtGui.QTableWidgetItem(str(order_size))
                    self.tableWidget_ord.setItem(i, 4, size_item)
                    size_item.setTextAlignment(QtCore.Qt.AlignCenter)

                    colour_item = QtGui.QTableWidgetItem(order_colour)
                    self.tableWidget_ord.setItem(i, 5, colour_item)
                    colour_item.setTextAlignment(QtCore.Qt.AlignCenter)

                    kolvo_item = QtGui.QTableWidgetItem(order_kolvo)
                    self.tableWidget_ord.setItem(i, 6, kolvo_item)
                    kolvo_item.setTextAlignment(QtCore.Qt.AlignCenter)

                    date_item = QtGui.QTableWidgetItem(order_date)
                    self.tableWidget_ord.setItem(i, 7, date_item)
                    date_item.setTextAlignment(QtCore.Qt.AlignCenter)
                    
                    i += 1
        con.close()



    def Approve2_Click(self):
        print "Approve2_Click called"
        try:
            order_id = unicode(self.tableWidget_10.item(0, 0).text().toUtf8(), "cp1251")
            tovar_id = unicode(self.tableWidget_10.item(1, 0).text().toUtf8(), "cp1251")
            order_colour = unicode(self.tableWidget_10.item(2, 0).text().toUtf8(), "cp1251")
            order_size  = unicode(self.tableWidget_10.item(3, 0).text().toUtf8(), "cp1251")
            order_kolvo  = unicode(self.tableWidget_10.item(4, 0).text().toUtf8(), "cp1251")
            order_date = unicode(self.tableWidget_10.item(5, 0).text().toUtf8(), "cp1251")
            
        except:
            msgBox1 = QtGui.QMessageBox()
            msgBox1.setWindowTitle(u"Уведомление")
            msgBox1.setText(u"Заполните все поля")
            msgBox1.exec_()
        con = lite.connect('warehouse.db')
        with con:
            cur = con.cursor()               
            cur.execute(u"""INSERT INTO submitted_orders (order_id, tovar_id, colour, size, kolvo, date)
                        VALUES(?,?,?,?,?,?)""",(int(order_id), int(tovar_id), int(order_colour), (order_size), int(order_kolvo), order_date))


            tovar_kolvo = cur.execute(u'SELECT kolvo FROM tovar WHERE tovar_id=%s'%int(tovar_id)).fetchone()[0]
            new_kolvo = int(tovar_kolvo) - int(order_kolvo)
            cur.execute(u"""UPDATE tovar SET kolvo=?
                WHERE tovar_id=?""",(int(new_kolvo), int(tovar_id)))
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle(u"Уведомление")
            msgBox.setText(u"Заказ на товар (id=%s) утвержден. Осталось товара на складе: %s"%(str(tovar_id).zfill(5), str(new_kolvo)))
            msgBox.exec_()
            print   new_kolvo
###
        con.close()

                    

        

app = QtGui.QApplication(sys.argv)
a = MainWindow()
a.show()
sys.exit(app.exec_())
