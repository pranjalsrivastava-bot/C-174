from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root = Tk()
root.geometry("900x500")

burger = ImageTk,PhotoImage(Image.open ("burger-cartoon_119631-249.avif"))
burger_image=Label(root)
burger_image["image"]=burger
burger_image.place(relx=0.7, rely=0.5, anchor=CENTER)

label_heading=Label(root, text="Rdonalds", font=("times", 40, "bold"), fg="Orange")
label_heading.place(relx=0.12, rely=0.1, anchor=CENTER)

label_select_dish=Label(root,text="Select Dish", font=("times", 15))
label_select_dish.place(relx==0.06, rely=0.2, anchor=CENTER)

dish=["burger", "iced_americano"]
dish_dropdown = ttk.Comboboc(root, state = "readonly", avlues = dish)
dish_dropdown.place(relx=0.25, rely=0.2, anchor=CENTER)

label_select_addons=Label(root, text="Select Add-Ons", font=("times", 15))
label_select_addons.place(relx=0.08, rely=0.5, anchor=CENTER)

toppigs=[]
toppings_dropdown = ttk.Combobox(root, state = "readonly", values= toppings)
toppings_dropdown.place(relx=0.25, rely=0.5, anchor=CENTER)

dish_amount=Label(root, font=("times", 15, "bold"))
dish_amount.place(relx=0.2, rely=0.75, anchor=CENTER)


class parent():
    
    def __init__(self):
        print("This is the parent class")
        
    def menu(dish):
        if dish=="sandwich":
            print("You can add the following fillings")
            print("Letuce leaves | Cheese slice")
        elif dish=="custard":
            print("You can add the following ingredients")
            print("Fruits | Dry Fruits")
        else:
            print("Please enter a valid dish")
    
    def final_amount(dish, add_ons):
        if dish=="sandwich" and add_ons=="letuce leaves":
            print("Amount : 349 INR")
        elif dish=="burger" and add_ons=="cheese slice":
            print("Amount : 399 INR")
        elif dish=="custard"and add_ons=="Fruits":
            print("Amount : 369 INR")
        elif dish=="custard" and add_ons=="Dry Fruits":
            print("Amount : 359 INR")
            
class child1(parent):
    
    def __init__(self,dish):
        self.new_dish = dish
    def get_menu(self):
        parent.menu(self.new_dish)
        
class child2(parent):
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.addons)
        
child1_object=child1("burger")
child1_object.get_menu()
child2_object=child2("burger","jalepeeno")
child2_object.get_final_amount()

btn_addons = Button(root, text="Check Add-ons", command=child1_object.get_menu, bg="Blue", fg="White", relief=FLAT)
btn_addons.place(relx=0.06, rely=0.3, anchor=CENTER)

btn_amount = Button(root, text="Amount", command=child2_object.get_final_amount, bg="Blue", fg="White", relief=FLAT)
btn_amount.place(relx=0.04, rely=0.6, anchor=CENTER)

root.mainloop()
        