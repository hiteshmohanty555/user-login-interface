import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client
import mysql.connector
def registration():
    root = tk.Tk()
    root.title("NEW REGISTRATION")

    # Database connection
    connection = mysql.connector.connect(
        host='localhost', user='root', password='123456', port='3306', database='test_py'
    )
    cursor = connection.cursor()

    bkg = "#636e72"
    flag = 0
    frame = tk.Frame(root, bg=bkg)

    label_firstname = tk.Label(frame, text="First Name: ", font=('verdana', 10), bg=bkg)
    entry_firstname = tk.Entry(frame, font=('verdana', 10))

    label_lastname = tk.Label(frame, text="Last Name: ", font=('verdana', 10), bg=bkg)
    entry_lastname = tk.Entry(frame, font=('verdana', 10))

    label_email = tk.Label(frame, text="Email: ", font=('verdana', 10), bg=bkg)
    entry_email = tk.Entry(frame, font=('verdana', 10))

    label_age = tk.Label(frame, text="Age: ", font=('verdana', 10), bg=bkg)
    entry_age = tk.Entry(frame, font=('verdana', 10))

    label_phoneno = tk.Label(frame, text="Phone number: ", font=('verdana', 10), bg=bkg)
    entry_phoneno = tk.Entry(frame, font=('verdana', 10))

    label_OTP = tk.Label(frame, text="OTP: ", font=('verdana', 10), bg=bkg)
    entry_OTP = tk.Entry(frame, font=('verdana', 10))
    
    def insert_data():
        firstname = entry_firstname.get()
        lastname = entry_lastname.get()
        email = entry_email.get()
        age = entry_age.get()
        phoneno = entry_phoneno.get()

        insert_query1 = "INSERT INTO users_2 (firstname, lastname, email, age, ph_no, d_o_r, t_o_r) VALUES (%s, %s, %s, %s, %s,NOW(),NOW())"
        values1 = (firstname, lastname, email, age, phoneno)
        #insert_query2 = "INSERT INTO users_3(ph_no, d_o_r, t_o_r) VALUES (%s, NOW(), NOW())"
        #values2 = [phoneno]
        try:
            cursor.execute(insert_query1, values1)
            connection.commit()
           # cursor.execute(insert_query2, values2)
           # connection.commit()
            messagebox.showinfo("Success", "Registration successful")
        except mysql.connector.Error as e:
            print("Error:", e)
            messagebox.showerror("Error", "Failed to register")

    def otp_verify(verify_sid, client):
        global flag
        phoneno = "+91" + entry_phoneno.get()
        OTP = entry_OTP.get()

        try:
            verification_check = client.verify.services(verify_sid).verification_checks.create(
                to=phoneno,
                code=OTP
            )
            print(verification_check.status)

            if verification_check.status == 'approved':
                flag = 1
                insert_data()
            else:
                print("Invalid OTP. Please enter the correct OTP and submit.")
                messagebox.showwarning("Warning", "Invalid OTP")
        except Exception as e:
            print("Error occurred during OTP verification:", e)
            messagebox.showerror("Error", "Failed to verify OTP")

    def send_otp():
        global flag
        flag = 0

        try:
            account_sid = "ACd582044349f11b6429fd85f6e9320f55"
            auth_token = "a1605d8c91d46453088b16b2b154f2f8"
            verify_sid = "VA1178d684025c191ab292eaca550acb25"
            client = Client(account_sid, auth_token)

            phoneno = "+91" + entry_phoneno.get()

            verification = client.verify.services(verify_sid).verifications.create(
                to=phoneno,
                channel="sms"
            )
            print(verification.status)

            label_OTP.grid(row=6, column=0, sticky='e')
            entry_OTP.grid(row=6, column=1, pady=10, padx=10)

            button_submit = tk.Button(frame, text="Submit", font=('verdana', 12), bg='orange',
                                    command=lambda: otp_verify(verify_sid, client))
            button_submit.grid(row=7, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')
        except Exception as e:
            print("Error occurred while sending OTP:", e)
            messagebox.showerror("Error", "Failed to send OTP")

    button_getotp = tk.Button(frame, text="Get OTP", font=('verdana', 12), bg='orange', command=send_otp)

    # Grid layout
    label_firstname.grid(row=0, column=0)
    entry_firstname.grid(row=0, column=1, pady=10, padx=10)

    label_lastname.grid(row=1, column=0)
    entry_lastname.grid(row=1, column=1, pady=10, padx=10)

    label_email.grid(row=2, column=0, sticky='e')
    entry_email.grid(row=2, column=1, pady=10, padx=10)

    label_age.grid(row=3, column=0, sticky='e')
    entry_age.grid(row=3, column=1, pady=10, padx=10)

    label_phoneno.grid(row=4, column=0, sticky='e')
    entry_phoneno.grid(row=4, column=1, pady=10, padx=10)

    button_getotp.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

    frame.grid(row=0, column=0)
    root.mainloop()
    exit()
