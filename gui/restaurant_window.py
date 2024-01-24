import tkinter as tk
import utils.gis as gis
import utils.backend as bknd


class restaurant_window:
    
    def __init__(self, client_id):
        self.root = tk.Toplevel()
        self.root.title("Restaurant")
        self.root.geometry("300x250")
        self.restaurant_id = client_id
        
        self.lbl_name = tk.Label(self.root, text="Nazwa:")
        self.lbl_name.grid(row=0, column=0)
        
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1)
        
        self.lbl_phone = tk.Label(self.root, text="Telefon:")
        self.lbl_phone.grid(row=1, column=0)
        
        self.entry_phone = tk.Entry(self.root)
        self.entry_phone.grid(row=1, column=1)
        
        self.lbl_rating = tk.Label(self.root, text="Rating:")
        self.lbl_rating.grid(row=2, column=0)
        
        self.entry_rating = tk.Entry(self.root)
        self.entry_rating.grid(row=2, column=1)
        
        self.lbl_postal = tk.Label(self.root, text="Kod pocztowy:")
        self.lbl_postal.grid(row=3, column=0)
        
        self.entry_postal = tk.Entry(self.root)
        self.entry_postal.grid(row=3, column=1)
        
        self.lbl_city = tk.Label(self.root, text="Miasto:")
        self.lbl_city.grid(row=4, column=0)
        
        self.entry_city = tk.Entry(self.root)
        self.entry_city.grid(row=4, column=1)
        
        self.lbl_street = tk.Label(self.root, text="Ulica:")
        self.lbl_street.grid(row=5, column=0)
        
        self.entry_street = tk.Entry(self.root)
        self.entry_street.grid(row=5, column=1)
        
        self.lbl_house = tk.Label(self.root, text="Numer domu:")
        self.lbl_house.grid(row=6, column=0)
        
        self.entry_house = tk.Entry(self.root)
        self.entry_house.grid(row=6, column=1)
        
        self.lbl_description = tk.Label(self.root, text="Opis:")
        self.lbl_description.grid(row=7, column=0)
        
        self.entry_description = tk.Entry(self.root)
        self.entry_description.grid(row=7, column=1, columnspan=2)
        
        self.btn_save = tk.Button(self.root, text="Zapisz", command=self.save)
        self.btn_save.grid(row=8, column=0, columnspan=2)
        
        self.populate(self.restaurant_id)
        
        
        
    def save(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        rating = self.entry_rating.get()
        postal = self.entry_postal.get()
        city = self.entry_city.get()
        street = self.entry_street.get()
        house = self.entry_house.get()
        description = self.entry_description.get()
        
        address = f'{postal} {city}, {street} {house}'
        localisation = gis.get_point_from_address(address)
        
        if self.restaurant_id == 0:
            bknd.add_restaurant(name, phone,description, rating, localisation)
            self.root.destroy()
        else:
            bknd.edit_restaurant(self.restaurant_id, name, phone, description,rating, localisation)
            self.root.destroy()
            
        
    def populate(self, restaurant_id:int):
        """
        Populates the restaurant window with data from the specified restaurant if editing.

        Args:
            restaurant_id (int): The ID of the restaurant to populate the window with.

        Returns:
            None
        """
        if restaurant_id == 0:
            return
        restaurant = bknd.get_restaurant(restaurant_id)
        self.entry_name.insert(0, restaurant.name)
        self.entry_phone.insert(0, restaurant.phone)
        self.entry_rating.insert(0, restaurant.rating)
        self.entry_description.insert(0, restaurant.description)
        lat, lon = gis.get_lat_lon(restaurant.location)
        address = gis.parse_address(gis.get_address_from_location(lat, lon))
        self.entry_postal.insert(0, address[2])
        self.entry_city.insert(0, address[3])
        self.entry_street.insert(0, address[0])
        self.entry_house.insert(0, address[1])
        
    def open_window(self):
        
        self.root.mainloop()
        