import tkinter as tk
import os.path
import orm.dml as dml
import gui.main_window_admin as main_window_admin
import gui.new_user_window as nuw
import utils.simulation as simulation
import utils.backend as bknd

class login_window():
    """
    Window for logging in.
    """
    root = tk.Tk()
    root.title("Login")
    root.geometry("600x200")
    
    lbl_login = tk.Label(root, text="Logowanie:")
    lbl_login.grid(row=0, column=0,columnspan=2)  
    lbl_username = tk.Label(root, text="Nazwa użytkownika:")
    lbl_username.grid(row=1, column=0)
    
    entry_username = tk.Entry(root)
    entry_username.grid(row=1, column=1)
    
    lbl_password = tk.Label(root, text="Hasło:")
    lbl_password.grid(row=2, column=0)
    
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=2, column=1)
    
    
    lbl_db_params = tk.Label(root, text="Parametry bazy danych:")
    lbl_db_params.grid(row= 0 , column=2,columnspan=2)
    
    lbl_db_name = tk.Label(root, text="Nazwa bazy danych:")
    lbl_db_name.grid(row=1, column=2)
    
    entry_db_name = tk.Entry(root)
    entry_db_name.grid(row=1, column=3)
    
    lbl_db_user = tk.Label(root, text="Użytkownik bazy danych:")
    lbl_db_user.grid(row=2, column=2)
    
    entry_db_user = tk.Entry(root)
    entry_db_user.grid(row=2, column=3)
    
    lbl_db_password = tk.Label(root, text="Hasło bazy danych:")
    lbl_db_password.grid(row=3, column=2)
    
    entry_db_password = tk.Entry(root, show="*")
    entry_db_password.grid(row=3, column=3)
    
    lbl_db_host = tk.Label(root, text="Host bazy danych:")
    lbl_db_host.grid(row=4, column=2)
    
    entry_db_host = tk.Entry(root)
    entry_db_host.grid(row=4, column=3)
    
    lbl_db_port = tk.Label(root, text="Port bazy danych:")
    lbl_db_port.grid(row=5, column=2)
    
    entry_db_port = tk.Entry(root)
    entry_db_port.grid(row=5, column=3)

    
    def hint()->None:
        """
        Fills the username and password entry fields with default values.
        """
        login_window.entry_username.delete(0, tk.END)
        login_window.entry_password.delete(0, tk.END)
        login_window.entry_username.insert(0, "admin")
        login_window.entry_password.insert(0, "admin")
    
    btn_hint = tk.Button(root, text="Podpowiedź dane logowania", command=hint)
    btn_hint.grid(row=3, column=0, columnspan=2)
    
    def check_if_env_exists() -> None:
        """
        Checks if the .env file exists and populates the login window fields with the database parameters if it does.
        """
        if os.path.isfile('./.env'):
            login_window.entry_db_name.delete(0, tk.END)
            login_window.entry_db_user.delete(0, tk.END)
            login_window.entry_db_password.delete(0, tk.END)
            login_window.entry_db_host.delete(0, tk.END)
            login_window.entry_db_port.delete(0, tk.END)
            dml.drivername, dml.username, dml.password, dml.database, dml.host, dml.port = dml.get_db_params()
            print(dml.drivername, dml.username, dml.password, dml.database, dml.host, dml.port)
            login_window.entry_db_name.insert(0, dml.database)
            login_window.entry_db_user.insert(0, dml.username)
            login_window.entry_db_password.insert(0, dml.password)
            login_window.entry_db_host.insert(0, dml.host)
            login_window.entry_db_port.insert(0, dml.port)
    
    btn_load_env = tk.Button(root, text="Wczytaj dane z pliku .env", command=check_if_env_exists)
    btn_load_env.grid(row=4, column=0, columnspan=2)
    
    
    chckbtn_var = tk.IntVar()
    chckbtn_simulate = tk.Checkbutton(root, text="Zapopuluj bazę danych", variable=chckbtn_var, onvalue=1, offvalue=0)
    chckbtn_simulate.grid(row=6, column=0, columnspan=2)
    
    lbl_connection_error = tk.Label(root, text="", fg="red")
    lbl_connection_error.grid(row=6, column=2, columnspan=2)
    
    def login_try()->None:
        """
        Attempts to log in with the provided credentials and performs necessary actions based on the result.

        This function retrieves the attributes from window's input fields.
        It then sets up the database connection using the provided information and checks if the connection is successful.
        If the connection is successful, it creates the database if it doesn't exist and proceeds with the login process.
        If the "simulate" checkbox is checked, it initiates a utils.simulation.simulate().
        It then checks the provided username and password against the users database.
        If the credentials are valid, opens the main window.
        Otherwise, it displays an error message indicating incorrect login credentials.

        """
        dml.username = login_window.entry_db_user.get()
        dml.password = login_window.entry_db_password.get()
        dml.database = login_window.entry_db_name.get()
        dml.host = login_window.entry_db_host.get()
        dml.port = login_window.entry_db_port.get()
        dml.engine = dml.create_engine()
        print(dml.engine.url)
        if dml.check_connection():
            dml.create_database_if_not_exists()
            if login_window.chckbtn_var.get() == 1:
                simulation.simulate()
            username = login_window.entry_username.get()
            password = login_window.entry_password.get()
            if bknd.check_user(username, password):
                bknd.is_logged_in = True
                # main_window = main_window_admin.main_window_admin()
                # main_window.open_window()
                login_window.close_window()
            else:
                login_window.lbl_connection_error.config(text="Błędne dane logowania")
        else:
            login_window.lbl_connection_error.config(text="Błąd połączenia z bazą danych")
 
    btn_login = tk.Button(root, text="Zaloguj", command=login_try)
    btn_login.grid(row=7, column=2)
    
    def close_window():
        login_window.root.destroy()
    
    btn_exit = tk.Button(root, text="Wyjdź", command=close_window)
    btn_exit.grid(row=7, column=3)
    
    def create_new_user() -> None:
        """
        Creates and opens a new user window.

        This function retrieves the database name, user, password, host, and port from the login window's entry fields,
        and passes them to the `new_user_window` function to create a new user window. The new user window is then opened.
        """
        new_user_window = nuw.new_user_window(login_window.entry_db_name.get(),
                                            login_window.entry_db_user.get(),
                                            login_window.entry_db_password.get(),
                                            login_window.entry_db_host.get(),
                                            login_window.entry_db_port.get())
    
    
    btn_create_new_user = tk.Button(root, text="Utwórz nowego użytkownika", command=create_new_user)
    btn_create_new_user.grid(row=7, column=0, columnspan=2)
    
    
    def open_window(self):
        login_window.root.mainloop()
        
    def close_window():
        login_window.root.destroy()