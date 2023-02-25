import os
import subprocess
import sys
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox, simpledialog

import gui_util
import psutil

#   I realize that most of the gui code is a bit ugly/not done properly. This is just a working prototype.
#   There is no error handling or anything to that nature, but if everything is done in order, it will work


class Main_Window:
    def __init__(self, root):
        #setting title
        root.title("Python-Steam-Idler")
        #setting window size
        width=360
        height=200
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        #Start Idle Button Creation
        start_idle_btn=tk.Button(root)
        start_idle_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        start_idle_btn["font"] = ft
        start_idle_btn["fg"] = "#000000"
        start_idle_btn["justify"] = "center"
        start_idle_btn["text"] = "Start Idling"
        start_idle_btn.place(x=200,y=160,width=90,height=25)
        start_idle_btn["command"] = self.start_idle_btn_command
        #Add Account Button Creation
        add_account_btn=tk.Button(root)
        add_account_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        add_account_btn["font"] = ft
        add_account_btn["fg"] = "#000000"
        add_account_btn["justify"] = "center"
        add_account_btn["text"] = "Add Account"
        add_account_btn.place(x=150,y=100,width=90,height=25)
        add_account_btn["command"] = self.add_account_btn_command
        #List Accounts Button Creation
        list_accounts_btn=tk.Button(root)
        list_accounts_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        list_accounts_btn["font"] = ft
        list_accounts_btn["fg"] = "#000000"
        list_accounts_btn["justify"] = "center"
        list_accounts_btn["text"] = "List Accounts"
        list_accounts_btn.place(x=150,y=50,width=90,height=25)
        list_accounts_btn["command"] = self.list_accounts_btn_command
        #Stop Idling Button Creation
        stop_idling_btn=tk.Button(root)
        stop_idling_btn["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        stop_idling_btn["font"] = ft
        stop_idling_btn["fg"] = "#000000"
        stop_idling_btn["justify"] = "center"
        stop_idling_btn["text"] = "Stop Idling"
        stop_idling_btn.place(x=100,y=160,width=90,height=25)
        stop_idling_btn["command"] = self.stop_idling_btn_command
        #Center Text Button Creation
        main_label_text=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        main_label_text["font"] = ft
        main_label_text["fg"] = "#333333"
        main_label_text["justify"] = "center"
        main_label_text["text"] = "Steam Account Idler GUI v0.1"
        main_label_text.place(x=90,y=0,width=190,height=30)

        self.idle_subproccess = []

    def start_idle_btn_command(self):
        accounts_to_idle = gui_util.read_config_file()

        for i in range(len(accounts_to_idle)):
            account = accounts_to_idle[i][0].split(':')
            usern = account[0]
            passw = account[1]
            games = account[2]
            self.idle_subproccess.append(subprocess.Popen([sys.executable, f"main.py", f"-u{usern}", f"-p{passw}", f"-g{games}"], creationflags=subprocess.CREATE_NEW_CONSOLE)) #Need to check support on linux/macOS



    def add_account_btn_command(self):
        usern = simpledialog.askstring(title="Add Account", prompt="What is the account username?")
        if usern != None:
            passw = simpledialog.askstring(title="Add Account", prompt="What is the account password?")
            if passw != None:
                games = simpledialog.askstring(title="Add Account", prompt="what games do you want to idle (Give the id's seperated by commas)")
                if games != None:
                    add_account_result = gui_util.add_account(usern,passw,games)
                    if add_account_result == True:
                        messagebox.showinfo("Success!", f"You have successfully added {usern} as an account")
                    elif add_account_result == False:
                        messagebox.showinfo("Failure!", f"Error while adding account")
                    return
        
        messagebox.showinfo("Failure!", f"Error: User Canceled")
        return

    def list_accounts_btn_command(self):
        accounts_to_idle = gui_util.read_config_file()
        if accounts_to_idle == False:
            messagebox.showinfo("Account Info", f"No accounts detected. Please add an account")
        else:
            messagebox.showinfo("Account Info", f"{accounts_to_idle}")
        return
    
    def stop_idling_btn_command(self):
        for i in self.idle_subproccess:
            i.terminate()
#        for proc in psutil.process_iter(["name"]):
#            if proc.info['name'] == 'Python-Steam-Idler': #meant for the exe, although n
#                proc.kill()
#        return

if __name__ == "__main__":
    root = tk.Tk()
    app = Main_Window(root)
    root.mainloop()
