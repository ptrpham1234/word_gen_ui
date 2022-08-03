#############################################################################################################
# Assignment:
# Author:              Peter Pham (pxp180041)
# Course:              CS 4348.002
# Date Started:        02/08/2022
# IDE:                 pycharm
#
# Description:
#

# TODO: Change the layout of the widgets. Put the text on top and the checkboxes down at the bottom
#############################################################################################################

################# I M P O R T S #################
from tkinter import *
import tkinter as tk
from tkinter import CENTER, Canvas, PhotoImage, ttk as widgets




class Window:

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.frame = Frame(self.root)
        self.root.title("learning_gui window")
        self.root.geometry("900x500")
        self.root.minsize(900, 500)
        self.root.maxsize(1920, 1080)
        self.root.resizable(False, False)

        self.rand_message = "This is a random test message to use"

        self.enable_home = IntVar()
        self.enable_top = IntVar()
        self.enable_bottom = IntVar()

        # Displays a Text box
        self.text_box = tk.Text(self.root, wrap="word", relief=tk.FLAT, border=20, width=100, height=20)
        self.text_box.grid(row=0, column=0, columnspan=3, padx=30, pady=20, sticky=tk.NS)
        self.text_box.insert("end", self.rand_message)

        # Checkboxes
        self.enable_homerow_check = Checkbutton(self.root, text="Home Row", variable=self.enable_home,
                                                onvalue=1, offvalue=0)
        self.enable_homerow_check.grid(row=1, column=0)

        # Checkboxes
        self.enable_toprow_check = Checkbutton(self.root, text="Top Row", variable=self.enable_top,
                                                onvalue=1, offvalue=0)
        self.enable_toprow_check.grid(row=1, column=1)

        # Checkboxes
        self.enable_bottomrow_check = Checkbutton(self.root, text="Bottom Row", variable=self.enable_bottom,
                                                onvalue=1, offvalue=0)
        self.enable_bottomrow_check.grid(row=1, column=2)

        # Button 
        self.button = Button(self.root, text="Generate", command=lambda: self.button_clicked(self.enable_home.get(), self.enable_top.get(), self.enable_bottom.get()))
        self.button.config(width=15, pady=8, borderwidth=3)
        self.button.grid(row=2, column=1, pady=15)

        # # Button to press
        # self.button = widgets.Button(self.root)
        # self.button.config(text="Generate", command=lambda: self.button_clicked(self.enable_home.get()))
        # self.button.bind("<Return>", self.return_pressed)
        # self.button.focus()
        # self.button.pack(side=tk.BOTTOM)




    #############################################################################################################
    #  * Function:            main
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        02/08/2022
    #  *
    #  * Description:
    #  * Main purpose is to check for arguments and start main function
    #  *
    #  * Parameters:
    #############################################################################################################
    def button_clicked(self, enable_home, enable_top, enable_bottom) -> None:
        if enable_home:
            print("\nhome checked")
        else:
            print("\nhome not checked")

        if enable_top:
            print("top row checked")
        else:
            print("top row not checked")

        if enable_bottom:
            print("bottom row checked")
        else:
            print("bottom row not checked")

    #############################################################################################################
    #  * Function:            main
    #  * Author:              Peter Pham (pxp180041)
    #  * Date Started:        02/08/2022
    #  *
    #  * Description:
    #  * Main purpose is to check for arguments and start main function
    #  *
    #  * Parameters:
    #############################################################################################################
    def return_pressed(self, event):
        print(event)

    def mainloop(self) -> None:
        self.root.mainloop()

#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        02/08/2022
#  *
#  * Description:
#  * Main purpose is to check for arguments and start main function
#  *
#  * Parameters:
#############################################################################################################
def main():

    root = Window()
    root.mainloop()

    print("done")


#############################################################################################################
#  * Function:            main
#  * Author:              Peter Pham (pxp180041)
#  * Date Started:        02/08/2022
#  *
#  * Description:
#  * Main purpose is to check for arguments and start main function
#  *
#  * Parameters:
#############################################################################################################
if __name__ == '__main__':
    main()