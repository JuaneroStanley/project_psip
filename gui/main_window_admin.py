import tkinter as tk
import tkintermapview
import utils.backend as bknd 

class main_window_admin:
            
    def hide_me(_,widget):
        widget.pack_forget()
        
    def show_me(_,widget):
        widget.pack()
        
    root = tk.Tk()
    root.title("My App")
    root.geometry("900x700")
    
    lbl_list="List"

    main_frame = tk.Frame(root)
    main_frame.pack(padx=15,pady=15)
    
    main_frame.grid_columnconfigure(0,weight=4)
    main_frame.grid_columnconfigure(1,weight=2)
    main_frame.grid_columnconfigure(2,weight=1)
      
    map_view = tkintermapview.TkinterMapView(main_frame,width=400,height=400,corner_radius=10)
    map_view.grid(row=0,column=0,rowspan=12)
    
    list_frame = tk.Frame(main_frame)
    list_frame.grid(row=0,column=1,rowspan=12,padx=15)
    
    buttons_frame = tk.Frame(main_frame)
    buttons_frame.grid(row=0,column=2,rowspan=12)
    
    details_frame = tk.Frame(main_frame)
    details_frame.grid(row=13,column=0,columnspan=2, rowspan=6,pady=30)
    
    details_buttons_frame = tk.Frame(main_frame)
    details_buttons_frame.grid(row=13,column=2,rowspan=6)
    
    # List Frame
    lbl_list = tk.Label(list_frame, text=lbl_list)
    lbl_list.pack()
    
    listbox = tk.Listbox(list_frame, width=50, height=22)
    listbox.pack()
    
    
    # Buttons Frame
    def details_client():
        main_window_admin.listbox.delete(0,tk.END)
        for client in bknd.get_all_clients():
            main_window_admin.listbox.insert(tk.END,client.name)
        main_window_admin.hide_me(main_window_admin.detail_curier_frame)
        main_window_admin.hide_me(main_window_admin.detail_restaurant_frame)
        main_window_admin.hide_me(main_window_admin.detail_order_frame)
        main_window_admin.show_me(main_window_admin.detail_client_frame)
        
    def details_curier():
        main_window_admin.listbox.delete(0,tk.END)
        for curier in bknd.get_all_couriers():
            main_window_admin.listbox.insert(tk.END,curier.name)
        main_window_admin.hide_me(main_window_admin.detail_client_frame)
        main_window_admin.hide_me(main_window_admin.detail_restaurant_frame)
        main_window_admin.hide_me(main_window_admin.detail_order_frame)
        main_window_admin.show_me(main_window_admin.detail_curier_frame)
        
    def details_restaurant():
        main_window_admin.listbox.delete(0,tk.END)
        for restaurant in bknd.get_all_restaurants():
            main_window_admin.listbox.insert(tk.END,restaurant.name)
        main_window_admin.hide_me(main_window_admin.detail_client_frame)
        main_window_admin.hide_me(main_window_admin.detail_curier_frame)
        main_window_admin.hide_me(main_window_admin.detail_order_frame)
        main_window_admin.show_me(main_window_admin.detail_restaurant_frame)
        
    def details_order():
        main_window_admin.listbox.delete(0,tk.END)
        for order in bknd.get_all_orders():
            main_window_admin.listbox.insert(tk.END,order.id)
        main_window_admin.hide_me(main_window_admin.detail_client_frame)
        main_window_admin.hide_me(main_window_admin.detail_curier_frame)
        main_window_admin.hide_me(main_window_admin.detail_restaurant_frame)
        main_window_admin.show_me(main_window_admin.detail_order_frame)
    
    
    
    btn_clients = tk.Button(buttons_frame, text="Clients", command=details_client, width=15)
    btn_clients.grid(row=1,column=0,pady=15)
    
    btn_curiers = tk.Button(buttons_frame, text="Curiers", command=details_curier, width=15)
    btn_curiers.grid(row=2,column=0,pady=15)
    
    btn_restaurants = tk.Button(buttons_frame, text="Restaurants", command=details_restaurant, width=15)
    btn_restaurants.grid(row=3,column=0,pady=15)
    
    btn_orders = tk.Button(buttons_frame, text="Orders", command=details_order, width=15)
    btn_orders.grid(row=4,column=0,pady=15)
    
    
    # Details Frame
    
    # Detail Client Frame
    
    detail_client_frame = tk.Frame(details_frame)
    detail_client_frame.pack()
    
    lbl_client_name = tk.Label(detail_client_frame, text="Name")
    lbl_client_name.grid(row=0,column=0)
    
    lbl_client_name_value = tk.Label(detail_client_frame, text="Name")
    lbl_client_name_value.grid(row=0,column=1)
    
    lbl_client_phone = tk.Label(detail_client_frame, text="Phone")
    lbl_client_phone.grid(row=1,column=0)
    
    lbl_client_phone_value = tk.Label(detail_client_frame, text="Phone")
    lbl_client_phone_value.grid(row=1,column=1)
    
    lbl_client_email = tk.Label(detail_client_frame, text="Email")
    lbl_client_email.grid(row=2,column=0)
    
    lbl_client_email_value = tk.Label(detail_client_frame, text="Email")
    lbl_client_email_value.grid(row=2,column=1)
    
    lbl_client_address = tk.Label(detail_client_frame, text="Address")
    lbl_client_address.grid(row=3,column=0)
    
    lbl_client_address_value = tk.Label(detail_client_frame, text="Address")
    lbl_client_address_value.grid(row=3,column=1)
    
    listbox_client_orders = tk.Listbox(detail_client_frame, width=50)
    listbox_client_orders.grid(row=0,column=2,rowspan=4)
    
    # Detail Curier Frame
    
    detail_curier_frame = tk.Frame(details_frame)
    detail_curier_frame.pack()
    
    lbl_curier_name = tk.Label(detail_curier_frame, text="Name")
    lbl_curier_name.grid(row=0,column=0)
    
    lbl_curier_name_value = tk.Label(detail_curier_frame, text="Name")
    lbl_curier_name_value.grid(row=0,column=1)
    
    lbl_curier_phone = tk.Label(detail_curier_frame, text="Phone")
    lbl_curier_phone.grid(row=1,column=0)
    
    lbl_curier_phone_value = tk.Label(detail_curier_frame, text="Phone")
    lbl_curier_phone_value.grid(row=1,column=1)
    
    lbl_curier_email = tk.Label(detail_curier_frame, text="Email")
    lbl_curier_email.grid(row=2,column=0)
    
    lbl_curier_email_value = tk.Label(detail_curier_frame, text="Email")
    lbl_curier_email_value.grid(row=2,column=1)
    
    lbl_curier_location = tk.Label(detail_curier_frame, text="Location")
    lbl_curier_location.grid(row=3,column=0)
    
    lbl_curier_location_value = tk.Label(detail_curier_frame, text="Location")
    lbl_curier_location_value.grid(row=3,column=1)
    
    lbl_curier_status = tk.Label(detail_curier_frame, text="Status")
    lbl_curier_status.grid(row=4,column=0)
    
    lbl_curier_status_value = tk.Label(detail_curier_frame, text="Status")
    lbl_curier_status_value.grid(row=4,column=1)
    
    listbox_curier_orders = tk.Listbox(detail_curier_frame, width=50)
    listbox_curier_orders.grid(row=0,column=2,rowspan=5)
    
    # Detail Restaurant Frame
    
    detail_restaurant_frame = tk.Frame(details_frame)
    detail_restaurant_frame.pack()
    
    lbl_restaurant_name = tk.Label(detail_restaurant_frame, text="Name")
    lbl_restaurant_name.grid(row=0,column=0)
    
    lbl_restaurant_name_value = tk.Label(detail_restaurant_frame, text="Name",width=50)
    lbl_restaurant_name_value.grid(row=0,column=1)
    
    lbl_restaurant_phone = tk.Label(detail_restaurant_frame, text="Phone")
    lbl_restaurant_phone.grid(row=1,column=0)
    
    lbl_restaurant_phone_value = tk.Label(detail_restaurant_frame, text="Phone",width=50)
    lbl_restaurant_phone_value.grid(row=1,column=1)
    
    lbl_restaurant_description = tk.Label(detail_restaurant_frame, text="Description")
    lbl_restaurant_description.grid(row=2,column=0)
    
    lbl_restaurant_description_value = tk.Label(detail_restaurant_frame, text="Description",width=50)
    lbl_restaurant_description_value.grid(row=2,column=1)
    
    lbl_restaurant_rating = tk.Label(detail_restaurant_frame, text="Rating")
    lbl_restaurant_rating.grid(row=4,column=0)
    
    lbl_restaurant_rating_value = tk.Label(detail_restaurant_frame, text="Rating",width=50)
    lbl_restaurant_rating_value.grid(row=4,column=1)
    
    lbl_restaurant_address = tk.Label(detail_restaurant_frame, text="Address")
    lbl_restaurant_address.grid(row=5,column=0)
    
    lbl_restaurant_address_value = tk.Label(detail_restaurant_frame, text="Address",width=50)
    lbl_restaurant_address_value.grid(row=5,column=1)
    
    lbl_restaurant_orders = tk.Label(detail_restaurant_frame, text="Orders",justify=tk.LEFT,width=20)
    lbl_restaurant_orders.grid(row=0,column=2)
    
    listbox_restaurant_orders = tk.Listbox(detail_restaurant_frame, width=20)
    listbox_restaurant_orders.grid(row=0,column=2,rowspan=4)
    
    btn_restaurant_show_orders = tk.Button(detail_restaurant_frame, text="Show Order", width=16)
    btn_restaurant_show_orders.grid(row=5,column=2)
    
    
    # Detail Order Frame
    
    detail_order_frame = tk.Frame(details_frame)
    detail_order_frame.pack(expand=True, fill='both')
    
    lbl_order_restaurant = tk.Label(detail_order_frame, text="Restaurant")
    lbl_order_restaurant.grid(row=0,column=0)
    
    lbl_order_restaurant_value = tk.Label(detail_order_frame, text="Restaurant",width=50)
    lbl_order_restaurant_value.grid(row=0,column=1)
    
    lbl_order_client = tk.Label(detail_order_frame, text="Client")
    lbl_order_client.grid(row=1,column=0)
    
    lbl_order_client_value = tk.Label(detail_order_frame, text="Client",width=50)
    lbl_order_client_value.grid(row=1,column=1)
    
    lbl_order_curier = tk.Label(detail_order_frame, text="Curier")
    lbl_order_curier.grid(row=2,column=0)
    
    lbl_order_curier_value = tk.Label(detail_order_frame, text="Curier",width=50)
    lbl_order_curier_value.grid(row=2,column=1)
    
    lbl_order_status = tk.Label(detail_order_frame, text="Status")
    lbl_order_status.grid(row=3,column=0)
    
    lbl_order_status_value = tk.Label(detail_order_frame, text="Status",width=50)
    lbl_order_status_value.grid(row=3,column=1)
    
    lbl_order_details = tk.Label(detail_order_frame, text="Details")
    lbl_order_details.grid(row=4,column=0)
    
    lbl_order_details_value = tk.Label(detail_order_frame, text="Details",width=50)
    lbl_order_details_value.grid(row=4,column=1)
    
    
    # Details Buttons Frame
    
    btn_details_edit = tk.Button(details_buttons_frame, text="Edit", width=15)
    btn_details_edit.grid(row=0,column=0,pady=15)
    
    btn_details_delete = tk.Button(details_buttons_frame, text="Delete", width=15)
    btn_details_delete.grid(row=1,column=0,pady=15)
    
    btn_details_add = tk.Button(details_buttons_frame, text="Add", width=15)
    btn_details_add.grid(row=2,column=0,pady=15)
    
    def initialize_details(self):
        self.detail_client_frame.pack_forget()
        self.detail_curier_frame.pack_forget()
        self.detail_restaurant_frame.pack_forget()

    def open_window(self):
        self.initialize_details()
        self.root.mainloop()
        
    def close_window(self):
        self.root.destroy()
    


