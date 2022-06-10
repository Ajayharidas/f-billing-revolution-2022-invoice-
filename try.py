sql = 'select * from company'
        fbcursor.execute(sql)
        compdataord = fbcursor.fetchone()
        if orde_templ.get() == 'Professional 1 (logo on left side)':
          previewcreate = Toplevel()
          previewcreate.geometry("1360x730")
          frame = Frame(previewcreate, width=953, height=300)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=5,y=30)
          canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,1200))
          
          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)

          canvas.config(width=1315,height=640)
          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(235, 25, 1035, 1430, outline='yellow',fill='white')
          # canvas.create_text(640, 80, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          # canvas.create_text(385, 210, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          try:
            image = Image.open("images/"+compdataord[13])
            resize_image = image.resize((250, 125))
            loimg = ImageTk.PhotoImage(resize_image)
            b2 = Label(canvas,image=loimg, height=125, width=250,)
            b2.photo = loimg
            canvas.create_window(380, 155,window=b2)
          except:
            pass
          canvas.create_text(295, 250, text="Order#", fill="black", font=('Helvetica 11'))
          canvas.create_text(305, 270, text="Order date", fill="black", font=('Helvetica 11'))
          canvas.create_text(300, 290, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(291, 310, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(305, 330, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(450, 250, text=""+orde_orderid.get(), fill="black", font=('Helvetica 11'))
          canvas.create_text(450, 270, text=orde_date.get_date(), fill="black", font=('Helvetica 11'))
          canvas.create_text(450, 290, text=orde_date.get_date(), fill="black", font=('Helvetica 11'))
          canvas.create_text(440, 310, text=""+orde_terms.get(), fill="black", font=('Helvetica 11'))      

          canvas.create_text(920, 180, text=compdataord[1], fill="black", font=('Helvetica 12 '))
          
          compadress = Text(canvas,font=('Helvetica 10'),width=30,height=5,fg= "black",
          bg="white",cursor="arrow",bd=0,)
          compadress.insert("1.0",compdataord[2])
          compadress.tag_configure("tag_name", justify='right')
          compadress.tag_add("tag_name", "1.0", "end")
          compadress.config(state=DISABLED)
          canvas.create_window(885, 233,window=compadress)

          taxcanvas = Label(canvas, font=('Helvetica 10 '),width=30,bg="white")
          taxcanvas.config(text=compdataord[4],anchor="e")
          canvas.create_window(870, 285,window=taxcanvas)
          canvas.create_text(950, 305, text="Order", fill="black", font=('Helvetica 14 bold'))
          canvas.create_text(946, 325, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          canvas.create_text(310, 350, text="Order to", fill="black", font=('Helvetica 10 underline'))
          ord_canvas_name = Label(canvas, font=('Helvetica 10 '),width=30)
          ord_canvas_name.config(text=orde_name.get(),anchor="w",bg="white")
          canvas.create_window(400, 370,window=ord_canvas_name)
          addr_can_lab = Text(canvas,font=('Helvetica 10'),width=30,height=4,bd=0,fg= "black",
          bg="white",cursor="arrow")
          addr_can_lab.insert("1.0",orde_addr.get("1.0",END))
          addr_can_lab.config(state=DISABLED)
          canvas.create_window(386, 412, window=addr_can_lab)
          canvas.create_text(650, 350, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          ord_canvas_ship = Label(canvas, font=('Helvetica 10 '),width=30)
          ord_canvas_ship.config(text=orde_ship.get(),anchor="w",bg="white")
          canvas.create_window(750, 370, window=ord_canvas_ship)
          shipaddr_can_lab = Text(canvas,font=('Helvetica 10'),width=30,height=4,bd=0,fg= "black",
          bg="white",cursor="arrow")
          shipaddr_can_lab.insert("1.0",orde_shipaddr.get("1.0",END))
          shipaddr_can_lab.config(state=DISABLED)
          canvas.create_window(737, 413,window=shipaddr_can_lab)

          s = ttk.Style()
          s.configure('Treeview.Heading', background='',State='DISABLE')

          # tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle.Treeview')

          # tree.column("# 1", anchor=E, stretch=NO, width=100)
          # tree.heading("# 1", text="ID/SKU")
          # tree.column("# 2", anchor=E, stretch=NO, width=350)
          # tree.heading("# 2", text="Product/Service - Description")
          # tree.column("# 3", anchor=E, stretch=NO, width=80)
          # tree.heading("# 3", text="Quantity")
          # tree.column("# 4", anchor=E, stretch=NO, width=90)
          # tree.heading("# 4", text="Unit Price")
          # tree.column("# 5", anchor=E, stretch=NO, width=80)
          # tree.heading("# 5", text="Price")
          ord_previewtree=ttk.Treeview(canvas, height=12,style='mystyle.Treeview')
          ord_previewtree["columns"]=["1","2","3", "4","5"]
          ord_previewtree.column("#0", width=1)
          ord_previewtree.column("1", width=100)
          ord_previewtree.column("2", width=350)
          ord_previewtree.column("3", width=80)
          ord_previewtree.column("4", width=90)
          ord_previewtree.column("5", width=80)
          ord_previewtree.heading("#0",text="")
          ord_previewtree.heading("1",text="ID/SKU")
          ord_previewtree.heading("2",text="Product/Service")
          ord_previewtree.heading("3",text="Quantity")
          ord_previewtree.heading("4",text="Unit Price")
          ord_previewtree.heading("5",text="Price")
          
          window = canvas.create_window(280, 452, anchor="nw", window=ord_previewtree)

          sql = "select * from company"
          fbcursor.execute(sql)
          taxcheck = fbcursor.fetchone()

          sql = "select currsignplace,currencysign from company"
          fbcursor.execute(sql)
          symbolcheck = fbcursor.fetchone()
          


          for child in edit_pro_tree.get_children():
            previewdata = list(edit_pro_tree.item(child, 'values'))
            if not taxcheck:
              ord_previewtree.insert(parent='', index='end',text='', values=(previewdata[0],previewdata[1],previewdata[4],previewdata[3],previewdata[6]))
            elif taxcheck[12] == "1":
              ord_previewtree.insert(parent='', index='end',text='', values=(previewdata[0],previewdata[1],previewdata[4],previewdata[3],previewdata[6]))
            elif taxcheck[12] == "2":
              ord_previewtree.insert(parent='', index='end',text='', values=(previewdata[0],previewdata[1],previewdata[4],previewdata[3],previewdata[7]))
            elif taxcheck[12] == "3":
              ord_previewtree.insert(parent='', index='end',text='', values=(previewdata[0],previewdata[1],previewdata[4],previewdata[3],previewdata[8]))

        
          if not taxcheck:
            canvas.create_line(980, 715, 980, 790 )
            canvas.create_line(720, 715, 720, 790 )
            canvas.create_line(860, 715, 860, 790 )#1st
            canvas.create_line(980, 715, 720, 715 )
            canvas.create_line(980, 740, 720, 740 )
            canvas.create_line(980, 765, 720, 765 ) 
            canvas.create_line(980, 790, 720, 790 )
            
            
            canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
            canvas.create_text(900, 730, text=sub1.cget("text"), fill="black", font=('Helvetica 10'))

            canvas.create_text(900, 755, text=orde_extracost.get(), fill="black", font=('Helvetica 10 bold'))
            canvas.create_text(780, 755, text="Extra Cost", fill="black", font=('Helvetica 10 bold'))

            canvas.create_text(900, 780, text=order1.cget("text"), fill="black", font=('Helvetica 10'))
            canvas.create_text(780, 780, text="Total Order", fill="black", font=('Helvetica 10'))
          elif taxcheck[12] == "1":
            canvas.create_line(980, 715, 980, 790 )
            canvas.create_line(720, 715, 720, 790 )
            canvas.create_line(860, 715, 860, 790 )#1st
            canvas.create_line(980, 715, 720, 715 )
            canvas.create_line(980, 740, 720, 740 )
            canvas.create_line(980, 765, 720, 765 ) 
            canvas.create_line(980, 790, 720, 790 )

            if symbolcheck[0] == "before amount":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=symbolcheck[1]+str(sub1.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 755, text=symbolcheck[1]+str(orde_extracost.get()), fill="black", font=('Helvetica 10'))
              canvas.create_text(780, 755, text="Extra Cost", fill="black", font=('Helvetica 10 '))
    
              canvas.create_text(900, 780, text=symbolcheck[1]+str(order1.cget("text")), fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 780, text="Total Order", fill="black", font=('Helvetica 10 bold'))
            elif symbolcheck[0] == "before amount with space":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=symbolcheck[1]+" "+str(sub1.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 755, text=symbolcheck[1]+" "+str(orde_extracost.get()), fill="black", font=('Helvetica 10'))
              canvas.create_text(780, 755, text="Extra Cost", fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 780, text=symbolcheck[1]+" "+str(order1.cget("text")), fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 780, text="Total Order", fill="black", font=('Helvetica 10 bold'))
            elif symbolcheck[0] == "after amount":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=str(sub1.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 755, text=str(orde_extracost.get())+symbolcheck[1], fill="black", font=('Helvetica 10 '))
              canvas.create_text(780, 755, text="Extra Cost", fill="black", font=('Helvetica 10 '))
    
              canvas.create_text(900, 780, text=str(order1.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 780, text="Total Order", fill="black", font=('Helvetica 10 bold'))

            elif symbolcheck[0] == "after amount with space":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=str(sub1.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 755, text=str(orde_extracost.get())+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
              canvas.create_text(780, 755, text="Extra Cost", fill="black", font=('Helvetica 10 '))
    
              canvas.create_text(900, 780, text=str(order1.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 780, text="Total Order", fill="black", font=('Helvetica 10 bold'))
          elif taxcheck[12] == "2":
            canvas.create_line(980, 715, 980, 815 )
            canvas.create_line(720, 715, 720, 815 )
            canvas.create_line(860, 715, 860, 815 )#1st
            canvas.create_line(980, 815, 720, 815 )
            canvas.create_line(980, 715, 720, 715 )
            canvas.create_line(980, 740, 720, 740 )
            canvas.create_line(980, 765, 720, 765 ) 
            canvas.create_line(980, 790, 720, 790 )
            canvas.create_line(980, 815, 720, 815 )

            if symbolcheck[0] == "before amount":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=symbolcheck[1]+str(sub1.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=symbolcheck[1]+str(tax1sum.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 780, text=symbolcheck[1]+str(orde_extracost.get()), fill="black", font=('Helvetica 10 '))
              canvas.create_text(780, 780, text="Extra Cost", fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 805, text=symbolcheck[1]+str(order1.cget("text")), fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 805, text="Total Order", fill="black", font=('Helvetica 10 bold'))
        
            elif symbolcheck[0] == "before amount with space":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=symbolcheck[1]+" "+str(sub1.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=symbolcheck[1]+" "+str(tax1sum.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 780, text=symbolcheck[1]+" "+str(orde_extracost.get()), fill="black", font=('Helvetica 10 '))
              canvas.create_text(780, 780, text="Extra Cost", fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 805, text=symbolcheck[1]+" "+str(order1.cget("text")), fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 805, text="Total Order", fill="black", font=('Helvetica 10 bold'))
            
            elif symbolcheck[0] == "after amount":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=str(sub1.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=str(tax1sum.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 780, text=str(orde_extracost.get())+symbolcheck[1], fill="black", font=('Helvetica 10 '))
              canvas.create_text(780, 780, text="Extra Cost", fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 805, text=str(order1.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 805, text="Total Order", fill="black", font=('Helvetica 10 bold'))
            
            elif symbolcheck[0] == "after amount with space":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=str(sub1.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=str(tax1sum.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 780, text=str(orde_extracost.get())+" "+symbolcheck[1], fill="black", font=('Helvetica 10 '))
              canvas.create_text(780, 780, text="Extra Cost", fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 805, text=str(order1.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 805, text="Total Order", fill="black", font=('Helvetica 10 bold'))
          elif taxcheck[12] == "3":
            canvas.create_line(980, 715, 980, 840 )
            canvas.create_line(720, 715, 720, 840 )
            canvas.create_line(860, 715, 860, 840 )#1st
            canvas.create_line(980, 815, 720, 815 )
            canvas.create_line(980, 715, 720, 715 )
            canvas.create_line(980, 740, 720, 740 )
            canvas.create_line(980, 765, 720, 765 ) 
            canvas.create_line(980, 790, 720, 790 )
            canvas.create_line(980, 815, 720, 815 )
            canvas.create_line(980, 840, 720, 840 )
              
            if symbolcheck[0] == "before amount":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=symbolcheck[1]+str(sub1.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=symbolcheck[1]+str(tax1sum.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 780, text="TAX2", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 780, text=symbolcheck[1]+str(tax2sum.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 805, text=symbolcheck[1]+str(orde_extracost.get()), fill="black", font=('Helvetica 10'))
              canvas.create_text(780, 805, text="Extra Cost", fill="black", font=('Helvetica 10 '))
    
              canvas.create_text(900, 830, text=symbolcheck[1]+str(order1.cget("text")), fill="black", font=('Helvetica 10   bold'))
              canvas.create_text(780, 830, text="Total Order", fill="black", font=('Helvetica 10 bold'))
            
            elif symbolcheck[0] == "before amount with space":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=symbolcheck[1]+" "+str(sub1.cget("text")), fill="black", font=('Helvetica 10'))

              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=symbolcheck[1]+" "+str(tax1sum.cget("text")), fill="black", font=('Helvetica 10'))

              canvas.create_text(780, 780, text="TAX2", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 780, text=symbolcheck[1]+" "+str(tax2sum.cget("text")), fill="black", font=('Helvetica 10'))

              canvas.create_text(900, 805, text=symbolcheck[1]+" "+str(orde_extracost.get()), fill="black", font=('Helvetica 10'))
              canvas.create_text(780, 805, text="Extra Cost", fill="black", font=('Helvetica 10 '))

              canvas.create_text(900, 830, text=symbolcheck[1]+" "+str(order1.cget("text")), fill="black", font=('Helvetica 10    bold'))
              canvas.create_text(780, 830, text="Total Order", fill="black", font=('Helvetica 10 bold'))
            elif symbolcheck[0] == "after amount":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=str(sub1.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=str(tax1sum.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 780, text="TAX2", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 780, text=str(tax2sum.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 805, text=str(orde_extracost.get())+symbolcheck[1], fill="black", font=('Helvetica 10'))
              canvas.create_text(780, 805, text="Extra Cost", fill="black", font=('Helvetica 10 '))
    
              canvas.create_text(900, 830, text=str(order1.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10   bold'))
              canvas.create_text(780, 830, text="Total Order", fill="black", font=('Helvetica 10 bold'))
            elif symbolcheck[0] == "after amount with space":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=str(sub1.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=str(tax1sum.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 780, text="TAX2", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 780, text=str(tax2sum.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 805, text=str(orde_extracost.get())+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
              canvas.create_text(780, 805, text="Extra Cost", fill="black", font=('Helvetica 10 '))
    
              canvas.create_text(900, 830, text=str(order1.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10   bold'))
              canvas.create_text(780, 830, text="Total Order", fill="black", font=('Helvetica 10 bold'))
          

         
          comments = Text(canvas,font=('Helvetica 10'),width=100,height=10,fg= "black",
          bg="white",cursor="arrow",bd=0)
          comments.insert("1.0",orde_commands.get("1.0",END))
          comments.config(state=DISABLED)

          
          canvas.create_window(630, 910,window=comments)
          
          
          canvas.create_text(620, 1050, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(250, 1070, 1015, 1070)
          
          pre_terms = Text(canvas,font=('Helvetica 10'),width=105,height=4,fg= "black",
          bg="white",cursor="arrow",bd=0)
          pre_terms.insert("1.0",orde_termsnotes.get("1.0",END))
          pre_terms.tag_configure("tag_name", justify='center')
          pre_terms.tag_add("tag_name", "1.0", "end")
          pre_terms.config(state=DISABLED)
          canvas.create_window(630, 1110,window=pre_terms)
          canvas.create_text(338, 1170, text="Sale Person:", fill="black", font=('Helvetica 10'))
          ord_saleper = Label(canvas, font=('Helvetica 10 '),width=30)
          ord_saleper.config(text=orde_sales.get(),anchor="w",bg="white")
          canvas.create_window(510, 1170, window = ord_saleper)

          canvas.create_text(380, 1190, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(920, 1190, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
        #----------------Professional 2 (logo on right side)------------------
        elif orde_templ.get() == 'Professional 2 (logo on right side)':
          previewcreate = Toplevel()
          previewcreate.geometry("1360x730")
          frame = Frame(previewcreate, width=953, height=300)
          frame.pack(expand=True, fill=BOTH)
          frame.place(x=5,y=30)
          
          canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,1200))
          
          vertibar=Scrollbar(frame, orient=VERTICAL)
          vertibar.pack(side=RIGHT,fill=Y)
          vertibar.config(command=canvas.yview)
          canvas.config(width=1315,height=640)
          
          canvas.config(yscrollcommand=vertibar.set)
          canvas.pack(expand=True,side=LEFT,fill=BOTH)
          canvas.create_rectangle(235, 25, 1035, 1430 , outline='yellow',fill='white')
          canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(850, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
          
          canvas.create_text(350, 180, text=compdataord[1], fill="black", font=('Helvetica 12 '))          
          compadress = Text(canvas,font=('Helvetica 10'),width=30,height=5,fg= "black",
          bg="white",cursor="arrow",bd=0)
          compadress.insert("1.0",compdataord[2])
          compadress.tag_configure("tag_name", justify='left')
          compadress.tag_add("tag_name", "1.0", "end")
          compadress.config(state=DISABLED)
          canvas.create_window(383, 235, window =compadress)
          
          taxcanvas = Label(canvas, font=('Helvetica 10 '),width=30,bg="white")
          taxcanvas.config(text=compdataord[4],anchor="w")
          canvas.create_window(395, 285, window=taxcanvas)
          canvas.create_text(325, 305, text="Order", fill="black", font=('Helvetica 14 bold'))
          canvas.create_text(332, 325, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
          
          canvas.create_text(752, 250, text="Order#", fill="black", font=('Helvetica 11'))
          canvas.create_text(765, 270, text="Order date", fill="black", font=('Helvetica 11'))
          canvas.create_text(750, 290, text="Due date", fill="black", font=('Helvetica 11'))
          canvas.create_text(741, 310, text="Terms", fill="black", font=('Helvetica 11'))
          canvas.create_text(755, 330, text="Order ref.#", fill="black", font=('Helvetica 11'))
          canvas.create_text(920, 250, text="ORD1/2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(920, 270, text="05-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(920, 290, text="20-05-2022", fill="black", font=('Helvetica 11'))
          canvas.create_text(920, 310, text="NET 15", fill="black", font=('Helvetica 11'))  
            
          canvas.create_text(310, 360, text="Order to", fill="black", font=('Helvetica 10 underline'))
          ord_canvas_name = Label(canvas, font=('Helvetica 10 '),width=30)
          ord_canvas_name.config(text=orde_name.get(),anchor="w")
          canvas.create_window(395, 379,window=ord_canvas_name)
          # addr_can_lab = Text(canvas,font=('Helvetica 10'),width=30,height=4,bd=0,fg= "black",
          # bg="white",cursor="arrow")
          # addr_can_lab.insert("1.0",orde_addr.get("1.0",END))
          # addr_can_lab.config(state=DISABLED)
          # canvas.create_window(386, 412, window=addr_can_lab)
         
          canvas.create_text(346, 395, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(355, 410, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(315, 425, text="United States", fill="black", font=('Helvetica 10'))
          canvas.create_text(650, 360, text="Ship to", fill="black", font=('Helvetica 10 underline'))
          canvas.create_text(656, 380, text="John Doe", fill="black", font=('Helvetica 10 '))
          canvas.create_text(698, 395, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
          canvas.create_text(708, 410, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
          canvas.create_text(668, 425, text="United States", fill="black", font=('Helvetica 10'))

          ord_previewtree=ttk.Treeview(canvas, height=12,style='mystyle.Treeview')
          ord_previewtree["columns"]=["1","2","3", "4","5"]
          ord_previewtree.column("#0", width=1)
          ord_previewtree.column("1", width=100)
          ord_previewtree.column("2", width=350)
          ord_previewtree.column("3", width=80)
          ord_previewtree.column("4", width=90)
          ord_previewtree.column("5", width=80)
          ord_previewtree.heading("#0",text="")
          ord_previewtree.heading("1",text="ID/SKU")
          ord_previewtree.heading("2",text="Product/Service")
          ord_previewtree.heading("3",text="Quantity")
          ord_previewtree.heading("4",text="Unit Price")
          ord_previewtree.heading("5",text="Price")
          
          window = canvas.create_window(280, 452, anchor="nw", window=ord_previewtree)

          sql = "select * from company"
          fbcursor.execute(sql)
          taxcheck = fbcursor.fetchone()

          sql = "select currsignplace,currencysign from company"
          fbcursor.execute(sql)
          symbolcheck = fbcursor.fetchone()
          


          for child in edit_pro_tree.get_children():
            previewdata = list(edit_pro_tree.item(child, 'values'))
            if not taxcheck:
              ord_previewtree.insert(parent='', index='end',text='', values=(previewdata[0],previewdata[1],previewdata[4],previewdata[3],previewdata[6]))
            elif taxcheck[12] == "1":
              ord_previewtree.insert(parent='', index='end',text='', values=(previewdata[0],previewdata[1],previewdata[4],previewdata[3],previewdata[6]))
            elif taxcheck[12] == "2":
              ord_previewtree.insert(parent='', index='end',text='', values=(previewdata[0],previewdata[1],previewdata[4],previewdata[3],previewdata[7]))
            elif taxcheck[12] == "3":
              ord_previewtree.insert(parent='', index='end',text='', values=(previewdata[0],previewdata[1],previewdata[4],previewdata[3],previewdata[8]))

        
          if not taxcheck:
            canvas.create_line(980, 715, 980, 790 )
            canvas.create_line(720, 715, 720, 790 )
            canvas.create_line(860, 715, 860, 790 )#1st
            canvas.create_line(980, 715, 720, 715 )
            canvas.create_line(980, 740, 720, 740 )
            canvas.create_line(980, 765, 720, 765 ) 
            canvas.create_line(980, 790, 720, 790 )
            
            
            canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
            canvas.create_text(900, 730, text=sub1.cget("text"), fill="black", font=('Helvetica 10'))

            canvas.create_text(900, 755, text=orde_extracost.get(), fill="black", font=('Helvetica 10 bold'))
            canvas.create_text(780, 755, text="Extra Cost", fill="black", font=('Helvetica 10 bold'))

            canvas.create_text(900, 780, text=order1.cget("text"), fill="black", font=('Helvetica 10'))
            canvas.create_text(780, 780, text="Total Order", fill="black", font=('Helvetica 10'))
          elif taxcheck[12] == "1":
            canvas.create_line(980, 715, 980, 790 )
            canvas.create_line(720, 715, 720, 790 )
            canvas.create_line(860, 715, 860, 790 )#1st
            canvas.create_line(980, 715, 720, 715 )
            canvas.create_line(980, 740, 720, 740 )
            canvas.create_line(980, 765, 720, 765 ) 
            canvas.create_line(980, 790, 720, 790 )

            if symbolcheck[0] == "before amount":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=symbolcheck[1]+str(sub1.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 755, text=symbolcheck[1]+str(orde_extracost.get()), fill="black", font=('Helvetica 10'))
              canvas.create_text(780, 755, text="Extra Cost", fill="black", font=('Helvetica 10 '))
    
              canvas.create_text(900, 780, text=symbolcheck[1]+str(order1.cget("text")), fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 780, text="Total Order", fill="black", font=('Helvetica 10 bold'))
            elif symbolcheck[0] == "before amount with space":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=symbolcheck[1]+" "+str(sub1.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 755, text=symbolcheck[1]+" "+str(orde_extracost.get()), fill="black", font=('Helvetica 10'))
              canvas.create_text(780, 755, text="Extra Cost", fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 780, text=symbolcheck[1]+" "+str(order1.cget("text")), fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 780, text="Total Order", fill="black", font=('Helvetica 10 bold'))
            elif symbolcheck[0] == "after amount":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=str(sub1.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 755, text=str(orde_extracost.get())+symbolcheck[1], fill="black", font=('Helvetica 10 '))
              canvas.create_text(780, 755, text="Extra Cost", fill="black", font=('Helvetica 10 '))
    
              canvas.create_text(900, 780, text=str(order1.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 780, text="Total Order", fill="black", font=('Helvetica 10 bold'))

            elif symbolcheck[0] == "after amount with space":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=str(sub1.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 755, text=str(orde_extracost.get())+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
              canvas.create_text(780, 755, text="Extra Cost", fill="black", font=('Helvetica 10 '))
    
              canvas.create_text(900, 780, text=str(order1.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 780, text="Total Order", fill="black", font=('Helvetica 10 bold'))
          elif taxcheck[12] == "2":
            canvas.create_line(980, 715, 980, 815 )
            canvas.create_line(720, 715, 720, 815 )
            canvas.create_line(860, 715, 860, 815 )#1st
            canvas.create_line(980, 815, 720, 815 )
            canvas.create_line(980, 715, 720, 715 )
            canvas.create_line(980, 740, 720, 740 )
            canvas.create_line(980, 765, 720, 765 ) 
            canvas.create_line(980, 790, 720, 790 )
            canvas.create_line(980, 815, 720, 815 )

            if symbolcheck[0] == "before amount":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=symbolcheck[1]+str(sub1.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=symbolcheck[1]+str(tax1sum.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 780, text=symbolcheck[1]+str(orde_extracost.get()), fill="black", font=('Helvetica 10 '))
              canvas.create_text(780, 780, text="Extra Cost", fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 805, text=symbolcheck[1]+str(order1.cget("text")), fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 805, text="Total Order", fill="black", font=('Helvetica 10 bold'))
        
            elif symbolcheck[0] == "before amount with space":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=symbolcheck[1]+" "+str(sub1.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=symbolcheck[1]+" "+str(tax1sum.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 780, text=symbolcheck[1]+" "+str(orde_extracost.get()), fill="black", font=('Helvetica 10 '))
              canvas.create_text(780, 780, text="Extra Cost", fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 805, text=symbolcheck[1]+" "+str(order1.cget("text")), fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 805, text="Total Order", fill="black", font=('Helvetica 10 bold'))
            
            elif symbolcheck[0] == "after amount":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=str(sub1.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=str(tax1sum.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 780, text=str(orde_extracost.get())+symbolcheck[1], fill="black", font=('Helvetica 10 '))
              canvas.create_text(780, 780, text="Extra Cost", fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 805, text=str(order1.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 805, text="Total Order", fill="black", font=('Helvetica 10 bold'))
            
            elif symbolcheck[0] == "after amount with space":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=str(sub1.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=str(tax1sum.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 780, text=str(orde_extracost.get())+" "+symbolcheck[1], fill="black", font=('Helvetica 10 '))
              canvas.create_text(780, 780, text="Extra Cost", fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 805, text=str(order1.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10 bold'))
              canvas.create_text(780, 805, text="Total Order", fill="black", font=('Helvetica 10 bold'))
          elif taxcheck[12] == "3":
            canvas.create_line(980, 715, 980, 840 )
            canvas.create_line(720, 715, 720, 840 )
            canvas.create_line(860, 715, 860, 840 )#1st
            canvas.create_line(980, 815, 720, 815 )
            canvas.create_line(980, 715, 720, 715 )
            canvas.create_line(980, 740, 720, 740 )
            canvas.create_line(980, 765, 720, 765 ) 
            canvas.create_line(980, 790, 720, 790 )
            canvas.create_line(980, 815, 720, 815 )
            canvas.create_line(980, 840, 720, 840 )
              
            if symbolcheck[0] == "before amount":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=symbolcheck[1]+str(sub1.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=symbolcheck[1]+str(tax1sum.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 780, text="TAX2", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 780, text=symbolcheck[1]+str(tax2sum.cget("text")), fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 805, text=symbolcheck[1]+str(orde_extracost.get()), fill="black", font=('Helvetica 10'))
              canvas.create_text(780, 805, text="Extra Cost", fill="black", font=('Helvetica 10 '))
    
              canvas.create_text(900, 830, text=symbolcheck[1]+str(order1.cget("text")), fill="black", font=('Helvetica 10   bold'))
              canvas.create_text(780, 830, text="Total Order", fill="black", font=('Helvetica 10 bold'))
            
            elif symbolcheck[0] == "before amount with space":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=symbolcheck[1]+" "+str(sub1.cget("text")), fill="black", font=('Helvetica 10'))

              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=symbolcheck[1]+" "+str(tax1sum.cget("text")), fill="black", font=('Helvetica 10'))

              canvas.create_text(780, 780, text="TAX2", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 780, text=symbolcheck[1]+" "+str(tax2sum.cget("text")), fill="black", font=('Helvetica 10'))

              canvas.create_text(900, 805, text=symbolcheck[1]+" "+str(orde_extracost.get()), fill="black", font=('Helvetica 10'))
              canvas.create_text(780, 805, text="Extra Cost", fill="black", font=('Helvetica 10 '))

              canvas.create_text(900, 830, text=symbolcheck[1]+" "+str(order1.cget("text")), fill="black", font=('Helvetica 10    bold'))
              canvas.create_text(780, 830, text="Total Order", fill="black", font=('Helvetica 10 bold'))
            elif symbolcheck[0] == "after amount":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=str(sub1.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=str(tax1sum.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 780, text="TAX2", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 780, text=str(tax2sum.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 805, text=str(orde_extracost.get())+symbolcheck[1], fill="black", font=('Helvetica 10'))
              canvas.create_text(780, 805, text="Extra Cost", fill="black", font=('Helvetica 10 '))
    
              canvas.create_text(900, 830, text=str(order1.cget("text"))+symbolcheck[1], fill="black", font=('Helvetica 10   bold'))
              canvas.create_text(780, 830, text="Total Order", fill="black", font=('Helvetica 10 bold'))
            elif symbolcheck[0] == "after amount with space":
              canvas.create_text(780, 730, text="Subtotal", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 730, text=str(sub1.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 755, text="TAX1", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 755, text=str(tax1sum.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(780, 780, text="TAX2", fill="black", font=('Helvetica 10'))
              canvas.create_text(900, 780, text=str(tax2sum.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
    
              canvas.create_text(900, 805, text=str(orde_extracost.get())+" "+symbolcheck[1], fill="black", font=('Helvetica 10'))
              canvas.create_text(780, 805, text="Extra Cost", fill="black", font=('Helvetica 10 '))
    
              canvas.create_text(900, 830, text=str(order1.cget("text"))+" "+symbolcheck[1], fill="black", font=('Helvetica 10   bold'))
              canvas.create_text(780, 830, text="Total Order", fill="black", font=('Helvetica 10 bold'))
          
          

          comments = Text(canvas,font=('Helvetica 10'),width=100,height=10,fg= "black",
          bg="white",cursor="arrow",bd=0)
          comments.insert("1.0",orde_commands.get("1.0",END))
          comments.config(state=DISABLED)

          
          canvas.create_window(630, 910,window=comments)

          canvas.create_text(620, 1050, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
          canvas.create_line(250, 1070, 1015, 1070)

          pre_terms = Text(canvas,font=('Helvetica 10'),width=105,height=4,fg= "black",
          bg="white",cursor="arrow",bd=0)
          pre_terms.insert("1.0",orde_termsnotes.get("1.0",END))
          pre_terms.tag_configure("tag_name", justify='center')
          pre_terms.tag_add("tag_name", "1.0", "end")
          pre_terms.config(state=DISABLED)
          canvas.create_window(630, 1110,window=pre_terms)
          canvas.create_text(338, 1170, text="Sale Person:", fill="black", font=('Helvetica 10'))
          ord_saleper = Label(canvas, font=('Helvetica 10 '),width=30)
          ord_saleper.config(text=orde_sales.get(),anchor="w",bg="white")
          canvas.create_window(510, 1170, window = ord_saleper)
          canvas.create_text(380,  1190, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
          canvas.create_text(920, 1190, text="Page 1 of 1", fill="black", font=('Helvetica 10'))