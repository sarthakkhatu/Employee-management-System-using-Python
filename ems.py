from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import requests



def add_f1():
	root.withdraw()
	aw.deiconify()

def view_f2():
	root.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0, END)
	con = None
	try:
		con = connect("emp.db")
		cursor = con.cursor()
		sql = "select * from employee order by id"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + "id = " +str(d[0]) +","  + "  name =" +str(d[1])  +"," +   "  salary =" +str (d[2]) +" \n"+"********************************************************" +"\n"
		vw_st_data.insert(INSERT, info)
	except Exception as e:
		showerror("Issue ", e)
	finally:
		if con is not None:
			con.close()			

def update_f3():
	root.withdraw()
	uw.deiconify()

def delete_f4():
	root.withdraw()
	dw.deiconify()

def add_save_f5():
	con = None
	try:
		con = connect("emp.db")
		cursor = con.cursor()
		sql = "insert into employee values('%d', '%s', '%d')"
		id = int(aw_ent_id.get())
		#if id is None:
		if cursor.rowcount != 1 :

			if id >= 1 :
				name = aw_ent_name.get()

				if len(name) >= 2:
					if name.isalpha():
						salary = int(aw_ent_salary.get())
						if salary > 8000:
							cursor.execute(sql %(id, name, salary))
							con.commit()
							showinfo("Success", "Record Created!!")
						else:
							showerror("Failed", "Salary Should be Minimum 8000")
					else: 
						showerror("Failed", "Name should contain alphabets only ")
				else:
					showerror("Failed", "Name should contain minimum two alphabets!!")

			else:
				showerror("Failed", "ID should have only positive integers!!")

		else:
			showerror("Failed", "already exists!!")
	except ValueError:
		con.rollback()
		showerror("Failed ", "Enter only integer value")



	except IntegrityError:
		con.rollback()
		showerror("Failed", "Id already exist")
	finally:
		if con is not None:
			con.close()
		aw_ent_id.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_salary.delete(0, END)
		aw_ent_id.focus()

def add_back_f6():
	aw.withdraw()
	root.deiconify()

def view_back_f7():
	vw.withdraw()
	root.deiconify()

def update_save_f8():
	con = None
	try:
		con = connect("emp.db")
		cursor = con.cursor()
		sql = "update employee set salary = '%d', name = '%s' where id = '%d' "
		id = int(uw_ent_id.get())
		name = uw_ent_name.get()
		salary = int(uw_ent_salary.get())
		cursor.execute(sql %(salary, name, id))
		if cursor.rowcount == 1:
			
			if id >= 1:
				name = uw_ent_name.get()
				if len(name) >= 2:
					if name.isalpha():
						salary = int(uw_ent_salary.get())

						if salary > 8000:
							
							con.commit()
							showinfo("Success", "Record Updated!!")
						else:
							showerror("Failed", "Salary Should be Minimum 8000")

					else: 
						showerror("Failed", "Name should contain alphabets only ")
				else:
					showerror("Failed", "Name should contain minimum two alphabets!!")
			else:
				showerror("Failed", "ID should have only positve integers!!")

		else:
			showerror("Failed", "Record does not exists!!")
	except ValueError :
		con.rollback()
		showerror("Failed ", "Enter Only Integer Value ")

	finally:
		if con is not None:
			con.close()
		uw_ent_id.delete(0, END)
		uw_ent_name.delete(0,END)
		uw_ent_salary.delete(0, END)
		uw_ent_id.focus()

def update_back_f9():
	uw.withdraw()
	root.deiconify()

def delete_save_f10():
	con = None
	try:
		con = connect("emp.db")
		cursor = con.cursor()
		sql = "delete from employee where id = '%d' "
		id = int(dw_ent_id.get())
		cursor.execute(sql %(id))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success", "Record Deleted!!")
		else:
			showerror("Failed", "Record does not exists!!")
	except ValueError:
		con.rollback()
		showerror("Failed ", "Enter only integer value")
	finally:
		if con is not None:
			con.close()
		dw_ent_id.delete(0, END)
		dw_ent_id.focus()

def delete_back_f11():
	dw.withdraw()
	root.deiconify()

def chartw():	
	con = None
	try:
		con = connect("emp.db")
		cursor = con.cursor()
		sql = "select name,salary from employee order by salary desc limit 5"
		cursor.execute(sql)
		name = []
		salary = []
		for row in cursor:
			name.append(row[0])
			salary.append(row[1])
		plt.bar(name, salary, label = "Salary", width = 0.40, color = "red")
		tick_values = plt.gca().get_yticks()
		plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in tick_values])
		plt.title("Employee Details")
		plt.xlabel("Employee Name")
		plt.ylabel("Salary")
		plt.legend()
		plt.show()
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
def cback():
	cw.withdraw()
	root.deiconify()
		

root = Tk()
root.title("Employee Management System")
root.geometry("700x600+50+50")
bg = PhotoImage(file="1234.png")
label1 = Label(root,image=bg)
label1.place(x=0,y=0)
root.iconbitmap("emp.ico")
f = ("Arial", 25, "bold")



btn_add = Button(root, text = "Add", font =f, width = 10, bg = "red", command = add_f1)
btn_add.place(x = 250, y = 20)

btn_view = Button(root, text = "View", font= f, width = 10, bg = "red", command = view_f2)
btn_view.place(x = 250, y = 100)

btn_update = Button(root, text = "Update", font = f, width = 10, bg = "red", command = update_f3)
btn_update.place(x = 250, y = 180)

btn_delete = Button(root, text = "Delete", font = f, width = 10, bg = "red", command = delete_f4)
btn_delete.place(x = 250, y = 260)

btn_charts = Button(root, text = "Charts", font = f, width = 10, bg = "red", command = chartw)
btn_charts.place(x = 250, y = 340)

try:
	a1 = "https://api.openweathermap.org/data/2.5/weather?"
	a2 = "q=mumbai"
	a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
	a4 = "&units=" + "metric"
	wa = a1 + a2 + a3 + a4
	res = requests.get(wa)
	data = res.json()
	city = data["name"]
	temp = data["main"]["temp"]
except Exception as e:
	showerror("Issue ", e)

lab_loc = Label(root, font = ("Arial", 20, "bold"))
lab_loc.place(x = 15, y = 525)
lab_loc.configure(text = "Location: "+ city)

lab_temp = Label(root, font = ("Arial", 20, "bold"))
lab_temp.place(x = 450, y = 525)
lab_temp.configure(text = "Temp: "+ str(temp)+ "\u00b0"+ "C")


#Window for adding Employee data
aw = Toplevel(root)
aw.title("Add Employee Data")
aw.geometry("700x600+50+50")
bg2 = PhotoImage(file="1234.png")
label2 = Label(aw,image=bg2)
label2.place(x=0,y=0)

aw.iconbitmap("emp.ico")
f1 = ("Arial", 20, "bold")



aw_lab_id = Label(aw, text = "Enter Employee Id:", font = f1)
aw_ent_id = Entry(aw, font = f1, bd = 2, width = 25)

aw_lab_id.pack(pady = 10)
aw_ent_id.pack(pady = 10)

aw_lab_name = Label(aw, text = "Enter Employee Name:", font = f1)
aw_ent_name = Entry(aw, font = f1, bd = 2, width = 25)

aw_lab_name.pack(pady = 10)
aw_ent_name.pack(pady = 10)

aw_lab_salary = Label(aw, text = "Enter Employee Salary:", font = f1)
aw_ent_salary = Entry(aw, font = f1, bd = 2, width = 25)

aw_lab_salary.pack(pady = 10)
aw_ent_salary.pack(pady = 10)

aw_btn_save = Button(aw, text = "Save", font = f1, width = 10, bg = "blue", fg = "white", bd = 3, command = add_save_f5)
aw_btn_save.pack(pady = 10)

aw_btn_back = Button(aw, text = "Back", font = f1, width = 10, bg = "yellow", fg = "white", bd = 3, command = add_back_f6)
aw_btn_back.pack(pady = 10)

aw.withdraw()



#View Employee Data Window
vw = Toplevel(root)
vw.title("View Employees Data")
vw.geometry("700x600+50+50")
bg3 = PhotoImage(file="1234.png")
label3 = Label(vw,image=bg3)
label3.place(x=0,y=0)

vw.iconbitmap("emp.ico")

vw_st_data = ScrolledText(vw, width = 42, height = 14, font = f1)
vw_st_data.pack(pady = 10)

vw_btn_back = Button(vw, text = "Back", font = f1, width = 10, bg = "blue", fg = "white", bd = 3, command = view_back_f7)
vw_btn_back.pack(pady = 20)

vw.withdraw()


#Update Employee Data Window
uw = Toplevel()
uw.title("Update Employee Data")
uw.geometry("700x600+50+50")
bg4 = PhotoImage(file="1234.png")
label4 = Label(uw,image=bg4)
label4.place(x=0,y=0)

uw.iconbitmap("emp.ico")

uw_lab_id = Label(uw, text = "Enter Employee ID:", font = f1)
uw_lab_id.pack(pady = 10)

uw_ent_id = Entry(uw, font = f1, bd = 2, width = 25)
uw_ent_id.pack(pady = 10)

uw_lab_name = Label(uw, text = "Enter Employee Name:", font = f1)
uw_lab_name.pack(pady = 10)

uw_ent_name = Entry(uw, font = f1, bd = 2, width = 25)
uw_ent_name.pack(pady = 10)

uw_lab_salary = Label(uw, text = "Enter Employee Salary:", font = f1)
uw_lab_salary.pack(pady = 10)

uw_ent_salary = Entry(uw, font = f1, bd = 2, width = 25)
uw_ent_salary.pack(pady = 10)

uw_btn_save = Button(uw, text = "Save", font = f1, width = 10, bg = "blue", fg = "white", bd = 3, command = update_save_f8)
uw_btn_save.pack(pady = 10)

uw_btn_back = Button(uw, text = "Back", font = f1, width = 10, bg = "yellow", fg = "white", bd = 3, command = update_back_f9)
uw_btn_back.pack(pady = 10)

uw.withdraw()


#Deleting Employee Data Window
dw = Toplevel(root)
dw.title("Delete Employee Data")
dw.geometry("700x600+50+50")
bg5 = PhotoImage(file="1234.png")
label5 = Label(dw,image=bg5)
label5.place(x=0,y=0)

dw.iconbitmap("emp.ico")

dw_lab_id = Label(dw, text = "Enter Employee ID:", font = f1)
dw_lab_id.pack(pady = 10)

dw_ent_id = Entry(dw, font = f1, bd = 2, width = 25)
dw_ent_id.pack(pady = 10)

dw_btn_save = Button(dw, text = "Save", font = f1, width = 10, bg = "blue", fg = "white", bd =3, command = delete_save_f10)
dw_btn_save.pack(pady = 10)

dw_btn_back = Button(dw, text = "Back", font = f1, width = 10, bg = "yellow", fg = "white", bd = 3, command = delete_back_f11)
dw_btn_back.pack(pady = 10)

dw.withdraw()

def f6():
	answer = askyesno(title='confirmation',message='Do you want to exit?')
	if answer:

		root.destroy()
root.protocol("WM_DELETE_WINDOW",f6)

root.mainloop()