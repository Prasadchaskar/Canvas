from tkinter import *
root=Tk()
root.title("Canvas")
canvas_width=800
canvas_height=500
root.geometry(f"{canvas_width}x{canvas_height}")

canvas_widget=Canvas(root,width=canvas_width,height=canvas_height)

def paint(event):
   
   x1, y1 = (event.x - 1), (event.y - 1)
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   canvas_widget.create_rectangle( x1, y1, x2, y2, fill = "red")
#Draw a line
canvas_widget.create_line(100,100,200,200,fill="red")

#draw rectangle
# canvas_widget.create_rectangle(50,20,150,80,fill="blue")
# canvas_widget.create_rectangle(150,80,200,140,fill="red")
#canvas_widget.create_text(canvas_width/2,canvas_height/2,text="Prasad")

canvas_widget.pack(expand = YES, fill = BOTH)
canvas_widget.bind( "<B1-Motion>", paint )

message = Label( root, text = "Press and Drag the mouse to draw" )
message.pack()
root.mainloop()