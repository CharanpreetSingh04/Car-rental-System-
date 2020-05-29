from tkinter import*
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Label
from tkinter import messagebox
import re
from random import randint
global q1,q2,q3
q1,q2,q3=0,0,0
def binary_search(arr, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if len(x)==8:
            if arr[mid][0][0:8]== x:
                return arr[mid][1]
            elif arr[mid][0][0:8] < x:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if arr[mid][0] == x:
                return arr[mid][1]
            elif arr[mid][0] < x:
                l = mid + 1
            else:
                r = mid - 1
    return -1


def sort_index():
    f = open('index.txt', 'r+')

    content = f.read()
    content.strip()

    items = content.split('$')
    if '' in items:
        items.remove('')

    records = []
    for i in items:
        v = i.split('|')
        if '' in v:
            v.remove('')
        records.append(list(v))

    records.sort()

    f = open('index.txt', 'w+')

    for i in records:
        for j in i:
            f.write(j + '|')
        f.write('$')


def search_details(v):
    rec = open('record.txt', 'r+')
    ind = open('index.txt', 'r+')

    s = v
    index = ind.read()

    if index == '':
        return -1

    index = index.split('$')
    index = [x for x in index if x != '']

    index_recs = []
    for i in index:
        a = list(i.split('|'))
        a = [x for x in a if x != '']
        index_recs.append(a)

    return int(binary_search(index_recs, 0, len(index_recs)-1, s))

def invoice1():
    add_invoice_screen = tk.Toplevel(main_screen)
    invoice = open('invoice.txt', 'a+')
    index_in = open('index_invoice.txt', 'a+')
    add_invoice_screen.title('Order placed')
    add_invoice_screen.geometry("1000x500")
    invoice_id=randint(1000000000,9999999999)
    tk.Label(add_invoice_screen, text = 'invoice_id: '+str(invoice_id), bg = "grey", width = '300', height = '2', font = ('Arial',15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    car_number='KA13'+str(randint(1000,9999))
    tk.Label(add_invoice_screen, text = 'Car: Mercedes', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    tk.Label(add_invoice_screen, text = 'Car number: '+car_number, bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    tk.Label(add_invoice_screen, text = 'Pickup Location: Majestic', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    tk.Label(add_invoice_screen, text = 'Estimated Cost: Rs'+str(int(val.get())*4000), bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    tk.Label(add_invoice_screen, text = 'Order Placed', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    off = invoice.tell()
    in_rec =  marks_user.get()+'|'+str(invoice_id)+'|'+'Mercedes'+'|'+car_number+'|'+str(int(val.get())*4000)+'|'+'$'
    in_ind = marks_user.get()+ '|' + str(off) + '|' + '$'
    in_rec.rstrip()
    in_ind.rstrip()

    invoice.write(in_rec)
    index_in.write(in_ind)
def invoice2():
    add_invoice_screen = tk.Toplevel(main_screen)
    add_invoice_screen.title('Order placed')
    add_invoice_screen.geometry("1000x500")
    invoice = open('invoice.txt', 'a+')
    index_in = open('index_invoice.txt', 'a+')
    invoice_id=randint(1000000000,9999999999)
    tk.Label(add_invoice_screen, text = 'invoice_id: '+str(invoice_id), bg = "grey", width = '300', height = '2', font = ('Arial',15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    car_number='KA13'+str(randint(1000,9999))
    tk.Label(add_invoice_screen, text = 'Car: Audi', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    tk.Label(add_invoice_screen, text = 'Car number: '+car_number, bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    tk.Label(add_invoice_screen, text = 'Pickup Location: Majestic', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    tk.Label(add_invoice_screen, text = 'Estimated Cost: Rs'+str(int(val.get())*5000), bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    tk.Label(add_invoice_screen, text = 'Order Placed', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    off = invoice.tell()
    in_rec =  marks_user.get()+'|'+str(invoice_id)+'|'+'Audi'+'|'+car_number+'|'+str(int(val.get())*5000)+'|'+'$'
    in_ind = marks_user.get()+ '|' + str(off) + '|' + '$'
    in_rec.rstrip()
    in_ind.rstrip()

    invoice.write(in_rec)
    index_in.write(in_ind)

def invoice3():
    add_invoice_screen = tk.Toplevel(main_screen)
    add_invoice_screen.title('Order placed')
    add_invoice_screen.geometry("1000x500")
    invoice = open('invoice.txt', 'a+')
    index_in = open('index_invoice.txt', 'a+')
    invoice_id=randint(1000000000,9999999999)
    tk.Label(add_invoice_screen, text = 'invoice_id: '+str(invoice_id), bg = "grey", width = '300', height = '2', font = ('Arial',15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    car_number='KA13'+str(randint(1000,9999))
    tk.Label(add_invoice_screen, text = 'Car: BMW', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    tk.Label(add_invoice_screen, text = 'Car number: '+car_number, bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    tk.Label(add_invoice_screen, text = 'Pickup Location: Majestic', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    tk.Label(add_invoice_screen, text = 'Estimated Cost: Rs'+str(int(val.get())*3000), bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    tk.Label(add_invoice_screen, text = 'Order Placed', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_invoice_screen, text = '').pack()
    off = invoice.tell()
    in_rec =  marks_user.get()+'|'+str(invoice_id)+'|'+'BMW'+'|'+car_number+'|'+str(int(val.get())*3000)+'|'+'$'
    in_ind = marks_user.get()+ '|' + str(off) + '|' + '$'
    in_rec.rstrip()
    in_ind.rstrip()

    invoice.write(in_rec)
    index_in.write(in_ind)


def info1():
    add_screen = tk.Toplevel(main_screen)
    add_screen.title('car details')
    add_screen.geometry("1000x500")
    p=val.get()
    q1=int(p)*4000
    tk.Label(add_screen, text = 'This is a luxurious car of MERCEDES BENZ series', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Label(add_screen, text = 'Car can be taken on rent for 24 hours at cost:', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Label(add_screen, text = '4000rs', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Label(add_screen, text = 'Your cost estimation for your order is:', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Label(add_screen, text=str(q1)+"rs", bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Button(add_screen, text = 'Book Now', width = 10, height = 1, command = invoice1).pack()

def info2():
    add_screen = tk.Toplevel(main_screen)
    add_screen.title('car details')
    add_screen.geometry("1000x500")
    p=val.get()
    q2=int(p)*5000
    tk.Label(add_screen, text = 'This is a luxurious car of Audi 4 series', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Label(add_screen, text = 'Car can be taken on rent for 24 hours at cost:', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Label(add_screen, text = '5000rs', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Label(add_screen, text = 'Your cost estimation for your order is:', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Label(add_screen, text=str(q2)+"rs", bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Button(add_screen, text = 'BOOK Now', width = 10, height = 1, command =  invoice2).pack()


def info3():
    add_screen = tk.Toplevel(main_screen)
    add_screen.title('car details')
    add_screen.geometry("1000x500")
    p=val.get()
    q3=int(p)*3000
    tk.Label(add_screen, text = 'This is a luxurious car of BMW 3 series', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Label(add_screen, text = 'Car can be taken on rent for 24 hours at cost:', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Label(add_screen, text = '3000rs', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Label(add_screen, text = 'Your cost estimation for your order is:', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Label(add_screen, text=str(q3)+"rs", bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Button(add_screen, text = 'Book Now', width = 10, height = 1, command =  invoice3).pack()


def check():
    rec = open('record.txt', 'r+')
    curr_user = marks_user.get()
    curr_pass = marks_pass.get()
    p=curr_user
    curr_user+='('+curr_pass+')'
    if search_details(curr_user) < 0 :
        messagebox.showinfo("Error", "Invalid User name or password")
        return 
    global addc_screen
    addc_screen = tk.Toplevel(main_screen)
    addc_screen.title("Hi, "+p)
    addc_screen.geometry("400x500")
    global val
    val=tk.StringVar()
    tk.Label(addc_screen, text = 'Choose your car', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(addc_screen, text = '').pack()
    tk.Label(addc_screen, text = 'Enter the number of days', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Entry(addc_screen, text = val).pack()
    tk.Button(addc_screen, text = 'MERCEDES', width = 10, height = 1, command =  info1).pack()
    tk.Label(addc_screen, text = '').pack()
    tk.Button(addc_screen, text = 'AUDI', width = 10, height = 1, command =  info2).pack()
    tk.Label(addc_screen, text = '').pack()
    tk.Button(addc_screen, text = 'BMW', width = 10, height = 1, command = info3).pack()
    tk.Label(addc_screen, text = '').pack()
    tk.Button(addc_screen, text = 'Delete Account', width = 15, height = 1, command =delete).pack()
    tk.Label(addc_screen, text = '').pack()
    rec.close()
    


def add_Login():
    add_screen = tk.Toplevel(main_screen)
    add_screen.title("Login")
    add_screen.geometry("300x350")

    global marks_user
    global marks_pass

    marks_user = tk.StringVar()
    marks_pass = tk.StringVar()
    tk.Label(add_screen, text = 'Enter details below', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Label(add_screen, text = 'username:').pack()
    tk.Entry(add_screen, textvariable = marks_user).pack()
    tk.Label(add_screen, text = 'password').pack()
    tk.Entry(add_screen, textvariable = marks_pass).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Button(add_screen, text = 'OK', width = 10, height = 1, command = check).pack()


def add_details_record():
    rec = open('record.txt', 'a+')
    ind = open('index.txt', 'a+')
    curr_user = add_user.get()
    curr_pass = add_pass.get()
    curr_name = add_name.get()
    curr_name = curr_name.upper()
    curr_email = add_email.get()
    curr_phone=add_phone.get()
    curr_address = add_address.get()
    curr_address = curr_address.upper()
    if curr_user == '' or curr_pass =='' or curr_name == '' or curr_email == '' or curr_phone== ''or curr_address== '':
        messagebox.showinfo('Error', "Fields can't be empty")
        return
    if len(curr_user)< 8 or len(curr_user)> 8:
        messagebox.showinfo('Error', "User name must consist of 8 letters")
        return
    if search_details(curr_user) >= 0:
        messagebox.showinfo("Error", "User name already taken")
        return

    off = rec.tell()
    p_rec = curr_user+'('+curr_pass+')' + '|' + curr_name + '|' + curr_email + '|' + curr_phone + '|' + curr_address + '|' +'$'
    p_ind = curr_user+'('+curr_pass+')' + '|' + str(off) + '|' + '$'
    p_rec.rstrip()
    p_ind.rstrip()

    rec.write(p_rec)
    ind.write(p_ind)

    messagebox.showinfo("Yippie :)", "Account registered successfully")
    rec.close()
    ind.close()

    sort_index()


def add_details():
    global add_screen
    add_screen = tk.Toplevel(main_screen)
    add_screen.title("Details")
    add_screen.geometry("300x350")

    global add_email
    global add_name
    global add_phone
    global add_address
    global add_user
    global add_pass
    add_user=tk.StringVar()
    add_pass=tk.StringVar()
    add_email = tk.StringVar()
    add_name = tk.StringVar()
    add_phone = tk.StringVar()
    add_address = tk.StringVar()

    tk.Label(add_screen, text = 'Enter details below', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Label(add_screen, text = ' Desired UserName').pack()
    tk.Entry(add_screen, textvariable = add_user).pack()
    tk.Label(add_screen, text = ' Desired password').pack()
    tk.Entry(add_screen, textvariable = add_pass).pack()
    tk.Label(add_screen, text = 'Name').pack()
    tk.Entry(add_screen, textvariable = add_name).pack()
    tk.Label(add_screen, text = 'email').pack()
    tk.Entry(add_screen, textvariable = add_email).pack()
    tk.Label(add_screen, text = 'Phone').pack()
    tk.Entry(add_screen, textvariable = add_phone).pack()
    tk.Label(add_screen, text = 'Address').pack()
    tk.Entry(add_screen, textvariable = add_address).pack()
    tk.Label(add_screen, text = '').pack()
    tk.Button(add_screen, text = 'OK', width = 10, height = 1, command = add_details_record).pack()


def add_options():
    global add_options_screen
    add_options_screen = tk.Toplevel(main_screen)
    add_options_screen.title("Sign up to CAR RENTAL SYSTEM")
    add_options_screen.geometry("300x200")
    tk.Label(add_options_screen, text = 'Select Option', bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(add_options_screen, text = '').pack()
    tk.Button(add_options_screen, text = 'NEW USER!!!', width = 10, height = 1, command = add_details).pack()
    tk.Label(add_options_screen, text = '').pack()
    tk.Button(add_options_screen, text = 'Already a customer', width = 20, height = 1, command = add_Login).pack()

def delete_record():
    rec = open('record.txt', 'r+')
    ind = open('index.txt', 'r+')
    s = marks_user.get()+'('+marks_pass.get()+')'

    found_record = search_details(s)

    if found_record < 0:
        messagebox.showinfo('Error', 'Record not found')
        return
    else:
        rec.seek(found_record)
        record = rec.read()
        rec.seek(found_record)
        rec.write('*')
        index = ind.read()
        index = index.split('$')
        index.remove('')
        new_index = ''
        for i in index:
            a = i.split('|')
            a.remove('')
            if(a[0] != s):
                new_index += i
                new_index += '$'
            if(a[0]==s):
                ind.write('*')
        ind.seek(0)
        ind.truncate()
        ind.write(new_index)
        messagebox.showinfo('successful', 'Account deleted successfully')


def delete():
    global delete_screen
    delete_screen = tk.Toplevel(addc_screen)
    delete_screen.title('Delete Account')
    delete_screen.geometry('300x350')

    
    tk.Label(delete_screen, text = 'Are u sure u want to delete this account').pack()
    tk.Button(delete_screen, text = 'OK', width = 10, height = 1, command = delete_record).pack()
    tk.Label(delete_screen, text = '').pack()
    tk.Button(delete_screen, text = 'Cancel', width = 10, height = 1, command = addc_screen.quit).pack()
    tk.Label(delete_screen, text = '').pack()

def main():
    global main_screen
    main_screen = tk.Tk()
    main_screen.geometry('1200x1000')
    canvas=Canvas(main_screen,width=1000,height=800)
    image=ImageTk.PhotoImage(Image.open('car.jpg'))
    canvas.create_image(0,0,anchor=NW,image=image)
    canvas.place(relx=0.15,rely=0.060)
    main_screen.title("Car Rental System")
    tk.Label(text="CAR RENTAL SYSTEM", bg = "grey", width = '300', height = '2', font = ('Arial', 15)).pack()
    tk.Label(text='').pack()
    tk.Button(text = 'Sign Up', height = '2', width = '30', command = add_options).pack()
    tk.Label(text='').pack()
    '''tk.Button(text = 'Delete', height = '2', width = '30', command = delete).pack()
    tk.Label(text='').pack()
    '''
    main_screen.mainloop()

if __name__ == "__main__":
    main()
