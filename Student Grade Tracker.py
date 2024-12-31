from tkinter import *

window = Tk()
window.geometry("900x800")
window.title("Student Grade")

# Title Label with a better font
lab = Label(window, text="STUDENT GRADE", font=("Verdana", 20, "bold"), background="lightblue")
lab.pack(side=TOP, fill=X, pady=10)

def calculate():
    Name = str(txtname.get())
    CP = int(txtCompProg.get())  # Computer Programming
    OS = int(txtOS.get())  # Operating System
    CN = int(txtNet.get())  # Computer Networks
    DBMS = int(txtDBMS.get())  # Database Management
    DS = int(txtDS.get())  # Data Structures
    SE = int(txtSE.get())  # Software Engineering

    total = (CP + OS + CN + DBMS + DS + SE)
    Average = int(total / 6)

    # Adjust the placement of result values for better alignment
    Label(window, text=total, font=("Arial", 15, "bold"), fg="green").place(x=130, y=450)
    Label(window, text=Average, font=("Arial", 15, "bold"), fg="green").place(x=130, y=490)

    if Average >= 85:
        grade = "A"
    elif Average >= 75:
        grade = "B"
    elif Average >= 65:
        grade = "C"
    elif Average >= 40:
        grade = "D"
    else:
        grade = "E"

    Label(window, text=grade, font=("Arial", 15, "bold"), fg="green").place(x=130, y=530)

# Labels and text boxes for subjects with adjusted font and positioning
lblname = Label(window, text="Name", font=("Times New Roman", 15, "bold"))
lblname.place(x=30, y=120)
txtname = Entry(window, font=("Times New Roman", 14), width=25)
txtname.place(x=200, y=120)

lblCompProg = Label(window, text="CP", font=("Times New Roman", 15, "bold"))
lblCompProg.place(x=30, y=170)
txtCompProg = Entry(window, font=("Times New Roman", 14), width=25)
txtCompProg.place(x=200, y=170)

lblOS = Label(window, text="OS", font=("Times New Roman", 15, "bold"))
lblOS.place(x=30, y=210)
txtOS = Entry(window, font=("Times New Roman", 14), width=25)
txtOS.place(x=200, y=210)

lblNet = Label(window, text="CN", font=("Times New Roman", 15, "bold"))
lblNet.place(x=30, y=250)
txtNet = Entry(window, font=("Times New Roman", 14), width=25)
txtNet.place(x=200, y=250)

lblDBMS = Label(window, text="DBMS", font=("Times New Roman", 15, "bold"))
lblDBMS.place(x=30, y=290)
txtDBMS = Entry(window, font=("Times New Roman", 14), width=25)
txtDBMS.place(x=200, y=290)

lblDS = Label(window, text="DS", font=("Times New Roman", 15, "bold"))
lblDS.place(x=30, y=330)
txtDS = Entry(window, font=("Times New Roman", 14), width=25)
txtDS.place(x=200, y=330)

lblSE = Label(window, text="SE", font=("Times New Roman", 15, "bold"))
lblSE.place(x=30, y=370)
txtSE = Entry(window, font=("Times New Roman", 14), width=25)
txtSE.place(x=200, y=370)

# Adjusted Y-positions for result labels to ensure correct spacing between them
lblTot = Label(window, text="Total:", font=("Arial", 15, "bold"))
lblTot.place(x=30, y=450)

lblAvg = Label(window, text="Average:", font=("Arial", 15, "bold"))
lblAvg.place(x=30, y=490)

lblGrade = Label(window, text="Grade:", font=("Arial", 15, "bold"))
lblGrade.place(x=30, y=530)

# Buttons with updated style
btnCal = Button(window, text="Calculate", bg="#3498DB", width=15, padx=10, pady=10, font=("Helvetica", 14, "bold"), fg="white", relief="raised", command=calculate)
btnCal.place(x=30, y=570)

btnExit = Button(window, text="Exit", bg="#E74C3C", width=15, padx=10, pady=10, font=("Helvetica", 14, "bold"), fg="white", relief="raised", command=window.quit)
btnExit.place(x=200, y=570)

mainloop()
