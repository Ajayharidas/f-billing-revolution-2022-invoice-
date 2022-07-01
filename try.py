
inv_sql = "SELECT * FROM invoice WHERE stop_recurring_check=%s"
inv_val = (0,)
fbcursor.execute(inv_sql,inv_val)
inv_data = fbcursor.fetchall()
today = dt.datetime.today().date()
try:
  def auto_msg(subject="test",text="",img=None,attachment=None):
    msg = MIMEMultipart()
    msg['subject'] = subject
    msg.attach(MIMEText(text))
    if img is not None:
      if type(img) is not list:
        img = [img]
      for one_img in img:
        img_data = open(one_img,'rb').read()
        msg.attach(MIMEImage(img_data,name=os.path.basename(one_img)))
    if attachment is not None:
      if type(attachment) is not list:
        attachment = [attachment]
      for one_attachment in attachment:
        with open(one_attachment,'rb') as f:
          file = MIMEApplication(f.read(),name=os.path.basename(one_attachment))
        file['Content-Disposition'] = f'attachment;\
          filename = "{os.path.basename(one_attachment)}"'
        msg.attach(file)
    return msg
  def auto_mail():
    sender_mail = "infoxfbilling77@gmail.com"
    sender_password = "dinkiurlziohgfok"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_mail,sender_password)

    msg = auto_msg("Good!","Hi there!",r"C:\Users\AJAY\tkinter\Project\F-Billing Revolution 2022_ajay\F-Billing Revolution 2022\F-Billing Revolution 2022\images\default.png",r"C:\Users\AJAY\tkinter\Project\F-Billing Revolution 2022_ajay\F-Billing Revolution 2022\F-Billing Revolution 2022\Invoice Documents\INV00002.pdf")
    to = ["ajayharidas77@gmail.com",]
    try:
      for i in inv_data:
        if i[25] == "Month(s)":
          print("yes")
          if int(today.month) == int(i[26].month):
            print("yes")
            if int(today.day) == int(i[26].day):
              print("yes")
              server.sendmail(from_addr=sender_mail,to_addrs=to,msg=msg.as_string())
              print("test successfull")
              server.quit()
            else:
              pass
          else:
            pass
        else:
          pass
    except:
      pass
  schedule.every().day.at("6:01:00").do(auto_mail)
  while True:
    schedule.run_pending()
    time.sleep(1)
except:
  pass