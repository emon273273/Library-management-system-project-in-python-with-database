
from tkinter import *
from tkinter import ttk

import mysql.connector

from tkinter import messagebox

import tkinter

import datetime





class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Libaray management system")
        self.root.geometry("1550x800+0+0")
############################variable#################################


        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finallprice=StringVar()









        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
 #####################################dataframeleft#############
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)


        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staf","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        
        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN NO",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)

        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)



        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID NO:",padx=2,pady=4,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)


        lblFirstName=Label(DataFrameLeft,font=("arial",12,"bold"),text="FirstName",padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=28)
        txtFirstName.grid(row=3,column=1)




        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="LastName",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)



        lblAdress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1",padx=2,pady=6,bg="powder blue")
        lblAdress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)


        lblAdress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2",padx=2,pady=6,bg="powder blue")
        lblAdress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6 ,column=1)



        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="Post Code",padx=2,pady=4,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7 ,column=1)

        lblMObile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile",padx=2,pady=6,bg="powder blue")
        lblMObile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8 ,column=1)
        


        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id :",padx=2,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0 ,column=3)



        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title :",padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1 ,column=3)



        lblAuther=Label(DataFrameLeft,font=("arial",12,"bold"),text="Auther Name :",padx=2,pady=6,bg="powder blue")
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.auther_var,width=29)
        txtAuther.grid(row=2 ,column=3)


        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed:",padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3 ,column=3)


        

        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4 ,column=3)



        lblDaysOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days on Book:",padx=2,pady=6,bg="powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook,width=29)
        txtDaysOnBook.grid(row=5 ,column=3)




        lblLateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,pady=6,bg="powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.lateratefine_var,width=29)
        txtReturnFine.grid(row=6 ,column=3)



        lblDateOverdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date over Due:",padx=2,pady=6,bg="powder blue")
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        txtDateOverdate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue,width=29)
        txtDateOverdate.grid(row=7 ,column=3)




        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual price:",padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finallprice,width=29)
        txtActualPrice.grid(row=8 ,column=3)



        #######################dataframe right################


      


        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=870,y=5,width=580,height=350)




        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)


        listscrollbar=Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0,column=1,sticky="ns")


        listBooks=["Head First Book","Learn Python The Hard Way","python programming","C++ Primer","python cookBook","Python Machine Learning","Fluent Python","Machine Techno","Java For Dummies", "Thinking in Java","Teach Yourself Java","Test-Driven Java Development","R for Data Science","The Book of R","The R Book"]

        def selectBook(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            if (x=="Head First Book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("python manual")
                self.auther_var.set("paul Berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.788")




            elif (x=="Learn Python The Hard Way"):
                self.bookid_var.set("BKID8796")
                self.booktitle_var.set("Basic of python")
                self.auther_var.set("Zed A.shaw")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.688")

            elif (x=="python programming"):
                self.bookid_var.set("BKID8798")
                self.booktitle_var.set("Basic of python")
                self.auther_var.set("Andrew shaw")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.600")

            
            elif (x=="python cookBook"):
                self.bookid_var.set("BKID8798")
                self.booktitle_var.set("Basic of python")
                self.auther_var.set("Brian K. Jones")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.900")




            elif (x=="C++ Primer"):
                self.bookid_var.set("BKID8777")
                self.booktitle_var.set("Basic of c++")
                self.auther_var.set("Stanley B. Lippman")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.200")

            elif (x=="Python Machine Learning"):
                self.bookid_var.set("BKID8777")
                self.booktitle_var.set("Basic of python")
                self.auther_var.set("Sebastian Raschka")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.200")
           
            elif (x=="Fluent Python"):
                self.bookid_var.set("BKID8777")
                self.booktitle_var.set("Basic of python")
                self.auther_var.set("Luciano Ramalho")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.500")

            elif (x=="Machine Techno"):
                self.bookid_var.set("BKID8717")
                self.booktitle_var.set("Basic of python")
                self.auther_var.set("Youssef")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.500")

            elif (x=="Java For Dummies"):
                self.bookid_var.set("BKID897")
                self.booktitle_var.set("Basic of java")
                self.auther_var.set("Barry Burd")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.500")
            

            elif (x=="Thinking in Java"):
                self.bookid_var.set("BKID1197")
                self.booktitle_var.set("Basic of java")
                self.auther_var.set("Bruce Eckel")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.900")


            elif(x=="Teach Yourself Java"):
                self.bookid_var.set("BKID2198")
                self.booktitle_var.set("advance of java")
                self.auther_var.set("Laura Lemay")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.1100")



            elif(x=="Test-Driven Java Development"):
                self.bookid_var.set("BKID2108")
                self.booktitle_var.set("advance of java")
                self.auther_var.set("Viktor Farcic")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.1400")


########## 
            elif(x=="R for Data Science"):
                self.bookid_var.set("BKID00108")
                self.booktitle_var.set("advance of R")
                self.auther_var.set("Hadley Wickham")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.2400")


            
            elif(x=="The Book of R"):
                self.bookid_var.set("BKID00108")
                self.booktitle_var.set("basic of R")
                self.auther_var.set("Tilman M. Davies")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.1400")

            

            elif(x=="The R Book"):
                self.bookid_var.set("BKID002108")
                self.booktitle_var.set("basic of R")
                self.auther_var.set("Michael J. Crawley")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set("taka.50")
                self.dateoverdue.set("NO")
                self.finallprice.set("taka.14500")




        listbox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)

        listbox.bind("<<ListboxSelect>>",selectBook)

        listbox.grid(row=0,column=0,padx=4)

        listscrollbar.config(command=listbox.yview)  #somossa ase


        for item in listBooks:
            listbox.insert(END,item)





        #BUTTONS FRAME

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")

        btnAddData.grid(row=0,column=0)




        btnAddData=Button(Framebutton,command=self.showdata,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")

        btnAddData.grid(row=0,column=1)



        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")

        btnAddData.grid(row=0,column=2)


        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")

        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")

        btnAddData.grid(row=0,column=4)



        btnAddData=Button(Framebutton,command=self.pexit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")

        btnAddData.grid(row=0,column=5)


    ## infromation frame ###########

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=210)



        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)



        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)

        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.libary_table=ttk.Treeview(Table_frame,columns=("membertype","prnno","title","firstname","lastname","adress1","adress2","postid","mobile","bookid","booktitle","auther","dateborrowed","datedue","days","laterfines","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)


        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.libary_table.xview)
        yscroll.config(command=self.libary_table.yview)




        self.libary_table.heading("membertype",text="Member Type")
        self.libary_table.heading("prnno",text=" PRN No.")
        self.libary_table.heading("title",text="Title")
        self.libary_table.heading("firstname",text="First Name")

        self.libary_table.heading("lastname",text="Last Name")

        self.libary_table.heading("adress1",text="Address1")
        self.libary_table.heading("adress2",text="Address2")

        self.libary_table.heading("postid",text="Post ID")
        self.libary_table.heading("mobile",text="Mobile Number")

        self.libary_table.heading("bookid",text="Book Id")

        self.libary_table.heading("booktitle",text="Book Title")

        self.libary_table.heading("auther",text="Auther")

        self.libary_table.heading("dateborrowed",text="Date of Borrowed")
        self.libary_table.heading("datedue",text="Date Due")

        self.libary_table.heading("days",text="DaysonBook")

        self.libary_table.heading("laterfines",text="LateRuturnFine")
        self.libary_table.heading("dateoverdue",text="DateOverDue")

        self.libary_table.heading("finalprice",text="Final price")

        

        













        self.libary_table["show"]="headings"
        self.libary_table.pack(fill=BOTH,expand=1)

        self.libary_table.column("membertype",width=110)

        self.libary_table.column("prnno",width=100)
        self.libary_table.column("title",width=100)
        self.libary_table.column("firstname",width=100)
        self.libary_table.column("lastname",width=100)
        self.libary_table.column("adress1",width=100)

        self.libary_table.column("adress2",width=100)

        self.libary_table.column("postid",width=100)
        self.libary_table.column("mobile",width=120)
        self.libary_table.column("bookid",width=100)
        self.libary_table.column("booktitle",width=100)
        self.libary_table.column("auther",width=100)
        self.libary_table.column("dateborrowed",width=133)

        self.libary_table.column("datedue",width=100)
        self.libary_table.column("days",width=100)
        self.libary_table.column("laterfines",width=100)
        self.libary_table.column("dateoverdue",width=100)
        self.libary_table.column("finalprice",width=100)
    

        self.fatch_data()
        self.libary_table.bind("<ButtonRelease-1>",self.get_cursor)
         

    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="password",database="mydata",auth_plugin='mysql_native_password')
        
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.member_var.get(),
                                        self.prn_var.get(),
                                        self.id_var.get(),
                                        self.firstname_var.get(),
                                        self.lastname_var.get(),
                                        self.address1_var.get(),
                                        self.address2_var.get(),
                                        self.postcode_var.get(),
                                        self.mobile_var.get(),
                                        self.bookid_var.get(),
                                        self.booktitle_var.get(),
                                        self.auther_var.get(),
                                        self.dateborrowed_var.get(),
                                        self.datedue_var.get(),
                                        self.daysonbook.get(),
                                        self.lateratefine_var.get(),
                                        self.dateoverdue.get(),
                                        self.finallprice.get()
                        



                                          ))
        conn.commit()

        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success","Member has been inserted sucessfully")

    def update(self):


        conn=mysql.connector.connect(host="localhost",user="root",password="password",database="mydata",auth_plugin='mysql_native_password')
        
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s, Address2=%s, postid=%s, Mobile=%s,Bookid=%s,Auther=%s,Databorrowed=%s, datedue=%s, daysofbook=%s, latereturnfine=%s, dateoverdue=%s, finalprice=%s, booktitle=%s where PRN_NO=%s",(



                                        self.member_var.get(),
                                        
                                        self.id_var.get(),
                                        self.firstname_var.get(),
                                        self.lastname_var.get(),
                                        self.address1_var.get(),
                                        self.address2_var.get(),
                                        self.postcode_var.get(),
                                        self.mobile_var.get(),
                                        self.bookid_var.get(),
                                        self.booktitle_var.get(),
                                        self.auther_var.get(),
                                        self.dateborrowed_var.get(),
                                        self.datedue_var.get(),
                                        self.daysonbook.get(),
                                        self.lateratefine_var.get(),
                                        self.dateoverdue.get(),
                                        self.finallprice.get(),
                                        self.prn_var.get()
                                                     ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("sucess","member has been updated")


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="password",database="mydata",auth_plugin='mysql_native_password')
        
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        ##data insert korte hbe amar 

        if len(rows)!=0:
            self.libary_table.delete(*self.libary_table.get_children())
            
            for i in rows:
                self.libary_table.insert("",END,values=i)
            conn.commit()
            conn.close()


    
    def get_cursor(self,event=""):

        cursor_row=self.libary_table.focus()
        content=self.libary_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),

        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.auther_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook.set(row[14])
        self.lateratefine_var.set(row[15])
        self.datedue_var.set(row[16])
        self.finallprice.set(row[17])


        


    def showdata(self):

        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")

        self.txtBox.insert(END,"PRN NO: \t\t "+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID NO: \t\t "+self.id_var.get()+"\n")
        self.txtBox.insert(END,"FirstName: \t\t "+self.firstname_var.get()+"\n")

        self.txtBox.insert(END,"LastName: \t\t "+self.lastname_var.get()+"\n")

        self.txtBox.insert(END,"Address1: \t\t "+self.address1_var.get()+"\n")

        self.txtBox.insert(END,"Address2: \t\t "+self.address2_var.get()+"\n")

        self.txtBox.insert(END,"Post code: \t\t "+self.postcode_var.get()+"\n")

        self.txtBox.insert(END,"Mobile No: \t\t "+self.mobile_var.get()+"\n")

        self.txtBox.insert(END,"Book ID: \t\t "+self.bookid_var.get()+"\n")

        self.txtBox.insert(END,"Book Title: \t\t "+self.booktitle_var.get()+"\n")

        self.txtBox.insert(END,"Auther: \t\t "+self.auther_var.get()+"\n")

        self.txtBox.insert(END,"DateBorrowed: \t\t "+self.dateborrowed_var.get()+"\n")

        self.txtBox.insert(END,"DateDue: \t\t "+self.datedue_var.get()+"\n")

        self.txtBox.insert(END,"DaysOnBook: \t\t "+self.daysonbook.get()+"\n")

        self.txtBox.insert(END,"LateRateFine: \t\t "+self.lateratefine_var.get()+"\n")

        self.txtBox.insert(END,"DateOverDue: \t\t "+self.dateoverdue.get()+"\n")

        self.txtBox.insert(END,"FinalPrice: \t\t "+self.finallprice.get()+"\n")



    #reset 

    def reset(self):

        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set("")
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook.set(""),
        self.lateratefine_var.set(""),
        self.dateoverdue.set(""),
        self.finallprice.set(""),
        self.txtBox.delete("1.0",END)



    
    def pexit(self):
        pexit=tkinter.messagebox.askyesno("Library management system","Do you want to exit")

        if pexit>0:
            self.root.destroy()
            return

    


    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="password",database="mydata",auth_plugin='mysql_native_password')
        
        my_cursor=conn.cursor()

        query="delete from library where PRN_NO=%s"
        value=(self.prn_var.get(),)
        my_cursor.execute(query,value)


        
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        

        
        
        conn.close()


        messagebox.showinfo("success","Member has been deleted")




    

        

        

    


if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()