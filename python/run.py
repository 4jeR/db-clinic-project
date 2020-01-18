from guis import *


if __name__ == '__main__':
    connection, cursor = connect()
    root = Tk()
    root.title("Aplikacja bazodanowa - przychodnia specjalistyczna")
    root.wm_minsize(800, 600)  
    root.wm_maxsize(1200, 800) 
    root.configure(background=rgb(217, 240, 255))
    gui_main(connection, cursor, root, [])
    root.mainloop()
