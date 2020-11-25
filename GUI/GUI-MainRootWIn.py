from tkinter import *
from myDBFunc import *
from tkinter import messagebox


class RootWin() :
    def __init__(self) :
        root = Tk()
        p1 = PhotoImage(file = 'tg.png')
        root.iconphoto(False, p1)
        root.title("TailorGuide V.1.1.0")
        header = Label(root, text="Main menu",font="impact 30")
        header.grid(row=0,column=1,padx=80)
        bsearch = Button(root, text="Request Stylist",font="Helvetica 15",width=20,command=self.popSearchWin)
        bsearch.grid(row=1,column=1,pady=5)
        baddSt = Button(root, text="Add Stylist",font="Helvetica 15",width=20,command=self.popAddStylistWin)
        baddSt.grid(row=2,column=1,pady=5)
        bupSt = Button(root, text="Request Management",font="Helvetica 15",width=20,command=self.popRequestWin)
        bupSt.grid(row=3,column=1,pady=5)
        bdelSt = Button(root, text="Delete Stylist",font="Helvetica 15",width=20,command=self.popDeleteStylistWin)
        bdelSt.grid(row=4,column=1,pady=5)


        root.geometry('388x494')
        root.mainloop()
    
    def popSearchWin(self) :
        s = SearchWin("Search Stylist")
        
    def popAddStylistWin(self) :
        a = AddStylistWin("Add Stylist")
        
    def popDeleteStylistWin(self) :
        d = DeleteStylistWin("Delete Stylist")
    
    def popRequestWin(self) :
        r = RequestWin("Request Management")
        
    def exitProgram(self) :
        exit()



class CustomerWindow() :
    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('200x150+100+100')
        
        self.label_id=Label(self.cwin, text="Id = ")
        self.label_name=Label(self.cwin, text="Name = ")

        self.entry_id=Entry(self.cwin)
        self.entry_name=Entry(self.cwin)

        self.button_submit=Button(self.cwin, text ="SUBMIT", command=self.cwin.destroy)
        self.button_exit=Button(self.cwin, text="EXIT", command=self.cwin.destroy)

        self.label_id.grid(row=0,column=0)
        self.label_name.grid(row=1,column=0)
        
        self.entry_id.grid(row=0,column=1)
        self.entry_name.grid(row=1,column=1)

        self.button_submit.grid(row=2,column=1)
        self.button_exit.grid(row=3, column=1)

        self.label_status=Label(self.cwin, text="")
        self.label_status.grid(row=5, columnspan=2)
        

class DeleteStylistWin() :
    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('388x494')
        self.header=Label(self.cwin,text="Delete Stylist",font="ipact 30").grid(row=0,column=0,pady=10)
        self.label_username=Label(self.cwin, text="UserName").grid(row=1,column=0,padx=160)
            
        self.entry_Username = Entry(self.cwin)
        self.entry_Username.grid(row=2)
        self.button_submit=Button(self.cwin, text ="DELETE", command=self.deleteStylist).grid(row=5,pady=10)

    def deleteStylist(self) :
        dataentry = [self.entry_Username.get()]
        aCustomer = Customer(dataentry)
        retmsg = aCustomer.delete()
        messagebox.showinfo(parent=self.cwin,title='Result', message=retmsg[1])

class AddStylistWin() :
    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('388x494')
        self.header=Label(self.cwin,text="Add Stylist",font="impact 30").grid(row=0,column=0,pady=10,columnspan=2,padx=80)
        self.label_SSN=Label(self.cwin, text="SSN").grid(row=1,column=0,pady=5)
        self.entry_SSN = Entry(self.cwin)
        self.entry_SSN.grid(row=1,column=1,pady=5)
        self.label_username=Label(self.cwin, text="UserName").grid(row=2,column=0,pady=5,padx=10)
        self.entry_username = Entry(self.cwin)
        self.entry_username.grid(row=2,column=1,pady=5)
        self.label_firstname=Label(self.cwin, text="Firstname").grid(row=3,column=0,pady=5)
        self.entry_firstname = Entry(self.cwin)
        self.entry_firstname.grid(row=3,column=1,pady=5)
        self.label_lastname=Label(self.cwin, text="Lastname").grid(row=4,column=0,pady=5)
        self.entry_lastname = Entry(self.cwin)
        self.entry_lastname.grid(row=4,column=1,pady=5)
        self.label_phonenumber=Label(self.cwin, text="Phone NO.").grid(row=5,column=0,pady=5)
        self.entry_phonenumber = Entry(self.cwin)
        self.entry_phonenumber.grid(row=5,column=1,pady=5)
        self.label_bio=Label(self.cwin, text="Bio").grid(row=6,column=0,pady=5)
        self.entry_bio = Entry(self.cwin)
        self.entry_bio.grid(row=6,column=1,pady=5)
        
        alist = Customer(("t","t"))
        alist.allstyle()
        self.ltstyle = Listbox(self.cwin,height=5)
        self.label_style=Label(self.cwin, text="Select your styles").grid(row=7,column=0,pady=5,sticky="n")
        self.ltstyle.grid(row=7,column=1)
        for i in alist.getInfo() :
            self.ltstyle.insert(END, i[0])
        
        
        self.button_submit=Button(self.cwin, text ="CONFIRM", command=self.addStylist).grid(row=8,columnspan=2,pady=10)

    def addStylist(self) :
        index=self.ltstyle.curselection()[0]
        dataentry = [self.entry_SSN.get(),self.entry_username.get(),self.entry_firstname.get(),self.entry_lastname.get(),self.entry_phonenumber.get(),self.entry_bio.get(),self.ltstyle.get ( index, last=None )]
        aCustomer1 = Customer(dataentry)
        retmsg = aCustomer1.addStylist()
        messagebox.showinfo(parent=self.cwin,title='Result', message=retmsg[1])

            
class SRequestWin() :
    def __init__(self,title) :
        self.qwin = Toplevel()
        self.qwin.title(title)
        self.qwin.geometry('250x100')
        self.header = Label(self.qwin,text="Do you want to sent request?").grid(row=0,columnspan=2,padx=10)
        self.bConfirm = Button(self.qwin,text ="CONFIRM",command=self.confirmSent).grid(row=1,column=0,pady=10)
        self.bCancel = Button(self.qwin,text ="CANCEL",command=self.cancelSent).grid(row=1,column=1,pady=10)
        
    def confirmSent(self) :
        conCustomer = Customer("")
        conCustomer.conSent()
        self.qwin.destroy()
    def cancelSent(self) :
        canCustomer = Customer("")
        canCustomer.canSent()
        self.qwin.destroy()
class SearchWin() :
    def __init__(self, title) :
        self.swin = Toplevel()
        self.swin.title(title)
        self.swin.geometry('388x600')
        header = Label(self.swin, text="Request Stylist",font="impact 30")
        header.grid(row=0,padx=40,columnspan=2)
        
        self.cUsername = Label(self.swin,text="Customer Username",font="Helvetica 15")
        self.cUsername.grid(row=1,column=0)
        self.eUsername = Entry(self.swin,width= 15)
        self.eUsername.grid(row=1,column=1,sticky="W")
        
        self.lb2 = Label(self.swin, text="Style")
        self.lb2.grid(row=3,columnspan=2)

        alist = Customer(("t","t"))
        alist.allstyle()
        self.ltstyle = Listbox(self.swin,height=4)
        self.ltstyle.grid(row=4,columnspan=2)
        for i in alist.getInfo() :
            self.ltstyle.insert(END, i[0])

        bupdate = Button(self.swin, text="search",font="Helvetica 15",width=20,command=self.searchCust)
        bupdate.grid(row=5,pady=10,columnspan=2)

        self.lr = Listbox(self.swin,width=30)
        self.lr.grid(row=6,columnspan=2)
        bSendReq = Button(self.swin, text="Send Request",font="Helvetica 15",width=20,command=self.sendRequest)
        bSendReq.grid(row=7,pady=10,columnspan=2)
        self.uCustomer = Customer("")
    def searchCust(self) :
        self.swin.title("Searched")
        index=self.ltstyle.curselection()[0]
        dataentry = [self.ltstyle.get(index, last=None)]
        aCustomer = Customer(dataentry)
        self.uCustomer = aCustomer
        retmsg = aCustomer.searchName()

        if retmsg[0] == "0" :
            self.lr.delete(0, END)
            for i in aCustomer.getInfo() :
                self.lr.insert(END,"{:<15}{:^10}{:>15}".format(i[1],i[4],i[5]))
    
    def sendRequest(self) :
        index1=self.lr.curselection()[0]
        self.dataentry = [self.uCustomer.getInfo()[index1][0],self.eUsername.get(),"a"]
        fCustomer = Customer(self.dataentry)
        retmsg = fCustomer.sentingRequest()
        q = SRequestWin("Comfirm")
        #messagebox.showinfo(parent=self.swin,title='Result', message=retmsg[1])
        
class RequestWin() :
    def __init__(self, title) :
        self.swin = Toplevel()
        self.swin.title(title)
        self.swin.geometry('388x494')
        header = Label(self.swin, text="Request Management",font="impact 25")
        header.grid(row=0,padx=5,columnspan=3)

        self.lb2 = Label(self.swin, text="Username :",font="Times 12")
        self.lb2.place(x=30,y=60)

        self.ename = Entry(self.swin,font="Times 15",width=10)
        self.ename.place(x=125,y=60)
#         alist = Customer(("t","t"))
#         alist.allstyle()
#         self.ltstyle = Listbox(self.swin,height=4)
#         self.ltstyle.grid(row=4)
#         for i in alist.getInfo() :
#             self.ltstyle.insert(END, i[0])
        self.rid = []
        bupdate = Button(self.swin, text="search",font="Times 13",width=5,command=self.searchCust)
        bupdate.place(x=270,y=55)

        self.lr = Listbox(self.swin,width=37)
        self.lr.place(x=45,y=100)
        
        bac = Button(self.swin, text="Accept",font="Helvetica 10",width=10,command=self.acceptRe)
        bac.place(x=45,y=350)
        bde = Button(self.swin, text="Decline",font="Helvetica 10",width=10,command=self.declineRe)
        bde.place(x=205,y=350)
        
    def searchCust(self) :
        self.rid.clear()
        self.swin.title("Searched")
        dataentry = [self.ename.get()]
        aCustomer = Customer(dataentry)

        retmsg = aCustomer.searchRequest()

        if retmsg[0] == "0" :
            self.lr.delete(0, END)
            for i in aCustomer.getInfo() :
                self.rid.append(i[0])
                self.lr.insert(END, "Id :"+str(i[0])+" "+str(i[1])+" status :"+str(i[2]))
                
    def acceptRe(self) :
        self.swin.title("Searched")
        index=self.lr.curselection()[0]
        dataentry = [int(self.rid[index])]
        aCustomer = Customer(dataentry)
    
        retmsg = aCustomer.acceptRe()
        messagebox.showinfo(parent=self.swin,title='Result', message=retmsg[1])
        self.searchCust()
                
    def declineRe(self) :
        self.swin.title("Searched")
        index=self.lr.curselection()[0]
        dataentry = [int(self.rid[index])]
        aCustomer = Customer(dataentry)

        retmsg = aCustomer.declineRe()
        messagebox.showinfo(parent=self.swin,title='Result', message=retmsg[1])
        self.searchCust()

#Exercise Search by Name
class SearchNameWin(CustomerWindow) :
    def __init__(self, title,cname) :
        super().__init__(title)
        
        self.cwin.title("Searched")
        dataentry = ["test",cname]
        aCustomer = Customer(dataentry)
        
        retmsg = aCustomer.searchName()

        if retmsg[0] == "0" :
            self.entry_id.delete(0, END)
            self.entry_id.insert(0, aCustomer.getInfo()[0])
            self.entry_name.delete(0, END)
            self.entry_name.insert(0, aCustomer.getInfo()[1])
            
        else :
            self.entry_id.delete(0, END)
            self.entry_id.insert(0, "?????")
        self.label_status.config(text=retmsg[1])
        
class RegisterWin(CustomerWindow) :
    def __init__(self, title) :
        super().__init__(title)
        self.button_submit.configure(text="AddNew", command=self.submitNewCust)
        
    def submitNewCust(self) :
        self.cwin.title("Submitted")
        dataentry = [self.entry_id.get(), self.entry_name.get()]
        aCustomer = Customer(dataentry)
        retmsg = aCustomer.write()
        self.label_status.config(text=retmsg[1])
Mainmenu = RootWin()
