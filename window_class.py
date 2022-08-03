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
        self.root.resizable(True, True)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)

        self.rand_message = "This is a random test message to use"

        self.enable_home = IntVar()

        # Displays a Text box
        self.text_box = tk.Text(self.root, wrap="word", relief=tk.FLAT, border=20)
        self.text_box.grid(row=1, column=1, rowspan=5)
        self.text_box.insert("end", self.rand_message)

        # Checkboxes
        self.enable_homerow_check = Checkbutton(self.root, text="this is a checkbox part 2", variable=self.enable_home,
                                                onvalue=1, offvalue=0)
        self.enable_homerow_check.grid(row=1, column=0, padx=10)

        # Checkboxes
        # ! change the
        self.enable_toprow_check = Checkbutton(self.root, text="this is a checkbox part 2", variable=self.enable_home,
                                                onvalue=1, offvalue=0)
        self.enable_toprow_check.grid(row=2, column=0, padx=10)

        # Checkboxes
        self.enable_bottomrow_check = Checkbutton(self.root, text="this is a checkbox part 2", variable=self.enable_home,
                                               onvalue=1, offvalue=0)
        self.enable_bottomrow_check.grid(row=10, column=0, padx=10)

        # # Button to press
        # self.button = widgets.Button(self.root)
        # self.button.config(text="Generate", command=lambda: self.button_clicked(self.enable_home.get()))
        # self.button.bind("<Return>", self.return_pressed)
        # self.button.focus()
        # self.button.pack(side=tk.BOTTOM)

        # Create a size grip to resize easier
        self.size_grip = widgets.Sizegrip(self.root)
        self.size_grip.grid(row=5, column=1, sticky=tk.SE)




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
    def button_clicked(self, enable_home) -> None:
        if enable_home:
            print("checked")
        else:
            print("not checked")

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