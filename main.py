from orm.dml import check_if_tables_exist, check_if_schema_exists
from utils.simulation import simulate
import gui.login_window as login_window


login_window = login_window.login_window()
login_window.open_window()
