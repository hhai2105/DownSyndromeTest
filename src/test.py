button_up = Image.open((r"C:\Users\ezsaksa\Desktop\code\images_red.jpg"))
button_down = Image.open((r"C:\Users\ezsaksa\Desktop\code\images_green.jpg"))
b_t_size = [9, 9]
 
button_up.thumbnail((b_t_size[0],b_t_size[1]))
button_down.thumbnail((b_t_size[0],b_t_size[1]))
button_up = ImageTk.PhotoImage(button_up)
button_down = ImageTk.PhotoImage(button_down)
 
def PlayButtonDown():
     
   button_dict["Button" + str(i)] = tk.Button(image = button_down, command = lambda i = i: PlayButtonUp())
   button_dict["Button" + str(i)].update()
   return button_dict
 
def PlayButtonUp():
 
    button_dict["Button" + str(i)] = tk.Button(image = button_up, command = lambda i = i: PlayButtonDown())
    button_dict["Button" + str(i)].update()
    return button_dict 
 
button_dict = {}
 
while i < len(co_list):
    
    button_dict["Button" + str(i)] = tk.Button(image = button_up, command = lambda i = i: PlayButtonDown())
    button_dict["Button" + str(i)]["bg"] = "white"
    button_dict["Button" + str(i)]["border"] = "0"
    button_dict["Button" + str(i)].place(x=float(1.393)*co_list[i][0]-b_t_size[0]/2, y=float(1.392)*co_list[i][1]-b_t_size[1]/2)
    i += 1
 
root.mainloop()
