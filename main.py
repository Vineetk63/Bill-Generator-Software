from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
import mysql.connector



class Main:
    def __init__(self,root):

        self.root=root
        self.root.title("Billing App")
        self.root.geometry("1280x700+0+0")
        img=Image.open("image\American Softy Shuklaganj.jpg")
        self.photo=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.photo)
        lbl_img.place(x=0,y=0,width=1380,height=150)

        #================Variable==========================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.c_email=StringVar()
        self.product=StringVar()
        self.price=IntVar()
        self.qty=IntVar()
        self.totalamt=IntVar()
        self.bill_no=IntVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.Tax=10
    




    #Product categories lit

        self.icecreams=["Vanilla","Strawberry","Butterscotch","Mango","Chocolate","Indian Special Kulfi"]



        txt_label=Label(self.root,text="Billing System",font=('times new roman',20,'bold'),bg="white",fg='blue')
        txt_label.pack(fill=X,pady=150)
        
        main_frame=Frame(self.root,bd=5,relief="groove",bg="white")
        main_frame.place(x=2,y=190,width=1280,height=490)
        #Customer frame
        cust_frame=LabelFrame(main_frame,text="Customer's info",fg="red",font=("times new roman",19,"italic"),bd=7,relief="groove",bg='white')
        cust_frame.place(x=0,y=0,width=400,height=200,anchor='nw')
        #Mobile number
        self.label_mob=Label(cust_frame,text="Mobile No-",bg="white",fg="black",font=("times new roman",15,"bold"))
        self.label_mob.grid(row=0,column=0,sticky=W,padx=5,pady=10)

        self.entry_mob=ttk.Entry(cust_frame,font=("times new roman",12,"bold"),width=15,textvariable=self.c_phone)
        self.entry_mob.grid(row=0,column=1,sticky=W,padx=5,pady=10)

        #Name
        self.label_name=Label(cust_frame,text="Name:",bg="white",fg="black",font=("times new roman",15,"bold"))
        self.label_name.grid(row=1,column=0,sticky=W,padx=5,pady=10)

        self.entry_name=ttk.Entry(cust_frame,font=("times new roman",12,"bold"),width=30,textvariable=self.c_name)
        self.entry_name.grid(row=1,column=1,sticky=W,padx=2,pady=10)

        #Email

        self.label_email=Label(cust_frame,text="Email:",bg="white",fg="black",font=("times new roman",15,"bold"))
        self.label_email.grid(row=2,column=0,sticky=W,padx=5,pady=10)

        self.entry_email=ttk.Entry(cust_frame,font=("times new roman",12,"bold"),width=30,textvariable=self.c_email)
        self.entry_email.grid(row=2,column=1,sticky=W,padx=2,pady=10)

        # Product Frame
        product_frame=LabelFrame(main_frame,text="Orders",fg="red",font=("times new roman",19,"italic"),bd=7,relief="groove",bg='white')
        product_frame.place(x=450,y=0,width=400,height=200)
        #Select category
        self.category=Label(product_frame,text="Select Category:",bg="white",font=("times new roman,",14,"bold"))
        self.category.grid(row=0,column=0,sticky=W,padx=5,pady=10)

        self.combo_category=ttk.Combobox(product_frame,value=self.icecreams,font=("times new roman",11),width=24,state="readonly",textvariable=self.product)
        self.combo_category.grid(row=0,column=1,sticky=W,padx=4,pady=10)
        #Quantity
        self.label_QTY=Label(product_frame,text="Quantity:",bg="white",fg="black",font=("times new roman",15,"bold"))
        self.label_QTY.grid(row=2,column=0,sticky=W,padx=5,pady=10)

        self.entry_QTY=ttk.Entry(product_frame,font=("times new roman",12,"bold"),width=5,textvariable=self.qty)
        self.entry_QTY.grid(row=2,column=1,sticky=W,padx=5,pady=10)

# #---------------Price
#         self.Lbprice=Label(product_frame,text="Price:",bg="white",font=("times new roman,",14,"bold"))
#         self.Lbprice.grid(row=1,column=0,sticky=W,padx=5,pady=10)

#         self.entry_price=ttk.Entry(product_frame,font=("times new roman",12,"bold"),width=10,textvariable=self.price)
#         self.entry_price.grid(row=1,column=1,sticky=W,padx=2,pady=10)





        #---------Right frame billing
        right_frame_bill=LabelFrame(main_frame,text="Bill",bg="white",fg="red",font=("times new roman",19,"italic"),bd=5,relief="groove")
        right_frame_bill.place(x=900,y=0,width=350,height=350)

        #Scroll bar
        scroll_y=Scrollbar(right_frame_bill,orient=VERTICAL)
        #Text area
        self.textarea=Text(right_frame_bill,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        #Menu Frame
        menu_frame=LabelFrame(main_frame,text="Menu",fg="red",font=("times new roman",19,"italic"),bd=4,relief="groove",bg='pink')
        menu_frame.place(x=0,y=200,width=600,height=130,anchor='nw')

        vanilla_label=Label(menu_frame,text="Vanilla-70",font=("times new roman",19,"bold"),fg="black")
        vanilla_label.grid(row=0,column=0,padx=5)
        
        straw_label=Label(menu_frame,text="Strawberry-75",font=("times new roman",19,"bold"),fg="black")
        straw_label.grid(row=0,column=1,padx=5)

        butter_label=Label(menu_frame,text="Butterscotch-85",font=("times new roman",19,"bold"),fg="black")
        butter_label.grid(row=0,column=2,padx=5)

        mango_label=Label(menu_frame,text="Mango-60",font=("times new roman",19,"bold"),fg="black")
        mango_label.grid(row=1,column=0,padx=5,pady=5)

        chocolate_label=Label(menu_frame,text="Chocolate-100",font=("times new roman",19,"bold"),fg="black")
        chocolate_label.grid(row=1,column=1,padx=5,pady=5)

        Kulfi_label=Label(menu_frame,text="Indian Special Kulfi-50",font=("times new roman",19,"bold"),fg="black")
        Kulfi_label.grid(row=1,column=2,padx=5,pady=5)



        #Bottom Frame
        # Bottom_frame=LabelFrame(main_frame,text="Operations",bg="white",fg="red",font=("times new roman",19,"italic"),bd=5,relief="groove")
        # Bottom_frame.place(x=0,y=350,width=1270,height=130)
    #     #Sub total
    #     self.label_sub_total=Label(Bottom_frame,text="Sub Total:",bg="white",fg="black",font=("times new roman",10,"bold"))
    #     self.label_sub_total.grid(row=0,column=0,sticky=W,padx=5,pady=10)

    #     self.entry_sub_total=ttk.Entry(Bottom_frame,font=("times new roman",10,"bold"),textvariable=self.subtotal,width=8)
    #     self.entry_sub_total.grid(row=0,column=1,sticky=W,padx=1,pady=1)

    # #GST
    
    #     self.label_gst=Label(Bottom_frame,text="Gov Tax:",bg="white",fg="black",font=("times new roman",10,"bold"))
    #     self.label_gst.grid(row=0,column=2,sticky=W,padx=5,pady=10)

    #     self.entry_gst=ttk.Entry(Bottom_frame,font=("times new roman",10,"bold"),textvariable=self.tax_input,width=8)
    #     self.entry_gst.grid(row=0,column=3,sticky=W,padx=1,pady=1)


        #     #Total
        # self.label_total_amount=Label(Bottom_frame,text="Total Bill:",bg="white",fg="black",font=("times new roman",10,"bold"))
        # self.label_total_amount.grid(row=1,column=0,sticky=W,padx=3,pady=10)

        # self.entry_total_amount=ttk.Entry(Bottom_frame,font=("times new roman",10,"bold"),textvariable=self.totalamt,width=8)
        # self.entry_total_amount.grid(row=1,column=1,sticky=W,padx=2,pady=1)

        #Button Frame

        buttonframe=Frame(main_frame,bd=1,bg="white",relief="groove")
        buttonframe.place(x=0,y=350,width=1270,height=130)

        #btn ADD to  cart
        self.btnaddtocart=Button(buttonframe,text="Add To Cart",command=self.Additem,font=("times new roman",25,"bold"),bg="red",fg="white")
        self.btnaddtocart.grid(row=0,column=0,padx=20,pady=10)

        #Generate bill

        self.btngenbill=Button(buttonframe,text="Generate Bill",command=self.genbil,font=("times new roman",25,"bold"),bg="red",fg="white")
        self.btngenbill.grid(row=0,column=1,padx=20,pady=20)
        #Generate bill

        # self.btngenbill=Button(buttonframe,text="Generate Bill",font=("times new roman",25,"bold"),bg="red",fg="white")
        # self.btngenbill.grid(row=0,column=1,padx=20,pady=20)

        #Save Bill
        self.btnsavebill=Button(buttonframe,text="Save Bill",command=self.savebill,font=("times new roman",25,"bold"),bg="red",fg="white")
        self.btnsavebill.grid(row=0,column=2,padx=20,pady=20)
        #print bill

        self.btnprintbill=Button(buttonframe,text="Print Bill",command=self.iprint,font=("times new roman",25,"bold"),bg="red",fg="white")
        self.btnprintbill.grid(row=0,column=3,padx=20,pady=20)
        #Clear


        self.btnclear=Button(buttonframe,text="Clear",command=self.clear,font=("times new roman",25,"bold"),bg="red",fg="white")
        self.btnclear.grid(row=0,column=4,padx=20,pady=20)        

        #Exit
        self.btnexit=Button(buttonframe,text="Exit",command=self.root.destroy,font=("times new roman",25,"bold"),bg="red",fg="white")
        self.btnexit.grid(row=0,column=5,padx=20,pady=20)    
        self.welcome()
        self.l=[]
    #===================================Functions definition

    def clear(self):
        self.textarea.delete(1.0,END)
        
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.product.set('')
        self.price.set(0)
        self.qty.set(0)
        self.l=[0]
        self.totalamt.set(0)
        self.welcome()


    def iprint(self):
        q=self.textarea.get(1.0,"end -1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")




    def savebill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill ?")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('Bills/'+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            op=messagebox.showinfo("saved",f"Saved Bill no:{self.bill_no.get()} Sucessfully")
            f1.close()
        mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vin#@0786",
        database="shop"
        )
        c=mydb.cursor()
        sql="INSERT INTO customer(name,number,email,totalbill,bill_num) VALUES(%s,%s,%s,%s,%s)"
        ab=(self.c_name.get(),self.c_phone.get(),self.c_email.get(),self.totalamt.get(),self.bill_no.get())
        c.execute(sql,ab)
        mydb.commit()
        







    def genbil(self):
        if self.product.get()=="":
            messagebox.showerror("error","Please Add to Cart the order  first")
        else:
            test=self.textarea.get(9.0,(9.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,test)
            self.textarea.insert(END,"===================================")
            self.textarea.insert(END,f"\n\t\t Total Amount: {self.totalamt.get()}")
            #self.textarea.insert(END,"/n=================")
            self.textarea.insert(END,f"\n\n  \tThanks For Shopping with us ")



    def Additem(self):
        if self.product.get()=="Vanilla":
            self.price.set(70)
        elif self.product.get()=="Strawberry":
            self.price.set(75)
        elif self.product.get()=="Butterscotch":
            self.price.set(85)
        elif self.product.get()=="Mango":
            self.price.set(60)
        elif self.product.get()=="Chocolate":
            self.price.set(100)
        elif self.product.get()=="Indian Special Kulfi":
            self.price.set(50)

        self.n=self.price.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("error","Please select the Order first")

        else:
            self.textarea.insert(END,f"{self.product.get()}\t\t\t {self.qty.get()}\t{self.m}\n")
            #
            # self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.price.get()))*self.Tax)/100)))    
            self.totalamt.set(str(sum(self.l)))

    



    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"   Welcome in American softy Shuklaganj")
        self.textarea.insert(END,f"\n\n Bill number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n\n Customer name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n phome number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n===================================")
        self.textarea.insert(END,f"\n Orders\t\t\tQTY\tPrice")
        self.textarea.insert(END,f"\n===================================")




















if __name__=='__main__':
    root=Tk()
    obj=Main(root)
    root.mainloop()
























