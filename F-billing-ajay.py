from cgitb import text
from email import message

from itertools import count
from msilib.schema import ListBox
from numbers import Number
from operator import index
from pydoc import describe
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from turtle import width
from PIL import ImageTk, Image
from numpy import insert
import pandas as pd
from tkinter.messagebox import askyesno, showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date, datetime
from tkinter import filedialog
import subprocess
import io
import mysql.connector



fbilldb = mysql.connector.connect(
  host="localhost", user="root", password="", database=" fbilling", port="3306"
 )
fbcursor = fbilldb.cursor(buffered=True)

def reset():
  global root
  root.destroy()

root=Tk()
root.geometry("1060x730")

root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
p1 = PhotoImage(file = 'images/fbicon.png')
root.iconphoto(False, p1)


s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
invoices= PhotoImage(file="images/invoice.png")
orders = PhotoImage(file="images/order.png")
estimates = PhotoImage(file="images/estimate.png")
recurring = PhotoImage(file="images/recurring.png")
purchase = PhotoImage(file="images/purchase.png")
expenses = PhotoImage(file="images/expense.png")
customer = PhotoImage(file="images/customer.png")
product = PhotoImage(file="images/package.png")
reports = PhotoImage(file="images/report.png")
setting = PhotoImage(file="images/setting.png")
tick = PhotoImage(file="images/check.png")
warnin = PhotoImage(file="images/sign_warning.png")
cancel = PhotoImage(file="images/close.png")
saves = PhotoImage(file="images/save.png")
folder = PhotoImage(file="images/folder-black.png")
photo11 = PhotoImage(file = "images/invoice-pvt.png")
customer = PhotoImage(file="images/customer.png")
smslog = PhotoImage(file = "images/smslog.png")
video = PhotoImage(file = "images/video.png")
mark1 = PhotoImage(file="images/mark.png")
mark2 = PhotoImage(file="images/mark2.png")
photo10 = PhotoImage(file = "images/text-message.png")
addnew = PhotoImage(file="images/plus.png")
delete = PhotoImage(file="images/delete_E.png")
recalc = PhotoImage(file="images/recalculate.png")
plus_1 = PhotoImage(file="images/plus_1.png")
minus = PhotoImage(file="images/minus.png")
search_1 = PhotoImage(file="images/search_1.png")
message_1 = PhotoImage(file="images/message_1.png")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3=  ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6=  ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)
tab9 =  ttk.Frame(tabControl)
tab10=  ttk.Frame(tabControl)
tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoices',)
tabControl.add(tab2,image=orders,compound = LEFT, text ='Orders')
tabControl.add(tab3,image=estimates,compound = LEFT, text ='Estimates')
tabControl.add(tab4,image=recurring,compound = LEFT, text ='Recurring')
tabControl.add(tab5,image=purchase,compound = LEFT, text ='Purchase Orders') 
tabControl.add(tab6,image=expenses,compound = LEFT, text ='Expenses')
tabControl.add(tab7,image=customer,compound = LEFT, text ='Customers')
tabControl.add(tab8,image=product,compound = LEFT, text ='Product/Services')
tabControl.add(tab9,image=reports,compound = LEFT, text ='Report')
tabControl.add(tab10,image=setting,compound = LEFT, text ='Settings')
tabControl.pack(expand = 1, fill ="both")


selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")

right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
remove = PhotoImage(file="images/eraser.png")


photo = PhotoImage(file = "images/plus.png")
photo1 = PhotoImage(file = "images/edit.png")
photo2 = PhotoImage(file = "images/delete_E.png")
photo3 = PhotoImage(file = "images/export-file.png")
photo4 = PhotoImage(file = "images/seo.png")
photo5 = PhotoImage(file = "images/printer.png")
photo6 = PhotoImage(file = "images/gmail.png")
photo7 = PhotoImage(file = "images/priewok.png")
photo8 = PhotoImage(file = "images/refresh_E.png")
photo9 = PhotoImage(file = "images/sum.png")
photo10 = PhotoImage(file = "images/text-message.png")

def inv_create():
  pop=Toplevel(inv_midFrame)
  pop.title("Invoice")
  pop.geometry("950x690+150+0")

  def add_new_invoice():
    invoice_number = inv_number_entry.get()
    invodate = inv_date_entry.get_date()
    duedate = inv_duedate_entry.get_date()
    term_of_payment = inv_terms_combo.get()
    ref = inv_ref_entry.get()
    status = draft_label.cget("text")
    emailon = never1_label.cget("text")
    printon = never2_label.cget("text")
    # smson = 
    invoicetot = invoicetot1.cget("text")
    totpaid = total1.cget("text")
    balance = balance1.cget("text")
    extracostname = ex_costn_combo.get()
    extracost = ex_cost_entry.get()
    template = template_entry.get()
    salesper = sales_per_entry.get()
    discourate = dis_rate_entry.get()
    tax1 = tax1_entry.get()
    category = category_entry.get()
    businessname = inv_combo_e1.get()
    businessaddress = inv_addr_e2.get("1.0",END)
    shipname = inv_shipto_e3.get()
    shipaddress = inv_addr_e4.get("1.0",END)
    cpemail = inv_email_e5.get()
    cpmobileforsms = inv_sms_e6.get()
    recurring_period = recur_period_entry.get()
    recurring_period_month = recur_month_combo.get()
    next_invoice = recur_nxt_inv_date.get_date()
    stop_recurring = recur_stop_date.get_date()

    # cust_sql = "SELECT customerid FROM customer WHERE businessname=%s"
    # cust_val = (businessname,)
    # fbcursor.execute(cust_sql,cust_val)
    # cust_data = fbcursor.fetchone()
    # customerid = cust_data

    # pro_sql = "SELECT Productserviceid FROM storingproduct WHERE invoice_number=%s"
    # pro_val = (invoice_number,)
    # fbcursor.execute(pro_sql,pro_val)
    # pro_data = fbcursor.fetchone()
    # productserviceid = pro_data

    discount = dis_rate_entry.get()

    inv_sql='INSERT INTO Invoice (invoice_number,invodate,duedate,term_of_payment,ref,status,emailon,printon,invoicetot,totpaid,balance,extracostname,extracost,template,salesper,discourate,tax1,category,businessname,businessaddress,shipname,shipaddress,cpemail,cpmobileforsms,recurring_period,recurring_period_month,next_invoice,stop_recurring,discount) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' #adding values into db
    inv_val=(invoice_number,invodate,duedate,term_of_payment,ref,status,emailon,printon,invoicetot,totpaid,balance,extracostname,extracost,template,salesper,discourate,tax1,category,businessname,businessaddress,shipname,shipaddress,cpemail,cpmobileforsms,recurring_period,recurring_period_month,next_invoice,stop_recurring,discount)
    fbcursor.execute(inv_sql,inv_val)
    fbilldb.commit()

  #select customer
  def inv_sel_customer():
    global customer_selection
    customer_selection=Toplevel()
    customer_selection.title("Select Customer")
    customer_selection.geometry("930x650+240+10")
    customer_selection.resizable(False, False)

    global select_cust_tree

    select_cust_tree=ttk.Treeview(customer_selection, height=27)
    select_cust_tree["columns"]=["1","2","3","4"]
    select_cust_tree.column("#0", width=35)
    select_cust_tree.column("1", width=160)
    select_cust_tree.column("2", width=160)
    select_cust_tree.column("3", width=140)
    select_cust_tree.column("4", width=140)
    select_cust_tree.heading("#0",text="")
    select_cust_tree.heading("1",text="Customer/Ventor ID")
    select_cust_tree.heading("2",text="Customer/Ventor Name")
    select_cust_tree.heading("3",text="Tel.")
    select_cust_tree.heading("4",text="Contact Person")
    select_cust_tree.place(x=5, y=45)

    sql_sel_cust = "SELECT * FROM Customer"
    fbcursor.execute(sql_sel_cust)
    customer_details = fbcursor.fetchall()

    count=0
    for i in customer_details:
      if True:
        select_cust_tree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
      else:
        pass
    count += 1


    def cust_tree_fetch():
      cust_tree_item = select_cust_tree.item(select_cust_tree.focus())["values"][0]
      sql = "SELECT * FROM Customer WHERE customerid=%s"
      val = (cust_tree_item,)
      fbcursor.execute(sql,val)
      sel_cust_str = fbcursor.fetchone()
      inv_combo_e1.delete(0, END)
      inv_combo_e1.insert(0,sel_cust_str[4])
      inv_addr_e2.delete('1.0',END)
      inv_addr_e2.insert('1.0',sel_cust_str[5])
      inv_shipto_e3.delete(0, END)
      inv_shipto_e3.insert(0, sel_cust_str[6])
      inv_addr_e4.delete('1.0',END)
      inv_addr_e4.insert('1.0',sel_cust_str[7])
      inv_email_e5.delete(0,END)
      inv_email_e5.insert(0,sel_cust_str[9])
      inv_sms_e6.delete(0,END)
      inv_sms_e6.insert(0,sel_cust_str[12])

      customer_selection.destroy()
    
    

    
    # filter customers

    def filter_customer():
      if cust_filter_entry.get() == '':
        sql = "SELECT * FROM Customer"
        fbcursor.execute(sql,)
        customer_details = fbcursor.fetchall()
        for record in select_cust_tree.get_children():
          select_cust_tree.delete(record)

        count = 0
        for i in customer_details:
          if True:
            select_cust_tree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
          else:
            pass
        count += 1
      else:
        filter = cust_filter_entry.get()
        for record in select_cust_tree.get_children():
          select_cust_tree.delete(record)

        sql = "SELECT * FROM Customer WHERE businessname=%s"
        val = (filter, )
        fbcursor.execute(sql, val)
        customer_details = fbcursor.fetchall()

    
        count=0
        for i in customer_details:
          if True:
            select_cust_tree.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[10],i[8]))  
          else:
            pass
        count += 1
  

    cust_filter_label=Label(customer_selection, text="Enter filter text").place(x=5, y=10)
    cust_filter_entry=Entry(customer_selection, width=20)
    cust_filter_entry.place(x=110, y=10)
    cust_filter_button=Button(customer_selection, text='Click Here',command=filter_customer)
    cust_filter_button.place(x=240, y=9,height=20,width=60)




    #add new customer
    def inv_create_newcustomer():
      global checkvar1,checkvar2,cust_id,bus_name,bus_address,cat,ship_name,ship_address,cont_person,cont_email,cont_tel,cont_fax,cont_mob,shipcont_person,shipcont_email,shipcont_tel,shipcont_fax,cont_country,cont_city,cont_notes
      ven=Toplevel(inv_midFrame)
      ven.title("Add new vendor")
      ven.geometry("930x650+240+10")
      checkvar1=IntVar()
      checkvar2=IntVar()
      radio=IntVar()
      create_cust_frame=Frame(ven, bg="#f5f3f2", height=650)
      create_cust_frame.pack(side="top", fill="both")
      labelframe1 = LabelFrame(create_cust_frame,text="Customer",bg="#f5f3f2",font=("arial",15))
      labelframe1.place(x=10,y=5,width=910,height=600)
      customer_id=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
      cust_id=Entry(labelframe1,width=25).place(x=150,y=10)
      category=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
      cat=ttk.Combobox(labelframe1,width=25,value="Default").place(x=460 ,y=10)
      status=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
      Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
      
      labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
      labelframe2.place(x=5,y=40,width=420,height=150)
      bname = Label(labelframe2, text="Business name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
      bus_name = Entry(labelframe2,width=28).place(x=130,y=5)
      baddress = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
      bus_address = Entry(labelframe2,width=28).place(x=130,y=40,height=80)
      
      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

      labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
      labelframe3.place(x=480,y=40,width=420,height=150)
      sname = Label(labelframe3, text="Ship to name:",bg="#f5f3f2").place(x=5,y=5)
      ship_name = Entry(labelframe3,width=28).place(x=130,y=5)
      saddress = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
      ship_address = Entry(labelframe3,width=28).place(x=130,y=40,height=80)
      
      labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe4.place(x=5,y=195,width=420,height=150)
      cname = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      cont_person = Entry(labelframe4,width=28).place(x=130,y=5)
      cemail = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
      cont_email = Entry(labelframe4,width=28).place(x=130,y=35)
      ctel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      cont_tel = Entry(labelframe4,width=11).place(x=130,y=65)
      cfax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      cont_fax = Entry(labelframe4,width=11).place(x=280,y=65)
      csms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
      cont_mob = Entry(labelframe4,width=15).place(x=248,y=95)      

      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

      
      labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
      labelframe5.place(x=480,y=195,width=420,height=125)
      scname = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      shipcont_person = Entry(labelframe5,width=28).place(x=130,y=5)
      scemail = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
      shipcont_email = Entry(labelframe5,width=28).place(x=130,y=35)
      sctel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      shipcont_tel = Entry(labelframe5,width=11).place(x=130,y=65)
      scfax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      shipcont_fax = Entry(labelframe5,width=11).place(x=280,y=65)

      labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe6.place(x=5,y=350,width=420,height=100)
      Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
      tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
      e1 = Entry(labelframe6,width=10).place(x=290,y=5)
      discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe6,width=10).place(x=100,y=35)

      labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe7.place(x=480,y=330,width=420,height=100)
      country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
      cont_country = Entry(labelframe7,width=28).place(x=130,y=5)
      city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
      cont_city = Entry(labelframe7,width=28).place(x=130,y=35)

      labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
      labelframe8.place(x=5,y=460,width=420,height=100)
      R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
      R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
      R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
      

      labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
      labelframe9.place(x=480,y=430,width=420,height=150)
      cont_notes = Entry(labelframe9).place(x=10,y=10,height=100,width=390)

      btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK").place(x=20, y=615)
      btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
    
    


    cust_fil_cat_tree=ttk.Treeview(customer_selection, height=27)
    cust_fil_cat_tree["columns"]=["1"]
    cust_fil_cat_tree.column("#0", width=25, minwidth=20)
    cust_fil_cat_tree.column("1", width=217, minwidth=25, anchor=CENTER)    
    cust_fil_cat_tree.heading("#0",text="", anchor=W)
    cust_fil_cat_tree.heading("1",text="View filter by category", anchor=CENTER)
    cust_fil_cat_tree.place(x=660, y=45)

    #filter customer
    def list_filter_customer(event):
      selected_cust_indices = cust_fil_cat_list.curselection()
      selected_cust_filter = ",".join([cust_fil_cat_list.get(i) for i in selected_cust_indices])

      if selected_cust_filter == "               View all records" or selected_cust_filter == "               View only Client/Vendor" or selected_cust_filter == "               Default":
        cust_all_sql = "SELECT * FROM Customer"
        fbcursor.execute(cust_all_sql)
        cust_all_data = fbcursor.fetchall()
        for record in select_cust_tree.get_children():
          select_cust_tree.delete(record)
        count_all = 0
        for i in cust_all_data:
          select_cust_tree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
        count_all += 1
      elif selected_cust_filter == "               View only Client type":
        client_sql = "SELECT * FROM Customer WHERE customertype=%s"
        client_val = ('Client',)
        fbcursor.execute(client_sql,client_val)
        client_data = fbcursor.fetchall()
        for record in select_cust_tree.get_children():
          select_cust_tree.delete(record)
        count_c = 0
        for i in client_data:
          select_cust_tree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
        count_c += 1
      else:
        vendor_sql = "SELECT * FROM Customer WHERE customertype=%s"
        vendor_val = ('Vendor',)
        fbcursor.execute(vendor_sql,vendor_val)
        vendor_data = fbcursor.fetchall()
        for record in select_cust_tree.get_children():
          select_cust_tree.delete(record)
        count_v = 0
        for i in vendor_data:
          select_cust_tree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
        count_v += 1

    cust_fil_cat_list = Listbox(customer_selection,height=34,width=40,bg="white",activestyle="dotbox",fg="black",highlightbackground="white")
    cust_fil_cat_list.insert(0,"               View all records")
    cust_fil_cat_list.insert(1,"               View only Client/Vendor")
    cust_fil_cat_list.insert(2,"               View only Client type")
    cust_fil_cat_list.insert(3,"               View only Vendor type")
    cust_fil_cat_list.insert(4,"               Default")
    cust_fil_cat_list.place(x=660,y=63)
    cust_fil_cat_list.bind('<<ListboxSelect>>',list_filter_customer)


    scrollbar = Scrollbar(customer_selection)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=select_cust_tree.yview )

    ok_btn=Button(customer_selection,compound = LEFT,image=tick ,text="ok", width=60,command=cust_tree_fetch).place(x=15, y=610)
    edit_btn=Button(customer_selection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=inv_create_newcustomer).place(x=250, y=610)
    add_btn=Button(customer_selection,compound = LEFT,image=tick, text="Add new customer", width=150,command=inv_create_newcustomer).place(x=435, y=610)
    cancel_btn=Button(customer_selection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)   



    

  #add new line item
  def inv_newline():
    #fetch new line item
    def product_tree_fetch():
      global sel_pro_str
      product_tree_item = product_sel_tree.item(product_sel_tree.focus())["values"][0]
      sql = "SELECT * FROM Productservice WHERE Productserviceid=%s"
      val = (product_tree_item,)
      fbcursor.execute(sql,val)
      sel_pro_str = fbcursor.fetchone()
      add_newline_tree.insert(parent='',index='end',iid=sel_pro_str,text='',values=(sel_pro_str[0],sel_pro_str[4],sel_pro_str[5],sel_pro_str[7],sel_pro_str[18]))
      inv_newline_sel.destroy()
    show_newline = inv_combo_e1.get()
    if show_newline == '':
      messagebox.showinfo('F-Billing Revolution','Customer is required, please select customer before adding line item to invoice')
    else:
      inv_newline_sel=Toplevel()
      inv_newline_sel.title("Product/Services")
      inv_newline_sel.geometry("930x650+240+10")
      inv_newline_sel.resizable(False, False)

      global product_sel_tree

      product_sel_tree=ttk.Treeview(inv_newline_sel, height=27)
      product_sel_tree["columns"]=["1","2","3", "4","5"]
      product_sel_tree.column("#0", width=35)
      product_sel_tree.column("1", width=160)
      product_sel_tree.column("2", width=160)
      product_sel_tree.column("3", width=140)
      product_sel_tree.column("4", width=70)
      product_sel_tree.column("5", width=70)
      product_sel_tree.heading("#0",text="")
      product_sel_tree.heading("1",text="ID/SKU")
      product_sel_tree.heading("2",text="Product/Service Name")
      product_sel_tree.heading("3",text="Unit price")
      product_sel_tree.heading("4",text="Service")
      product_sel_tree.heading("5",text="Stock")
      product_sel_tree.place(x=5, y=45)

      sql = "SELECT * FROM Productservice"
      fbcursor.execute(sql)
      product_details = fbcursor.fetchall()

      count = 0
      for p in product_details:
        if True:
          product_sel_tree.insert(parent='',index='end',iid=p,text='',values=(p[0],p[4],p[7],p[12],p[13]))
        else:
          pass
      count += 1
    
    #filter product

    def filter_product():
      if product_filter_entry.get() == '':
        sql = "SELECT * FROM Productservice"
        fbcursor.execute(sql)
        product_details = fbcursor.fetchall()
        for record in product_sel_tree.get_children():
          product_sel_tree.delete(record)

        count = 0
        for p in product_details:
          if True:
            product_sel_tree.insert(parent='',index='end',iid=p,text='',values=(p[0],p[4],p[7],p[12],p[13]))
          else:
            pass
        count += 1

      else:
        filter = product_filter_entry.get()
        for record in product_sel_tree.get_children():
          product_sel_tree.delete(record)
        
        sql = "SELECT * FROM Productservice WHERE name=%s"
        val = (filter, )
        fbcursor.execute(sql, val)
        records = fbcursor.fetchall()
  
    
        count=0
        for i in records:
          if True:
            product_sel_tree.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[10],i[8]))  
          else:
            pass
        count += 1



    product_filter_label=Label(inv_newline_sel, text="Enter filter text").place(x=5, y=10)
    product_filter_entry=Entry(inv_newline_sel, width=20)
    product_filter_entry.place(x=110, y=10)
    product_filter_button=Button(inv_newline_sel, text='Click Here',command=filter_product)
    product_filter_button.place(x=240, y=9,height=20,width=60)

      


    #add new product
    def new_product():  
      top = Toplevel()  
      top.title("Add a new Product/Service")
      p2 = PhotoImage(file = 'images/fbicon.png')
      top.iconphoto(False, p2)
      top.geometry("700x550+390+15")
      tabControl = ttk.Notebook(top)
      s = ttk.Style()
      s.theme_use('default')
      s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)
          

      tab1 = ttk.Frame(tabControl)
      tab2 = ttk.Frame(tabControl)
     
      tabControl.add(tab1,compound = LEFT, text ='Product/Service')
      tabControl.add(tab2,compound = LEFT, text ='Product Image')
     
      tabControl.pack(expand = 1, fill ="both")
     
      innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
      innerFrame.pack(side="top",fill=BOTH)

      Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
      Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

      add_pro_code_label=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
      add_pro_code_label.place(x=20,y=0)
      add_pro_code_entry = Entry(Customerlabelframe,width=35)
      add_pro_code_entry.place(x=120,y=8)

      checkvarStatus=IntVar()
      add_pro_status=Label(Customerlabelframe,text="Status:")
      add_pro_status.place(x=500,y=8)
      add_pro_checkbtn_active = Checkbutton(Customerlabelframe,
                        variable = checkvarStatus,text="Active",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                       
                        width = 10)

      add_pro_checkbtn_active.place(x=550,y=5)

      add_pro_cat=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
      add_pro_cat.place(x=20,y=40)
      n = StringVar()
      add_pro_country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
       
      add_pro_country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
      
      add_pro_country.place(x=120,y=45)
      add_pro_country.current(0)


      add_pro_name_label=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
      add_pro_name_label.place(x=20,y=70)
      add_pro_name_entry = Entry(Customerlabelframe,width=60)
      add_pro_name_entry.place(x=120,y=75)

      add_pro_des_label=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
      add_pro_des_label.place(x=20,y=100)
      add_pro_des_entry = Entry(Customerlabelframe,width=60)
      add_pro_des_entry.place(x=120,y=105)

      uval = IntVar(Customerlabelframe, value='$0.00')
      add_pro_unit_label=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
      add_pro_unit_label.place(x=20,y=130)
      add_pro_unit_entry = Entry(Customerlabelframe,width=20,textvariable=uval)
      add_pro_unit_entry.place(x=120,y=135)

      pcsval = IntVar(Customerlabelframe, value='$0.00')
      add_pro_pcs_label=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
      add_pro_pcs_label.place(x=320,y=140)
      add_pro_pcs_entry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
      add_pro_pcs_entry.place(x=410,y=140)

      costval = IntVar(Customerlabelframe, value='$0.00')
      add_pro_cost_label=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
      add_pro_cost_label.place(x=20,y=160)
      add_pro_cost_entry = Entry(Customerlabelframe,width=20,textvariable=costval)
      add_pro_cost_entry.place(x=120,y=165)

      priceval = IntVar(Customerlabelframe, value='$0.00')
      add_pro_price_label=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
      add_pro_price_label.place(x=20,y=190)
      add_pro_price_entry = Entry(Customerlabelframe,width=20,textvariable=priceval)
      add_pro_price_entry.place(x=120,y=195)

      checkvarStatus2=IntVar()
     
      add_pro_checkbtn_tax = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                        text="Taxable Tax1rate",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                        height=2,
                        width = 12)

      add_pro_checkbtn_tax.place(x=415,y=170)


      checkvarStatus3=IntVar()
     
      add_pro_checkbtn_no = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                        text="No stock Control",
                        onvalue =1 ,
                        offvalue = 0,
                        height=3,
                        width = 15)

      add_pro_checkbtn_no.place(x=40,y=220)


      stockval = IntVar(Customerlabelframe)
      add_pro_stock_label=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
      add_pro_stock_label.place(x=90,y=260)
      add_pro_stock_entry = Entry(Customerlabelframe,width=15,textvariable=stockval)
      add_pro_stock_entry.place(x=150,y=265)

      lowval = IntVar(Customerlabelframe)
      add_pro_low_label=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
      add_pro_low_label.place(x=300,y=260)
      add_pro_low_entry = Entry(Customerlabelframe,width=10,textvariable=lowval)
      add_pro_low_entry.place(x=495,y=265)

     
      add_pro_ware_label=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
      add_pro_ware_label.place(x=60,y=290)
      add_pro_ware_entry = Entry(Customerlabelframe,width=50)
      add_pro_ware_entry.place(x=150,y=295)

      add_pro_pnote_label=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
      add_pro_pnote_label.place(x=20,y=330)

      add_pro_pnote_scroll = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
      add_pro_pnote_scroll.place(x=32,y=358)

      def add_new_product():
        sku = add_pro_code_entry.get()
        category = add_pro_country.get()
        name = add_pro_name_entry.get()
        description = add_pro_des_entry.get()
        unitprice = add_pro_unit_entry.get()
        peices = add_pro_pcs_entry.get()
        cost = add_pro_cost_entry.get()
        priceminuscost = add_pro_price_entry.get()
        stock = add_pro_stock_entry.get()
        stocklimit = add_pro_low_entry.get()
        warehouse = add_pro_ware_entry.get()
        privatenote = add_pro_pnote_scroll.get("1.0",'end-1c')
        status = checkvarStatus.get()
        taxable = checkvarStatus2.get()
        serviceornot = checkvarStatus3.get()
        sql='INSERT INTO Productservice (sku,category,name,description,unitprice,peices,cost,priceminuscost,stock,stocklimit,warehouse,privatenote,status,taxable,serviceornot) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' #adding values into db
        val=(sku,category,name,description,unitprice,peices,cost,priceminuscost,stock,stocklimit,warehouse,privatenote,status,taxable,serviceornot)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        top.destroy()
        messagebox.showinfo("F-Billing Revolution","Product registered successfully")

      # Cancel add new product
      def cancel_add():
        top.destroy()

      add_pro_ok_btn = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60,command=add_new_product)
      add_pro_ok_btn.pack(side=LEFT)

      add_pro_cancel_btn = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60,command=cancel_add)
      add_pro_cancel_btn.pack(side=RIGHT)

      imageFrame = Frame(tab2, relief=GROOVE,height=580)
      imageFrame.pack(side="top",fill=BOTH)

      browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
      browseimg.place(x=15,y=35)

      browsebutton=Button(imageFrame,text = 'Browse')
      browsebutton.place(x=580,y=30,height=30,width=50)
      
      removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
      removeButton.place(x=400,y=450)


    pro_fil_cat_tree=ttk.Treeview(inv_newline_sel, height=27)
    pro_fil_cat_tree["columns"]=["1"]
    pro_fil_cat_tree.column("#0", width=35, minwidth=20)
    pro_fil_cat_tree.column("1", width=205, minwidth=25, anchor=CENTER)    
    pro_fil_cat_tree.heading("#0",text="", anchor=W)
    pro_fil_cat_tree.heading("1",text="View filter by category", anchor=CENTER)
    pro_fil_cat_tree.place(x=660, y=45)


    def list_filter_product(evet):
      selected_indices = pro_fil_cat_list.curselection()
      selected_filter = ",".join([pro_fil_cat_list.get(i) for i in selected_indices])

      if selected_filter == "               View all Products/Services" or selected_filter == "               Default":
        pro_ser_sql = "SELECT * FROM Productservice"
        fbcursor.execute(pro_ser_sql)
        pro_ser_data = fbcursor.fetchall()
        for record in product_sel_tree.get_children():
          product_sel_tree.delete(record)
        count_ps = 0
        for i in pro_ser_data:
          product_sel_tree.insert(parent='',index='end',iid=i,text='',values=(i[2],i[4],i[7],i[12],i[13]))
        count_ps += 1
      elif selected_filter == "               View all Products":
        pro_sql = "SELECT * FROM Productservice WHERE serviceornot=%s"
        pro_val = ('0',)
        fbcursor.execute(pro_sql,pro_val)
        pro_data = fbcursor.fetchall()
        for record in product_sel_tree.get_children():
          product_sel_tree.delete(record)
        count_p = 0
        for i in pro_data:
          product_sel_tree.insert(parent='', index='end', iid=i, text='', values=(i[2],i[4],i[7],i[12],i[13]))
        count_p += 1
      elif selected_filter == "               View all Services":
        ser_sql = "SELECT * FROM Productservice WHERE serviceornot=%s"
        ser_val = ('1',)
        fbcursor.execute(ser_sql,ser_val)
        ser_data = fbcursor.fetchall()
        for record in product_sel_tree.get_children():
          product_sel_tree.delete(record)
        count_s = 0
        for i in ser_data:
          product_sel_tree.insert(parent='', index='end', iid=i, text='', values=(i[2],i[4],i[7],i[12],i[13]))
        count_s += 1


    pro_fil_cat_list = Listbox(inv_newline_sel,height=34,width=40,bg="white",activestyle="dotbox",fg="black",highlightbackground="white")
    pro_fil_cat_list.insert(0,"               View all Products/Services")
    pro_fil_cat_list.insert(1,"               View all Products")
    pro_fil_cat_list.insert(2,"               View all Services")
    pro_fil_cat_list.insert(3,"               Default")
    pro_fil_cat_list.place(x=660,y=63)
    pro_fil_cat_list.bind('<<ListboxSelect>>',list_filter_product)

    scrollbar = Scrollbar(inv_newline_sel)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=add_newline_tree.yview )
   

    product_ok_btn=Button(inv_newline_sel,compound = LEFT,image=tick ,text="ok", width=60,command=product_tree_fetch).place(x=15, y=610)
    product_edit_btn=Button(inv_newline_sel,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=product).place(x=250, y=610)
    product_add_btn=Button(inv_newline_sel,compound = LEFT,image=tick , text="Add product/Service", width=150,command=new_product)
    product_add_btn.place(x=435, y=610)
    product_cancel_btn=Button(inv_newline_sel,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)



  #preview new line
  def previewline():
    messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")


  
  #sms notification
  def sms1():
    send_SMS=Toplevel()
    send_SMS.geometry("700x480+240+150")
    send_SMS.title("Send SMS notification")

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    sms_Notebook = ttk.Notebook(send_SMS)
    SMS_Notification = Frame(sms_Notebook, height=470, width=700)
    SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
    sms_Notebook.add(SMS_Notification, text="SMS Notification")
    sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
    sms_Notebook.place(x=0, y=0)

    numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
    numlbel.place(x=10, y=10)
    numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
    stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
    stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
    
    dclbel=Label(SMS_Notification, text="Double click to insert into text")
    dclbel.place(x=410, y=60)
    dcl=Entry(SMS_Notification, width=30)
    dcl.place(x=400, y=85,height=200)
    
    smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
    smstype.place(x=10, y=223)
    snuvar=IntVar()
    normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
    unicode_rbtn.place(x=190, y=5)
    tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
    tiplbf.place(x=10, y=290)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
    tiplabl.place(x=5, y=5)

    btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
    btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
    btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
    

    smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
    smstype.place(x=10, y=5)
    snumvar=IntVar()
    normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
    unicode_rbtn.place(x=290, y=5)

    sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
    sms1type.place(x=10, y=80)
    name=Label(sms1type, text="Username").place(x=10, y=5)
    na=Entry(sms1type, width=20).place(x=100, y=5)
    password=Label(sms1type, text="Password").place(x=10, y=45)
    pas=Entry(sms1type, width=20).place(x=100, y=45)
    combo=Label(sms1type, text="Route").place(x=400, y=5)
    n = StringVar()
    combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
    btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

    
    tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
    tiplbf.place(x=10, y=190)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
    tiplabl.place(x=0, y=5)
    tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
    tiplabl1.place(x=0, y=60)
    tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
    tiplabl2.place(x=0, y=100)
    tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
    tiplabl3.place(x=0, y=140)
    checkvar1=IntVar()
    chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 

  #mark invoice
  def markinvo():
    mark_inv=Toplevel()
    mark_inv.geometry("700x480+240+150")
    mark_inv.title("Record Payement for Invoice")
    checkvar=IntVar()
    checkvar1=IntVar()
    checkvar2=IntVar()

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    mark_Notebook = ttk.Notebook(mark_inv)
    Mark_Invoice = Frame(mark_Notebook, height=470, width=750)
    mark_Notebook.add(Mark_Invoice, text="Mark Invoice")
    mark_Notebook.place(x=0, y=0)

    involbel=Label(Mark_Invoice, text="Invoice Balance")
    involbel.place(x=10, y=10)
    numentry=Entry(Mark_Invoice, width=45).place(x=130, y=10)

    labelframe5 = LabelFrame(Mark_Invoice,text="Payement Record Details",bg="#f5f3f2")
    labelframe5.place(x=10,y=60,width=670,height=250)
    e1 = Entry(labelframe5,width=28).place(x=30,y=45)
    pdate = Label(labelframe5, text="Payement Date:",bg="#f5f3f2").place(x=250,y=20)
    e2 = Entry(labelframe5,width=28).place(x=220,y=45)
    payd = Label(labelframe5, text="Paid By:",bg="#f5f3f2").place(x=450,y=20)
    drop = ttk.Combobox(labelframe5, value="Hello")
    drop.place(x=450,y=45)
    involbel=Label(labelframe5, text="Description")
    involbel.place(x=30, y=80)
    numentry=Entry(labelframe5, width=100).place(x=30, y=120)
    Checkbutton(labelframe5,text="Paid in full and close invoice",variable=checkvar,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=30 ,y=150)
    pl = Label(labelframe5,text="Payement Reciepts",bg="#f5f3f2")
    pl.place(x=300,y=145)
    Checkbutton(labelframe5,text="Send Payement Reciept",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=320 ,y=170)
    Checkbutton(labelframe5,text="Attach updated invoice",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=320 ,y=200)

    okbtn=Button(Mark_Invoice,compound = LEFT,image=tick , text="Save payement", width=100).place(x=10, y=350)
    canbtn=Button(Mark_Invoice,compound = LEFT,image=cancel, text="Cancel", width=100).place(x=500, y=350)

    
  #voidinvoice
  def voidinvoice():
    void_msg = messagebox.askyesno("F-Billing Revolution","Are you sure to avoid this invoice?\nAll products will be placed back into stock and all payemnts will be voided.")
    if void_msg == YES:
      select_customer_btn['state'] = DISABLED
      add_newline_btn['state'] = DISABLED
      del_line_item_btn['state'] = DISABLED
      mark_inv_paid['state'] = DISABLED
      void_invoice['state'] = DISABLED
      save_invoice['state'] = DISABLED
      inv_combo_e1['state'] = DISABLED
      inv_addr_e2['state'] = DISABLED
      inv_shipto_e3['state'] = DISABLED
      inv_addr_e4['state'] = DISABLED
      inv_email_e5['state'] = DISABLED
      inv_sms_e6['state'] = DISABLED
      inv_number_entry['state'] = DISABLED
      inv_date_entry['state'] = DISABLED
      inv_duedate_entry['state'] = DISABLED
      inv_terms_combo['state'] = DISABLED
      inv_ref_entry['state'] = DISABLED
      ex_costn_combo['state'] = DISABLED
      dis_rate_entry['state'] = DISABLED
      ex_cost_entry['state'] = DISABLED
      tax1_entry['state'] = DISABLED
      template_entry['state'] = DISABLED
      draft_label.config(text="Void")
      if draft_label['text'] == "Void":
        num = inv_number_entry.get()
        sql = "UPDATE Invoice SET status='Void' WHERE invoice_number=%s"
        val = (num,)
        fbcursor.execute(sql,val)
        fbilldb.commit()

      if checkrecStatus is not None:
        checkrecStatus.set(0)
      else:
        checkrecStatus.set(0)
      recur_check_btn['state'] = DISABLED
      recur_period_entry['state'] = DISABLED
      recur_month_combo['state'] = DISABLED
      recur_nxt_inv_date['state'] = DISABLED
      recur_stop_check['state'] = DISABLED
      recur_stop_date['state'] = DISABLED
      recur_recalc['state'] = DISABLED
      pay_plus['state'] = DISABLED
      pay_minus['state'] = DISABLED
      title_txt_combo['state'] = DISABLED
      pageh_txt_combo['state'] = DISABLED
      footer_txt_combo['state'] = DISABLED
      term_txt['state'] = DISABLED
      comment_txt['state'] = DISABLED
      doc_plus_btn['state'] = DISABLED
      doc_minus_btn['state'] = DISABLED
    else:
      pass



  
  #delete line item  
  def delete_line_item():
    selected_line_item = add_newline_tree.selection()[0]
    add_newline_tree.delete(selected_line_item)
    
    

  inv_first_frame=Frame(pop, bg="#f5f3f2", height=60)
  inv_first_frame.pack(side="top", fill=X)

  w = Canvas(inv_first_frame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  select_customer_btn = Button(inv_first_frame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=inv_sel_customer)
  select_customer_btn.pack(side="left", pady=3, ipadx=4)


  w = Canvas(inv_first_frame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  add_newline_btn= Button(inv_first_frame,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=inv_newline)
  add_newline_btn.pack(side="left", pady=3, ipadx=4)

  del_line_item_btn= Button(inv_first_frame,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=delete_line_item)
  del_line_item_btn.pack(side="left", pady=3, ipadx=4)

  w = Canvas(inv_first_frame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  prev_invoice= Button(inv_first_frame,compound="top", text="Preview\nInvoice",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=previewline)
  prev_invoice.pack(side="left", pady=3, ipadx=4)

  print_invoice= Button(inv_first_frame,compound="top", text="Print \nInvoice",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printsele)
  print_invoice.pack(side="left", pady=3, ipadx=4)

  w = Canvas(inv_first_frame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mail_invoice= Button(inv_first_frame,compound="top", text="Email\nInvoice",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=emailorder)
  mail_invoice.pack(side="left", pady=3, ipadx=4)

  sms_invoice= Button(inv_first_frame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=sms1)
  sms_invoice.pack(side="left", pady=3, ipadx=4)

  w = Canvas(inv_first_frame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mark_inv_paid= Button(inv_first_frame,compound="top", text="Mark invoice\nas 'Paid'",relief=RAISED, image=mark1,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=markinvo)
  mark_inv_paid.pack(side="left", pady=3, ipadx=4)

  void_invoice = Button(inv_first_frame,compound="top", text="Void\ninvoice",relief=RAISED, image=mark2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=voidinvoice)
  void_invoice.pack(side="left", pady=3, ipadx=4)


  w = Canvas(inv_first_frame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  calc= Button(inv_first_frame,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  calc.pack(side="left", pady=3, ipadx=4)

  save_invoice= Button(inv_first_frame,compound="top", text="Save",relief=RAISED, image=tick,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=add_new_invoice)
  save_invoice.pack(side="right", pady=3, ipadx=4)

  inv_first_frame_1=Frame(pop, height=180,bg="#f5f3f2")
  inv_first_frame_1.pack(side="top", fill=X)

  labelframe1 = LabelFrame(inv_first_frame_1,text="Customers",font=("arial",15))
  labelframe1.place(x=10,y=5,width=640,height=160)
  
  def inv_to_combo(event):
    global inv_sel_combo
    inv_to_str = inv_to.get()
    sql = "SELECT * FROM Customer WHERE businessname=%s"
    val = (inv_to_str,)
    fbcursor.execute(sql,val)
    inv_sel_combo = fbcursor.fetchone()
    inv_addr_e2.delete('1.0',END)
    inv_addr_e2.insert('1.0',inv_sel_combo[5])
    inv_shipto_e3.delete(0, END)
    inv_shipto_e3.insert(0, inv_sel_combo[6])
    inv_addr_e4.delete('1.0',END)
    inv_addr_e4.insert('1.0',inv_sel_combo[7])
    inv_email_e5.delete(0,END)
    inv_email_e5.insert(0,inv_sel_combo[9])
    inv_sms_e6.delete(0,END)
    inv_sms_e6.insert(0,inv_sel_combo[12])

  def copy_cust_details():
      inv_shipto_e3.delete(0, END)
      inv_shipto_e3.insert(0, inv_sel_combo[4])
      inv_addr_e4.delete('1.0',END)
      inv_addr_e4.insert('1.0',inv_sel_combo[5])


  sql = "select businessname from Customer"
  fbcursor.execute(sql,)
  pdata = fbcursor.fetchall()

  # global inv_combo_e1,inv_addr_e2,inv_shipto_e3,inv_addr_e4,inv_email_e5,inv_sms_e6,inv_number_entry,inv_date_entry,inv_duedate_entry,inv_terms_combo,inv_ref_entry


  invoice_to = Label(labelframe1, text="Invoice to").place(x=10,y=5)
  inv_to = StringVar()
  inv_combo_e1 = ttk.Combobox(labelframe1,width=28,textvariable=inv_to)
  inv_combo_e1.place(x=80,y=5)
  inv_combo_e1['values'] = pdata
  inv_combo_e1.bind("<<ComboboxSelected>>", inv_to_combo)
  inv_address=Label(labelframe1,text="Address").place(x=10,y=30)
  inv_addr_e2=scrolledtext.Text(labelframe1, undo=True,width=23)
  inv_addr_e2.place(x=80,y=30,height=70)
  inv_ship_to=Label(labelframe1,text="Ship to").place(x=342,y=5)
  inv_shipto_e3=Entry(labelframe1,width=30)
  inv_shipto_e3.place(x=402,y=3)
  inv_address1=Label(labelframe1,text="Address").place(x=340,y=30)
  inv_addr_e4=scrolledtext.Text(labelframe1, undo=True,width=23)
  inv_addr_e4.place(x=402,y=30,height=70)

  inv_copy_cust=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>",command=copy_cust_details)
  inv_copy_cust.place(x=280, y=50)
  
  labelframe2 = LabelFrame(inv_first_frame_1,text="")
  labelframe2.place(x=10,y=130,width=640,height=42)
  inv_email=Label(labelframe2,text="Email").place(x=10,y=5)
  inv_email_e5=Entry(labelframe2,width=30)
  inv_email_e5.place(x=80,y=5)
  inv_sms=Label(labelframe2,text="SMS Number").place(x=328,y=5)
  inv_sms_e6=Entry(labelframe2,width=30)
  inv_sms_e6.place(x=402,y=5)
    
  labelframe = LabelFrame(inv_first_frame_1,text="Invoice",font=("arial",15))
  labelframe.place(x=652,y=5,width=290,height=170)

  fbcursor.execute("SELECT * FROM Invoice ORDER BY invoiceid DESC LIMIT 1")
  inv_number_data = fbcursor.fetchone()

  inv_number_label=Label(labelframe,text="Invoice#").place(x=5,y=5)
  inv_number_entry=Entry(labelframe,width=25)
  inv_number_entry.place(x=100,y=5,)

  inv_number_entry.delete(0,'end')

  def inv_num_increment(inum):
    result = ""
    numberStr = ""
    i = len(inum) - 1
    while i > 0:
      c = inum[i]
      if not c.isdigit():
        break
      numberStr = c + numberStr
      i -= 1
    number = int(numberStr)
    number += 1
    result += inum[0 : i + 1]
    result += "0" if number < 10 else ""
    result += str(number)
    return result
  
  if not inv_number_data == None:
    a = inv_number_data[1]
    inv_no = inv_num_increment(a)
  else:
    inv_no = 1
  inv_number_entry.insert(0,inv_no)

  def inv_due_check():
    if checkvarStatus5.get() == 0:
      inv_duedate_entry['state'] = DISABLED
    else:
      inv_duedate_entry['state'] = NORMAL

  inv_date_label =Label(labelframe,text="Invoice date").place(x=5,y=33)
  inv_date_entry =DateEntry(labelframe,width=15)
  inv_date_entry.place(x=150,y=33)
  checkvarStatus5=IntVar()
  inv_duedate_check=Checkbutton(labelframe,variable = checkvarStatus5,text="Due date",onvalue = 1,offvalue = 0,command=inv_due_check)
  inv_duedate_check.place(x=5,y=62)
  inv_duedate_entry=DateEntry(labelframe,width=15,state=DISABLED)
  inv_duedate_entry.place(x=150,y=62)
  inv_terms_label=Label(labelframe,text="Terms").place(x=5,y=92)
  inv_terms_combo=ttk.Combobox(labelframe, value="",width=23)
  inv_terms_combo.place(x=100,y=92)
  inv_ref_label=Label(labelframe,text="Invoice ref#").place(x=5,y=118)
  inv_ref_entry=Entry(labelframe,width=25)
  inv_ref_entry.place(x=100,y=118)

  fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
  fir2Frame.pack(side="top", fill=X)
  listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
  
  add_newline_tree=ttk.Treeview(listFrame)
  add_newline_tree["columns"]=["1","2","3","4","5","6","7","8"]

  add_newline_tree.column("#0", width=40)
  add_newline_tree.column("1", width=80)
  add_newline_tree.column("2", width=190)
  add_newline_tree.column("3", width=190)
  add_newline_tree.column("4", width=80)
  add_newline_tree.column("5", width=60)
  add_newline_tree.column("6", width=60)
  add_newline_tree.column("7", width=60)
  add_newline_tree.column("8", width=80)
  
  add_newline_tree.heading("#0")
  add_newline_tree.heading("1",text="ID/SKU")
  add_newline_tree.heading("2",text="Product/Service")
  add_newline_tree.heading("3",text="Description")
  add_newline_tree.heading("4",text="Unit Price")
  add_newline_tree.heading("5",text="Quality")
  add_newline_tree.heading("6",text="Pcs/Weight")
  add_newline_tree.heading("7",text="Tax1")
  add_newline_tree.heading("8",text="Price")
  
  add_newline_tree.pack(fill="both", expand=1)
  listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

  fir3Frame=Frame(pop,height=200,width=700,bg="#f5f3f2")
  fir3Frame.place(x=0,y=490)

  tabStyle = ttk.Style()
  tabStyle.theme_use('default')
  tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
  myNotebook=ttk.Notebook(fir3Frame)
  invoiceFrame = Frame(myNotebook, height=200, width=800)
  recurFrame = Frame(myNotebook, height=200, width=800)
  payementFrame = Frame(myNotebook, height=200, width=800)
  headerFrame = Frame(myNotebook, height=200, width=800)
  commentFrame = Frame(myNotebook, height=200, width=800)
  termsFrame = Frame(myNotebook, height=200, width=800)
  noteFrame = Frame(myNotebook, height=200, width=800)
  documentFrame = Frame(myNotebook, height=200, width=800)
  
  myNotebook.add(invoiceFrame,compound="left", text="Invoice")
  myNotebook.add(recurFrame,compound="left", text="Recurring")
  myNotebook.add(payementFrame,compound="left", text="Payements")
  myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
  myNotebook.add(commentFrame,compound="left",  text="Comments")
  myNotebook.add(termsFrame,compound="left", text="Terms")
  myNotebook.add(noteFrame,compound="left",  text="Private notes")
  myNotebook.add(documentFrame,compound="left",  text="Documents")
  myNotebook.pack(expand = 1, fill ="both")  


  def recur_check():
    if checkrecStatus.get() == 0:
      recur_period_entry['state'] = DISABLED
      recur_month_combo['state'] = DISABLED
      recur_nxt_inv_date['state'] = DISABLED
      recur_stop_check['state'] = DISABLED
      recur_stop_date['state'] = DISABLED
      recur_recalc['state'] = DISABLED
    else:
      recur_period_entry['state'] = NORMAL
      recur_month_combo['state'] = NORMAL
      recur_nxt_inv_date['state'] = NORMAL
      recur_stop_check['state'] = NORMAL
      recur_stop_date['state'] = NORMAL
      recur_recalc['state'] = NORMAL


  labelframe1 = LabelFrame(invoiceFrame,text="",font=("arial",15))
  labelframe1.place(x=1,y=1,width=735,height=170)

  # global ex_costn_combo,dis_rate_entry,ex_cost_entry,tax1_entry,template_entry,sales_per_entry,category_entry,draft_label,never1_label,never2_label,title_txt_combo,pageh_txt_combo,footer_txt_combo,private_note_txt,term_txt,comment_txt,discount1,sub1,tax1,cost1,invoicetot1,total1,balance1

  ex_costn_label=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
  ex_costn_combo=ttk.Combobox(labelframe1, value="",width=20)
  ex_costn_combo.place(x=115,y=5)
  dis_rate_label=Label(labelframe1,text="Discount rate").place(x=370,y=5)
  dis_rate_entry=Entry(labelframe1,width=6)
  dis_rate_entry.place(x=460,y=5)
  ex_cost_label=Label(labelframe1,text="Extra cost").place(x=35,y=35)
  ex_cost_entry=Entry(labelframe1,width=10)
  ex_cost_entry.place(x=115,y=35)
  tax1_label=Label(labelframe1,text="Tax1").place(x=420,y=35)
  tax1_entry=Entry(labelframe1,width=7)
  tax1_entry.place(x=460,y=35)
  template_label=Label(labelframe1,text="Template").place(x=37,y=70)
  template_entry=ttk.Combobox(labelframe1, value="",width=25)
  template_entry.place(x=115,y=70)
  sales_per_label=Label(labelframe1,text="Sales Person").place(x=25,y=100)
  sales_per_entry=Entry(labelframe1,width=18)
  sales_per_entry.place(x=115,y=100)
  category_label=Label(labelframe1,text="Category").place(x=300,y=100)
  category_entry=Entry(labelframe1,width=22)
  category_entry.place(x=370,y=100)
  
  statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
  statusfrme.place(x=540,y=0,width=160,height=160)
  draft_label=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey")
  draft_label.place(x=50, y=3)
  email_on_label=Label(statusfrme, text="Emailed on:").place( y=50)
  never1_label=Label(statusfrme, text="Never")
  never1_label.place(x=100,y=50)
  print_on_label=Label(statusfrme, text="Printed on:").place( y=90)
  never2_label=Label(statusfrme, text="Never")
  never2_label.place(x=100,y=90)

  recur_labelframe = LabelFrame(recurFrame,text="",font=("arial",15))
  recur_labelframe.place(x=1,y=1,width=735,height=170)

  # def inv_stop_check():
  #   if checkstopStatus.get() == 0:
  #     recur_stop_date['state'] = NORMAL
  #   else:
  #     recur_stop_date['state'] = DISABLED

  mdata = ["Month(s)","Day(s)"]

  checkrecStatus=IntVar()
  recur_check_btn = Checkbutton(recur_labelframe,variable=checkrecStatus,text="Recurring",onvalue=1,offvalue=0,command=recur_check)
  recur_check_btn.place(x=25,y=20)
  recur_period_label = Label(recur_labelframe,text="Recurring period (interval)").place(x=130,y=45)
  recur_period_entry = Spinbox(recur_labelframe,width=10,state=DISABLED,from_=1,to=10)
  recur_period_entry.place(x=280,y=45)
  recur_month_combo = ttk.Combobox(recur_labelframe,values="",width=15,state=DISABLED)
  recur_month_combo.place(x=360,y=45)
  recur_month_combo['values'] = mdata
  recur_month_combo.set(mdata[0])
  recur_nxt_inv_label = Label(recur_labelframe,text="Next Invoice").place(x=280,y=70)
  recur_nxt_inv_date = DateEntry(recur_labelframe,width=20,state=DISABLED)
  recur_nxt_inv_date.place(x=360,y=70)
  checkstopStatus = IntVar()
  recur_stop_check = Checkbutton(recur_labelframe,variable=checkstopStatus,text="Stop recurring after",onvalue=1,offvalue=0,state=DISABLED)
  recur_stop_check.place(x=225,y=95)
  recur_stop_date = DateEntry(recur_labelframe,width=20,state=DISABLED)
  recur_stop_date.place(x=360,y=95)
  recur_recalc = Button(recur_labelframe,compound=LEFT,image=recalc,text="Recalculate",width=80,height=12,state=DISABLED)
  recur_recalc.place(x=540,y=70)

  pay_labelframe_1 = LabelFrame(payementFrame,text="",font=("arial",15))
  pay_labelframe_1.place(x=1,y=1,width=735,height=170)

  pay_tree = ttk.Treeview(payementFrame,height=6)
  pay_tree["columns"] = ["1","2","3","4","5"]
  pay_tree.column("#0", width=10)
  pay_tree.column("1", width=130)
  pay_tree.column("2", width=130)
  pay_tree.column("3", width=130)
  pay_tree.column("4", width=130)
  pay_tree.column("5", width=130)
  pay_tree.heading("#0", text="",anchor=W)
  pay_tree.heading("1",text="Payment ID")
  pay_tree.heading("2",text="Payment date")
  pay_tree.heading("3",text="Paid by")
  pay_tree.heading("4",text="Description")
  pay_tree.heading("5",text="Amount")
  pay_tree.place(x=45,y=20)

  pay_plus = Button(payementFrame,compound=LEFT,image=plus_1,text="",width=20,height=25)
  pay_plus.place(x=10,y=20)
  pay_minus = Button(payementFrame,compound=LEFT,image=minus,text="",width=20,height=25)
  pay_minus.place(x=10,y=55)
  pay_srch = Button(payementFrame,compound=LEFT,image=photo4,text="",width=20,height=25)
  pay_srch.place(x=10,y=90)
  pay_msg = Button(payementFrame,compound=LEFT,image=photo6,text="",width=20,height=25)
  pay_msg.place(x=10,y=125)


  header_labelframe = LabelFrame(headerFrame,text="",font=("arial",15))
  header_labelframe.place(x=1,y=1,width=735,height=170)

  header_sql = "SELECT headerandfooter FROM header_and_footer"
  fbcursor.execute(header_sql,)
  header_data = fbcursor.fetchall()
  hdata = []
  for i in header_data:
    hdata.append(i[0])

  title_txt_label=Label(header_labelframe,text="Title text").place(x=50,y=5)
  title_txt_combo=ttk.Combobox(header_labelframe, value=hdata,width=60)
  title_txt_combo.place(x=125,y=5)
  title_txt_combo.bind("<<ComboboxSelected>>")
  pageh_txt_label=Label(header_labelframe,text="Page header text").place(x=2,y=45)
  pageh_txt_combo=ttk.Combobox(header_labelframe, value=hdata,width=60)
  pageh_txt_combo.place(x=125,y=45)
  pageh_txt_combo.bind("<<ComboboxSelected>>")
  footer_txt_label=Label(header_labelframe,text="Footer text").place(x=35,y=85)
  footer_txt_combo=ttk.Combobox(header_labelframe, value=hdata,width=60)
  footer_txt_combo.place(x=125,y=85)
  footer_txt_combo.bind("<<ComboboxSelected>>")

  private_labelframe = LabelFrame(noteFrame,text="",font=("arial",15))
  private_labelframe.place(x=1,y=1,width=735,height=170)

  private_label=Label(private_labelframe,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
  private_note_txt=Text(private_labelframe,width=89,height=7).place(x=7,y=32)

  term_labelframe = LabelFrame(termsFrame,text="",font=("arial",15))
  term_labelframe.place(x=1,y=1,width=735,height=170)

  term_txt=Text(term_labelframe,width=89,height=9)
  term_txt.place(x=7,y=10)

  comment_labelframe = LabelFrame(commentFrame,text="",font=("arial",15))
  comment_labelframe.place(x=1,y=1,width=735,height=170)

  comment_txt=Text(comment_labelframe,width=89,height=9)
  comment_txt.place(x=7,y=10)

  doc_labelframe = LabelFrame(documentFrame,text="",font=("arial",15))
  doc_labelframe.place(x=1,y=1,width=735,height=170)

  doc_plus_btn=Button(doc_labelframe,image=plus_1,text="",width=20,height=25)
  doc_plus_btn.place(x=5,y=10)
  doc_minus_btn=Button(doc_labelframe,height=25,width=20,text="",image=minus)
  doc_minus_btn.place(x=5,y=50)
  doc_txt_label=Label(doc_labelframe,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
  doc_tree=ttk.Treeview(doc_labelframe, height=5)
  doc_tree["columns"]=["1","2","3"]
  doc_tree.column("#0", width=20)
  doc_tree.column("1", width=130)
  doc_tree.column("2", width=380)
  doc_tree.column("3", width=130)
  doc_tree.heading("#0",text="", anchor=W)
  doc_tree.heading("1",text="Attach to Email")
  doc_tree.heading("2",text="Filename")
  doc_tree.heading("3",text="Filesize")  
  doc_tree.place(x=50, y=45)
  

  fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
  fir4Frame.place(x=740,y=520)
  summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
  summaryfrme.place(x=0,y=0,width=200,height=170)
  discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
  discount1=Label(summaryfrme, text="$0.00")
  discount1.place(x=130 ,y=0)
  sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
  sub1=Label(summaryfrme, text="$0.00")
  sub1.place(x=130 ,y=21)
  tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
  tax1=Label(summaryfrme, text="$0.00")
  tax1.place(x=130 ,y=42)
  cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
  cost1=Label(summaryfrme, text="$0.00")
  cost1.place(x=130 ,y=63)
  invoicetot=Label(summaryfrme, text="Invoice total").place(x=0 ,y=84)
  invoicetot1=Label(summaryfrme, text="$0.00")
  invoicetot1.place(x=130 ,y=84)
  total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
  total1=Label(summaryfrme, text="$0.00")
  total1.place(x=130 ,y=105)
  balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
  balance1=Label(summaryfrme, text="$0.00")
  balance1.place(x=130 ,y=126)

  fir5Frame=Frame(pop,height=38,width=210)
  fir5Frame.place(x=735,y=485)
  btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
  btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)


###################### End create invoice ####################


def inv_edit_view():
  pop_1=Toplevel(inv_midFrame)
  pop_1.title("Invoice")
  pop_1.geometry("950x690+150+0")
  edit_inv_fetch = inv_tree.item(inv_tree.focus())["values"][1]
  sql_edit = "SELECT * FROM Invoice WHERE invoice_number=%s"
  val_edit = (edit_inv_fetch,)
  fbcursor.execute(sql_edit,val_edit)
  edit_inv_data = fbcursor.fetchone()
  
    # num = inv_number_entry_1.get()
    # sql = "SELECT status FROM invoice WHERE invoice_number=%s"
    # val = (num,)
    # fbcursor.execute(sql,val)
    # status_data = fbcursor.fetchone()
    # print(status_data)
    


  #select customer
  def inv_sel_customer_1():
    customer_selection_1=Toplevel()
    customer_selection_1.title("Select Customer")
    customer_selection_1.geometry("930x650+240+10")
    customer_selection_1.resizable(False, False)

    global select_cust_tree_1

    select_cust_tree_1=ttk.Treeview(customer_selection_1, height=27)
    select_cust_tree_1["columns"]=["1","2","3", "4"]
    select_cust_tree_1.column("#0", width=35)
    select_cust_tree_1.column("1", width=160)
    select_cust_tree_1.column("2", width=160)
    select_cust_tree_1.column("3", width=140)
    select_cust_tree_1.column("4", width=140)
    select_cust_tree_1.heading("#0",text="")
    select_cust_tree_1.heading("1",text="Customer/Ventor ID")
    select_cust_tree_1.heading("2",text="Customer/Ventor Name")
    select_cust_tree_1.heading("3",text="Tel.")
    select_cust_tree_1.heading("4",text="Contact Person")
    select_cust_tree_1.place(x=5, y=45)

    sql = "SELECT * FROM Customer"
    fbcursor.execute(sql)
    customer_details = fbcursor.fetchall()

    count=0
    for i in customer_details:
      if True:
        select_cust_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
      else:
        pass
    count += 1



    def cust_tree_fetch_1():
      cust_tree_item_1 = select_cust_tree_1.item(select_cust_tree_1.focus())["values"][0]
      sql = "SELECT * FROM Customer WHERE customerid=%s"
      val = (cust_tree_item_1,)
      fbcursor.execute(sql,val)
      sel_cust_str_1 = fbcursor.fetchone()
      inv_combo_e1_1.delete(0, END)
      inv_combo_e1_1.insert(0,sel_cust_str_1[4])
      inv_addr_e2_1.delete('1.0',END)
      inv_addr_e2_1.insert('1.0',sel_cust_str_1[5])
      inv_shipto_e3_1.delete(0, END)
      inv_shipto_e3_1.insert(0, sel_cust_str_1[6])
      inv_addr_e4_1.delete('1.0',END)
      inv_addr_e4_1.insert('1.0',sel_cust_str_1[7])
      inv_email_e5_1.delete(0,END)
      inv_email_e5_1.insert(0,sel_cust_str_1[9])
      inv_sms_e6_1.delete(0,END)
      inv_sms_e6_1.insert(0,sel_cust_str_1[12])

      customer_selection_1.destroy()


    #add new customer
    def create1():
      ven=Toplevel(inv_midFrame)
      ven.title("Add new vendor")
      ven.geometry("930x650+240+10")
      checkvar1=IntVar()
      checkvar2=IntVar()
      radio=IntVar()
      createFrame=Frame(ven, bg="#f5f3f2", height=650)
      createFrame.pack(side="top", fill="both")
      labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
      labelframe1.place(x=10,y=5,width=910,height=600)
      text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
      e1=Entry(labelframe1,width=25).place(x=150,y=10)
      text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
      e2=ttk.Combobox(labelframe1,width=25,value="Default").place(x=460 ,y=10)
      text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
      Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
      
      labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
      labelframe2.place(x=5,y=40,width=420,height=150)
      name = Label(labelframe2, text="Business name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
      e1 = Entry(labelframe2,width=28).place(x=130,y=5)
      addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
      e2 = Entry(labelframe2,width=28).place(x=130,y=40,height=80)
      
      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

      labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
      labelframe3.place(x=480,y=40,width=420,height=150)
      name = Label(labelframe3, text="Ship to name:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe3,width=28).place(x=130,y=5)
      addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
      e2 = Entry(labelframe3,width=28).place(x=130,y=40,height=80)
      
      labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe4.place(x=5,y=195,width=420,height=150)
      name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe4,width=28).place(x=130,y=5)
      email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
      e2 = Entry(labelframe4,width=28).place(x=130,y=35)
      tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      e3 = Entry(labelframe4,width=11).place(x=130,y=65)
      fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      e4 = Entry(labelframe4,width=11).place(x=280,y=65)
      sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
      e5 = Entry(labelframe4,width=15).place(x=248,y=95)      

      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

      
      labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
      labelframe5.place(x=480,y=195,width=420,height=125)
      name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe5,width=28).place(x=130,y=5)
      email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe5,width=28).place(x=130,y=35)
      tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      e3 = Entry(labelframe5,width=11).place(x=130,y=65)
      fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      e4 = Entry(labelframe5,width=11).place(x=280,y=65)

      labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe6.place(x=5,y=350,width=420,height=100)
      Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
      tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
      e1 = Entry(labelframe6,width=10).place(x=290,y=5)
      discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe6,width=10).place(x=100,y=35)

      labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe7.place(x=480,y=330,width=420,height=100)
      country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe7,width=28).place(x=130,y=5)
      city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe7,width=28).place(x=130,y=35)

      labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
      labelframe8.place(x=5,y=460,width=420,height=100)
      R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
      R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
      R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
      

      labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
      labelframe9.place(x=480,y=430,width=420,height=150)
      e1 = Entry(labelframe9).place(x=10,y=10,height=100,width=390)

      btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK").place(x=20, y=615)
      btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)


    # filter customers
    
    def filter_customer_1():
      if cust_filter_entry_1.get() == '':
        sql = "SELECT * FROM Customer"
        fbcursor.execute(sql)
        customer_details = fbcursor.fetchall()
        for record in select_cust_tree_1.get_children():
          select_cust_tree_1.delete(record)

        count=0
        for i in customer_details:
          if True:
            select_cust_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
          else:
            pass
        count += 1
      else:
        filter = cust_filter_entry_1.get()
        for record in select_cust_tree_1.get_children():
          select_cust_tree_1.delete(record)

        sql = "SELECT * FROM Customer WHERE businessname=%s"
        val = (filter, )
        fbcursor.execute(sql,val)
        customer_details = fbcursor.fetchall() 

        count = 0
        for i in customer_details:
          if True:
            select_cust_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
          else:
            pass
        count += 1



      
    
    cust_filter_label_1=Label(customer_selection_1, text="Enter filter text").place(x=5, y=10)
    cust_filter_entry_1=Entry(customer_selection_1, width=20)
    cust_filter_entry_1.place(x=110, y=10)
    cust_filter_button_1=Button(customer_selection_1, text="Click Here",command=filter_customer_1)
    cust_filter_button_1.place(x=240, y=9,height=20,width=60)

  

    cust_fil_cat_tree_1=ttk.Treeview(customer_selection_1, height=27)
    cust_fil_cat_tree_1["columns"]=["1"]
    cust_fil_cat_tree_1.column("#0", width=25, minwidth=20)
    cust_fil_cat_tree_1.column("1", width=217, minwidth=25, anchor=CENTER)    
    cust_fil_cat_tree_1.heading("#0",text="", anchor=W)
    cust_fil_cat_tree_1.heading("1",text="View filter by category", anchor=CENTER)
    cust_fil_cat_tree_1.place(x=660, y=45)

    #filter customer
    def list_filter_customer_1(event):
      selected_cust_indices_1 = cust_fil_cat_list_1.curselection()
      selected_cust_filter_1 = ",".join([cust_fil_cat_list_1.get(i) for i in selected_cust_indices_1])

      if selected_cust_filter_1 == "               View all records" or selected_cust_filter_1 == "               View only Client/Vendor" or selected_cust_filter_1 == "               Default":
        cust_all_sql_1 = "SELECT * FROM Customer"
        fbcursor.execute(cust_all_sql_1)
        cust_all_data_1 = fbcursor.fetchall()
        for record in select_cust_tree_1.get_children():
          select_cust_tree_1.delete(record)
        count_all = 0
        for i in cust_all_data_1:
          select_cust_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
        count_all += 1
      elif selected_cust_filter_1 == "               View only Client type":
        client_sql_1 = "SELECT * FROM Customer WHERE customertype=%s"
        client_val_1 = ('Client',)
        fbcursor.execute(client_sql_1,client_val_1)
        client_data_1 = fbcursor.fetchall()
        for record in select_cust_tree_1.get_children():
          select_cust_tree_1.delete(record)
        count_c = 0
        for i in client_data_1:
          select_cust_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
        count_c += 1
      else:
        vendor_sql_1 = "SELECT * FROM Customer WHERE customertype=%s"
        vendor_val_1 = ('Vendor',)
        fbcursor.execute(vendor_sql_1,vendor_val_1)
        vendor_data_1 = fbcursor.fetchall()
        for record in select_cust_tree_1.get_children():
          select_cust_tree_1.delete(record)
        count_v = 0
        for i in vendor_data_1:
          select_cust_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
        count_v += 1





    cust_fil_cat_list_1 = Listbox(customer_selection_1,height=34,width=40,bg="white",activestyle="dotbox",fg="black",highlightbackground="white")
    cust_fil_cat_list_1.insert(0,"               View all records")
    cust_fil_cat_list_1.insert(1,"               View only Client/Vendor")
    cust_fil_cat_list_1.insert(2,"               View only Client type")
    cust_fil_cat_list_1.insert(3,"               View only Vendor type")
    cust_fil_cat_list_1.insert(4,"               Default")
    cust_fil_cat_list_1.place(x=660,y=63)
    cust_fil_cat_list_1.bind('<<ListboxSelect>>',list_filter_customer_1)

    scrollbar = Scrollbar(customer_selection_1)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=select_cust_tree_1.yview )

    ok_btn_1=Button(customer_selection_1,compound = LEFT,image=tick ,text="ok", width=60,command=cust_tree_fetch_1)
    ok_btn_1.place(x=15, y=610)
    edit_btn_1=Button(customer_selection_1,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=create1).place(x=250, y=610)
    add_btn_1=Button(customer_selection_1,compound = LEFT,image=tick, text="Add new customer", width=150,command=create1).place(x=435, y=610)
    cancel_btn_1=Button(customer_selection_1,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)   



    

  #add new line item
  def inv_newline_1():
    #fetch new line item
    def product_tree_fetch_1():
      product_tree_item_1 = product_sel_tree_1.item(product_sel_tree_1.focus())["values"][0]
      sql = "SELECT * FROM Productservice WHERE Productserviceid=%s"
      val = (product_tree_item_1,)
      fbcursor.execute(sql,val)
      sel_pro_str = fbcursor.fetchone()
      add_newline_tree_1.insert(parent='',index='end',iid=sel_pro_str,text='',values=(sel_pro_str[0],sel_pro_str[4],sel_pro_str[5],sel_pro_str[7],sel_pro_str[18]))
      inv_newline_sel_1.destroy()
    show_newline_1 = inv_combo_e1_1.get()
    if show_newline_1 == '':
      messagebox.showinfo('F-Billing Revolution','Customer is required, please select customer before adding line item to invoice')
    else:
      inv_newline_sel_1=Toplevel()
      inv_newline_sel_1.title("Product/Services")
      inv_newline_sel_1.geometry("930x650+240+10")
      inv_newline_sel_1.resizable(False, False)

      global product_sel_tree_1

      product_sel_tree_1=ttk.Treeview(inv_newline_sel_1, height=27)
      product_sel_tree_1["columns"]=["1","2","3", "4","5"]
      product_sel_tree_1.column("#0", width=35)
      product_sel_tree_1.column("1", width=160)
      product_sel_tree_1.column("2", width=160)
      product_sel_tree_1.column("3", width=140)
      product_sel_tree_1.column("4", width=70)
      product_sel_tree_1.column("5", width=70)
      product_sel_tree_1.heading("#0",text="")
      product_sel_tree_1.heading("1",text="ID/SKU")
      product_sel_tree_1.heading("2",text="Product/Service Name")
      product_sel_tree_1.heading("3",text="Unit price")
      product_sel_tree_1.heading("4",text="Service")
      product_sel_tree_1.heading("5",text="Stock")
      product_sel_tree_1.place(x=5, y=45)

      sql = "SELECT * FROM Productservice"
      fbcursor.execute(sql)
      product_details = fbcursor.fetchall()

      count = 0
      for p in product_details:
        if True:
          product_sel_tree_1.insert(parent='',index='end',iid=p,text='',values=(p[0],p[4],p[7],p[12],p[13]))
        else:
          pass
      count += 1

      #filter product

      def filter_product_1():
        if product_filter_entry_1.get() == '':
          sql = "SELECT * FROM Productservice"
          fbcursor.execute(sql)
          product_details = fbcursor.fetchall()
          for record in product_sel_tree_1.get_children():
            product_sel_tree_1.delete(record)

          count = 0
          for p in product_details:
            if True:
              product_sel_tree_1.insert(parent='',index='end',iid=p,text='',values=(p[0],p[4],p[7],p[12],p[13]))
            else:
              pass
          count += 1

        else:
          filter = product_filter_entry_1.get()
          for record in product_sel_tree_1.get_children():
            product_sel_tree_1.delete(record)
          
          sql = "SELECT * FROM Productservice WHERE name=%s"
          val = (filter, )
          fbcursor.execute(sql, val)
          records = fbcursor.fetchall()
    
      
          count=0
          for i in records:
            if True:
              product_sel_tree_1.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[10],i[8]))  
            else:
              pass
          count += 1



    product_filter_label_1=Label(inv_newline_sel_1, text="Enter filter text").place(x=5, y=10)
    product_filter_entry_1=Entry(inv_newline_sel_1, width=20)
    product_filter_entry_1.place(x=110, y=10)
    product_filter_button_1=Button(inv_newline_sel_1, text='Click Here',command=filter_product_1)
    product_filter_button_1.place(x=240, y=9,height=20,width=60)


    #add new product
    def new_product_1(): 
      top = Toplevel()  
      top.title("Add a new Product/Service")
      p2 = PhotoImage(file = 'images/fbicon.png')
      top.iconphoto(False, p2)
    
      top.geometry("700x550+390+15")
      tabControl = ttk.Notebook(top)
      s = ttk.Style()
      s.theme_use('default')
      s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


      tab1 = ttk.Frame(tabControl)
      tab2 = ttk.Frame(tabControl)
     
      tabControl.add(tab1,compound = LEFT, text ='Product/Service')
      tabControl.add(tab2,compound = LEFT, text ='Product Image')
     
      tabControl.pack(expand = 1, fill ="both")
     
      innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
      innerFrame.pack(side="top",fill=BOTH)

      Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
      Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

      add_pro_code_label_1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
      add_pro_code_label_1.place(x=20,y=0)
      add_pro_code_entry_1 = Entry(Customerlabelframe,width=35)
      add_pro_code_entry_1.place(x=120,y=8)

      checkvarStatus=IntVar()
      add_pro_status_1=Label(Customerlabelframe,text="Status:")
      add_pro_status_1.place(x=500,y=8)
      add_pro_checkbtn_active_1 = Checkbutton(Customerlabelframe,
                        variable = checkvarStatus,text="Active",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                       
                        width = 10)

      add_pro_checkbtn_active_1.place(x=550,y=5)

      add_pro_cat_1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
      add_pro_cat_1.place(x=20,y=40)
      n = StringVar()
      add_pro_country_1 = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
       
      add_pro_country_1['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
      
      add_pro_country_1.place(x=120,y=45)
      add_pro_country_1.current(0)


      add_pro_name_label_1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
      add_pro_name_label_1.place(x=20,y=70)
      add_pro_name_entry_1 = Entry(Customerlabelframe,width=60)
      add_pro_name_entry_1.place(x=120,y=75)

      add_pro_des_label_1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
      add_pro_des_label_1.place(x=20,y=100)
      add_pro_des_entry_1 = Entry(Customerlabelframe,width=60)
      add_pro_des_entry_1.place(x=120,y=105)

      uval = IntVar(Customerlabelframe, value='$0.00')
      add_pro_unit_label_1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
      add_pro_unit_label_1.place(x=20,y=130)
      add_pro_unit_entry_1 = Entry(Customerlabelframe,width=20,textvariable=uval)
      add_pro_unit_entry_1.place(x=120,y=135)

      pcsval = IntVar(Customerlabelframe, value='$0.00')
      add_pro_pcs_label_1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
      add_pro_pcs_label_1.place(x=320,y=140)
      add_pro_pcs_entry_1 = Entry(Customerlabelframe,width=20,textvariable=pcsval)
      add_pro_pcs_entry_1.place(x=410,y=140)

      costval = IntVar(Customerlabelframe, value='$0.00')
      add_pro_cost_label_1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
      add_pro_cost_label_1.place(x=20,y=160)
      add_pro_cost_entry_1 = Entry(Customerlabelframe,width=20,textvariable=costval)
      add_pro_cost_entry_1.place(x=120,y=165)

      priceval = IntVar(Customerlabelframe, value='$0.00')
      add_pro_price_label_1=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
      add_pro_price_label_1.place(x=20,y=190)
      add_pro_price_entry_1 = Entry(Customerlabelframe,width=20,textvariable=priceval)
      add_pro_price_entry_1.place(x=120,y=195)

      checkvarStatus2=IntVar()
     
      add_pro_checkbtn_tax_1 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                        text="Taxable Tax1rate",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                        height=2,
                        width = 12)

      add_pro_checkbtn_tax_1.place(x=415,y=170)


      checkvarStatus3=IntVar()
     
      add_pro_checkbtn_no_1 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                        text="No stock Control",
                        onvalue =1 ,
                        offvalue = 0,
                        height=3,
                        width = 15)

      add_pro_checkbtn_no_1.place(x=40,y=220)


      stockval = IntVar(Customerlabelframe)
      add_pro_stock_label_1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
      add_pro_stock_label_1.place(x=90,y=260)
      add_pro_stock_entry_1 = Entry(Customerlabelframe,width=15,textvariable=stockval)
      add_pro_stock_entry_1.place(x=150,y=265)

      lowval = IntVar(Customerlabelframe)
      add_pro_low_label_1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
      add_pro_low_label_1.place(x=300,y=260)
      add_pro_low_entry_1 = Entry(Customerlabelframe,width=10,textvariable=lowval)
      add_pro_low_entry_1.place(x=495,y=265)

     
      add_pro_ware_label_1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
      add_pro_ware_label_1.place(x=60,y=290)
      add_pro_ware_entry_1 = Entry(Customerlabelframe,width=50)
      add_pro_ware_entry_1.place(x=150,y=295)

      add_pro_pnote_label_1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
      add_pro_pnote_label_1.place(x=20,y=330)

      add_pro_pnote_scroll_1 = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
      add_pro_pnote_scroll_1.place(x=32,y=358)


      def add_new_product_1():
        sku_1 = add_pro_code_entry_1.get()
        category_1 = add_pro_country_1.get()
        name_1 = add_pro_name_entry_1.get()
        description_1 = add_pro_des_entry_1.get()
        unitprice_1 = add_pro_unit_entry_1.get()
        peices_1 = add_pro_pcs_entry_1.get()
        cost_1 = add_pro_cost_entry_1.get()
        priceminuscost_1 = add_pro_price_entry_1.get()
        stock_1 = add_pro_stock_entry_1.get()
        stocklimit_1 = add_pro_low_entry_1.get()
        warehouse_1 = add_pro_ware_entry_1.get()
        privatenote_1 = add_pro_pnote_scroll_1.get("1.0",'end-1c')
        status_1 = checkvarStatus.get()
        taxable_1 = checkvarStatus2.get()
        serviceornot_1 = checkvarStatus3.get()
        sql='INSERT INTO Productservice (sku,category,name,description,unitprice,peices,cost,priceminuscost,stock,stocklimit,warehouse,privatenote,status,taxable,serviceornot) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' #adding values into db
        val=(sku_1,category_1,name_1,description_1,unitprice_1,peices_1,cost_1,priceminuscost_1,stock_1,stocklimit_1,warehouse_1,privatenote_1,status_1,taxable_1,serviceornot_1)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        messagebox.showinfo("F-Billing Revolution","Product registered successfully")


      # Cancel add new product
      def cancel_add_1():
        top.destroy()




      add_pro_ok_btn_1 = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60,command=add_new_product_1)
      add_pro_ok_btn_1.pack(side=LEFT)

      add_pro_cancel_btn_1 = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60,command=cancel_add_1)
      add_pro_cancel_btn_1.pack(side=RIGHT)

      imageFrame = Frame(tab2, relief=GROOVE,height=580)
      imageFrame.pack(side="top",fill=BOTH)

      add_pro_browse_img_1=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
      add_pro_browse_img_1.place(x=15,y=35)

      add_pro_browse_btn_1=Button(imageFrame,text = 'Browse')
      add_pro_browse_btn_1.place(x=580,y=30,height=30,width=50)
      
      add_pro_remove_img_1 = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
      add_pro_remove_img_1.place(x=400,y=450)




    pro_fil_cat_tree_1=ttk.Treeview(inv_newline_sel_1, height=27)
    pro_fil_cat_tree_1["columns"]=["1"]
    pro_fil_cat_tree_1.column("#0", width=35, minwidth=20)
    pro_fil_cat_tree_1.column("1", width=205, minwidth=25, anchor=CENTER)    
    pro_fil_cat_tree_1.heading("#0",text="", anchor=W)
    pro_fil_cat_tree_1.heading("1",text="View filter by category", anchor=CENTER)
    pro_fil_cat_tree_1.place(x=660, y=45)
    #filter product
    def list_filter_product_1(evet):
      selected_indices_1 = pro_fil_cat_list_1.curselection()
      selected_filter_1 = ",".join([pro_fil_cat_list_1.get(i) for i in selected_indices_1])

      if selected_filter_1 == "               View all Products/Services" or selected_filter_1 == "               Default":
        pro_ser_sql_1 = "SELECT * FROM Productservice"
        fbcursor.execute(pro_ser_sql_1)
        pro_ser_data_1 = fbcursor.fetchall()
        for record in product_sel_tree_1.get_children():
          product_sel_tree_1.delete(record)
        count_ps = 0
        for i in pro_ser_data_1:
          product_sel_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[2],i[4],i[7],i[12],i[13]))
        count_ps += 1
      elif selected_filter_1 == "               View all Products":
        pro_sql_1 = "SELECT * FROM Productservice WHERE serviceornot=%s"
        pro_val_1 = ('0',)
        fbcursor.execute(pro_sql_1,pro_val_1)
        pro_data_1 = fbcursor.fetchall()
        for record in product_sel_tree_1.get_children():
          product_sel_tree_1.delete(record)
        count_p = 0
        for i in pro_data_1:
          product_sel_tree_1.insert(parent='', index='end', iid=i, text='', values=(i[2],i[4],i[7],i[12],i[13]))
        count_p += 1
      elif selected_filter_1 == "               View all Services":
        ser_sql_1 = "SELECT * FROM Productservice WHERE serviceornot=%s"
        ser_val_1 = ('1',)
        fbcursor.execute(ser_sql_1,ser_val_1)
        ser_data_1 = fbcursor.fetchall()
        for record in product_sel_tree_1.get_children():
          product_sel_tree_1.delete(record)
        count_s = 0
        for i in ser_data_1:
          product_sel_tree_1.insert(parent='', index='end', iid=i, text='', values=(i[2],i[4],i[7],i[12],i[13]))
        count_s += 1






    pro_fil_cat_list_1 = Listbox(inv_newline_sel_1,height=34,width=40,bg="white",activestyle="dotbox",fg="black",highlightbackground="white")
    pro_fil_cat_list_1.insert(0,"               View all Products/Services")
    pro_fil_cat_list_1.insert(1,"               View all Products")
    pro_fil_cat_list_1.insert(2,"               View all Services")
    pro_fil_cat_list_1.insert(3,"               Default")
    pro_fil_cat_list_1.place(x=660,y=63)
    pro_fil_cat_list_1.bind('<<ListboxSelect>>',list_filter_product_1)




    scrollbar = Scrollbar(inv_newline_sel_1)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=product_sel_tree_1.yview )
   

    product_ok_btn_1=Button(inv_newline_sel_1,compound = LEFT,image=tick ,text="ok", width=60,command=product_tree_fetch_1)
    product_ok_btn_1.place(x=15, y=610)
    product_edit_btn_1=Button(inv_newline_sel_1,compound = LEFT,image=tick , text="Edit product/Service", width=150)
    product_edit_btn_1.place(x=250, y=610)
    product_add_btn_1=Button(inv_newline_sel_1,compound = LEFT,image=tick , text="Add product/Service", width=150,command=new_product_1)
    product_add_btn_1.place(x=435, y=610)
    product_cancel_btn_1=Button(inv_newline_sel_1,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)



  #preview new line
  def previewline():
    messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")


  
  #sms notification
  def sms1():
    send_SMS=Toplevel()
    send_SMS.geometry("700x480+240+150")
    send_SMS.title("Send SMS notification")

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    sms_Notebook = ttk.Notebook(send_SMS)
    SMS_Notification = Frame(sms_Notebook, height=470, width=700)
    SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
    sms_Notebook.add(SMS_Notification, text="SMS Notification")
    sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
    sms_Notebook.place(x=0, y=0)

    numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
    numlbel.place(x=10, y=10)
    numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
    stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
    stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
    
    dclbel=Label(SMS_Notification, text="Double click to insert into text")
    dclbel.place(x=410, y=60)
    dcl=Entry(SMS_Notification, width=30)
    dcl.place(x=400, y=85,height=200)
    
    smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
    smstype.place(x=10, y=223)
    snuvar=IntVar()
    normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
    unicode_rbtn.place(x=190, y=5)
    tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
    tiplbf.place(x=10, y=290)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
    tiplabl.place(x=5, y=5)

    btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
    btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
    btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
    

    smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
    smstype.place(x=10, y=5)
    snumvar=IntVar()
    normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
    unicode_rbtn.place(x=290, y=5)

    sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
    sms1type.place(x=10, y=80)
    name=Label(sms1type, text="Username").place(x=10, y=5)
    na=Entry(sms1type, width=20).place(x=100, y=5)
    password=Label(sms1type, text="Password").place(x=10, y=45)
    pas=Entry(sms1type, width=20).place(x=100, y=45)
    combo=Label(sms1type, text="Route").place(x=400, y=5)
    n = StringVar()
    combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
    btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

    
    tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
    tiplbf.place(x=10, y=190)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
    tiplabl.place(x=0, y=5)
    tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
    tiplabl1.place(x=0, y=60)
    tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
    tiplabl2.place(x=0, y=100)
    tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
    tiplabl3.place(x=0, y=140)
    checkvar1=IntVar()
    chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 

  #mark invoice
  def markinvo_1():
    mark_inv=Toplevel()
    mark_inv.geometry("700x480+240+150")
    mark_inv.title("Record Payement for Invoice")
    # def new_payment():

    checkvar=IntVar()
    checkvar1=IntVar()
    checkvar2=IntVar()

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    mark_Notebook = ttk.Notebook(mark_inv)
    Mark_Invoice = Frame(mark_Notebook, height=470, width=750)
    mark_Notebook.add(Mark_Invoice, text="Mark Invoice")
    mark_Notebook.place(x=0, y=0)

    inv_bal_label_1=Label(Mark_Invoice, text="Invoice Balance").place(x=10, y=10)
    inv_bal_entry_1=Entry(Mark_Invoice, width=45).place(x=130, y=10)

    labelframe5 = LabelFrame(Mark_Invoice,text="Payement Record Details",bg="#f5f3f2")
    labelframe5.place(x=10,y=60,width=670,height=250)
    inv_amnt_entry_1 = Entry(labelframe5,width=28)
    inv_amnt_entry_1.place(x=30,y=45)
    inv_pdate_label_1 = Label(labelframe5, text="Payement Date:",bg="#f5f3f2").place(x=250,y=20)
    inv_pdate_entry_1 = Entry(labelframe5,width=28)
    inv_pdate_entry_1.place(x=220,y=45)
    inv_pby_label_1 = Label(labelframe5, text="Paid By:",bg="#f5f3f2").place(x=450,y=20)
    inv_pby_combo_1 = ttk.Combobox(labelframe5, value="Hello")
    inv_pby_combo_1.place(x=450,y=45)
    inv_des_label_1=Label(labelframe5, text="Description").place(x=30, y=80)
    inv_des_entry_1=Entry(labelframe5, width=100).place(x=30, y=120)
    inv_pfull_check_1 = Checkbutton(labelframe5,text="Paid in full and close invoice",variable=checkvar,onvalue=1,offvalue=0,bg="#f5f3f2")
    inv_pfull_check_1.place(x=30 ,y=150)
    inv_precp_label_1 = Label(labelframe5,text="Payement Reciepts",bg="#f5f3f2").place(x=300,y=145)
    inv_send_precp_1 = Checkbutton(labelframe5,text="Send Payement Reciept",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=320 ,y=170)
    inv_att_upinv_1 = Checkbutton(labelframe5,text="Attach updated invoice",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=320 ,y=200)

    inv_pok_btn_1 =Button(Mark_Invoice,compound = LEFT,image=tick , text="Save payement", width=100).place(x=10, y=350)
    inv_pcan_btn_1 =Button(Mark_Invoice,compound = LEFT,image=cancel, text="Cancel", width=100).place(x=500, y=350)

    
  #voidinvoice
  def voidinvoice_1():
    if void_msg_1 == YES:
      select_customer_btn_1['state'] = DISABLED
      add_newline_btn_1['state'] = DISABLED
      del_line_item_btn_1['state'] = DISABLED
      mark_inv_paid_1['state'] = DISABLED
      void_invoice_1['state'] = DISABLED
      save_invoice_1['state'] = DISABLED
      inv_combo_e1_1['state'] = DISABLED
      inv_addr_e2_1['state'] = DISABLED
      inv_shipto_e3_1['state'] = DISABLED
      inv_addr_e4_1['state'] = DISABLED
      inv_email_e5_1['state'] = DISABLED
      inv_sms_e6_1['state'] = DISABLED
      inv_number_entry_1['state'] = DISABLED
      inv_date_entry_1['state'] = DISABLED
      inv_duedate_entry_1['state'] = DISABLED
      inv_terms_combo_1['state'] = DISABLED
      inv_ref_entry_1['state'] = DISABLED
      ex_costn_combo_1['state'] = DISABLED
      dis_rate_entry_1['state'] = DISABLED
      ex_cost_entry_1['state'] = DISABLED
      tax1_entry_1['state'] = DISABLED
      template_entry_1['state'] = DISABLED
      draft_label_1.config(text="void")
      if checkrecStatus_1 is not None:
        checkrecStatus_1.set(0)
      else:
        checkrecStatus_1.set(0)
      recur_check_btn_1['state'] = DISABLED
      recur_period_entry_1['state'] = DISABLED
      recur_month_combo_1['state'] = DISABLED
      recur_nxt_inv_date_1['state'] = DISABLED
      recur_stop_check_1['state'] = DISABLED
      recur_stop_date_1['state'] = DISABLED
      recur_recalc_1['state'] = DISABLED
      pay_plus_1['state'] = DISABLED
      pay_minus_1['state'] = DISABLED
      title_txt_combo_1['state'] = DISABLED
      pageh_txt_combo_1['state'] = DISABLED
      footer_txt_combo_1['state'] = DISABLED
      term_txt_1['state'] = DISABLED
      comment_txt_1['state'] = DISABLED
      doc_plus_btn_1['state'] = DISABLED
      doc_minus_btn_1['state'] = DISABLED
    else:
      pass
  
  #delete line item  
  def delete_line_item_1():
    selected_line_item_1 = add_newline_tree_1.selection()[0]
    add_newline_tree_1.delete(selected_line_item_1)
    
    
    

  inv_first_frame2=Frame(pop_1, bg="#f5f3f2", height=60)
  inv_first_frame2.pack(side="top", fill=X)

  w = Canvas(inv_first_frame2, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  select_customer_btn_1 = Button(inv_first_frame2,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=inv_sel_customer_1)
  select_customer_btn_1.pack(side="left", pady=3, ipadx=4)


  w = Canvas(inv_first_frame2, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  add_newline_btn_1 = Button(inv_first_frame2,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=inv_newline_1)
  add_newline_btn_1.pack(side="left", pady=3, ipadx=4)

  del_line_item_btn_1= Button(inv_first_frame2,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=delete_line_item_1)
  del_line_item_btn_1.pack(side="left", pady=3, ipadx=4)

  w = Canvas(inv_first_frame2, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  prev= Button(inv_first_frame2,compound="top", text="Preview\nInvoice",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=previewline)
  prev.pack(side="left", pady=3, ipadx=4)

  prin= Button(inv_first_frame2,compound="top", text="Print \nInvoice",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printsele)
  prin.pack(side="left", pady=3, ipadx=4)

  w = Canvas(inv_first_frame2, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mail= Button(inv_first_frame2,compound="top", text="Email\nInvoice",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=emailorder)
  mail.pack(side="left", pady=3, ipadx=4)

  sms1= Button(inv_first_frame2,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=sms1)
  sms1.pack(side="left", pady=3, ipadx=4)

  w = Canvas(inv_first_frame2, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mark_inv_paid_1= Button(inv_first_frame2,compound="top", text="Mark invoice\nas 'Paid'",relief=RAISED, image=mark1,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=markinvo_1)
  mark_inv_paid_1.pack(side="left", pady=3, ipadx=4)

  void_invoice_1= Button(inv_first_frame2,compound="top", text="Void\ninvoice",relief=RAISED, image=mark2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=voidinvoice_1)
  void_invoice_1.pack(side="left", pady=3, ipadx=4)


  w = Canvas(inv_first_frame2, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  calc= Button(inv_first_frame2,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  calc.pack(side="left", pady=3, ipadx=4)

  save_invoice_1 = Button(inv_first_frame2,compound="top", text="Save",relief=RAISED, image=tick,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  save_invoice_1.pack(side="right", pady=3, ipadx=4)

  inv_first_frame2_1=Frame(pop_1, height=180,bg="#f5f3f2")
  inv_first_frame2_1.pack(side="top", fill=X)

  labelframe1 = LabelFrame(inv_first_frame2_1,text="Customers",font=("arial",15))
  labelframe1.place(x=10,y=5,width=640,height=160)

  def inv_to_combo_1(event):
    global inv_sel_combo_1
    inv_to_str_1 = inv_to_1.get()
    sql = "SELECT * FROM Customer WHERE businessname=%s"
    val = (inv_to_str_1,)
    fbcursor.execute(sql,val)
    inv_sel_combo_1 = fbcursor.fetchone()
    inv_addr_e2_1.delete('1.0',END)
    inv_addr_e2_1.insert('1.0',inv_sel_combo_1[5])
    inv_shipto_e3_1.delete(0, END)
    inv_shipto_e3_1.insert(0, inv_sel_combo_1[6])
    inv_addr_e4_1.delete('1.0',END)
    inv_addr_e4_1.insert('1.0',inv_sel_combo_1[7])
    inv_email_e5_1.delete(0,END)
    inv_email_e5_1.insert(0,inv_sel_combo_1[9])
    inv_sms_e6_1.delete(0,END)
    inv_sms_e6_1.insert(0,inv_sel_combo_1[12])

  def copy_cust_details_1():
    inv_to_str_2 = inv_to_1.get()
    if inv_to_str_2 != "":
      sql = "SELECT * FROM Customer WHERE businessname=%s"
      val = (inv_to_str_2,)
      fbcursor.execute(sql,val)
      inv_sel_combo_2 = fbcursor.fetchone()
      inv_shipto_e3_1.delete(0, END)
      inv_shipto_e3_1.insert(0, inv_sel_combo_2[4])
      inv_addr_e4_1.delete('1.0',END)
      inv_addr_e4_1.insert('1.0',inv_sel_combo_2[5])
    else:
      inv_shipto_e3_1.delete(0, END)
      inv_shipto_e3_1.insert(0, edit_inv_data[18])
      inv_addr_e4_1.delete('1.0',END)
      inv_addr_e4_1.insert('1.0',edit_inv_data[19])


      
      

  sql = "select businessname from Customer"
  fbcursor.execute(sql,)
  cdata = fbcursor.fetchall()

  global inv_combo_e1_1,inv_addr_e2_1,inv_shipto_e3_1,inv_addr_e4_1,inv_email_e5_1,inv_sms_e6_1

  invoice_to_1 = Label(labelframe1, text="Invoice to").place(x=10,y=5)
  inv_to_1 = StringVar()
  inv_combo_e1_1 = ttk.Combobox(labelframe1,width=28,textvariable=inv_to_1)
  inv_combo_e1_1.place(x=80,y=5)
  inv_combo_e1_1['values'] = cdata
  inv_combo_e1_1.bind("<<ComboboxSelected>>", inv_to_combo_1)
  inv_address_1=Label(labelframe1,text="Address").place(x=10,y=30)
  inv_addr_e2_1=scrolledtext.Text(labelframe1, undo=True,width=23)
  inv_addr_e2_1.place(x=80,y=30,height=70)
  inv_ship_to_1=Label(labelframe1,text="Ship to").place(x=342,y=5)
  inv_shipto_e3_1=Entry(labelframe1,width=30)
  inv_shipto_e3_1.place(x=402,y=3)
  inv_address1_1=Label(labelframe1,text="Address").place(x=340,y=30)
  inv_addr_e4_1=scrolledtext.Text(labelframe1, undo=True,width=23)
  inv_addr_e4_1.place(x=402,y=30,height=70)

  inv_copy_cust_1 =Button(labelframe1,width=3,height=2,compound = LEFT,text=">>",command=copy_cust_details_1)
  inv_copy_cust_1.place(x=280, y=50)
  
  labelframe2 = LabelFrame(inv_first_frame2_1,text="")
  labelframe2.place(x=10,y=130,width=640,height=42)
  inv_email_1=Label(labelframe2,text="Email").place(x=10,y=5)
  inv_email_e5_1=Entry(labelframe2,width=30)
  inv_email_e5_1.place(x=80,y=5)
  inv_sms_1=Label(labelframe2,text="SMS Number").place(x=328,y=5)
  inv_sms_e6_1=Entry(labelframe2,width=30)
  inv_sms_e6_1.place(x=402,y=5)
  

  inv_combo_e1_1.delete(0,END)
  inv_combo_e1_1.insert(0,edit_inv_data[18])
  inv_addr_e2_1.delete('1.0',END)
  inv_addr_e2_1.insert('1.0',edit_inv_data[19])
  inv_shipto_e3_1.delete(0, END)
  inv_shipto_e3_1.insert(0, edit_inv_data[20])
  inv_addr_e4_1.delete('1.0',END)
  inv_addr_e4_1.insert('1.0',edit_inv_data[21])
  inv_email_e5_1.delete(0,END)
  inv_email_e5_1.insert(0,edit_inv_data[22])
  inv_sms_e6_1.delete(0,END)
  inv_sms_e6_1.insert(0,edit_inv_data[23])
    
  labelframe = LabelFrame(inv_first_frame2_1,text="Invoice",font=("arial",15))
  labelframe.place(x=652,y=5,width=290,height=170)

  fbcursor.execute("SELECT * FROM Invoice ORDER BY invoiceid DESC LIMIT 1")
  inv_number_data_1 = fbcursor.fetchone()

  inv_number_label_1=Label(labelframe,text="Invoice#").place(x=5,y=5)
  inv_number_entry_1=Entry(labelframe,width=25)
  inv_number_entry_1.place(x=100,y=5,)

  inv_number_entry_1.delete(0,'end')
  inv_number_entry_1.insert(0, edit_inv_data[1])

  def inv_due_check_1():
    if checkvarStatus5.get() == 0:
      inv_duedate_entry_1['state'] = DISABLED
    else:
      inv_duedate_entry_1['state'] = NORMAL
 
  sql_term = 'SELECT terms_of_payment FROM terms_of_payment'
  fbcursor.execute(sql_term,)
  term_data = fbcursor.fetchall()

  inv_date_label_1 =Label(labelframe,text="Invoice date").place(x=5,y=33)
  inv_date_entry_1 =DateEntry(labelframe,width=15)
  inv_date_entry_1.place(x=150,y=33)
  checkvarStatus5=IntVar()
  inv_duedate_check_1=Checkbutton(labelframe,variable = checkvarStatus5,text="Due date",onvalue =1 ,offvalue = 0,command=inv_due_check_1)
  inv_duedate_check_1.place(x=5,y=62)
  inv_duedate_entry_1=DateEntry(labelframe,width=15,state=DISABLED)
  inv_duedate_entry_1.place(x=150,y=62)
  inv_terms_label_1=Label(labelframe,text="Terms").place(x=5,y=92)
  term = StringVar()
  inv_terms_combo_1=ttk.Combobox(labelframe,textvariable=term,width=23)
  inv_terms_combo_1.place(x=100,y=92)
  inv_terms_combo_1['values'] = term_data
  inv_terms_combo_1.bind("<<ComboboxSelected>>")
  inv_ref_label_1=Label(labelframe,text="Invoice ref#").place(x=5,y=118)
  inv_ref_entry_1=Entry(labelframe,width=25 )
  inv_ref_entry_1.place(x=100,y=118)

  inv_date_entry_1.delete(0, END)
  inv_date_entry_1.insert(0, edit_inv_data[2])
  if checkvarStatus5 is not None:
    checkvarStatus5.set(1)
  else:
    checkvarStatus5.set(1)
  inv_duedate_entry_1['state'] = NORMAL
  inv_duedate_entry_1.delete(0, END)
  inv_duedate_entry_1.insert(0, edit_inv_data[3])
  # inv_terms_combo_1.delete(0, END)
  # inv_terms_combo_1.insert(0, )
  # inv_ref_entry_1.delete(0, END)
  # inv_ref_entry_1.insert(0,)
  
  

  fir2Frame=Frame(pop_1, height=150,width=100,bg="#f5f3f2")
  fir2Frame.pack(side="top", fill=X)
  listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
  
  add_newline_tree_1=ttk.Treeview(listFrame)
  add_newline_tree_1["columns"]=["1","2","3","4","5","6","7","8"]

  add_newline_tree_1.column("#0", width=40)
  add_newline_tree_1.column("1", width=80)
  add_newline_tree_1.column("2", width=190)
  add_newline_tree_1.column("3", width=190)
  add_newline_tree_1.column("4", width=80)
  add_newline_tree_1.column("5", width=60)
  add_newline_tree_1.column("6", width=60)
  add_newline_tree_1.column("7", width=60)
  add_newline_tree_1.column("8", width=80)
  
  add_newline_tree_1.heading("#0")
  add_newline_tree_1.heading("1",text="ID/SKU")
  add_newline_tree_1.heading("2",text="Product/Service")
  add_newline_tree_1.heading("3",text="Description")
  add_newline_tree_1.heading("4",text="Unit Price")
  add_newline_tree_1.heading("5",text="Quality")
  add_newline_tree_1.heading("6",text="Pcs/Weight")
  add_newline_tree_1.heading("7",text="Tax1")
  add_newline_tree_1.heading("8",text="Price")
  
  add_newline_tree_1.pack(fill="both", expand=1)
  listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

  corresp_pro = inv_number_entry_1.get()
  sql = "SELECT * FROM storingproduct WHERE invoice_number=%s"
  val = (corresp_pro,)
  fbcursor.execute(sql,val)
  product_details = fbcursor.fetchall()
  count = 0
  for i in product_details:
    add_newline_tree_1.insert(parent='',index='end',iid=i,text='',values=(i[4], i[6], i[7],i[9],i[22],i[10],'',i[11]))
  count += 1

  fir3Frame=Frame(pop_1,height=200,width=700,bg="#f5f3f2")
  fir3Frame.place(x=0,y=490)

  tabStyle = ttk.Style()
  tabStyle.theme_use('default')
  tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
  myNotebook=ttk.Notebook(fir3Frame)
  invoiceFrame = Frame(myNotebook, height=200, width=800)
  recurFrame = Frame(myNotebook, height=200, width=800)
  payementFrame = Frame(myNotebook, height=200, width=800)
  headerFrame = Frame(myNotebook, height=200, width=800)
  commentFrame = Frame(myNotebook, height=200, width=800)
  termsFrame = Frame(myNotebook, height=200, width=800)
  noteFrame = Frame(myNotebook, height=200, width=800)
  documentFrame = Frame(myNotebook, height=200, width=800)
  
  myNotebook.add(invoiceFrame,compound="left", text="Invoice")
  myNotebook.add(recurFrame,compound="left", text="Recurring")
  myNotebook.add(payementFrame,compound="left", text="Payements")
  myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
  myNotebook.add(commentFrame,compound="left",  text="Comments")
  myNotebook.add(termsFrame,compound="left", text="Terms")
  myNotebook.add(noteFrame,compound="left",  text="Private notes")
  myNotebook.add(documentFrame,compound="left",  text="Documents")
  myNotebook.pack(expand = 1, fill ="both") 


  def recur_check_1():
    if checkrecStatus_1.get() == 0:
      recur_period_entry_1['state'] = DISABLED
      recur_month_combo_1['state'] = DISABLED
      recur_nxt_inv_date_1['state'] = DISABLED
      recur_stop_check_1['state'] = DISABLED
      recur_stop_date_1['state'] = DISABLED
      recur_recalc_1['state'] = DISABLED
    else:
      recur_period_entry_1['state'] = NORMAL
      recur_month_combo_1['state'] = NORMAL
      recur_nxt_inv_date_1['state'] = NORMAL
      recur_stop_check_1['state'] = NORMAL
      recur_stop_date_1['state'] = NORMAL
      recur_recalc_1['state'] = NORMAL 

  sql_exn = "SELECT extra_cost_name FROM extra_cost_name"
  fbcursor.execute(sql_exn)
  ex_data = fbcursor.fetchall()

  labelframe1 = LabelFrame(invoiceFrame,text="",font=("arial",15))
  labelframe1.place(x=1,y=1,width=735,height=170)
  ex_costn_label_1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
  ex_costn_combo_1=ttk.Combobox(labelframe1, value="",width=20)
  ex_costn_combo_1.place(x=115,y=5)
  ex_costn_combo_1['values'] = ex_data
  ex_costn_combo_1.bind("<<ComboboxSelected>>")
  dis_rate_label_1=Label(labelframe1,text="Discount rate").place(x=370,y=5)
  dis_rate_entry_1=Entry(labelframe1,width=6)
  dis_rate_entry_1.place(x=460,y=5)
  ex_cost_label_1=Label(labelframe1,text="Extra cost").place(x=35,y=35)
  ex_cost_entry_1=Entry(labelframe1,width=10)
  ex_cost_entry_1.place(x=115,y=35)
  tax1_label_1=Label(labelframe1,text="Tax1").place(x=420,y=35)
  tax1_entry_1=Entry(labelframe1,width=7)
  tax1_entry_1.place(x=460,y=35)
  template_label_1=Label(labelframe1,text="Template").place(x=37,y=70)
  template_entry_1=ttk.Combobox(labelframe1, value="",width=25)
  template_entry_1.place(x=115,y=70)
  sales_per_label_1=Label(labelframe1,text="Sales Person").place(x=25,y=100)
  sales_per_entry_1=Entry(labelframe1,width=18)
  sales_per_entry_1.place(x=115,y=100)
  category_label_1=Label(labelframe1,text="Category").place(x=300,y=100)
  category_entry_1=Entry(labelframe1,width=22)
  category_entry_1.place(x=370,y=100)
  
  statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
  statusfrme.place(x=540,y=0,width=160,height=160)
  draft_label_1=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey")
  draft_label_1.place(x=50, y=3)
  email_on_label_1=Label(statusfrme, text="Emailed on:").place( y=50)
  never1_label_1=Label(statusfrme, text="Never")
  never1_label_1.place(x=100,y=50)
  print_on_label_1=Label(statusfrme, text="Printed on:").place( y=90)
  never2_label_1=Label(statusfrme, text="Never")
  never2_label_1.place(x=100,y=90)

  recur_labelframe_1 = LabelFrame(recurFrame,text="",font=("arial",15))
  recur_labelframe_1.place(x=1,y=1,width=735,height=170)

  # def inv_stop_check_1():
  #   if checkstopStatus_1.get() == 0:
  #     recur_stop_date_1['state'] = NORMAL
  #   else:
  #     recur_stop_date_1['state'] = DISABLED

  mdata_1 = ["Month(s)","Day(s)"]

  checkrecStatus_1=IntVar()
  recur_check_btn_1 = Checkbutton(recur_labelframe_1,variable=checkrecStatus_1,text="Recurring",onvalue= 1,offvalue=0,command=recur_check_1)
  recur_check_btn_1.place(x=25,y=20)
  recur_period_label_1 = Label(recur_labelframe_1,text="Recurring period (interval)").place(x=130,y=45)
  recur_period_entry_1 = Spinbox(recur_labelframe_1,width=10,state=DISABLED,from_=1,to=10)
  recur_period_entry_1.place(x=280,y=45)
  recur_month_combo_1 = ttk.Combobox(recur_labelframe_1,values="",width=15,state=DISABLED)
  recur_month_combo_1.place(x=360,y=45)
  recur_month_combo_1['values'] = mdata_1
  recur_nxt_inv_label_1 = Label(recur_labelframe_1,text="Next Invoice").place(x=280,y=70)
  recur_nxt_inv_date_1 = DateEntry(recur_labelframe_1,width=20,state=DISABLED)
  recur_nxt_inv_date_1.place(x=360,y=70)
  checkstopStatus_1 = IntVar()
  recur_stop_check_1 = Checkbutton(recur_labelframe_1,variable=checkstopStatus_1,text="Stop recurring after",onvalue=1,offvalue=0,state=DISABLED)
  recur_stop_check_1.place(x=225,y=95)
  recur_stop_date_1 = DateEntry(recur_labelframe_1,width=20,state=DISABLED)
  recur_stop_date_1.place(x=360,y=95)
  recur_recalc_1 = Button(recur_labelframe_1,compound=LEFT,image=recalc,text="Recalculate",width=80,height=12,state=DISABLED)
  recur_recalc_1.place(x=540,y=70)

  pay_labelframe_1 = LabelFrame(payementFrame,text="",font=("arial",15))
  pay_labelframe_1.place(x=1,y=1,width=735,height=170)

  pay_tree_1 = ttk.Treeview(payementFrame,height=6)
  pay_tree_1["columns"] = ["1","2","3","4","5"]
  pay_tree_1.column("#0", width=10)
  pay_tree_1.column("1", width=130)
  pay_tree_1.column("2", width=130)
  pay_tree_1.column("3", width=130)
  pay_tree_1.column("4", width=130)
  pay_tree_1.column("5", width=130)
  pay_tree_1.heading("#0", text="",anchor=W)
  pay_tree_1.heading("1",text="Payment ID")
  pay_tree_1.heading("2",text="Payment date")
  pay_tree_1.heading("3",text="Paid by")
  pay_tree_1.heading("4",text="Description")
  pay_tree_1.heading("5",text="Amount")
  pay_tree_1.place(x=45,y=20)

  pay_plus_1 = Button(payementFrame,image=plus_1,text="",width=20,height=25,command=markinvo_1)
  pay_plus_1.place(x=10,y=20)
  pay_minus_1 = Button(payementFrame,image=minus,text="",width=20,height=25)
  pay_minus_1.place(x=10,y=55)
  pay_srch_1 = Button(payementFrame,image=photo4,text="",width=20,height=25)
  pay_srch_1.place(x=10,y=90)
  pay_msg_1 = Button(payementFrame,image=photo6,text="",width=20,height=25)
  pay_msg_1.place(x=10,y=125)


  header_labelframe_1 = LabelFrame(headerFrame,text="",font=("arial",15))
  header_labelframe_1.place(x=1,y=1,width=735,height=170)

  header_sql_1 = "SELECT headerandfooter FROM header_and_footer"
  fbcursor.execute(header_sql_1,)
  header_data_1 = fbcursor.fetchall()
  hdata_1 = []
  for i in header_data_1:
    hdata_1.append(i[0])
  

  title_txt_label_1=Label(header_labelframe_1,text="Title text").place(x=50,y=5)
  title_txt_combo_1=ttk.Combobox(header_labelframe_1, value="",width=60)
  title_txt_combo_1.place(x=125,y=5)
  title_txt_combo_1['values'] = hdata_1
  title_txt_combo_1.bind("<<ComboboxSelected>>")
  pageh_txt_label_1=Label(header_labelframe_1,text="Page header text").place(x=2,y=45)
  pageh_txt_combo_1=ttk.Combobox(header_labelframe_1, value=hdata_1,width=60)
  pageh_txt_combo_1.place(x=125,y=45)
  pageh_txt_combo_1.bind("<<ComboboxSelected>>")
  footer_txt_label_1=Label(header_labelframe_1,text="Footer text").place(x=35,y=85)
  footer_txt_combo_1=ttk.Combobox(header_labelframe_1, value=hdata_1,width=60)
  footer_txt_combo_1.place(x=125,y=85)
  footer_txt_combo_1.bind("<<ComboboxSelected>>")

  private_labelframe_1 = LabelFrame(noteFrame,text="",font=("arial",15))
  private_labelframe_1.place(x=1,y=1,width=735,height=170)

  private_label_1=Label(private_labelframe_1,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
  private_note_txt_1=Text(private_labelframe_1,width=89,height=7)
  private_note_txt_1.place(x=7,y=32)

  term_labelframe_1 = LabelFrame(termsFrame,text="",font=("arial",15))
  term_labelframe_1.place(x=1,y=1,width=735,height=170)

  term_txt_1=Text(term_labelframe_1,width=89,height=9)
  term_txt_1.place(x=7,y=10)


  comment_labelframe_1 = LabelFrame(commentFrame,text="",font=("arial",15))
  comment_labelframe_1.place(x=1,y=1,width=735,height=170)

  comment_txt_1=Text(comment_labelframe_1,width=89,height=9)
  comment_txt_1.place(x=7,y=10)

  doc_labelframe_1 = LabelFrame(documentFrame,text="",font=("arial",15))
  doc_labelframe_1.place(x=1,y=1,width=735,height=170)

  doc_plus_btn_1=Button(doc_labelframe_1,image=plus_1,text="",width=20,height=25)
  doc_plus_btn_1.place(x=5,y=10)
  doc_minus_btn_1=Button(doc_labelframe_1,height=25,width=20,text="",image=minus)
  doc_minus_btn_1.place(x=5,y=50)
  doc_txt_label_1=Label(doc_labelframe_1,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
  doc_tree_1=ttk.Treeview(doc_labelframe_1, height=5)
  doc_tree_1["columns"]=["1","2","3"]
  doc_tree_1.column("#0", width=20)
  doc_tree_1.column("1", width=130)
  doc_tree_1.column("2", width=380)
  doc_tree_1.column("3", width=130)
  doc_tree_1.heading("#0",text="", anchor=W)
  doc_tree_1.heading("1",text="Attach to Email")
  doc_tree_1.heading("2",text="Filename")
  doc_tree_1.heading("3",text="Filesize")  
  doc_tree_1.place(x=50, y=45)
  

  fir4Frame=Frame(pop_1,height=190,width=210,bg="#f5f3f2")
  fir4Frame.place(x=740,y=520)
  summaryfrme_1 = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
  summaryfrme_1.place(x=0,y=0,width=200,height=170)
  discount_1=Label(summaryfrme_1, text="Discount").place(x=0 ,y=0)
  discount1_1=Label(summaryfrme_1, text="$0.00")
  discount1_1.place(x=130 ,y=0)
  sub_1=Label(summaryfrme_1, text="Subtotal").place(x=0 ,y=21)
  sub1_1=Label(summaryfrme_1, text="$0.00")
  sub1_1.place(x=130 ,y=21)
  tax_1=Label(summaryfrme_1, text="Tax1").place(x=0 ,y=42)
  tax1_1=Label(summaryfrme_1, text="$0.00")
  tax1_1.place(x=130 ,y=42)
  cost_1=Label(summaryfrme_1, text="Extra cost").place(x=0 ,y=63)
  cost1_1=Label(summaryfrme_1, text="$0.00")
  cost1_1.place(x=130 ,y=63)
  invoicetot_1=Label(summaryfrme_1, text="Invoice total").place(x=0 ,y=84)
  invoicetot1_1=Label(summaryfrme_1, text="$0.00")
  invoicetot1_1.place(x=130 ,y=84)
  total_1=Label(summaryfrme_1, text="Total paid").place(x=0 ,y=105)
  total1_1=Label(summaryfrme_1, text="$0.00")
  total1_1.place(x=130 ,y=105)
  balance_1=Label(summaryfrme_1, text="Balance").place(x=0 ,y=126)
  balance1_1=Label(summaryfrme_1, text="$0.00")
  balance1_1.place(x=130 ,y=126)

  fir5Frame=Frame(pop_1,height=38,width=210)
  fir5Frame.place(x=735,y=485)
  btndown_1=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
  btnup_1=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)

  ex_costn_combo_1.delete(0, END)
  ex_costn_combo_1.insert(0, edit_inv_data[11])
  dis_rate_entry_1.delete(0, END)
  dis_rate_entry_1.insert(0, edit_inv_data[15])
  ex_cost_entry_1.delete(0, END)
  ex_cost_entry_1.insert(0, edit_inv_data[12])
  tax1_entry_1.delete(0, END)
  tax1_entry_1.insert(0, edit_inv_data[16])
  template_entry_1.delete(0, END)
  template_entry_1.insert(0, edit_inv_data[13])
  sales_per_entry_1.delete(0, END)
  sales_per_entry_1.insert(0, edit_inv_data[14])
  category_entry_1.delete(0, END)
  category_entry_1.insert(0, edit_inv_data[17])
  draft_label_1.config(text=edit_inv_data[4])
  if draft_label_1['text'] == "Void":
    select_customer_btn_1['state'] = DISABLED
    add_newline_btn_1['state'] = DISABLED
    del_line_item_btn_1['state'] = DISABLED
    mark_inv_paid_1['state'] = DISABLED
    void_invoice_1['state'] = DISABLED
    save_invoice_1['state'] = DISABLED
    inv_combo_e1_1['state'] = DISABLED
    inv_addr_e2_1['state'] = DISABLED
    inv_shipto_e3_1['state'] = DISABLED
    inv_addr_e4_1['state'] = DISABLED
    inv_email_e5_1['state'] = DISABLED
    inv_sms_e6_1['state'] = DISABLED
    inv_number_entry_1['state'] = DISABLED
    inv_date_entry_1['state'] = DISABLED
    inv_duedate_entry_1['state'] = DISABLED
    inv_terms_combo_1['state'] = DISABLED
    inv_ref_entry_1['state'] = DISABLED
    ex_costn_combo_1['state'] = DISABLED
    dis_rate_entry_1['state'] = DISABLED
    ex_cost_entry_1['state'] = DISABLED
    tax1_entry_1['state'] = DISABLED
    template_entry_1['state'] = DISABLED
    recur_check_btn_1['state'] = DISABLED
    recur_period_entry_1['state'] = DISABLED
    recur_month_combo_1['state'] = DISABLED
    recur_nxt_inv_date_1['state'] = DISABLED
    recur_stop_check_1['state'] = DISABLED
    recur_stop_date_1['state'] = DISABLED
    recur_recalc_1['state'] = DISABLED
    pay_plus_1['state'] = DISABLED
    pay_minus_1['state'] = DISABLED
    title_txt_combo_1['state'] = DISABLED
    pageh_txt_combo_1['state'] = DISABLED
    footer_txt_combo_1['state'] = DISABLED
    term_txt_1['state'] = DISABLED
    comment_txt_1['state'] = DISABLED
    doc_plus_btn_1['state'] = DISABLED
    doc_minus_btn_1['state'] = DISABLED
  else:
    pass
  never1_label_1.config(text=edit_inv_data[5])
  never2_label_1.config(text=edit_inv_data[6])
  if draft_label_1['text'] == "Void":
    recur_check_btn_1['state'] = DISABLED
    recur_period_entry_1['state'] = DISABLED
    recur_month_combo_1['state'] = DISABLED
    recur_nxt_inv_date_1['state'] = DISABLED
    recur_stop_check_1['state'] = DISABLED
    recur_stop_date_1['state'] = DISABLED
    recur_recalc_1['state'] = DISABLED
  else:
    checkrecStatus_1.set(1)
    recur_period_entry_1['state'] = NORMAL
    recur_month_combo_1['state'] = NORMAL
    recur_nxt_inv_date_1['state'] = NORMAL
    recur_stop_check_1['state'] = NORMAL
    recur_stop_date_1['state'] = NORMAL
    recur_recalc_1['state'] = NORMAL
  recur_period_entry_1.delete(0, END)
  recur_period_entry_1.insert(0, edit_inv_data[24])
  recur_month_combo_1.delete(0,END)
  recur_month_combo_1.insert(0,edit_inv_data[25])
  recur_nxt_inv_date_1.delete(0,END)
  recur_nxt_inv_date_1.insert(0,edit_inv_data[26])
  recur_stop_date_1.delete(0,END)
  recur_stop_date_1.insert(0,edit_inv_data[27])

  pay_sql = "SELECT * FROM markinvoice WHERE companyid=%s"
  pay_val = (edit_inv_data[28],)
  fbcursor.execute(pay_sql,pay_val)
  pay_data = fbcursor.fetchone()
  pay_tree_1.insert(parent='',index='end',iid=i,text='',values=(pay_data[0],pay_data[3],pay_data[4],pay_data[5],pay_data[6]))

####################### End edit/view invoice ##################

#printselected order
  
def printsele():

  def property1():
    propert=Toplevel()
    propert.title("Microsoft Print To PDF Advanced Document Settings")
    propert.geometry("670x500+240+150")

    def property2():
      propert1=Toplevel()
      propert1.title("Microsoft Print To PDF Advanced Document Settings")
      propert1.geometry("670x500+240+150")

      name=Label(propert1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
      paper=Label(propert1, text="Paper/Output").place(x=30, y=35)
      size=Label(propert1, text="Paper size").place(x=55, y=65)
      n = StringVar()
      search = ttk.Combobox(propert1, width = 15, textvariable = n )
      search['values'] = ('letter')
      search.place(x=150,y=65)
      search.current(0)
      copy=Label(propert1, text="Copy count:").place(x=55, y=95)

      okbtn=Button(propert1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=450)
      canbtn=Button(propert1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=450)
      
      


    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    property_Notebook = ttk.Notebook(propert)
    property_Frame = Frame(property_Notebook, height=500, width=670)
    property_Notebook.add(property_Frame, text="Layout")
    property_Notebook.place(x=0, y=0)

    name=Label(property_Frame, text="Orientation:").place(x=10, y=5)
    n = StringVar()
    search = ttk.Combobox(property_Frame, width = 23, textvariable = n )
    search['values'] = ('Portrait')
    search.place(x=10,y=25)
    search.current(0)

    text=Text(property_Frame,width=50).place(x=250, y=5,height=350)

    btn=Button(property_Frame, text="Advanced",command=property2).place(x=550, y=380)
    btn=Button(property_Frame,compound = LEFT,image=tick  ,text="OK", width=60,).place(x=430, y=420)
    btn=Button(property_Frame,compound = LEFT,image=cancel , text="Cancel", width=60,).place(x=550, y=420)     


    
  if(False):
      messagebox.showwarning("FBilling Revelution 2020", "Customer is required, Please select customer for this invoice\nbefore printing")
  elif(False):
      messagebox.showinfo("FBilling Revelution 2020", "Print job has been completed.")
  else:
      print1=Toplevel()
      print1.title("Print")
      print1.geometry("670x400+240+150")
      
      printerframe=LabelFrame(print1, text="Printer", height=80, width=650)
      printerframe.place(x=7, y=5)      
      name=Label(printerframe, text="Name:").place(x=10, y=5)
      e1= ttk.Combobox(printerframe, width=40).place(x=70, y=5)
      where=Label(printerframe, text="Where:").place(x=10, y=30)
      printocheckvar=IntVar()
      printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
      printochkbtn.place(x=450, y=30)
      btn=Button(printerframe, text="Properties", width=10,command=property1).place(x=540, y=5)

      pageslblframe=LabelFrame(print1, text="Pages", height=140, width=320)
      pageslblframe.place(x=10, y=90)
      radvar=IntVar()
      radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
      radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
      radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
      pagecountentry = Entry(pageslblframe, width=23).place(x=80, y=47)
      pageinfolabl=Label(pageslblframe, text="Enter page numbers and/or page ranges\nseperated by commas. For example:1,3,5-12")
      pageinfolabl.place(x=5, y=75)

      copylblframe=LabelFrame(print1, text="Copies", height=140, width=320)
      copylblframe.place(x=335, y=90)
      nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
      noentry = Entry(copylblframe, width=18).place(x=130, y=5)      
      one=Frame(copylblframe, width=30, height=40, bg="black").place(x=20, y=40)     
      two=Frame(copylblframe, width=30, height=40, bg="grey").place(x=15, y=45)     
      three=Frame(copylblframe, width=30, height=40, bg="white").place(x=10, y=50)      
      four=Frame(copylblframe, width=30, height=40, bg="black").place(x=80, y=40)      
      fiv=Frame(copylblframe, width=30, height=40, bg="grey").place(x=75, y=45)      
      six=Frame(copylblframe, width=30, height=40, bg="white").place(x=70, y=50)      
      collatecheckvar=IntVar()
      collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
      collatechkbtn.place(x=130, y=70)

      othrlblframe=LabelFrame(print1, text="Other", height=120, width=320)
      othrlblframe.place(x=10, y=235)
      printlb=Label(othrlblframe, text="Print").place(x=5, y=0)
      dropprint = ttk.Combobox(othrlblframe, width=23).place(x=80, y=0)
      orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
      dropord = ttk.Combobox(othrlblframe, width=23).place(x=80, y=25)
      duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)
      droplex = ttk.Combobox(othrlblframe, width=23).place(x=80, y=50)

      prmodelblframe=LabelFrame(print1, text="Print mode", height=120, width=320)
      prmodelblframe.place(x=335, y=235)
      dropscal = ttk.Combobox(prmodelblframe, width=30).place(x=5, y=5)
      poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=35)
      droppos = ttk.Combobox(prmodelblframe, width=10).place(x=155, y=35)

      okbtn=Button(print1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=370)
      canbtn=Button(print1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=370)
      


#email
      
def emailorder():
  mailDetail=Toplevel()
  mailDetail.title("E-Mail Invoice List")
  p2 = PhotoImage(file = "images/fbicon.png")
  mailDetail.iconphoto(False, p2)
  mailDetail.geometry("1030x550+150+120")
 
  def my_SMTP():
      if True:
          em_ser_conbtn.destroy()
          mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
          mysmtpservercon.place(x=610, y=110)
          lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
          hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
          lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
          portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
          lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
          unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
          lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
          pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
          ssl_chkvar=IntVar()
          ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
          ssl_chkbtn.place(x=50, y=110)
          em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
      else:
          pass
    
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  email_Notebook = ttk.Notebook(mailDetail)
  email_Frame = Frame(email_Notebook, height=500, width=1080)
  account_Frame = Frame(email_Notebook, height=550, width=1080)
  email_Notebook.add(email_Frame, text="E-mail")
  email_Notebook.add(account_Frame, text="Account")
  email_Notebook.place(x=0, y=0)
  messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
  messagelbframe.place(x=5, y=5)
  lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
  emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
  sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
  lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
  carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
  stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
  lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
  subent=Entry(messagelbframe, width=50).place(x=120, y=59)

  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
  mess_Notebook = ttk.Notebook(messagelbframe)
  emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
  htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
  mess_Notebook.place(x=5, y=90)

  btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
  btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

  dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
  dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
  mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)
  btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
  btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)
  attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
  attachlbframe.place(x=740, y=5)
  htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
  lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
  btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
  btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
  lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
  lbl_tt_info.place(x=740, y=370)

  ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
  
  sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
  sendatalbframe.place(x=5, y=5)
  lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
  sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
  lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
  nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
  lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
  replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
  lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
  signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
  confirm_chkvar=IntVar()
  confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
  confirm_chkbtn.place(x=200, y=215)
  btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

  sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
  sendatalbframe.place(x=610, y=5)
  servar=IntVar()
  SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
  SMTP_rbtn.place(x=10, y=10)
  MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=my_SMTP)
  MySMTP_rbtn.place(x=10, y=40)
  em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
  em_ser_conbtn.place(x=710, y=110)





#sms notification order
  
def sms():
  send_SMS=Toplevel()
  send_SMS.geometry("700x480+240+150")
  send_SMS.title("Send SMS notification")

  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  sms_Notebook = ttk.Notebook(send_SMS)
  SMS_Notification = Frame(sms_Notebook, height=470, width=700)
  SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
  sms_Notebook.add(SMS_Notification, text="SMS Notification")
  sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
  sms_Notebook.place(x=0, y=0)

  numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
  numlbel.place(x=10, y=10)
  numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
  stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
  stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
  
  dclbel=Label(SMS_Notification, text="Double click to insert into text")
  dclbel.place(x=410, y=60)
  dcl=Entry(SMS_Notification, width=30)
  dcl.place(x=400, y=85,height=200)
  
  smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
  smstype.place(x=10, y=223)
  snuvar=IntVar()
  normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
  unicode_rbtn.place(x=190, y=5)
  tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
  tiplbf.place(x=10, y=290)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
  tiplabl.place(x=5, y=5)

  btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
  btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
  btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
  

  smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
  smstype.place(x=10, y=5)
  snumvar=IntVar()
  normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
  unicode_rbtn.place(x=290, y=5)

  sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
  sms1type.place(x=10, y=80)
  name=Label(sms1type, text="Username").place(x=10, y=5)
  na=Entry(sms1type, width=20).place(x=100, y=5)
  password=Label(sms1type, text="Password").place(x=10, y=45)
  pas=Entry(sms1type, width=20).place(x=100, y=45)
  combo=Label(sms1type, text="Route").place(x=400, y=5)
  n = StringVar()
  combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
  btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

  
  tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
  tiplbf.place(x=10, y=190)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
  tiplabl.place(x=0, y=5)
  tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
  tiplabl1.place(x=0, y=60)
  tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
  tiplabl2.place(x=0, y=100)
  tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
  tiplabl3.place(x=0, y=140)
  checkvar1=IntVar()
  chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200)  



#print preview order
def printpreview():
  messagebox.showerror("F-Billing Revolution","Customer is required,please select customer for this order before printing.")



#convert to invoice
def convert():
  if messagebox.askyesno("Make invoice from Orders", "Are you sure to make invoice from this Orders ") == True:
        messagebox.askyesno("Make invoice from Estimate", "Invoice Creation was Successfull.\n New Invoice is \n Would you like to open this invoice ")
  else:
      messagebox.destroy()
  

#delete orders  
def dele():  
  messagebox.askyesno("Delete order", "Are you sure to delete this order? All products will be placed back into stock")




#search in orders  
def search():  
    top = Toplevel()     
    top.title("Find Text")   
    top.geometry("600x250+390+250")
    findwhat1=Label(top,text="Find What:",pady=5,padx=10).place(x=5,y=20)
    n = StringVar()
    findwhat = ttk.Combobox(top, width = 40, textvariable = n ).place(x=90,y=25)
   
    findin1=Label(top,text="Find in:",pady=5,padx=10).place(x=5,y=47)
    n = StringVar()
    findIN = ttk.Combobox(top, width = 30, textvariable = n )
    findIN['values'] = ('Product/Service id', ' Category', ' Active',' name',' stock',' location', ' image',' <<All>>')                       
    findIN.place(x=90,y=54)
    findIN.current(0)

    findButton = Button(top, text ="Find next",width=10).place(x=480,y=22)
    closeButton = Button(top,text ="Close",width=10).place(x=480,y=52)
    
    match1=Label(top,text="Match:",pady=5,padx=10).place(x=5,y=74)
    n = StringVar()
    match = ttk.Combobox(top, width = 23, textvariable = n )   
    match['values'] = ('From Any part',' Whole Field',' From the beginning of the field')                                   
    match.place(x=90,y=83)
    match.current(0)

    search1=Label(top,text="Search:",pady=5,padx=10).place(x=5,y=102)
    n = StringVar()
    search = ttk.Combobox(top, width = 23, textvariable = n )
    search['values'] = ('All', 'up',' Down')
    search.place(x=90,y=112)
    search.current(0)
    checkvarStatus4=IntVar()  
    Button4 = Checkbutton(top,variable = checkvarStatus4,text="Match Case",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button4.place(x=90,y=141)
    checkvarStatus5=IntVar()   
    Button5 = Checkbutton(top,variable = checkvarStatus5,text="Match Format",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button5.place(x=300,y=141)


inv_mainFrame=Frame(tab1, relief=GROOVE, bg="#f8f8f2")
inv_mainFrame.pack(side="top", fill=BOTH)

inv_midFrame=Frame(inv_mainFrame, bg="#f5f3f2", height=60)
inv_midFrame.pack(side="top", fill=X)

w = Canvas(inv_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))
w = Canvas(inv_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))

invoiceLabel = Button(inv_midFrame,compound="top", text="Create new\nInvoice",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=inv_create)
invoiceLabel.pack(side="left", pady=3, ipadx=4)

orderLabel = Button(inv_midFrame,compound="top", text="View/Edit\nInvoice",relief=RAISED, image=photo1,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=inv_edit_view)
orderLabel.pack(side="left")

estimateLabel = Button(inv_midFrame,compound="top", text="Delete\nSelected",relief=RAISED, image=photo2,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=dele)
estimateLabel.pack(side="left")

w = Canvas(inv_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)


w = Canvas(inv_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

previewLabel = Button(inv_midFrame,compound="top", text="Print\nPreview",relief=RAISED, image=photo4,bg="#f8f8f2", fg="black", height=55, bd=1, width=55, activebackground="red",command=printpreview)
previewLabel.pack(side="left")

purchaseLabel = Button(inv_midFrame,compound="top", text="Print\nSelected",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=printsele)
purchaseLabel.pack(side="left")

w = Canvas(inv_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

expenseLabel = Button(inv_midFrame,compound="top", text=" E-mail \nInvoice",relief=RAISED, image=photo6,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=emailorder)
expenseLabel.pack(side="left")

smsLabel = Button(inv_midFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=sms)
smsLabel.pack(side="left")

w = Canvas(inv_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(inv_midFrame,compound="top", text="Search in\nInvoices",relief=RAISED, image=photo7,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=search)
productLabel.pack(side="left")

inv_lbframe = LabelFrame(inv_midFrame, height=60, width=200, bg="#f8f8f2")
inv_lbframe.pack(side="left", padx=10, pady=0)
lbl_invdt = Label(inv_lbframe, text="Invoice date from : ", bg="#f8f8f2")
lbl_invdt.grid(row=0, column=0, pady=5, padx=(5, 0))
lbl_invdtt = Label(inv_lbframe, text="Invoice date to  :  ", bg="#f8f8f2")
lbl_invdtt.grid(row=1, column=0, pady=5, padx=(5, 0))
invdt = Entry(inv_lbframe, width=15)
invdt.grid(row=0, column=1)
invdtt = Entry(inv_lbframe, width=15)
invdtt.grid(row=1, column=1)
checkvar1 = IntVar()
chkbtn1 = Checkbutton(inv_lbframe, text = "Apply filter", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2")
chkbtn1.grid(row=0, column=2, rowspan=2, padx=(5,5))


# Refresh Invoice
def refresh_invoice():
  for record in inv_tree.get_children():
    inv_tree.delete(record)
    count = 0
  fbcursor.execute('SELECT * FROM invoice;')
  for i in fbcursor:
    if True:
      inv_tree.insert(parent='',index='end',iid=i,text='',value=('',i[1], i[2], i[3], i[18], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
    else:
      pass
  count += 1

inv_refresh_btn = Button(inv_midFrame,compound="top", text="Refresh\nInvoice list",relief=RAISED, image=photo8,fg="black", height=55, bd=1, width=55,command=refresh_invoice)
inv_refresh_btn.pack(side="left")

w = Canvas(inv_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(inv_midFrame,compound="top", text="Hide totals\nSum",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
productLabel.pack(side="left")

invoilabel = Label(inv_midFrame, text="Invoices(All)", font=("arial", 18), bg="#f8f8f2")
invoilabel.pack(side="left", padx=(20,0))
drop = ttk.Combobox(inv_midFrame, value="Hello")
drop.pack(side="right", padx=(0,10))
invoilabel = Label(inv_midFrame, text="Category filter", font=("arial", 15), bg="#f8f8f2")
invoilabel.pack(side="right", padx=(0,10))

class MyApp:
  def __init__(self, parent):
    
    self.myParent = parent 

    self.myContainer1 = Frame(parent) 
    self.myContainer1.pack()
    
    self.top_frame = Frame(self.myContainer1) 
    self.top_frame.pack(side=TOP,
      fill=BOTH, 
      expand=YES,
      )  

    self.left_frame = Frame(self.top_frame, background="white",
      borderwidth=5,  relief=RIDGE,
      height=250, 
      width=2000, 
      )
    self.left_frame.pack(side=LEFT,
      fill=BOTH, 
      expand=YES,
      )

    #Invoice all tree
    global inv_tree
    inv_tree = ttk.Treeview(self.left_frame, columns = (1,2,3,4,5,6,7,8,9,10,11,12), height = 15, show = "headings")
    inv_tree.pack(side = 'top')
    inv_tree.heading(1)
    inv_tree.heading(2, text="Invoice#")
    inv_tree.heading(3, text="Invoice date")
    inv_tree.heading(4, text="Due date")
    inv_tree.heading(5, text="Customer Name")
    inv_tree.heading(6, text="Status")
    inv_tree.heading(7, text="Emailed on")
    inv_tree.heading(8, text="Printed on")
    inv_tree.heading(9, text="SMS on")
    inv_tree.heading(10, text="Invoice Total")
    inv_tree.heading(11, text="Total Paid")
    inv_tree.heading(12, text="Balance")
    inv_tree.column(1, width = 35)
    inv_tree.column(2, width = 130)
    inv_tree.column(3, width = 110)
    inv_tree.column(4, width = 110)
    inv_tree.column(5, width = 180)
    inv_tree.column(6, width = 110)
    inv_tree.column(7, width = 130)
    inv_tree.column(8, width = 110)
    inv_tree.column(9, width = 110)
    inv_tree.column(10, width = 110)
    inv_tree.column(11, width = 110)
    inv_tree.column(12, width = 100)


    sql = "SELECT * FROM Invoice"
    fbcursor.execute(sql)
    invoice_records = fbcursor.fetchall()

    count = 0
    for record in invoice_records:
      if True:
        inv_tree.insert(parent='',index='end',iid=record,text='',values=('',record[1],record[2],record[3],record[18],record[4],record[5],record[6],record[7],record[8],record[9],record[10]))
      else:
        pass
    count += 1


    def product_picker(event):
      selected_inv = inv_tree.focus()
      selected_product = inv_tree.item(selected_inv)["values"][1]
      for record in inv_product_tree.get_children():
        inv_product_tree.delete(record)
      sql = "SELECT * FROM storingproduct WHERE invoice_number=%s"
      val = (selected_product,)
      fbcursor.execute(sql,val)
      product_details = fbcursor.fetchall()

      count = 0
      for i in product_details:
        inv_product_tree.insert(parent='',index='end',iid=i,text='',values=(' ',i[21], i[6], i[7],i[9],i[22],i[12]))
      count += 1
    inv_tree.bind('<Double-Button-1>',product_picker)



    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=995+340, y=0, height=300+20)
    scrollbar.config( command=inv_tree.yview )

    tabControl = ttk.Notebook(self.left_frame,width=1)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3=  ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoice Items',)
    tabControl.add(tab2,image=photo11,compound = LEFT, text ='Payements')
    tabControl.add(tab3,image=smslog,compound = LEFT, text ='Invoice private notes')
    tabControl.add(tab4,image=photo11,compound = LEFT, text ='SMS Log')
    tabControl.add(tab5,image=photo11,compound = LEFT, text ='Documents')
    tabControl.pack(expand = 1, fill ="both")
    
    
    inv_product_tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8), height = 15, show = "headings")
    inv_product_tree.pack(side = 'top')
    inv_product_tree.heading(1)
    inv_product_tree.heading(2, text="Product/Service ID",)
    inv_product_tree.heading(3, text="Name")
    inv_product_tree.heading(4, text="Description")
    inv_product_tree.heading(5, text="Price")
    inv_product_tree.heading(6, text="QTY")
    inv_product_tree.heading(7, text="Tax1")
    inv_product_tree.heading(8, text="Line Total")   
    inv_product_tree.column(1, width = 75)
    inv_product_tree.column(2, width = 230)
    inv_product_tree.column(3, width = 230)
    inv_product_tree.column(4, width = 275)
    inv_product_tree.column(5, width = 130)
    inv_product_tree.column(6, width = 130)
    inv_product_tree.column(7, width = 137)
    inv_product_tree.column(8, width = 130)


    inv_pay_tree = ttk.Treeview(tab2, columns = (1,2,3,4,5,6), height = 15, show = "headings")
    inv_pay_tree.pack(side = 'top')
    inv_pay_tree.heading(1)
    inv_pay_tree.heading(2, text="Payement ID",)
    inv_pay_tree.heading(3, text="Payement Date")
    inv_pay_tree.heading(4, text="PaidBy")
    inv_pay_tree.heading(5, text="Description")
    inv_pay_tree.heading(6, text="Amount")
    inv_pay_tree.column(1, width = 50)
    inv_pay_tree.column(2, width = 270)
    inv_pay_tree.column(3, width = 270)
    inv_pay_tree.column(4, width = 300)
    inv_pay_tree.column(5, width = 450)
    inv_pay_tree.column(6, width = 150)
    

    note1=Text(tab3, width=170,height=10).place(x=10, y=10)

    inv_email_tree = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
    inv_email_tree.pack(side = 'top')
    inv_email_tree.heading(1)
    inv_email_tree.heading(2, text="Attach to Email",)
    inv_email_tree.heading(3, text="Filename")
    inv_email_tree.column(1, width = 70)
    inv_email_tree.column(2, width = 430)
    inv_email_tree.column(3, width = 1000)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=980+350, y=360, height=195)
    scrollbar.config( command=inv_email_tree.yview )
       
myapp = MyApp(tab1)



root.mainloop()
