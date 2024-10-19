from tkinter import *
from tkinter import ttk
import random
from sorts_aux import *

VEL: float = 0.075

root: Tk = Tk()
root.title('Sort algorithm visualizer')
root.maxsize(1800,1000)
root.config(bg='Black')

select_alg: StringVar = StringVar()
data: list[int] = []

# Generate data with given values range
def generate() -> None:
    global data

    min_val: int = int(min_entry.get())
    max_val: int = int(max_entry.get())
    size_val: int = int(size_entry.get())

    data = []
    for _ in range(size_val):
        data.append(random.randrange(min_val,max_val+1))

    drawData(data, ['Red' for x in range(len(data))])

def drawData(data: list[int], colorlist: list[str]) -> None:
    canvas.delete('all')
    can_height: int = 600
    can_width: int = 1100
    x_width: int = can_width/(len(data)+1)
    offset: int = 60
    spacing: int = 10

    normalized_data: list[int] = [d / max(data) for d in data]

    for i, height in enumerate(normalized_data):
        # Top left corner
        x0: int = i*x_width+offset+spacing
        y0: int = can_height-height*500
        # Bottom right corner
        x1: int = ((i+1)*x_width)+offset
        y1: int = can_height

        canvas.create_rectangle(x0,y0,x1,y1, fill=colorlist[i])
        canvas.create_text(x0+2, y0, anchor=SE, text=str(data[i]))
    root.update_idletasks()


def start_alg() -> None:
    global data
    # bubble(data, drawData, speedbar.get())
    if select_alg.get() == 'Bubble Sort':
        bubble(data, drawData, VEL)
    elif select_alg.get() == 'Insertion Sort':
        insertion(data, drawData, VEL)
    # elif select_alg.get() == 'Merge Sort':
    #     merge(data, drawData, VEL)
    elif select_alg.get() == 'Quick Sort':
        # quicksort(data, drawData, VEL)
        # quick_sort(data, 0, len(data)-1, drawData, VEL)
        quick_sort(data, drawData, VEL)

# Frame for the main UI
Mainframe: Frame = Frame(root, width=1200, height=600, bg='Light grey')
Mainframe.grid(row=0, column=0, padx=10, pady=5)

canvas: Canvas = Canvas(root, width=1200, height=600, bg='Light grey')
canvas.grid(row=1, column=0, padx=10, pady=5)

label: Label = Label(
    Mainframe, 
    text='Sorting Algorithms Visualizer', 
    bg='Light grey'
)
label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

alg_menu: ttk.Combobox = ttk.Combobox(
    Mainframe,
    textvariable=select_alg,
    values=[
        'Bubble Sort',
        'Insertion Sort',
        # 'Merge Sort',
        'Quick Sort'
    ]
)
alg_menu.grid(row=0, column=1, padx=5, pady=5)
alg_menu.current(0)

start_button: Button = Button(
    Mainframe,
    text='START',
    bg='Blue',
    command=start_alg
)
start_button.grid(row=1, column=3, padx=5, pady=5)

# speedbar: Scale = Scale(
#     Mainframe,
#     from_=0.10,
#     to=2.0,
#     length=100,
#     digits=2,
#     resolution=0.2,
#     orient=HORIZONTAL,
#     label='Select speed'
# )
# speedbar.grid(row=0, column=2, padx=5, pady=5)

size_entry: Scale = Scale(
    Mainframe,
    from_=5,
    to=60,
    resolution=1,
    orient=HORIZONTAL,
    label='Size'
)
size_entry.grid(row=1, column=0, padx=5, pady=5)

min_entry: Scale = Scale(
    Mainframe,
    from_=1,
    to=10,
    resolution=1,
    orient=HORIZONTAL,
    label='Minimum value'
)
min_entry.grid(row=1, column=1, padx=5, pady=5)

max_entry: Scale = Scale(
    Mainframe,
    from_=10,
    to=100,
    resolution=1,
    orient=HORIZONTAL,
    label='Maximum value'
)
max_entry.grid(row=1, column=2, padx=5, pady=5)

gen_button: Button = Button(
    Mainframe,
    text='Generate',
    bg='Red',
    command=generate
)
gen_button.grid(row=0, column=3, padx=5, pady=5)

if __name__ == '__main__':
    root.mainloop()