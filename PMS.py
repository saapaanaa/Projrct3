from tkinter import *
import pymysql
from matplotlib import pyplot as plt
from matplotlib import style


conn = pymysql.connect(host="localhost", user="root", passwd="", db="my_python1")
myCursor = conn.cursor()

class welcome():
    def __init__(self,master):
        self.master=master
        self.master.title("WELCOME TO VTU")
        self.master.geometry('500x400')

        #self.master.config(bg='linen')

        self.photo1 = PhotoImage(file="camp2.png", height='1270', width='1210')

        self.label6 = Label(master, image=self.photo1).place(x=15, y=60)

        #self.photo1 = PhotoImage(file="camp.png", height='5570', width='4610')

        #self.label6 = Label(master, image=self.photo1, bg='linen').place(x=100, y=20)
        self.label6=Label(self.master, text="Publication management system", font=("Times new roman Bold", 20)).place(x=45, y=10)

        self.button2 = Button(self.master, text="Institute", font=("Times New Roman Bold", 16), command=self.goto1).place(x=25, y=150)
        self.button2 = Button(self.master, text="Department", font=("Times New Roman Bold", 16),command=self.goto2).place(x=25, y=200)
        self.button2 = Button(self.master, text="Faculty", font=("Times New Roman Bold", 16),command=self.goto3).place(x=25, y=250)
        self.button1 = Button(self.master, text="Publish", font=("Times New Roman Bold",16),command=self.goto4).place(x=25, y=300)
        #self.button1 = Button(self.master, text="Citation", font=("Times New Roman Bold", 16),command=self.goto5).place(x=250, y=350)

        self.button5 = Button(self.master, text="cancle", font = ("Times New Roman Bold", 12),command=self.myquit2,bg='red').place(x=250,y=350)
    def myquit2(self):
        self.master.destroy()

    def goto1(self):
        root1 = Toplevel(self.master)
        institute(root1)

    def goto2(self):
        root2 = Toplevel(self.master)
        department(root2)

    def goto3(self):
        root3 = Toplevel(self.master)
        faculty(root3)

    def goto4(self):
        root4 = Toplevel(self.master)
        publish(root4)

class institute():

    def __init__(self, master):
        self.iname = StringVar()
        self.iaddr = StringVar()
        self.icode = IntVar()

        self.master = master
        self.master.geometry('350x250')
        self.master.config(bg='white')
        #self.photo = PhotoImage(file="inss.png", height='1070', width='910')
        #self.label6 = Label(master, image=self.photo, bg='linen').place(x=5, y=1)
        self.label6 = Label(self.master, text="Institute details", font=("Times new roman Bold", 20),bg='white').place(x=85, y=5)
        self.label1 = Label(self.master, text='Institute Name',font = ("Times New Roman Bold", 12),bg='white').place(x=5,y=50)
        self.id = Entry(self.master, textvariable=self.iname,font = ("Times New Roman Bold", 12)).place(x=150, y=50)

        self.label1 = Label(self.master, text='Institute Address',font = ("Times New Roman Bold", 12),bg='white').place(x=5, y=100)
        self.i = Entry(self.master, textvariable=self.iaddr,font = ("Times New Roman Bold", 12)).place(x=150, y=100)

        self.label2 = Label(self.master, text='Code',font = ("Times New Roman Bold", 12),bg='white').place(x=5, y=150)
        self.i1 = Entry(self.master, textvariable=self.icode,font = ("Times New Roman Bold", 12)).place(x=150, y=150)

        self.button2 = Button(self.master, text='submit', command=self.submit1,font = ("Times New Roman Bold", 12),bg='white').place(x=150, y=200)
        self.button3 = Button(self.master, text='back', command=self.myquit1,font = ("Times New Roman Bold", 12),bg='white').place(x=230, y=200)
    def myquit1(self):
        self.master.destroy()
    def submit1(self):
        s11=self.iname.get()
        s12=self.iaddr.get()
        s13= self.icode.get()

        #myCursor.execute("""CREATE TABLE institute(iname varchar(20),iaddr varchar(20),icode int(10))""")
        myCursor.execute('INSERT INTO institute5(iname,iaddr,icode) VALUES(%s,%s,%s);', (s11,s12,s13))
        conn.commit()

class department():

    def __init__(self, master):
        self.dept_name = StringVar()

        self.dept_id = IntVar()
        self.inst_code= IntVar()

        self.master = master
        self.master.geometry('350x250')
        self.master.config(bg='white')
        #self.photo = PhotoImage(file="d.png", height='870', width='710')
        #self.label6 = Label(master, image=self.photo, bg='linen').place(x=10, y=20)
        self.label6 = Label(self.master, text="Department details", font=("Times new roman Bold", 20),bg='white').place(x=45, y=4)

        self.label1 = Label(self.master, text='Department Name',font = ("Times New Roman Bold", 12),bg='white').place(x=10,y=60)
        self.id = Entry(self.master, textvariable=self.dept_name,font = ("Times New Roman Bold", 12)).place(x=160, y=60)

        self.label2 = Label(self.master, text='Department ID',font = ("Times New Roman Bold", 12),bg='white').place(x=10, y=100)
        self.i1 = Entry(self.master, textvariable=self.dept_id,font = ("Times New Roman Bold", 12)).place(x=160, y=100)

        self.label1 = Label(self.master, text='Institute Code', font=("Times New Roman Bold", 12),bg='white').place(x=10, y=140)
        self.i3 = Entry(self.master, textvariable=self.inst_code, font=("Times New Roman Bold", 12)).place(x=160, y=140)

        self.button2 = Button(self.master, text='submit', command=self.submit2,font = ("Times New Roman Bold", 12)).place(x=10, y=180)
        self.button2 = Button(self.master, text='Graph', command=self.graph2,font=("Times New Roman Bold", 12)).place(x=90, y=180)

        self.button3 = Button(self.master, text='back', command=self.myquit1,font = ("Times New Roman Bold", 12)).place(x=150, y=180)
    def myquit1(self):
        self.master.destroy()
    def submit2(self):
        k1=self.dept_name.get()
        #k2=self.fac_id.get()
        k2=self.dept_id.get()
        k3=self.inst_code.get()
        #myCursor.execute("""CREATE TABLE Department(dept_name varchar(20),fac_id int(10),dept_id int(10),inst_code int (10)""")
        myCursor.execute('INSERT INTO department5(dept_name,dept_id,inst_code) VALUES(%s,%s,%s);', (k1,k2,k3))
        conn.commit()

    def graph2(self):
        myCursor.execute("select department5.dept_name,count(publish5.title)from institute5 join department5 on institute5.icode = department5.inst_code join faculty5 on department5.dept_id = faculty5.dep_id join publish5 on publish5.fact_id = faculty5.fac_id group by department5.dept_name")
        myresult = myCursor.fetchall()

        # print(myresult)
        # for x in myresult:
        # print(x)
        list1, list2 = zip(*myresult)
        print(list1)
        print(list2)

        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        plt.pie(list2, labels=list1, colors=colors, startangle=90, autopct='%.1f%%')
        plt.axis('equal')
        plt.title('Over All Department')
        plt.tight_layout()
        plt.show()

        conn.commit()

class  faculty():

    def __init__(self, master):
        self.fac_name = StringVar()
        self.fac_id = IntVar()
        self.date_updated = StringVar()


        self.dep_id=IntVar()

        self.master = master
        self.master.geometry('450x350')
        self.master.config(bg='white')
        #self.photo = PhotoImage(file="kk1.png", height='870', width='710')
        #self.label6 = Label(master, image=self.photo).place(x=5, y=5)
        self.label6 = Label(self.master, text="Faculty details", font=("Times new roman Bold", 20),bg='white').place(x=130, y=3)

        self.label1 = Label(self.master, text='Faculty Name',font = ("Times New Roman Bold", 12),bg='white').place(x=70,y=60)
        self.id = Entry(self.master, textvariable=self.fac_name,font = ("Times New Roman Bold", 12)).place(x=200, y=60)

        self.label1 = Label(self.master, text='Faculty ID',font = ("Times New Roman Bold", 12),bg='white').place(x=70, y=100)
        self.i = Entry(self.master, textvariable=self.fac_id,font = ("Times New Roman Bold", 12)).place(x=200, y=100)

        self.label2 = Label(self.master, text='Date Updated',font = ("Times New Roman Bold", 12),bg='white').place(x=70, y=140)
        self.i1 = Entry(self.master, textvariable=self.date_updated,font = ("Times New Roman Bold", 12)).place(x=200, y=140)
        self.date_updated.set(u"YYYY/DD/MM")
        self.label2 = Label(self.master, text='Department ID', font=("Times New Roman Bold", 12),bg='white').place(x=70, y=180)
        self.i1 = Entry(self.master, textvariable=self.dep_id, font=("Times New Roman Bold", 12)).place(x=200, y=180)

        self.button2 = Button(self.master, text='submit', command=self.submit3,font = ("Times New Roman Bold", 12),bg='white').place(x=70, y=250)
        self.button2 = Button(self.master, text='Graph', command=self.graph3, font=("Times New Roman Bold", 12),bg='white').place(x=140, y=250)
        self.button3 = Button(self.master, text='back', command=self.myquit1,font = ("Times New Roman Bold", 12),bg='white').place(x=200, y=250)

    def myquit1(self):
        self.master.destroy()

    def submit3(self):
        k11=self.fac_name.get()
        k12=self.fac_id.get()
        k13= self.date_updated.get()
        k14=self.dep_id.get()

        #myCursor.execute("""CREATE TABLE Faculty(fac_name varchar(20),fac_id int(10),date_updated int(10),indx int(10),imp_fact int(10))""")
        myCursor.execute('INSERT INTO faculty5(fac_name,fac_id,date_updated,dep_id) VALUES(%s,%s,%s,%s);', (k11,k12,k13,k14))
        conn.commit()

    def graph3(self):
        myCursor.execute("select year(date_updated),count(year(date_updated)) from faculty5 group by year(date_updated)")

        myresult = myCursor.fetchall()
        # print(myresult)
        list1, list2 = zip(*myresult)

        print(list1)
        print(list2)

        style.use('ggplot')
        plt.bar(list1, list2, color='b')
        plt.title('Publication Management system')
        plt.xlabel('year of publication')
        plt.ylabel('articles')
        plt.show()
        conn.commit()


class publish():
    def __init__(self, master):
        self.ref_id = IntVar()
        self.title = StringVar()
        self.first_author = StringVar()
        self.second_author = StringVar()

        self.type = StringVar()
        self.imp_fact = IntVar()
        self.publisher = StringVar()
        self.credit_to_fac = IntVar()
        self.pp = IntVar()
        self.volume = IntVar()

        self.fact_id=IntVar()

        self.master = master
        self.master.geometry('500x600')
        self.master.config(bg='white')
        #self.photo = PhotoImage(file="p11.png", height='1070', width='810')
        #self.label6 = Label(master, image=self.photo).place(x=10, y=60)
        self.label6 = Label(self.master, text="Publishment Details", font=("Times new roman Bold", 17),bg='white').place(x=170,y=5)

        self.label1 = Label(self.master, text='Reference ID', font=("Times New Roman Bold", 12),bg='white').place(x=100, y=60)
        self.id = Entry(self.master, textvariable=self.ref_id, font=("Times New Roman Bold", 12)).place(x=250,y=60)

        self.label3 = Label(self.master, text='Tittle', font=("Times New Roman Bold", 12),bg='white').place(x=100, y=100)
        self.i1 = Entry(self.master, textvariable=self.title, font=("Times New Roman Bold", 12)).place(x=250, y=100)

        self.label4 = Label(self.master, text='First Author', font=("Times New Roman Bold", 12),bg='white').place(x=100,y=140)
        self.i2 = Entry(self.master, textvariable=self.first_author, font=("Times New Roman Bold", 12)).place(x=250, y=140)

        self.label4 = Label(self.master, text='Second Author', font=("Times New Roman Bold", 12),bg='white').place(x=100,y=180)
        self.i2 = Entry(self.master, textvariable=self.second_author, font=("Times New Roman Bold", 12)).place(x=250, y=180)

        self.label5 = Label(self.master, text='Impact factor', font=("Times New Roman Bold", 12),bg='white').place(x=100, y=220)
        self.i2 = Entry(self.master, textvariable=self.imp_fact, font=("Times New Roman Bold", 12)).place(x=250,y=220)

        self.label6 = Label(self.master, text='Publisher', font=("Times New Roman Bold", 12),bg='white').place(x=100, y=260)
        self.i2 = Entry(self.master, textvariable=self.publisher, font=("Times New Roman Bold", 12)).place(x=250, y=260)

        self.label7 = Label(self.master, text='Credits To Faculty ', font=("Times New Roman Bold", 12),bg='white').place(x=100, y=300)
        self.i2 = Entry(self.master, textvariable=self.credit_to_fac , font=("Times New Roman Bold", 12)).place(x=250, y=300)

        self.label7 = Label(self.master, text='Page Number', font=("Times New Roman Bold", 12),bg='white').place(x=100, y=340)
        self.i2 = Entry(self.master, textvariable=self.pp, font=("Times New Roman Bold", 12)).place(x=250,y=340)

        self.label8 = Label(self.master, text='Volume', font=("Times New Roman Bold", 12),bg='white').place(x=100, y=380)
        self.i2 = Entry(self.master, textvariable=self.volume, font=("Times New Roman Bold", 12)).place(x=250, y=380)

        self.label9 = Label(self.master, text='Faculty ID', font=("Times New Roman Bold", 12),bg='white').place(x=100, y=420)
        self.i2 = Entry(self.master, textvariable=self.fact_id, font=("Times New Roman Bold", 12)).place(x=250, y=420)

        self.label10 = Label(master, text="Type of Journal\n", width=20, font=("Times New Roman Bold", 12),bg='white').place(x=0,y=460)
        self.list1 = ['International Journal', 'National Journal', 'International conference','National conference']

        self.droplist = OptionMenu(self.master, self.type, *self.list1)
        self.droplist.config(width=30,bg='white')
        self.type.set('Select Type')
        self.droplist.place(x=200, y=460)

        self.button2 = Button(self.master, text='submit', command=self.submit4,font=("Times New Roman Bold", 12)).place(x=230, y=500)
        self.button2 = Button(self.master, text='Institute Graph', command=self.graph4,font=("Times New Roman Bold", 12)).place(x=80, y=540)
        self.button2 = Button(self.master, text='College Graph', command=self.graph5, font=("Times New Roman Bold", 12)).place(x=200, y=540)
        self.button2 = Button(self.master, text='Faculty Graph', command=self.graph6,font=("Times New Roman Bold", 12)).place(x=320, y=540)

    def submit4(self):
        a11 = self.ref_id.get()
        a12 = self.title.get()
        a13 = self.first_author.get()
        a14 = self.second_author.get()

        a16 = self.type.get()
        a17 = self.imp_fact.get()
        a18 = self.publisher.get()
        a118=self.credit_to_fac.get()
        a19 = self.pp.get()
        a20 = self.volume.get()

        a22 =self.fact_id.get()
        #myCursor.execute("""CREATE TABLE p2(ref_id int(10),title varchar(20),first_author varchar(20),second_author varchar(20),other_author varchar(20), type varchar(20), imp_fact int(10), publisher varchar(20), pp varchar(20),volume int(10), other_details varchar(20))""")
        myCursor.execute('INSERT INTO publish5(ref_id,title,first_author,second_author,type,imp_fact,publisher,credit_to_fac,pp,volume,fact_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',(a11, a12, a13, a14, a16, a17, a18,a118, a19, a20,a22))

        conn.commit()

    def graph4(self):
        myCursor.execute(
            "select institute5.iname,count(publish5.title) from institute5 join department5 on institute5.icode = department5.inst_code join faculty5 on department5.dept_id = faculty5.dep_id join publish5 on publish5.fact_id = faculty5.fac_id group by institute5.iname")
        myresult = myCursor.fetchall()

        # print(myresult)
        # for x in myresult:
        # print(x)
        list1, list2 = zip(*myresult)
        print(list1)
        print(list2)

        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        plt.pie(list2, labels=list1, colors=colors, startangle=90, autopct='%.1f%%')
        plt.axis('equal')
        plt.title('Over All Institutions')
        plt.tight_layout()
        plt.show()

        conn.commit()

    def graph5(self):
        myCursor.execute("select department5.dept_name,count(publish5.title)from institute5 join department5 on institute5.icode = department5.inst_code join faculty5 on department5.dept_id = faculty5.dep_id join publish5 on publish5.fact_id = faculty5.fac_id where institute5.iname = 'KLE' group by department5.dept_name")
        myresult = myCursor.fetchall()

        # print(myresult)
        # for x in myresult:
        # print(x)
        list1, list2 = zip(*myresult)
        print(list1)
        print(list2)

        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        plt.pie(list2, labels=list1, colors=colors, startangle=90, autopct='%.1f%%')
        plt.axis('equal')
        plt.title('Perticular Institution: KLE')
        plt.tight_layout()
        plt.show()

        conn.commit()

    def graph6(self):
        myCursor.execute("select faculty5.fac_id,count(publish5.title)from institute5 join department5 on institute5.icode = department5.inst_code join faculty5 on department5.dept_id = faculty5.dep_id join publish5 on publish5.fact_id = faculty5.fac_id where department5.dept_name = 'CSE' group by faculty5.fac_id")
        myresult = myCursor.fetchall()

        # print(myresult)
        # for x in myresult:
        # print(x)
        list1, list2 = zip(*myresult)
        print(list1)
        print(list2)

        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        plt.pie(list2, labels=list1, colors=colors, startangle=90, autopct='%.1f%%')
        plt.axis('equal')
        plt.title('CSE Department')
        plt.tight_layout()
        plt.show()

        conn.commit()

        conn.close()

def main():
    root = Tk()
    welcome(root)

    root.mainloop()

if __name__ == '__main__':
    main()
