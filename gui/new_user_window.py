import tkinter as tk
import utils.backend as bknd
import orm.dml as dml

class new_user_window():
    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        
        self.root = tk.Toplevel()
        self.root.title("Dodaj użytkownika")
        self.root.geometry("300x150")

        self.lbl_username = tk.Label(self.root, text="Nazwa użytkownika:")
        self.lbl_username.grid(row=0, column=0)
        
        self.entry_username = tk.Entry(self.root)
        self.entry_username.grid(row=0, column=1)
        
        self.lbl_password = tk.Label(self.root, text="Hasło:")
        self.lbl_password.grid(row=1, column=0)
        
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.grid(row=1, column=1)
        
        self.lbl_confirm_password = tk.Label(self.root, text="Potwierdź hasło:")
        self.lbl_confirm_password.grid(row=2, column=0)
        
        self.entry_confirm_password = tk.Entry(self.root, show="*")
        self.entry_confirm_password.grid(row=2, column=1)
        
        self.lbl_email = tk.Label(self.root, text="Email:")
        self.lbl_email.grid(row=3, column=0)
        
        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=3, column=1)
        
        self.btn_add = tk.Button(self.root, text="Dodaj", command=self.add_user)
        self.btn_add.grid(row=4, column=0, columnspan=2)
        
    def add_user(self):
        if self.entry_password.get() == self.entry_confirm_password.get():
            if self.entry_username.get() != "" and self.entry_password.get() != "" and self.entry_email.get() != "":
                if self.login_try():
                    bknd.add_user(self.entry_username.get(), self.entry_password.get(), self.entry_email.get())         
                    self.root.destroy()
            else:
                tk.messagebox.showerror(title="Error",message="Wypełnij wszystkie pola")
        else:
            tk.messagebox.showerror(title="Error",message="Hasła nie są takie same")
    
    def login_try(self):
        dml.username = self.db_user
        dml.password = self.db_password
        dml.database = self.db_name
        dml.host = self.db_host
        dml.port = self.db_port
        dml.engine = dml.create_engine()
        if dml.check_connection():
            dml.create_database_if_not_exists()
        else:
            tk.messagebox.showerror(title="Error",message="Błąd połączenia z bazą danych")
            return False
        return True
        