import sys             # For providing access to some variables used or maintained by the interpreter 
import os.path         # For providing a way of using operating system dependent functionality 
import re              # Used to work with Regular Expressions 
from PyQt5 import QtCore, QtGui, uic,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time                       # To providing functions for working with times 
import xlwings as xw              # To interact excel with python 
#from notify import Ui_Dialog_2    # To make the errorlog dialog popup in screen and Importing Ui_Dialog_2 class from notify.py
import xlrd                       # To read excel with python 
from xlrd import open_workbook    # To open a excel file for data extraction 
#from xlrd import empty_cell        Used to check whether the input excel is empty or not       
import win32com.client            # For COM client used by python and for generating .py files for certain COM servers 
#from shutil import copyfile       # To copy a file to a new file in current directory 
#from shutil import rmtree         # To remove a directory 
import subprocess                  # To allow us to release a new process and get their return codes
xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True
path = ""

qtCreatorFile = "RDBI.ui"            # Assigning the RDBI PyQt file 
Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFile)  # Loading GUI

qtCreatorFile_1 = "RDBI_nw.ui"            # Assigning the RDBI PyQt file 
Ui_Dialog_1, QtBaseClass_1 = uic.loadUiType(qtCreatorFile_1)  # Loading GUI

qtCreatorFile_2 = "RDBI_nw_2.ui"            # Assigning the RDBI PyQt file 
Ui_Dialog_2, QtBaseClass_2 = uic.loadUiType(qtCreatorFile_2)  # Loading GUI




class FileSelection(QMainWindow, Ui_Dialog,QtBaseClass):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_Dialog.__init__(self)
        QtBaseClass.__init__(self)
        self.setupUi(self)
        self.excel_path.setText("")
        self.path = ""
        self.check=''
        self.l3=[]
        self.initialize_action()       # Calling the function initialize_action 
        self.initialize_interface()    # Calling the function initialize_interface 


    def initialize_action(self):
        self.excel_file_open.clicked.connect(self.set_excel_path)      # Calling the set_excel_path function when the DID_Info button is clicked in GUI
        #self.a2l_file_open.clicked.connect(self.set_ecuextract_path)          # Calling the set_a2l_path function when the A2L button is clicked in GUI
        self.output_file_open.clicked.connect(self.set_output_path)    # Calling the set_output_path function when the Output button is clicked in GUI
        self.btn_testcase_generate.clicked.connect(self.window2)    # Calling the create_xls function when the generate button is clicked in GUI
        self.btn_testcase_generate_2.clicked.connect(self.window3) 
        self.help.clicked.connect(self.open_manual)                    # Calling the open_manual function when the help button is clicked in GUI
        self.about.clicked.connect(self.open_about)                    # Calling the open_about function when the about button is clicked in GUI
        self.test_case_type.activated[str].connect(self.Test_Case_type)# Calling the Test_Case_type function when an option is selected in UDS Service(GUI)
             
    def initialize_interface(self):   
        username = os.path.join(os.getlogin())   # Getting the username
        self.entercomment.setText("")
        self.entername.setText("")
        self.entervariant.setText("")
        self.user_name_spec.setText(username)
        self.user_name.setText(username)
        #self.excel_path.setText("")
        self.output_path.setText("")

    def open_manual(self):
        os.startfile("User_manual.pdf")
    
    def open_about(self):
        os.startfile("About.pdf")



   
    def set_excel_path(self):
        #print("i am herer")
        self.path = QtWidgets.QFileDialog.getOpenFileName(None, "Open Excel File", os.path.expanduser("~/Desktop/"), "Excel(*.xls *.xlsm *.xlsx)") 
        #print(self.path)
        if self.path:
            self.excel_path.setText(self.path[0])
            self.check=str(self.excel_path.text())
            #print(self.check)
            
        self.xl()
        intended_list=[]
        non_intended_list=[]
        for i in self.l3:
            if 'true' in i:
                intended_list.append(i[0])
            else:
                non_intended_list.append(i[0])
        print(len(intended_list))
        print(len(non_intended_list))
        a=intended_list
        b=non_intended_list
        def arrayA():
            for i in range(len(a)):
                if a[i]==a[len(a)-1]:
                    f.write("%s"%a[i])
                else:
                    f.write("%s,"%a[i])
        def arrayB():
            for i in range(len(b)):
                if b[i]==b[len(b)-1]:
                    f.write("%s"%b[i])
                else:
                    f.write("%s,"%b[i])
        with open('readme1.txt', 'w') as f:
            #variables
            f.write("variables \n")
            f.write("{ \n")
            f.write("int i,j,c=1; \n")

            f.write("\nint a[500]=\n{\n")
            arrayA()
            f.write("\n};\n")
            
            f.write("\nint b[500]=\n{\n")
            arrayB()
            f.write("\n};\n")

            f.write("\n}\n")

            #onstart

            f.write("on start\n")
            f.write("{\n")

            f.write("   for(i=0;i<elcount(a);i++)\n")
            f.write("   {\n")
            f.write("       for(j=0;j<elcount(b);j++)\n")
            f.write("        {\n")
            f.write("           if(a[i]==b[j])\n")
            f.write("           {\n")
            f.write("               break;\n")
            f.write("           }\n")
            f.write("       }\n")
            f.write("   if(j==elcount(b))\n")
            f.write("       {\n")
            f.write("""           write("0x%02X is not there in non-intended list",a[i]);\n""")
            f.write("""           writeToLogEx("testcase_%d ---> 0x%02X is not there in non-intended list\n",c,a[i]);\n""")
            f.write("             c++;\n")
            f.write("       }\n")
            f.write("   }\n")
            f.write("}\n")



        
    
    def get_check_path(self):
        #print("############")
        return self.check
        
    
    def xl(self):
        vbox=QVBoxLayout()
        #loc=('C:\\Users\\riswa\\OneDrive\\Documents\\GUI_Ref\\sample.xlsx')
        loc=self.check
        #print('success',loc)
        wb=xlrd.open_workbook(loc)
        sheet=wb.sheet_by_index(0)
        sheet.cell_value(0,0)
        a1=sheet.nrows
        b1=sheet.ncols

        for i in range(1,a1):
            l1=[]
            l2=[]
            for j in range(b1):
                if sheet.cell_value(0,j)=='Identifier':
                    a=sheet.cell_value(i,j)
                    l1.append(a)
                    #print(a,end=' :{ ')
                    #self.listWidget.insertItem(a1,a)
                elif sheet.cell_value(0,j)=='Senders':
                    if sheet.cell_value(i,j) =='ECM,':
                        b='Tx'    
                        #print(b,end=' , ')
                        l1.append(b)
                elif sheet.cell_value(0,j)=='Receivers':
                    if sheet.cell_value(i,j) =='ECM,':
                        c='Rx'   
                        l1.append(c) 
                        #print(c,end=' , ')
                elif sheet.cell_value(0,j)=='Periodocity':
                    if sheet.cell_value(i,j) == '':
                        e=0
                        #print(e,end=' , ')
                        l1.append(e)
                    else:
                        f=sheet.cell_value(i,j)    
                        #print(f,end=' , ')
                        l1.append(f)
                elif sheet.cell_value(0,j)=='Intended':
                    g=sheet.cell_value(i,j)
                    l1.append(g)
                l2.append(l1)
            #print(l1,sep=' ')
            self.l3.append(l2[j])
            #print("333333333333333333")
        #print(len(self.l3))
        
    def get_l3_list(self):
        #print("444444444444444444444444")
        #print(self.l3)
        #print(len(self.l3))
        self.li=[]
        for i in self.l3:
            if i not in self.li:
                self.li.append(i)
        #print(len(self.li))
        return self.li

    def set_output_path(self):
        path = QFileDialog.getExistingDirectory(None, "Output Directory", os.path.expanduser("~/Desktop/"))
        if path:
            self.output_path.setText(path)

    def Test_Case_type(self):
        TC_type = str(self.test_case_type.currentText())
        if TC_type == "URT":
            self.test_method_label.show()
            self.test_method.show()
        else:
            self.test_method_label.hide()
            self.test_method.hide()

    def window2(self):
        #print(self.check)
        self.w=Window2()
        
        self.w.show()
        self.hide()
    
    def window3(self):
        #print(self.check)
        self.w1=Window3()
        
        self.w1.show()
        self.hide()


class Window2(QMainWindow,Ui_Dialog_1):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        Ui_Dialog_1.__init__(self)
        QtBaseClass_1.__init__(self)
        self.setupUi(self)
        #self.rxchooses=[]
        self.InitUI()

    def InitUI(self):
        #self.setWindowTitle(self.title)
        #self.setGeometry(self.left,self.top,self.width,self.height)

        vbox=QVBoxLayout()

        #self.list=QListWidget()
        window1.xl()
        
        self.l4=[]
        l5=[]
        p_rx=[]
        p_tx=[]
        self.final_p=[]
        #print(len(window1.get_l3_list()))
        for i in list(window1.get_l3_list()):
            if('Rx' in i):
                if type(i[2])!=str and i[2]!=0:
                    self.l4.append(i[0])
                    self.final_p.append(i[2]*1000)     
            else:
                l5.append(i[0])
        #print(final_p)
        print(len(self.final_p))
        #print(l4)
        print(len(self.l4))
        for i in self.l4:
            box=QCheckBox(i)
            item = QListWidgetItem() 
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, box) 
            box.stateChanged.connect(self.rxgetChoose)
        #print(l3,sep=' ')   
        username = os.path.join(os.getlogin()) 
        
        #self.label=QLabel()
        self.label_2.setFont(QtGui.QFont('Arial',14))
        vbox.addWidget(self.label_2)
        self.back.clicked.connect(self.back1)
        vbox.addWidget(self.listWidget)
        self.setLayout(vbox) 
        self.show()
    
    def back1(self):
        self.f=FileSelection()
        
        self.f.show()
        self.hide()

    def rxgetChoose(self):
        count = self.listWidget.count()  # Get the total number of QListWidget
        cb_list = [self.listWidget.itemWidget(self.listWidget.item(i))
                  for i in range(count)]  # QListWidget get inside all QListWidgetItem in QCheckBox
        # print(cb_list)
        self.rxchooses = []  # Storage of data is selected
        for cb in cb_list:  # type:QCheckBox
            if cb.isChecked():
                self.rxchooses.append(cb.text())
        #item=self.listWidget.currentItem()
                self.label_2.setText(str('The selected Rx msg ID''s : '+' , '.join(map(str,self.rxchooses))))
        #print(self.rxchooses)
        a=self.rxchooses
        print(a)
        self.rx_id_start_capl()
        return a

    def rx_id_start_capl(self):
        with open('readme.txt', 'w') as f:
                #variables
                f.write("variables \n")
                f.write("{ \n")

                for i in self.rxchooses:
                    f.write("message %s msg_%s= {DLC=8,DIR=Tx,byte(0) = 0x01,byte(1) = 0x02,byte(2) = 0x03,byte(3) = 0x04,byte(4) = 0x05,byte(5) = 0x06,byte(6) = 0x07,byte(7) = 0x08};"%(i,i))
                    f.write('\n')

                f.write("int time = 10000; //ms time\n\n")

                for i in self.rxchooses:
                    f.write("float time_%s = %f;\n"%(i,self.final_p[self.l4.index(i)]))
                
                f.write("\n")

                for i in self.rxchooses:
                    f.write("msTimer clk_mst_%s;\n"%i)
                    f.write("msTimer clk_t_%s;\n"%i)
                
                f.write("\n")

                for i in self.rxchooses:
                    f.write("int check_%s;\n"%i)
                    f.write("int count_%s = 1;\n"%i)
                
                f.write("\n")

                f.write("}\n\n")
                
                #on timer clk_mst
                for i in self.rxchooses:
                    f.write("on timer clk_mst_%s\n{\n"%i)
                    f.write("output(msg_%s);\n"%i)
                    f.write("cancelTimer(clk_mst_%s);\n"%i)
                    f.write("setTimer(clk_mst_%s,time_%s);\n"%(i,i))
                    f.write("count_%s++;\n}\n"%i)
                
                f.write("\n\n")

                #on timer clk_t
                c=1
                for i in self.rxchooses:
                    f.write("on timer clk_t_%s\n{\n"%i)
                    f.write("int i,c=1;\n")
                    f.write("cancelTimer(clk_mst_%s);\n"%i)
                    f.write("""write("%%d",check_%s);\n"""%i)
                    f.write("""write("%%d",count_%s);\n"""%i)
                    #if
                    f.write("if(count_%s>=check_%s)\n"%(i,i))
                    f.write("{\n")
                    f.write("""writeToLogEx("    \\nTestcase_%d--> Message ID = 0x%%02x || DLC = %%x || Timestamp = %%f || DIR=Tx ",msg_%s.id,msg_%s.dlc,timeNowNS());"""%(c,i,i))
                    f.write("\nfor(i=0;i<msg_%s.dlc;i++)\n{"%i)
                    f.write("""\nwriteToLogEx("          bytes(%%d) = 0x%%02x",i,msg_%s.byte(i));\n}\n"""%i)
                    f.write("writeToLogEx(\"          The message ID 0x%%0x is \"\"SUCCESS\"\"\",msg_%s.id);\n"%i)
                    f.write("}\n")
                    #else
                    f.write("else\n")
                    f.write("{\n")
                    f.write("""writeToLogEx("    \\nTestcase_%d--> Message ID = 0x%%02x || DLC = %%x || Timestamp = %%f || DIR=Tx ",msg_%s.id,msg_%s.dlc,timeNowNS());"""%(c,i,i))
                    f.write("\nfor(i=0;i<msg_%s.dlc;i++)\n{"%i)
                    f.write("""\nwriteToLogEx("          bytes(%%d) = 0x%%02x",i,msg_%s.byte(i));\n}\n"""%i)
                    f.write("writeToLogEx(\"          The message ID 0x%%0x is \"\"FAIL\"\"\",msg_%s.id);\n"%i)
                    f.write("c++;\n")
                    f.write("}\n}\n\n")
                    c=c+1

                #void
                for i in self.rxchooses:
                    f.write("void msg_%s()\n"%i)
                    f.write("{\n")
                    f.write("check_%s=time/time_%s;\n"%(i,i))
                    f.write("setTimer(clk_mst_%s,time_%s);\n"%(i,i))
                    f.write("setTimer(clk_t_%s,time);\n"%i)
                    f.write("}\n\n")

                #onstart
                f.write("on start\n")
                f.write("{ \n")
                for i in self.rxchooses:
                    f.write("msg_%s();\n"%i)
                f.write("}")


class Window3(QMainWindow,Ui_Dialog_2):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        Ui_Dialog_2.__init__(self)
        QtBaseClass_2.__init__(self)
        self.setupUi(self)
        #self.txchooses=[]
        self.InitUI1()

    def InitUI1(self):
        #self.setWindowTitle(self.title)
        #self.setGeometry(self.left,self.top,self.width,self.height)

        

        #self.list=QListWidget()
        vbox=QVBoxLayout()
        #print("check")
        #print(window1.get_check_path())
        #print(window1.get_l3_list())
        window1.xl()
        self.rx=[]
        self.tx=[]
        #print(len(window1.get_l3_list()))
        for i in window1.get_l3_list():
            if 'Rx' in i:
                self.rx.append(i[0])
            else:
                self.tx.append(i[0])

        anamoly=['ID_Anamoly' , 'DLC_Anamoly' , 'Min_Max_Anamoly' , 'Payload_Anamoly' , 'Time_Variation_Anamoly']
        for j in anamoly:
            box1=QCheckBox(j)
            item1 = QListWidgetItem() 
            self.listWidget_2.addItem(item1)
            self.listWidget_2.setItemWidget(item1,box1)
            box1.stateChanged.connect(self.txgetChoose_anomaly)


        for i in self.tx:
            box=QCheckBox(i)
            item = QListWidgetItem() 
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, box)
            box.stateChanged.connect(self.txgetChoose)
        

        #print(l3,sep=' ')   
        username = os.path.join(os.getlogin()) 
        #self.listWidget.clicked.connect(self.txgetChoose)
        #self.label=QLabel()
        self.label_2.setFont(QtGui.QFont('Arial',14))
        vbox.addWidget(self.label_2)

        #self.listWidget_2.itemDoubleClicked.connect(self.txgetChoose_anomaly)
        #self.label=QLabel()
        #self.label_4.setFont(QtGui.QFont('Arial',8))
        #vbox.addWidget(self.label_4)

        self.back_1.clicked.connect(self.back2)
        vbox.addWidget(self.listWidget)
        vbox.addWidget(self.listWidget_2)
        self.setLayout(vbox) 
        self.show()
        
    def back2(self):
        self.f=FileSelection()
        self.f.show()
        self.hide()

    def txgetChoose(self):
        count = self.listWidget.count()  # Get the total number of QListWidget
        cb_list = [self.listWidget.itemWidget(self.listWidget.item(i))
                  for i in range(count)]  # QListWidget get inside all QListWidgetItem in QCheckBox
        # print(cb_list)
        self.txchooses = []  # Storage of data is selected
        for cb in cb_list:  # type:QCheckBox
            if cb.isChecked():
                self.txchooses.append(cb.text())
        #item=self.listWidget.currentItem()
                self.label_2.setText(str('The selected Tx msg ID''s : '+' , '.join(map(str,self.txchooses))))
        print(self.txchooses)
        self.tx_id_start_capl()
        return self.txchooses

    def txgetChoose_anomaly(self):
        #print('1')
        count1 = self.listWidget_2.count()  # Get the total number of QListWidget
        cb_list1 = [self.listWidget_2.itemWidget(self.listWidget_2.item(i))
                    for i in range(count1)]  # QListWidget get inside all QListWidgetItem in QCheckBox
        # print(cb_list)
        self.txanomaly = []  # Storage of data is selected
        for cb in cb_list1:  # type:QCheckBox
            if cb.isChecked():
                self.txanomaly.append(cb.text())
        #item=self.listWidget.currentItem()
                #self.label_4.setText(str('anomaly : '+' , '.join(map(str,self.txanomaly))))
        print(self.txanomaly)
        return self.txanomaly

    def tx_id_start_capl(self):
        with open('readme.txt', 'w') as f:
            #variables
            f.write("variables \n")
            f.write("{ \n")
            f.write("int i; \n")
            c=1
            
            f.write("dword handle=0; \n")
            if 'Time_Variation_Anamoly' in self.txanomaly:
                for i in self.txchooses:
                    f.write("msTimer clk_%s;\n"%i)
                for i in self.txchooses:
                    f.write("message %s msg_%s= {DLC=8,DIR=Tx,byte(0) = 0x01,byte(1) = 0x02,byte(2) = 0x03,byte(3) = 0x04,byte(4) = 0x05,byte(5) = 0x06,byte(6) = 0x07,byte(7) = 0x08};"%(i,i))
                    f.write('\n')
                    c=c+1
            f.write("}\n")
            #dlc
            if 'DLC_Anamoly' in self.txanomaly:
                f.write("\nvoid DLC_Anamoly()\n{\n")
                c1=1
                f.write("int c=1;\n")
                for i in self.txchooses:
                    f.write("message %s msg_%s= {DLC=%d,DIR=Tx,byte(0) = 0x01,byte(1) = 0x02,byte(2) = 0x03,byte(3) = 0x04,byte(4) = 0x05,byte(5) = 0x06,byte(6) = 0x07,byte(7) = 0x08};"%(i,i,c1))
                    f.write('\n')
                    c1=c1+1
                f.write("""writeToLogEx("----------DLC ANAMOLY LOG--------------");\n""")
                for i in self.txchooses:
                    f.write("output(msg_%s);\n"%i)
                    f.write("""writeToLogEx("    \\nTestcase_%%d--> Message ID = 0x%%02x || DLC = %%x || Timestamp = %%f || DIR=Tx ",c,msg_%s.id,msg_%s.dlc,timeNowNS());"""%(i,i))
                    f.write("\nfor(i=0;i<msg_%s.dlc;i++)\n{"%i)
                    f.write("""\nwriteToLogEx("          bytes(%%d) = 0x%%02x",i,msg_%s.byte(i));\n}\n"""%i)
                    f.write("c++;\n\n")
                f.write("""writeToLogEx("-------------------------------------------");\n""")
                f.write("}\n")
            #min_max
            if 'Min_Max_Anamoly' in self.txanomaly:
                f.write("\nvoid min_max_Anamoly()\n{\n")
                f.write("int c=1;\n")
                for i in self.txchooses:
                    f.write("message %s msg_%s= {DLC=8,DIR=Tx,byte(0) = 0x01,byte(1) = 0x02,byte(2) = 0x03,byte(3) = 0x04,byte(4) = 0x05,byte(5) = 0x06,byte(6) = 0x07,byte(7) = 0x08};"%(i,i))
                    f.write('\n')
                    f.write("message %s msg_%sff= {DLC=8,DIR=Tx,byte(0) = 0xff,byte(1) = 0xff,byte(2) = 0xff,byte(3) = 0xff,byte(4) = 0xff,byte(5) = 0xff,byte(6) = 0xff,byte(7) = 0xff};"%(i,i))
                    f.write('\n')
                f.write("""writeToLogEx("----------MIN MAX ANAMOLY LOG--------------");\n""")
                for i in self.txchooses:
                    f.write("output(msg_%s);\n"%i)
                    f.write("""writeToLogEx("    \\nTestcase_%%d--> Message ID = 0x%%02x || DLC = %%x || Timestamp = %%f || DIR=Tx ",c,msg_%s.id,msg_%s.dlc,timeNowNS());"""%(i,i))
                    f.write("\nfor(i=0;i<msg_%s.dlc;i++)\n{"%i)
                    f.write("""\nwriteToLogEx("          bytes(%%d) = 0x%%02x",i,msg_%s.byte(i));\n}\n"""%i)
                    f.write("c++;\n\n")
                    f.write("output(msg_%sff);\n"%i)
                    f.write("""writeToLogEx("    \\nTestcase_%%d--> Message ID = 0x%%02x || DLC = %%x || Timestamp = %%f || DIR=Tx ",c,msg_%sff.id,msg_%sff.dlc,timeNowNS());"""%(i,i))
                    f.write("\nfor(i=0;i<msg_%sff.dlc;i++)\n{"%i)
                    f.write("""\nwriteToLogEx("          bytes(%%d) = 0x%%02x",i,msg_%sff.byte(i));\n}\n"""%i)
                    f.write("c++;\n\n")
                f.write("""writeToLogEx("-------------------------------------------");\n""")
                f.write("}\n")
            #payload
            if 'Payload_Anamoly' in self.txanomaly:
                f.write("\nvoid payload_Anamoly()\n{\n")
                f.write("int c=1,j=0;\n")
                for i in self.txchooses:
                    f.write("message %s msg_%s= {DLC=8,DIR=Tx,byte(0) = 0x01,byte(1) = 0x02,byte(2) = 0x03,byte(3) = 0x04,byte(4) = 0x05,byte(5) = 0x06,byte(6) = 0x07,byte(7) = 0x08};"%(i,i))
                    f.write('\n')
                f.write("""writeToLogEx("----------PAYLOAD ANAMOLY LOG--------------");\n""")
                f.write("for(i=1;i<=1000;i++)\n{\n")
                for i in self.txchooses:
                    f.write("output(msg_%s);\n"%i)
                    f.write("""writeToLogEx("    \\nTestcase_%%d--> Message ID = 0x%%02x || DLC = %%x || Timestamp = %%f || DIR=Tx ",c,msg_%s.id,msg_%s.dlc,timeNowNS());"""%(i,i))
                    f.write("\nfor(j=0;j<msg_%s.dlc;j++)\n{"%i)
                    f.write("""\nwriteToLogEx("          bytes(%%d) = 0x%%02x",j,msg_%s.byte(j));\n}\n"""%i)
                    f.write("c++;\n\n")
                f.write("}\n")
                f.write("""writeToLogEx("-------------------------------------------");\n""")
                f.write("}\n")
            #id_anamoloy
            if 'ID_Anamoly' in self.txanomaly:
                import random
                l=[]
                for i in range(256*4):
                    l.append(hex((i)))
                random.shuffle(l)
                l1=[]
                f.write("\nvoid Id_Anamoly()\n{\n")
                f.write("int c=1;\n")
                for i in l:
                    if i not in self.tx:
                        l1.append(i)
                        f.write("message %s msg_%s= {DLC=8,DIR=Tx,byte(0) = 0x01,byte(1) = 0x02,byte(2) = 0x03,byte(3) = 0x04,byte(4) = 0x05,byte(5) = 0x06,byte(6) = 0x07,byte(7) = 0x08};"%(i,i))
                        f.write('\n')
                f.write("""writeToLogEx("----------RANDOM-ID ANAMOLY LOG--------------");\n""")
                for i in l:
                    if i not in self.tx:
                        f.write("output(msg_%s);\n"%i)
                        f.write("""writeToLogEx("    \\nTestcase_%%d--> Message ID = 0x%%02x || DLC = %%x || Timestamp = %%f || DIR=Tx ",c,msg_%s.id,msg_%s.dlc,timeNowNS());"""%(i,i))
                        f.write("\nfor(i=0;i<msg_%s.dlc;i++)\n{"%i)
                        f.write("""\nwriteToLogEx("          bytes(%%d) = 0x%%02x",i,msg_%s.byte(i));\n}\n"""%i)
                        f.write("c++;\n\n")
                f.write("""writeToLogEx("-------------------------------------------");\n""")
                f.write("}\n")
            #time_var_anamoly
            if 'Time_Variation_Anamoly' in self.txanomaly:
                time=[90,95,99,101,105,110]
                f.write("\nvoid time_variation_Anamoly()\n{\n")
                
                count=0
                for i in self.txchooses:
                    f.write("message %s msg_%s= {DLC=8,DIR=Tx,byte(0) = 0x01,byte(1) = 0x02,byte(2) = 0x03,byte(3) = 0x04,byte(4) = 0x05,byte(5) = 0x06,byte(6) = 0x07,byte(7) = 0x08};"%(i,i))
                    f.write('\n')
                f.write("""writeToLogEx("----------TIME VARIATION ANAMOLY LOG--------------");\n""")
                for i in self.txchooses:
                    f.write("setTimer(clk_%s,%d);\n"%(i,time[count]))
                    count=count+1
                    if count>=len(time):
                        count=0
                f.write("}\n")
                count1=0
                for i in self.txchooses:
                    f.write("\non timer clk_%s\n{\n"%i)
                    f.write("int c=1;\n")
                    f.write("setTimer(clk_%s,%d);\n"%(i,time[count1]))
                    f.write("output(msg_%s);\n"%i)
                    f.write("""writeToLogEx("    \\nTestcase_%%d--> Message ID = 0x%%02x || DLC = %%x || Timestamp = %%f || DIR=Tx ",c,msg_%s.id,msg_%s.dlc,timeNowNS());"""%(i,i))
                    f.write("\nfor(i=0;i<msg_%s.dlc;i++)\n{"%i)
                    f.write("""\nwriteToLogEx("          bytes(%%d) = 0x%%02x",i,msg_%s.byte(i));\n}\n"""%i)
                    f.write("c++;\n\n")
                    count1=count1+1
                    if count1>=len(time):
                        count1=0
                    f.write("}\n")

            #onstart
            f.write("on start\n")
            f.write("{ \n")
            for i in self.txanomaly:
                f.write('%s();\n'%i)
            f.write("""write("req rxd\\n");\n""")
            f.write("startLogging(\"Logging\");\n")
            f.write("""setLogFileName("C:\\\\Logging\\\\log");\n""")
            f.write("}\n")
            f.write("on preStop\n{\n")
            f.write("stopLogging(\"Logging\");\n")
            f.write("}\n")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    print(type(app))
    window1 = FileSelection()
    window1.show()
    sys.exit(app.exec_())
 
