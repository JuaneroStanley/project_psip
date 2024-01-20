import tkinter as tk
import tkintermapview


def hide_me(widget):
    widget.pack_forget()

window = tk.Tk()
window.title("New Order")
window.geometry("600x600")

lbl_new_order = tk.Label(window, text="New Order")
lbl_new_order.pack()

frm_restaurant = tk.Frame(window)
frm_restaurant.pack()


lbl_choose_restaurant = tk.Label(frm_restaurant, text="Choose Restaurant")
lbl_choose_restaurant.pack()

enr_restaurant = tk.Entry(frm_restaurant, width=50)
enr_restaurant.pack()

btn_search_restaurant = tk.Button(frm_restaurant, text="Search")
btn_search_restaurant.pack(side=tk.LEFT)

btn_choose_restaurant = tk.Button(frm_restaurant, text="Choose")
btn_choose_restaurant.pack(side=tk.RIGHT)
btn_choose_restaurant.bind('<Button-1>', lambda event: hide_me(mpv_restaurant))

mpv_restaurant = tkintermapview.TkinterMapView(window,width=400,height=400,corner_radius=10)
mpv_restaurant.pack()





window.mainloop()