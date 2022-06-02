  def est_send_mail():

      sender_email = "infoxfbilling@gmail.com" #email_from.get()                                 
      sender_password = "fbilling@2022"        #email_pswrd.get() 

      server = smtplib.SMTP('smtp.gmail.com', 587)
      print("Login successful1")
      server.starttls()
      print("Login successful2")
      server.login(sender_email, sender_password)
      print("Login successful3")
      carbcopy_info = "sagmanaduvil@gmail.com"      #carcopyem_address.get()
      print(carbcopy_info)
      
      
      msg = MIMEMultipart()
      msg['Subject'] = email_subject.get() 
      mail_content  = estmemaiframe.get('1.0','end-1c') 
      msg['From'] = email_from.get()
      msg['To'] = estimate_emailtoent.get()
      
      gettingimg=estframe.get()
      print(gettingimg)
      lst_data = gettingimg[1:-1].split(',')
      print(lst_data,"happy")
      # print(gettingimg)
      msg.attach(MIMEText(mail_content, 'plain'))

      for i in lst_data:
        if len(i.strip()[1:-1])>1:
        # print(i[0],"IMAGE")
          with open('images/'+ i.strip()[1:-1], "rb") as attachment:
              # MIME attachment is a binary file for that content type "application/octet-stream" is used
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
          # encode into base64 
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % 'images/'+ i.strip()[1:-1]) 

        # attach the instance 'part' to instance 'message' 
            msg.attach(part)
        # message_body = email_body.get()

      server.sendmail(email_from.get(),estimate_emailtoent.get(),msg.as_string())
      server.sendmail(email_from.get(), carbcopy_info,msg.as_string())


      dateeem=dt.datetime.now()
      emitemid = est_tree.item(est_tree.focus())["values"][1]
      for record in est_tree.get_children():
        est_tree.delete(record)
      sqlq = "UPDATE estimate SET emailon=%s WHERE estimate_number=%s"
      valq = (dateeem,emitemid, )
      fbcursor.execute(sqlq, valq,)
      fbilldb.commit()
      fbcursor.execute('SELECT * FROM estimate;')
      ordertotalinput=0
      j = 0
      for i in fbcursor:
       est_tree.insert(parent='', index='end', iid=i, text='', values=(i[0], i[1], i[2], i[3], i[4],i[5], i[6], i[7], i[8]))
      for line in est_tree.get_children():
        idsave1=est_tree.item(line)['values'][9]
      ordertotalinput += idsave1
      j += 1
      #estimate_total1.config(text=ordertotalinput)

      print("message sent")
  def est_empsfile_image(event):
      global yawn
      for i in  estimate_htcodeframe.curselection():
        print("hloo", estimate_htcodeframe.get(i))
        yawn= estimate_htcodeframe.get(i)        
        edit_window_img = Toplevel()
        edit_window_img.title("View Image")
        edit_window_img.geometry("700x500")
        image = Image.open("images/"+yawn)
        resize_image = image.resize((700, 500))
        image = ImageTk.PhotoImage(resize_image)
        psimage = Label(edit_window_img,image=image)
        psimage.photo = image
        psimage.pack()

  def est_UploadAction(event=None):
      global filenamez

      filenamez = askopenfilename(filetypes=(("png file ",'.png'),("jpg file", ".jpg"), ('PDF', '.pdf',), ("All files", ".*"),))
      shutil.copyfile(filenamez, os.getcwd()+'/images/'+filenamez.split('/')[-1])
      estimate_htcodeframe.insert(0, filenamez.split('/')[-1])
        
  def estimate_emailord():
    estimate_mailDetail=Toplevel()
    estimate_mailDetail.title("E-Mail")
    estimate_ep2 = PhotoImage(file = "images/fbicon.png")
    estimate_mailDetail.iconphoto(False, estimate_ep2)
    estimate_mailDetail.geometry("1030x550+150+120")
    
    def estimate_my_SMTP():
        if True:
            #estimate_em_ser_conbtn.destroy()
            estimate_mysmtpservercon=LabelFrame(estimate_account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
            estimate_mysmtpservercon.place(x=610, y=110)
            estimate_lbl_hostn=Label(estimate_mysmtpservercon, text="Hostname")
            estimate_lbl_hostn.place(x=5, y=10)
            estimate_hostnent=Entry(estimate_mysmtpservercon, width=30)
            estimate_hostnent.place(x=80, y=10)
            estimate_lbl_portn=Label(estimate_mysmtpservercon, text="Port")
            estimate_lbl_portn.place(x=5, y=35)
            estimate_portent=Entry(estimate_mysmtpservercon, width=30)
            estimate_portent.place(x=80, y=35)
            estimate_elbl_usn=Label(estimate_mysmtpservercon, text="Username")
            estimate_elbl_usn.place(x=5, y=60)
            estimate_unament=Entry(estimate_mysmtpservercon, width=30)
            estimate_unament.place(x=80, y=60)
            estimate_eelbl_pasn=Label(estimate_mysmtpservercon, text="Password")
            estimate_eelbl_pasn.place(x=5, y=85)
            estimate_pwdent=Entry(estimate_mysmtpservercon, width=30)
            estimate_pwdent.place(x=80, y=85)
            estimate_ssl_chkvar=IntVar()
            estimate_ssl_chkbtn=Checkbutton(estimate_mysmtpservercon, variable=estimate_ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
            estimate_ssl_chkbtn.place(x=50, y=110)
            estimate_em_ser_conbtn1=Button(estimate_account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
        else:
            pass
      
    estimate_mystyle = ttk.Style()
    estimate_mystyle.theme_use('default')
    estimate_mystyle.configure('TNotebook.Tab', background="#999999", padding=5)
    estimate_email_Notebook = ttk.Notebook(estimate_mailDetail)
    estimate_email_Frame = Frame(estimate_email_Notebook, height=500, width=1080)
    estimate_account_Frame = Frame(estimate_email_Notebook, height=550, width=1080)
    estimate_email_Notebook.add(estimate_email_Frame, text="E-mail")
    estimate_email_Notebook.add(estimate_account_Frame, text="Account")
    estimate_email_Notebook.place(x=0, y=0)
    estimate_messagelbframe=LabelFrame(estimate_email_Frame,text="Message", height=495, width=730)
    estimate_messagelbframe.place(x=5, y=5)

    global estimate_emailtoent, email_subject, email_from,email_pswrd, estimate_cctoent,estmemaiframe, estimate_htcodeframe, estframe
    email_subject = StringVar()
    email_from = StringVar()
    email_pswrd = StringVar()

    estimate_mylbl_emailtoaddr=Label(estimate_messagelbframe, text="Email to address").place(x=5, y=5)
    estimate_emailtoent=Entry(estimate_messagelbframe, width=70)
    estimate_emailtoent.place(x=120, y=5)
    estimate_mylbl_ccto=Label(estimate_messagelbframe, text="Carbon Copy to").place(x=5, y=30)
    estimate_cctoent=Entry(estimate_messagelbframe, width=70)
    estimate_cctoent.place(x=120, y=30)
    estimate_mylbl_emailsub=Label(estimate_messagelbframe, text="Subject").place(x=5, y=55)
    estimate_subent=Entry(estimate_messagelbframe, width=70, textvariable=email_subject)
    estimate_subent.place(x=120, y=55)
    
    estimate_sendemail_btn=Button(estimate_messagelbframe, text="Send Email", width=10, height=1,command=est_send_mail)
    estimate_sendemail_btn.place(x=600, y=10)
    # estimate_sendemail_btn=Button(estimate_messagelbframe, text="Stop Sending", width=10, height=1).place(x=600, y=50)
    
    estimate_nstyle = ttk.Style()
    estimate_nstyle.theme_use('default')
    estimate_nstyle.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
    estimate_mess_Notebook = ttk.Notebook(estimate_messagelbframe)
    estimate_emailmessage_Frame = Frame(estimate_mess_Notebook, height=350, width=710)
    estimate_htmlsourse_Frame = Frame(estimate_mess_Notebook, height=350, width=710)
    estimate_mess_Notebook.add(estimate_emailmessage_Frame, text="E-mail message")
    # estimate_mess_Notebook.add(estimate_htmlsourse_Frame, text="Html sourse code")
    estimate_mess_Notebook.place(x=5, y=90)

    estimate_mybtn1=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall, command=lambda:estmemaiframe.event_generate('<Control a>'))
    estimate_mybtn1.place(x=0, y=1)

    estimate_mybtn2=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut,command=lambda :estmemaiframe.event_generate('<Control x>'))
    estimate_mybtn2.place(x=36, y=1)

    estimate_mybtn3=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy,command=lambda :estmemaiframe.event_generate('<Control c>'))
    estimate_mybtn3.place(x=73, y=1)

    estimate_mybtn4=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste,command=lambda :estmemaiframe.event_generate('<Control v>'))
    estimate_mybtn4.place(x=105, y=1)

    estimate_mybtn5=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo)
    estimate_mybtn5.place(x=140, y=1)

    estimate_mybtn6=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo)
    estimate_mybtn6.place(x=175, y=1)

    # fontSize=12
    # fontStyle='Helvetica'
    # def font_style(event):
    #   global fontStyle
    #   fontStyle=font_family__variable.get()
    #   estmemaiframe.config(font=(fontStyle,fontSize))

    estimate_mybtn7=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold)
    estimate_mybtn7.place(x=210, y=1)

    estimate_mybtn8=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics)
    estimate_mybtn8.place(x=245, y=1)

    estimate_mybtn9=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline)
    estimate_mybtn9.place(x=280, y=1)

    def est_align_left():
      data=estmemaiframe.get(0.0,END)
      estmemaiframe.tag_config('left',justify=LEFT)
      estmemaiframe.delete(0.0,END)
      estmemaiframe.insert(INSERT,data,'left')

    estimate_mybtn10=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=left, command=est_align_left)
    estimate_mybtn10.place(x=315, y=1)

    def est_align_right():
      data=estmemaiframe.get(0.0,END)
      estmemaiframe.tag_config('right',justify=RIGHT)
      estmemaiframe.delete(0.0,END)
      estmemaiframe.insert(INSERT,data,'right')

    estimate_mybtn11=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=right, command=est_align_right)
    estimate_mybtn11.place(x=350, y=1)

    def est_align_center():
      data=estmemaiframe.get(0.0,END)
      estmemaiframe.tag_config('center',justify=CENTER)
      estmemaiframe.delete(0.0,END)
      estmemaiframe.insert(INSERT,data,'center')

    estimate_mybtn12=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=center, command=est_align_center)
    estimate_mybtn12.place(x=385, y=1)

    estimate_mybtn13=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink)
    estimate_mybtn13.place(x=420, y=1)

    estimate_mybtn14=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove,command=lambda :estmemaiframe.delete(0.0,END))
    estimate_mybtn14.place(x=455, y=1)

    estimate_dropcomp = ttk.Combobox(estimate_emailmessage_Frame, width=12, height=7)
    estimate_dropcomp['values'] = ('Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','Active Border','Active Caption','Application','Background','Button Face','Button Highlight','Button Shadow','Button Text','Caption Text','Gradient Active','Gradient Inactive','Gray Text','Highlight Background','Highlight Text','Hot Light','Inactive Border','Inactive Caption','Inactive Caption','Info Background','Info Text','meny Background','Menu Bar','Menu Highlight','Menu Text','Scroll Bar','3D dark Shadow','3D Light','Window Background','Window Frame','Window Text')
    estimate_dropcomp.place(x=500, y=5)    
    estimate_dropcomp.current(0)

    # def est_color_select():
    #   color=colorchooser.askcolor()
    #   estmemaiframe.config(fg=color[1])

    # estimate_mybtn15=Button(estimate_emailmessage_Frame,width=31,height=23,compound = LEFT,image=color,command=est_color_select)
    # estimate_mybtn15.place(x=485, y=1)

    
    estimate_mydropcompo = ttk.Combobox(estimate_emailmessage_Frame, width=6, height=7)
    estimate_mydropcompo['values'] = ('1','2','3','4','5','6','7')
    estimate_mydropcompo.place(x=600, y=5)
    estimate_mydropcompo.current(0)
    estimate_mframe=Frame(estimate_emailmessage_Frame, height=350, width=710, bg="white")
    estimate_mframe.place(x=0, y=28)
  
    estscrollbar = Scrollbar(estimate_mframe)
    estscrollbar.place(x=20, y=120, height=5)
    estmemaiframe=Text(estimate_mframe,yscrollcommand=estscrollbar.set,font=('Helvetica',12),undo=True)
    estmemaiframe.pack(fill=BOTH,pady=5,expand=True)
    estscrollbar.config(command=estmemaiframe.yview)


    # estimate_e_btn1=Button(estimate_htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
    # estimate_e_btn2=Button(estimate_htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
    # estimate_e_btn3=Button(estimate_htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
    # estimate_e_btn4=Button(estimate_htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
    # estimate_e_mframe=Frame(estimate_htmlsourse_Frame, height=350, width=710, bg="white")
    # estimate_e_mframe.place(x=0, y=28)
    estimate_attachlbframe=LabelFrame(estimate_email_Frame,text="Attachment(s)", height=365, width=280)
    estimate_attachlbframe.place(x=740, y=5)
    estframe = StringVar()
    estimate_htcodeframe=Listbox(estimate_attachlbframe, height=13, width=43, bg="white",listvariable=estframe)
    estimate_htcodeframe.place(x=5, y=5)
    estimate_htcodeframe.bind('<Double-Button-1>',est_empsfile_image)
    estimate_lbl_btn_info=Label(estimate_attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
    estimate_e_btn17=Button(estimate_attachlbframe,image=photo,compound = LEFT,width=140,text="Add attacment file...",command=est_UploadAction)
    estimate_e_btn17.place(x=60, y=260)
    def est_deletefile():
      est_remove=estimate_htcodeframe.curselection()
      yawn=estimate_htcodeframe.get(est_remove) 
      print(yawn)       
      estimate_htcodeframe.delete(ACTIVE)
    estimate_e_btn18=Button(estimate_attachlbframe, width=20, text="Remove attacment",command=est_deletefile)
    estimate_e_btn18.place(x=60, y=305)
    estimate_lbl_tt_info=Label(estimate_email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
    estimate_lbl_tt_info.place(x=740, y=370)

    estimate_ready_frame=Frame(estimate_mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
    
    estimate_sendatalbframe=LabelFrame(estimate_account_Frame,text="E-Mail(Sender data)",height=150, width=600)
    estimate_sendatalbframe.place(x=200, y=150)
    estimate_lbl_sendermail=Label(estimate_sendatalbframe, text="Email address").place(x=120, y=30)
    estimate_sentent=Entry(estimate_sendatalbframe, width=40)
    estimate_sentent.place(x=250, y=30)
    estimate_lbl_orcompanyname=Label(estimate_sendatalbframe, text="Password").place(x=120, y=70)
    estimate_nament=Entry(estimate_sendatalbframe, width=40,show="*")
    estimate_nament.place(x=250, y=70)