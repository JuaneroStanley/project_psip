import tkinter as tk
import utils.gis as gis
import utils.backend as bknd


class order_window:
    """
    Window for adding and editing orders.
    """
    
    def __init__(self, order_id: int)->None:
        self.root = tk.Toplevel()
        self.root.title("Order")
        self.root.geometry("300x200")
        self.order_id = order_id
        
        clients = bknd.get_all_clients()
        restaurants = bknd.get_all_restaurants()
        couriers = bknd.get_all_couriers()
        
        
        self.lbl_restaurant = tk.Label(self.root, text="Restauracja:")
        self.lbl_restaurant.grid(row=0, column=0)
        
        self.cmbbox_restaurant = tk.ttk.Combobox(self.root, values=[restaurant.name for restaurant in restaurants],state='readonly')
        self.cmbbox_restaurant.grid(row=0, column=1)
        
        self.lbl_client = tk.Label(self.root, text="Klient:")
        self.lbl_client.grid(row=1, column=0)
        
        self.cmbbox_client = tk.ttk.Combobox(self.root, values=[client.name for client in clients],state='readonly')
        self.cmbbox_client.grid(row=1, column=1)
        
        self.lbl_client = tk.Label(self.root, text="Kurier:")
        self.lbl_client.grid(row=2, column=0)

        self.cmbbox_courier = tk.ttk.Combobox(self.root, values=[courier.name for courier in couriers],state='readonly')
        self.cmbbox_courier.grid(row=2, column=1)
        
        self.lbl_details = tk.Label(self.root, text="Detale:")
        self.lbl_details.grid(row=3, column=0)
        
        self.entry_details = tk.Entry(self.root)
        self.entry_details.grid(row=3, column=1)
        
        self.lbl_status = tk.Label(self.root, text="Status:")
        self.lbl_status.grid(row=4, column=0)
        
        self.cmbbox_status = tk.ttk.Combobox(self.root, values=["Delivered", "Picked up", "Preparing"])
        self.cmbbox_status.grid(row=4, column=1)
    
        
        self.btn_save = tk.Button(self.root, text="Zapisz", command=self.save)
        self.btn_save.grid(row=7, column=0, columnspan=2)
        
        self.populate(self.order_id)
        
        
        
    def save(self)->None:
            """
            Saves the order information.

            Retrieves the selected client, restaurant, courier, status, and details from the GUI.
            If the order_id is 0, adds a new order using the backend function add_order.
            Otherwise, edits the existing order using the backend function edit_order.
            """
            
            client = bknd.client_by_name(self.cmbbox_client.get())
            restaurant = bknd.restaurant_by_name(self.cmbbox_restaurant.get())
            courier = bknd.courier_by_name(self.cmbbox_courier.get())
            status = self.cmbbox_status.get()
            if status == "Delivered":
                status = 0
            elif status == "Picked up":
                status = 1
            elif status == "Preparing":
                status = 2
            details = self.entry_details.get()
            
            if self.order_id == 0:
                bknd.add_order(restaurant.id, client.id, courier.id, status, details)
                self.root.destroy()
            else:
                bknd.edit_order(self.order_id, restaurant.id, client.id, courier.id, status, details)
                self.root.destroy()
            
        
    def populate(self, order_id: int) -> None:
        """
        Populates the order window with data from the specified order ID.

        Args:
            order_id (int): The ID of the order if it's 0 then no data is populated.
        """
        if order_id == 0:
            return

        order = bknd.get_order(order_id)
        restaurant_name = bknd.get_restaurant(order.restaurant_id).name
        courier_name = bknd.get_courier(order.courier_id).name
        client_name = bknd.get_client(order.client_id).name
        values_restaurant = self.cmbbox_restaurant.cget("values")
        values_courier = self.cmbbox_courier.cget("values")
        values_client = self.cmbbox_client.cget("values")
        self.cmbbox_restaurant.current(values_restaurant.index(restaurant_name))
        self.cmbbox_courier.current(values_courier.index(courier_name))
        self.cmbbox_client.current(values_client.index(client_name))
        self.cmbbox_status.current(order.status)
        details = order.description
        self.entry_details.insert(0, details)
        
    def open_window(self):
        
        self.root.mainloop()
        