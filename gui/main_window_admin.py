import tkinter as tk
import tkintermapview
import utils.backend as bknd 
import orm.dml as dml
import utils.gis as gis
import gui.client_window as clnt
import gui.restaurant_window as rest
import gui.courier_window as cur
import gui.order_window as ord

class main_window_admin:
    """
    Main window of the application.
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My App")
        self.root.geometry("950x700")
        self.selection_mode = {"client":1,"curier":2,"restaurant":3,"order":4}
        self.selected_mode = 1
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=15,pady=15)
    
        self.main_frame.grid_columnconfigure(0,weight=4)
        self.main_frame.grid_columnconfigure(1,weight=2)
        self.main_frame.grid_columnconfigure(2,weight=1)
        
        self.map_view = tkintermapview.TkinterMapView(self.main_frame,width=400,height=400,corner_radius=10)
        self.map_view.grid(row=0,column=0,rowspan=12)
        
        self.list_frame = tk.Frame(self.main_frame)
        self.list_frame.grid(row=0,column=1,rowspan=12,padx=15)
        
        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.grid(row=0,column=2,rowspan=12)
        
        self.details_frame = tk.Frame(self.main_frame)
        self.details_frame.grid(row=13,column=0,columnspan=2, rowspan=6,pady=30)
        
        self.details_buttons_frame = tk.Frame(self.main_frame)
        self.details_buttons_frame.grid(row=13,column=2,rowspan=6)
        
        # List Frame
    
        self.lbl_list = tk.Label(self.list_frame, text="list")
        self.lbl_list.pack()
        self.list_listbox = []
        self.listbox_main = tk.Listbox(self.list_frame, width=50, height=22)
        self.listbox_main.bind('<<ListboxSelect>>', self.onselect)
        self.listbox_main.pack()
        
        self.btn_clients = tk.Button(self.buttons_frame, text="Clients", command=self.details_client, width=15)
        self.btn_clients.grid(row=1,column=0,pady=15)
        
        self.btn_curiers = tk.Button(self.buttons_frame, text="Curiers", command=self.details_curier, width=15)
        self.btn_curiers.grid(row=2,column=0,pady=15)
        
        self.btn_restaurants = tk.Button(self.buttons_frame, text="Restaurants", command=self.details_restaurant, width=15)
        self.btn_restaurants.grid(row=3,column=0,pady=15)
        
        self.btn_orders = tk.Button(self.buttons_frame, text="Orders", command=self.details_order, width=15)
        self.btn_orders.grid(row=4,column=0,pady=15)
        
        self.detail_client_frame = tk.Frame(self.details_frame)
        self.detail_client_frame.pack()
        
        self.lbl_client_name = tk.Label(self.detail_client_frame, text="Name")
        self.lbl_client_name.grid(row=0,column=0)
        
        self.lbl_client_name_value = tk.Label(self.detail_client_frame, text="Name")
        self.lbl_client_name_value.grid(row=0,column=1)
        
        self.lbl_client_phone = tk.Label(self.detail_client_frame, text="Phone")
        self.lbl_client_phone.grid(row=1,column=0)
        
        self.lbl_client_phone_value = tk.Label(self.detail_client_frame, text="Phone")
        self.lbl_client_phone_value.grid(row=1,column=1)
        
        self.lbl_client_email = tk.Label(self.detail_client_frame, text="Email")
        self.lbl_client_email.grid(row=2,column=0)
        
        self.lbl_client_email_value = tk.Label(self.detail_client_frame, text="Email")
        self.lbl_client_email_value.grid(row=2,column=1)
        
        self.lbl_client_address = tk.Label(self.detail_client_frame, text="Address")
        self.lbl_client_address.grid(row=3,column=0)
        
        self.lbl_client_address_value = tk.Label(self.detail_client_frame, text="Address")
        self.lbl_client_address_value.grid(row=3,column=1)
        
        self.listbox_client_orders = tk.Listbox(self.detail_client_frame, width=50)
        self.listbox_client_orders.grid(row=0,column=2,rowspan=4)
        
        # Detail Curier Frame
        
        self.detail_curier_frame = tk.Frame(self.details_frame)
        self.detail_curier_frame.pack()
        
        self.lbl_curier_name = tk.Label(self.detail_curier_frame, text="Name")
        self.lbl_curier_name.grid(row=0,column=0)
        
        self.lbl_curier_name_value = tk.Label(self.detail_curier_frame, text="Name")
        self.lbl_curier_name_value.grid(row=0,column=1)
        
        self.lbl_curier_phone = tk.Label(self.detail_curier_frame, text="Phone")
        self.lbl_curier_phone.grid(row=1,column=0)
        
        self.lbl_curier_phone_value = tk.Label(self.detail_curier_frame, text="Phone")
        self.lbl_curier_phone_value.grid(row=1,column=1)
        
        self.lbl_curier_location = tk.Label(self.detail_curier_frame, text="Location")
        self.lbl_curier_location.grid(row=2,column=0)
        
        self.lbl_curier_location_value = tk.Label(self.detail_curier_frame, text="Location")
        self.lbl_curier_location_value.grid(row=2,column=1)
        
        self.lbl_curier_status = tk.Label(self.detail_curier_frame, text="Status")
        self.lbl_curier_status.grid(row=3,column=0)
        
        self.lbl_curier_status_value = tk.Label(self.detail_curier_frame, text="Status")
        self.lbl_curier_status_value.grid(row=3,column=1)
        
        self.listbox_curier_orders = tk.Listbox(self.detail_curier_frame, width=50)
        self.listbox_curier_orders.grid(row=0,column=2,rowspan=5)
        
        # Detail Restaurant Frame
        
        self.detail_restaurant_frame = tk.Frame(self.details_frame)
        self.detail_restaurant_frame.pack()
        
        self.lbl_restaurant_name = tk.Label(self.detail_restaurant_frame, text="Name")
        self.lbl_restaurant_name.grid(row=0,column=0)
        
        self.lbl_restaurant_name_value = tk.Label(self.detail_restaurant_frame, text="Name")
        self.lbl_restaurant_name_value.grid(row=0,column=1)
        
        self.lbl_restaurant_phone = tk.Label(self.detail_restaurant_frame, text="Phone")
        self.lbl_restaurant_phone.grid(row=1,column=0)
        
        self.lbl_restaurant_phone_value = tk.Label(self.detail_restaurant_frame, text="Phone")
        self.lbl_restaurant_phone_value.grid(row=1,column=1)
        
        self.lbl_restaurant_description = tk.Label(self.detail_restaurant_frame, text="Description")
        self.lbl_restaurant_description.grid(row=2,column=0)
        
        self.lbl_restaurant_description_value = tk.Label(self.detail_restaurant_frame, text="Description")
        self.lbl_restaurant_description_value.grid(row=2,column=1)
        
        self.lbl_restaurant_rating = tk.Label(self.detail_restaurant_frame, text="Rating")
        self.lbl_restaurant_rating.grid(row=4,column=0)
        
        self.lbl_restaurant_rating_value = tk.Label(self.detail_restaurant_frame, text="Rating")
        self.lbl_restaurant_rating_value.grid(row=4,column=1)
        
        self.lbl_restaurant_address = tk.Label(self.detail_restaurant_frame, text="Address")
        self.lbl_restaurant_address.grid(row=5,column=0)
        
        self.lbl_restaurant_address_value = tk.Label(self.detail_restaurant_frame, text="Address")
        self.lbl_restaurant_address_value.grid(row=5,column=1)
        
        self.listbox_restaurant_orders = tk.Listbox(self.detail_restaurant_frame, width=50)
        self.listbox_restaurant_orders.grid(row=0,column=2,rowspan=4)
        
        self.btn_restaurant_couriers = tk.Button(self.detail_restaurant_frame, text="Clients", command=self.restaurant_couriers_btn,width=15)
        self.btn_restaurant_couriers.grid(row=6,column=2)
        
        
        # Detail Order Frame
        
        self.detail_order_frame = tk.Frame(self.details_frame)
        self.detail_order_frame.pack(expand=True, fill='both')
        
        self.lbl_order_restaurant = tk.Label(self.detail_order_frame, text="Restaurant")
        self.lbl_order_restaurant.grid(row=0,column=0)
        
        self.lbl_order_restaurant_value = tk.Label(self.detail_order_frame, text="Restaurant",width=50)
        self.lbl_order_restaurant_value.grid(row=0,column=1)
        
        self.lbl_order_client = tk.Label(self.detail_order_frame, text="Client")
        self.lbl_order_client.grid(row=1,column=0)
        
        self.lbl_order_client_value = tk.Label(self.detail_order_frame, text="Client",width=50)
        self.lbl_order_client_value.grid(row=1,column=1)
        
        self.lbl_order_curier = tk.Label(self.detail_order_frame, text="Curier")
        self.lbl_order_curier.grid(row=2,column=0)
        
        self.lbl_order_curier_value = tk.Label(self.detail_order_frame, text="Curier",width=50)
        self.lbl_order_curier_value.grid(row=2,column=1)
        
        self.lbl_order_status = tk.Label(self.detail_order_frame, text="Status")
        self.lbl_order_status.grid(row=3,column=0)
        
        self.lbl_order_status_value = tk.Label(self.detail_order_frame, text="Status",width=50)
        self.lbl_order_status_value.grid(row=3,column=1)
        
        self.lbl_order_details = tk.Label(self.detail_order_frame, text="Details")
        self.lbl_order_details.grid(row=4,column=0)
        
        self.lbl_order_details_value = tk.Label(self.detail_order_frame, text="Details",width=50)
        self.lbl_order_details_value.grid(row=4,column=1)
        
        
        # Details Buttons Frame
        
        self.btn_details_edit = tk.Button(self.details_buttons_frame, text="Edit",command=self.edit_btn, width=15)
        self.btn_details_edit.grid(row=0,column=0,pady=15)
        
        self.btn_details_delete = tk.Button(self.details_buttons_frame, text="Delete",command=self.delete_btn, width=15)
        self.btn_details_delete.grid(row=1,column=0,pady=15)
        
        self.btn_details_add = tk.Button(self.details_buttons_frame, text="Add",command=self.add_btn, width=15)
        self.btn_details_add.grid(row=2,column=0,pady=15)
       

    
    def hide_me(self,widget):
        widget.pack_forget()
        
    def show_me(self,widget):
        widget.pack()
    
    def populate_listbox(self, listbox: tk.Listbox, list: list) -> None:
        """
        Populates the given listbox with items from the provided list.
        If selection_mode is "order", the listbox will be populated with restaurant name.
        Otherwise, the listbox will be populated with object from list attribute name.

        Parameters:
        - listbox (tk.Listbox): The listbox to populate.
        - list (list): The list of items to populate the listbox with.

        """
        listbox.delete(0, tk.END)
        if self.selected_mode == self.selection_mode["order"]:
            for item in list:
                listbox.insert(tk.END, f'{item.id} {bknd.get_restaurant(item.restaurant_id).name} {bknd.get_order_status(item.status)}')
        else:
            for item in list:
                listbox.insert(tk.END, f'{item.name}')
                    
   
    
    def populate_list(self) -> list:
        """
        Populates the list based on the selected mode.

        Returns:
            A list of items based on the selected mode.
        """
        if self.selected_mode == self.selection_mode["client"]:
            return bknd.get_all_clients()
        elif self.selected_mode == self.selection_mode["curier"]:
            return bknd.get_all_couriers()
        elif self.selected_mode == self.selection_mode["restaurant"]:
            return bknd.get_all_restaurants()
        elif self.selected_mode == self.selection_mode["order"]:
            return bknd.get_all_orders()
    
    def refresh_listbox(self):
        """
        Refreshes the list_listbox with updated data.
        """
        self.list_listbox = self.populate_list()
        self.populate_listbox(self.listbox_main, self.list_listbox)
    
    
    def onselect(self, evt: tk.Event) -> None:
        """
        Handle the selection event of a listbox item.
        Updates the details frame with the selected item's data.

        Parameters:
        - evt (tk.Event): The event object containing information about the select event.
        """
        widget = evt.widget
        if len(widget.curselection()) == 0:
            return
        index = int(widget.curselection()[0])
        if self.selected_mode == self.selection_mode["client"]:
            name_value = self.list_listbox[index].name
            phone_value = self.list_listbox[index].phone
            email_value = self.list_listbox[index].email
            location = gis.get_lat_lon(self.list_listbox[index].location)
            self.map_view.set_position(location[0], location[1])
            address_value = gis.parse_address(gis.get_address_from_location(location[0], location[1]))
            self.lbl_client_name_value.config(text=name_value)
            self.lbl_client_phone_value.config(text=phone_value)
            self.lbl_client_email_value.config(text=email_value)
            self.lbl_client_address_value.config(text=address_value)
            orders = bknd.get_all_orders_by_client(self.list_listbox[index].id)
            self.listbox_client_orders.delete(0, tk.END)
            for order in orders:
                self.listbox_client_orders.insert(tk.END, str(order.id) + " " + bknd.get_order_status(order.status))
        elif self.selected_mode == self.selection_mode["curier"]:
            name_value = self.list_listbox[index].name
            phone_value = self.list_listbox[index].phone
            location = gis.get_lat_lon(self.list_listbox[index].location)
            self.map_view.set_position(location[0], location[1])
            address_value = gis.parse_address(gis.get_address_from_location(location[0], location[1]))
            status_value = bknd.get_courier_status(self.list_listbox[index].status)
            self.lbl_curier_name_value.config(text=name_value)
            self.lbl_curier_phone_value.config(text=phone_value)
            self.lbl_curier_location_value.config(text=address_value)
            self.lbl_curier_status_value.config(text=status_value)
            orders = bknd.get_all_orders_by_courier(self.list_listbox[index].id)
            self.listbox_curier_orders.delete(0, tk.END)
            for order in orders:
                self.listbox_curier_orders.insert(tk.END, str(order.id) + " " + bknd.get_order_status(order.status))
        elif self.selected_mode == self.selection_mode["restaurant"]:
            name_value = self.list_listbox[index].name
            phone_value = self.list_listbox[index].phone
            description_value = self.list_listbox[index].description
            rating_value = self.list_listbox[index].rating
            location = gis.get_lat_lon(self.list_listbox[index].location)
            self.map_view.set_position(location[0], location[1])
            address_value = gis.parse_address(gis.get_address_from_location(location[0], location[1]))
            self.lbl_restaurant_name_value.config(text=name_value)
            self.lbl_restaurant_phone_value.config(text=phone_value)
            self.lbl_restaurant_description_value.config(text=description_value)
            self.lbl_restaurant_rating_value.config(text=rating_value)
            self.lbl_restaurant_address_value.config(text=address_value)
            orders = bknd.get_all_orders_by_restaurant(self.list_listbox[index].id)
            self.listbox_restaurant_orders.delete(0, tk.END)
            for order in orders:
                self.listbox_restaurant_orders.insert(tk.END, str(order.id) + " " + bknd.get_order_status(order.status))
        elif self.selected_mode == self.selection_mode["order"]:
            restaurant_value = bknd.get_restaurant(self.list_listbox[index].restaurant_id).name
            client_value = bknd.get_client(self.list_listbox[index].client_id).name
            courier_value = bknd.get_courier(self.list_listbox[index].courier_id).name
            status_value = bknd.get_order_status(self.list_listbox[index].status)
            details_value = self.list_listbox[index].description
            self.lbl_order_restaurant_value.config(text=restaurant_value)
            self.lbl_order_client_value.config(text=client_value)
            self.lbl_order_curier_value.config(text=courier_value)
            self.lbl_order_status_value.config(text=status_value)
            self.lbl_order_details_value.config(text=details_value)
              
    
    def set_up_map(self, map_view: tkintermapview.TkinterMapView) -> None:
        """
        Sets up the map view based on the selected mode - self.selection_mode .
        """
        map_view.delete_all_marker()
        if self.selected_mode == self.selection_mode["client"]:
            for client in bknd.get_all_clients():
                lat, lon = gis.get_lat_lon(client.location)
                map_view.set_marker(lat, lon, text=client.name)
                map_view.set_position(lat, lon)
                map_view.set_zoom(5)
        elif self.selected_mode == self.selection_mode["curier"]:
            for curier in bknd.get_all_couriers():
                lat, lon = gis.get_lat_lon(curier.location)
                map_view.set_marker(lat, lon, text=curier.name)
                map_view.set_position(lat, lon)
                map_view.set_zoom(5)
        elif self.selected_mode == self.selection_mode["restaurant"]:
            for restaurant in bknd.get_all_restaurants():
                lat, lon = gis.get_lat_lon(restaurant.location)
                map_view.set_marker(lat, lon, text=restaurant.name)
                map_view.set_position(lat, lon)
                map_view.set_zoom(5)
                
    
    def restaurant_couriers_btn(self) -> None:
        """
        Populates the listbox with couriers of the selected restaurant.
        """
        self.selected_mode = 2
        self.hide_me(self.detail_restaurant_frame)
        self.show_me(self.detail_curier_frame)
        self.list_listbox = bknd.get_couriers_by_restaurant(self.list_listbox[self.listbox_main.curselection()[0]].id)
        print(self.list_listbox)
        self.populate_listbox(self.listbox_main, self.list_listbox)
    
    
    # Buttons Frame
    def details_client(self) -> None:
        """
        Displays the details of a client.
        This method sets the selected mode to client, refreshes the listbox, sets up the map view,
        shows the client detail, frame hides other frames"""
        self.selected_mode = 1
        self.refresh_listbox()
        self.set_up_map(self.map_view)
        self.lbl_list.config(text="Clients")
        self.hide_me(self.detail_curier_frame)
        self.hide_me(self.detail_restaurant_frame)
        self.hide_me(self.detail_order_frame)
        self.show_me(self.detail_client_frame)
        
    def details_curier(self)-> None:
        """
        Displays the details of couriers.
        It sets the selected mode to courier, refreshes the listbox, sets up the map view,
        updates the label text, hides other frames, and shows the courier frame.
        """
        self.selected_mode = 2
        self.refresh_listbox()
        self.set_up_map(self.map_view)
        self.lbl_list.config(text="Curiers")
        self.hide_me(self.detail_client_frame)
        self.hide_me(self.detail_restaurant_frame)
        self.hide_me(self.detail_order_frame)
        self.show_me(self.detail_curier_frame)
        
    def details_restaurant(self)-> None:
        """
        Displays details of a restaurant.
        It sets the selected mode to restaurant, refreshes the listbox, sets up the map view,
        updates the label text, hides other frames, and shows the restaurant frame.
        """
        self.selected_mode = 3
        self.refresh_listbox()
        self.set_up_map(self.map_view)
        self.lbl_list.config(text="Restaurants")
        self.hide_me(self.detail_client_frame)
        self.hide_me(self.detail_curier_frame)
        self.hide_me(self.detail_order_frame)
        self.show_me(self.detail_restaurant_frame)
        
    def details_order(self)-> None:
        """
        Displays the details of an order.
        It sets the selected mode to order, refreshes the listbox, sets up the map view,
        updates the label text, hides other frames, and shows the orders frame.
        """
        self.selected_mode = 4
        self.refresh_listbox()
        self.set_up_map(self.map_view)
        self.lbl_list.config(text="Orders")
        self.hide_me(self.detail_client_frame)
        self.hide_me(self.detail_curier_frame)
        self.hide_me(self.detail_restaurant_frame)
        self.show_me(self.detail_order_frame)

    def open_window(self):
        self.details_client()
        self.root.mainloop()
        
    def close_window(self):
        self.root.destroy()
    

    def edit_btn(self)-> None:
        """
        Edit button handler that calls the appropriate edit method based on the selected mode.
        """
        if self.selected_mode == self.selection_mode["client"]:
            self.edit_client()
        elif self.selected_mode == self.selection_mode["curier"]:
            self.edit_courier()
        elif self.selected_mode == self.selection_mode["restaurant"]:
            self.edit_restaurant()
        elif self.selected_mode == self.selection_mode["order"]:
            self.edit_order()
    
    def delete_btn(self)-> None:
        """
        Delete button handler that calls the appropriate delete method based on the selected mode.
        """
        if self.selected_mode == self.selection_mode["client"]:
            bknd.delete_client(self.list_listbox[self.listbox_main.curselection()[0]].id)
            self.details_client()
        elif self.selected_mode == self.selection_mode["curier"]:
            bknd.delete_courier(self.list_listbox[self.listbox_main.curselection()[0]].id)
            self.details_curier()
        elif self.selected_mode == self.selection_mode["restaurant"]:
            bknd.delete_restaurant(self.list_listbox[self.listbox_main.curselection()[0]].id)
            self.details_restaurant()
        elif self.selected_mode == self.selection_mode["order"]:
            bknd.delete_order(self.list_listbox[self.listbox_main.curselection()[0]].id)
    
    def add_btn(self)-> None:
        """
        Add button handler that calls the appropriate add method based on the selected mode.
        """
        if self.selected_mode == self.selection_mode["client"]:
            self.add_client()
        elif self.selected_mode == self.selection_mode["curier"]:
            self.add_courier()
        elif self.selected_mode == self.selection_mode["restaurant"]:
            self.add_restaurant()
        elif self.selected_mode == self.selection_mode["order"]:
            self.add_order()
            
    def edit_restaurant(self) -> None:
        """
        Opens a restaurant window with the id of the selected restaurant.
        """
        id = self.list_listbox[self.listbox_main.curselection()[0]].id
        restaurant_window = rest.restaurant_window(id)
        restaurant_window.open_window()
        
    def add_restaurant(self) -> None:
        """
        Opens a restaurant window. Passes 0 as the id parameter.
        """
        restaurant_window = rest.restaurant_window(0)
        restaurant_window.open_window()

    def edit_client(self) -> None:
        """
        Opens a client window with the id of the selected client.
        """
        id = self.list_listbox[self.listbox_main.curselection()[0]].id
        client_window = clnt.client_window(id)
        client_window.open_window()
    
    def add_client(self) -> None:
        """
        Opens a client window. Passes 0 as the id parameter.
        """
        client_window = clnt.client_window(0)
        client_window.open_window()
        
    def edit_courier(self) -> None:
        """
        Opens a courier window with the id of the selected courier.
        """
        id = self.list_listbox[self.listbox_main.curselection()[0]].id
        curier_window = cur.courier_window(id)
        curier_window.open_window()

    def add_courier(self) -> None:
        """
        Opens the courier window. Passes 0 as the id parameter.
        """
        curier_window = cur.courier_window(0)
        curier_window.open_window()
    
    def edit_order(self) -> None:
        """
        Opens the order window with the id of the selected order.
        """
        id = self.list_listbox[self.listbox_main.curselection()[0]].id
        order_window = ord.order_window(id)
        order_window.open_window()

    def add_order(self) -> None:
        """
        Opens a new order window. Passes 0 as the id parameter.
        """
        order_window = ord.order_window(0)
        order_window.open_window()