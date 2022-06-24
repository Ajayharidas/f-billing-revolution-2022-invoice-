def search():
    def find_cus_row():
      print(find_txt_var.get())
      if find_txt_var.get()=="P.Order#":
        fnd_sql="select * from porder where porder_no=%s"
        fnd_sql_val=(fnd_srh_txt.get(),)
        fbcursor.execute(fnd_sql,fnd_sql_val)
        htj=fbcursor.fetchall()
        for record in pord_tree.get_children():
          pord_tree.delete(record)
        count_cus=0

        for i in htj:
          
          pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
          count_cus +=1
        top.destroy()
     
      elif find_txt_var.get()=="Customer Name":
        fnd_sql="select * from porder where businessname=%s"
        fnd_sql_val=(fnd_srh_txt.get(),)
        fbcursor.execute(fnd_sql,fnd_sql_val)
        htj=fbcursor.fetchall()
        for record in pord_tree.get_children():
          pord_tree.delete(record)
        count_cus=0

        for i in htj:
          
          pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
          count_cus +=1
        top.destroy()
 
      elif find_txt_var.get()=="Order Total":
        fnd_sql="select * from porder where 	ordertot=%s"
        fnd_sql_val=(fnd_srh_txt.get(),)
        fbcursor.execute(fnd_sql,fnd_sql_val)
        htj=fbcursor.fetchall()
        for record in pord_tree.get_children():
          pord_tree.delete(record)
        count_cus=0

        for i in htj:
          
          pord_tree.insert(parent='', index='end', iid=count_cus, text='hello', values=(' ',i[39], i[2], i[3], i[25],i[5], i[6], i[7], i[8], i[9], i[10]))
          count_cus +=1
        top.destroy()  

      
    top = Toplevel()  
    top.title("Find Text")
    p2 = PhotoImage(file = "images/fbicon.png")
    top.iconphoto(False, p2)
    top.geometry("520x150+390+250")
    findwhat1=Label(top,text="Find What:")
    findwhat1.place(x=5,y=15)
    fnd_srh_txt = StringVar() 
    findwhat = ttk.Combobox(top, width = 50, textvariable = fnd_srh_txt )
    findwhat.place(x=85,y=15,height=23) 
    findButton = Button(top, text ="Find next",width=10, command=lambda:find_cus_row())
    findButton.place(x=420,y=15)
    findin1=Label(top,text="Find in:")
    findin1.place(x=5,y=40)
    find_txt_var = StringVar() 
    findIN = ttk.Combobox(top, width = 37, textvariable =find_txt_var )
    findIN['values'] = ('P.Order#',
                              'Customer Name', 
                              'Order Total')        
    findIN.place(x=85,y=40,height=23) 
    findIN.current(0)
    closeButton = Button(top, text ="Close",width=10, command=lambda:fnd_dist())
    closeButton.place(x=420,y=45)
   
    # up_var = StringVar() 
    # checkvarStatus4=IntVar()
    # Button4 = Checkbutton(top,variable = checkvarStatus4, 
    #                   text="Match Case", 
    #                   onvalue =0 ,
    #                   offvalue = 1,
    #                   height=3,
    #                   width = 15)
    # Button4.select()
    # Button4.place(x=60,y=80)
    # checkvarStatus5=IntVar()  
    # Button5 = Checkbutton(top,variable = checkvarStatus5, 
    #                   text="Match Format", 
    #                   onvalue =0 ,
    #                   offvalue = 1,
    #                   height=3,
    #                   width = 15)
    # Button5.select()
    # Button5.place(x=270,y=80)