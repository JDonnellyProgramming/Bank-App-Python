import tkinter as tk




root = tk.Tk()
root.geometry("1000x800")
root.resizable(False, False)




def change_cursor(event):
  global number_label
  global email_label
  underline_label.config(cursor="hand2")
  label3.config(cursor="hand2")
  number_label.config(cursor="hand2")
  email_label.config(cursor="hand2")
def cookies_click(event):
  cookies_window = tk.Tk()
  cookies_window.geometry("1000x800")
  cookies_window.resizable(False, False)
  label = tk.Label(cookies_window, text="Our cookies policy")
  label.place(x=300, y=200)




  cookies_window.mainloop()
def toggle_contact(event):
  global contact_menu_click_count
  contact_menu_click_count += 1
  global contact_frame
  global number_label
  global email_label
  if (contact_menu_click_count % 2 != 0):
          contact_frame = tk.Frame(root, width=240, height=400, bd=1,
                           relief='solid', bg='white')
          contact_frame.place(x=760, y=80)
          number_label = tk.Label(root, text="Call Us", font=("arial", 10, "bold"))
          number_label.place(x=860, y=100)
          number_label.bind("<Enter>", change_cursor)
          number_label.bind("<Button-1>", show_number)
          email_label = tk.Label(root, text="Email", font=("arial", 10, "bold"))
          email_label.place(x=860, y=200)
          email_label.bind("<Enter>", change_cursor)
          email_label.bind("<Button-1>", show_email)
  else:
      contact_frame.config(bd=0)
      number_label.config(text="")
      email_label.config(text="")
def show_number(event):
  global number_count
  global label4
  number_count += 1
  if (number_count % 2 != 0):
      label4 = tk.Label(root, text="0231020399", font=("arial", 14, "bold"))
      label4.place(x=820, y=120)
  else:
      label4.config(text="")
def show_email(event):
  global email_open
  global email_height
  global email_frame
  if not email_open:
      email_open = True
      animate_email_open()
  else:
      email_open = False
      email_frame.destroy()
def animate_email_open():
  global email_height
  global email_frame
  email_frame = tk.Frame(root, width=240, height=email_height, bd=1, relief='solid')
  email_frame.place(x=760, y=220)
  email_height += 1




  if email_height <= 40:
      root.after(5, animate_email_open)
def password_show(event):
  global showing_password
  global password
  if showing_password == False:
      password = password_input.get()
      password_input.config(show=password)
      showing_password = True
  else:
      password_input.config(show="*")
      showing_password = False
def user_input_clicked(event):
  username_input.config(bd=3)
def pass_input_clicked(event):
  password_input.config(bd=3)
def user_input_left(event):
  username_input.config(bd=1)
def pass_input_left(event):
  password_input.config(bd=1)
def button_hover(event):
  button.config(cursor="hand2")
def loading_animate():
  global loading_front
  global loading_width
  if loading_width <= 60:
      loading_front.config(width=loading_width)
      loading_width += 1
      root.after(5, loading_animate)
  else:
      new_page()
def add_credentials(username1, password1):
   with open(r"C:\Users\josep\Downloads\usernames.txt", "a") as usernames_file:
       usernames_file.write(username1 + "\n")
       usernames_file.flush()
       usernames_file.close()
   with open(r"C:\Users\josep\Downloads\passwords.txt", "a") as passwords_file:
       passwords_file.write(password1 + "\n")
       passwords_file.flush()
       passwords_file.close()
def validate():
   global username_note, sign_in, text1, text1_list
   global confirm_password_input, confirm_password_input_note, usernames, username_index
   lower = False
   capital = False
   digit = False
   usernames_data = open(r"C:\Users\josep\Downloads\usernames.txt").read()
   usernames = usernames_data.split('\n')
   password_data = open(r"C:\Users\josep\Downloads\passwords.txt").read()
   passwords = password_data.split('\n')
   if sign_in:
       if username_input.get() not in usernames:
           username_note.config(text="Username incorrect")
       elif username_input.get() in usernames:
           username_note.config(text="")
           username_input.config(bg="green")
           username_index = usernames.index(username_input.get())
       if passwords[username_index] == password_input.get():
           password_note.config(text="Correct")
           password_input.config(bg="green")
           submit()
       elif passwords[username_index] != password_input.get():
           password_note.config(text="Incorrect Password")
           password_input.config(bg="red")
   else:
       password_problems_list = ["Password too short", "Password too long",
                                 "Must contain at least one digit, number and capital",
                                 "Must not contain number in consecutive pattern"]
       digits = "1234567890"
       capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
       lowers = "abcdefghijklmnopqrstuvwxyz"
       if username_input.get() in usernames:
           username_note.config(text="Username already taken")
       elif username_input.get() not in usernames:
           username_note.config(text="")
       if len(password_input.get()) < 6:
           if password_problems_list[0] not in text1_list:
               text1_list.append(password_problems_list[0])
           if password_problems_list[1] in text1_list:
               text1_list.remove(password_problems_list[1])
           text1 = ', '.join(text1_list)
           password_note.config(text=text1)
       if len(password_input.get()) > 16:
           if password_problems_list[1] not in text1_list:
               text1_list.append(password_problems_list[1])
           if password_problems_list[0] in text1_list:
               text1_list.remove(password_problems_list[0])
           text2 = ', '.join(text1_list)
           password_note.config(text=text2)
       elif 6 <= len(password_input.get()) <= 16:
           password_note.config(text="That's okay")
       for i in password_input.get():
           if i.islower():
               lower = True
           elif i.isupper():
               capital = True
           elif i.isdigit():
               digit = True
       if lower and capital and digit:
           if password_problems_list[2] in text1_list:
               text1_list.remove(password_problems_list[2])  # Remove from the list if it was previously added
               password_note.config(text="")
       else:
           if password_problems_list[2] not in text1_list:
               text1_list.append(password_problems_list[2])
           password_note.config(text=", ".join(text1_list))
       for j in range(len(password_input.get()) - 1):
           if password_input.get()[j].isdigit() and password_input.get()[j + 1].isdigit() and (
                   int(password_input.get()[j + 1]) - int(password_input.get()[j]) == 1):
               if password_problems_list[3] not in text1_list:
                   text1_list.append(password_problems_list[3])
               password_note.config(text=", ".join(text1_list))
           else:
               if password_problems_list[3] in text1_list:
                   text1_list.remove(password_problems_list[3])
                   password_note.config(text=", ".join(text1_list))


       if confirm_password_input.get() != password_input.get() and (confirm_password_input.get() != ""):
           confirm_password_input_note.config(text="Passwords don't match")
       if (username_input.get() != "") and (password_input.get() != "") and (username_note.cget("text") == "") and (password_note.cget("text") == "" or password_note.cget("text") == "That's okay") and (confirm_password_input_note.cget("text") == ""):
           add_credentials(username_input.get(), password_input.get())
           submit()
text1_list = []


def sign_up_func(event):
   global sign_in
   global confirm_password, confirm_password_input, confirm_password_input_note
   if sign_in:
       button.place(x=450, y=580)
       sign_up.place(x=480, y=650)
       sign_up.config(text="Sign In")
       confirm_password = tk.Label(root, text="Confirm Password", font=("arial", 14, "bold"))
       confirm_password.place(x=400, y=450)
       confirm_password_input = tk.Entry(root, width=24, bd=1, font=("arial", 14, "bold"), show="*")
       confirm_password_input.place(x=370, y=500)
       confirm_password_input_note = tk.Label(root, text="", font=("arial", 10, "normal"))
       confirm_password_input_note.place(x=370, y=530)
       sign_in = False
       username_input.delete(0, 'end')
       password_input.delete(0, 'end')
   else:
       button.place(x=450, y=420)
       sign_up.place(x=480, y=500)
       sign_up.config(text="sign Up")
       username_note.config(text="")
       password_note.config(text="")
       confirm_password_input_note.config(text="")
       confirm_password.destroy()
       confirm_password_input.destroy()
       sign_in = True
       username_input.delete(0, 'end')
       password_input.delete(0, 'end')


def submit():
      global loading_width
      global loading_front
      global username_valid, password_valid
      global confirm_password
      global confirm_password_input
      global confirm_password_input_note
      global loading_label
      global loading_back
      global username_value
      username_value = username_input.get()
      sign_up.destroy()
      username_label.destroy()
      username_input.destroy()
      password_label.destroy()
      password_input.destroy()
      username_note.destroy()
      password_note.destroy()
      show_password.destroy()
      button.destroy()
      underline_label.destroy()
      side_frame.destroy()
      label2.destroy()
      label3.destroy()
      show_password.destroy()
      center_frame.destroy()
      loading_label = tk.Label(root, text="Loading", font=("arial", 16, "bold"))
      loading_label.place(x=470, y=320)
      loading_back = tk.Label(root, width=60, height=2, bd=2, relief="solid")
      loading_back.place(x=300, y=360)
      loading_front = tk.Label(root, width=loading_width, height=2, bg="red")
      loading_front.place(x=300, y=360)
      loading_animate()
def update_balance(username, new_balance):
   with open(r"C:\Users\josep\Downloads\usernames.txt") as usernames_file:
       usernames2 = usernames_file.readlines()
   with open(r"C:\Users\josep\Downloads\balances.txt") as balances_file:
       balances2 = balances_file.readlines()
   index1 = usernames2.index(username)
   balances2[index1] = f"{new_balance}"


   with open(r"C:\Users\josep\Downloads\balances.txt") as balances_file:
       balances_file.writelines(balances2)


def pay():
   global give_money_input, money_value, user_select_input, usernames, balances, username_value
   global user2_index, main_user
   amount = int(give_money_input.get())
   main_user = usernames.index(username_value)
   user2_index = usernames.index(user_select_input.get())


   if amount >= 0:
       if user_select_input.get() in usernames:
           balances[user2_index] = int(balances[user2_index]) + amount
           balances[main_user] = int(balances[main_user]) - amount
           update_balance(username_value, balances[main_user])
           update_balance(user_select_input.get(), balances[user2_index])


def new_page():
   global loading_back, loading_label, username_value, usernames, username_index, money_value
   global give_money_input, user_select_input, balances, username_value
   loading_front.destroy()
   loading_back.destroy()
   loading_label.destroy()
   balance_data = open(r"C:\Users\josep\Downloads\balances.txt").read()
   balances = balance_data.split('\n')
   money_value = balances[username_index]
   user_label = tk.Label(root, text=f"Welcome {username_value}", font=("arial", 18, "normal"))
   user_label.place(x=400, y=200)
   balance_label = tk.Label(root, text=f"You have £{money_value}")
   balance_label.place(x=400, y=400)


   give_money_label = tk.Label(root, text="Give money to a user?", font=("arial", 16, "normal"))
   give_money_label.place(x=200, y=500)
   give_money_input = tk.Entry(root, width=24, bd=1, font=("arial", 14, "normal"))
   give_money_input.place(x=200, y=540)
   user_select = tk.Label(root, text="Select a user", font=("arial", 14, "normal"))
   user_select.place(x=600, y=500)
   user_select_input = tk.Entry(root, width=20, bd=1, font=("arial", 14, "normal"))
   user_select_input.place(x=600, y=540)
   money_button = tk.Button(root, width=10, height=4, text="Pay", command=pay)
   money_button.place(x=600, y=600)
loading_width = 1
top_frame = tk.Frame(root, bg='blue', height=80)
top_frame.pack(side=tk.TOP, fill=tk.X)


username_correct = False
password_correct = False


main_label = tk.Label(root, text="Kingsway Banking", bg='blue',
                    font=("arial", 20, "bold"))
main_label.place(x=10, y=20)




underline_label = tk.Label(root, text="Cookie Policy", font=("arial", 10, "bold"), bg='blue')
underline_label.place(x=600, y=30)
showing_password = False
underline_label.bind("<Button-1>", cookies_click)




center_frame = tk.Frame(root, width=500, height=600,
                      bd=1, relief='solid')
center_frame.place(x=250, y=100)




side_frame = tk.Frame(root, width=240, height=80,
                    bd=1, relief="solid", bg='blue')
side_frame.place(x=760, y=0)
label2 = tk.Label(root, text="Contact Us", font=("arial", 14, "bold"), bg='blue')
label2.place(x=820, y=25)
label3 = tk.Label(root, text="|||", font=("arial", 20, "bold"), bg='blue')
label3.place(x=950, y=20)
label3.bind("<Enter>", change_cursor)
label3.bind("<Button-1>", toggle_contact)
contact_menu_click_count = 0
number_count = 0
email_open = False
email_height = 0
username_valid = False
password_valid = False
sign_in = True


username_label = tk.Label(root, text="Username", font=("arial", 16, "bold"))
username_label.place(x=450, y=200)
username_input = tk.Entry(root, width=24, bd=1, font=("arial", 14, "bold"))
username_input.place(x=370, y=240)
username_note = tk.Label(root, text="", font=("arial", 10, "normal"))
username_note.place(x=370, y=270)
password_label = tk.Label(root, text="Password", font=("arial", 16, "bold"))
password_label.place(x=450, y=320)
password_input = tk.Entry(root, width=24, bd=1, font=("arial", 14, "bold"), show="*")
password_input.place(x=370, y=360)
password_note = tk.Label(root, text="", font=("arial", 10, "normal"))
password_note.place(x=370, y=390)
show_password = tk.Label(root, text="show", font=("arial", 8, "bold"))
show_password.place(x=600, y=366)
show_password.bind("<Button-1>", password_show)
username_input.bind("<FocusIn>", user_input_clicked)
password_input.bind("<FocusIn>", pass_input_clicked)
username_input.bind("<FocusOut>", user_input_left)
password_input.bind("<FocusOut>", pass_input_left)




button = tk.Button(root, width=14, height=3, text="Submit", bg="blue",
                command=validate)
button.place(x=450, y=420)
button.bind("<Enter>", button_hover)


sign_up = tk.Label(root, text="Sign Up", font=("arial", 12, "normal"))
sign_up.place(x=480, y=500)
sign_up.bind("<Button-1>", sign_up_func)




root.mainloop()
