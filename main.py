import gui.login_window as login_window
import utils.backend as bknd
import gui.main_window_admin as main_window_admin


login_window = login_window.login_window()
login_window.open_window()
if bknd.is_logged_in: # if looged in after login_window closed open main_window_admin
    main_window = main_window_admin.main_window_admin()
    main_window.open_window()