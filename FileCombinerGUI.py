import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

def combine_files():
    line_break = int(line_break_var.get())
    remove_old = int(remove_old_var.get())
    inputs = input_entry.get().split(',')
    output = output_entry.get()

    with open(output, 'w') as outfile:
        for word in inputs:
            filename = word.strip()
            outfile.write(open(filename).read())
            if line_break:
                outfile.write("\n")
            if remove_old:
                remove_msg = f"Do you want to remove {filename}? (0 or 1): "
                temp = int(input(remove_msg))
                if temp:
                    os.remove(filename)

    result_label.config(text = "Write complete.")
    output_size = os.path.getsize(output)
    size_msg = f"Size of {output}: {str(f'{output_size:,d}')} bytes"
    size_label.config(text=size_msg)
    path_name = Path.cwd()
    ps = 0
    for path, dirs, files in os.walk(path_name):
        for f in files:
            ps += os.path.getsize(os.path.join(path, f))
    path_size = int(str(ps))
    path_msg = f"Size of {path_name}: {str(f'{path_size:,d}')} bytes"
    path_label.config(text=path_msg)
    
def browse_file(entry):
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(tk.END, filename)

root = tk.Tk()
root.title("File Combiner")
line_break_label = tk.Label(root, text="Insert newline between files:")
line_break_label.grid(row=0, column=0)
line_break_var = tk.StringVar(value="0")
line_break_check = tk.Checkbutton(root, variable=line_break_var)
line_break_check.grid(row=0, column=1)
remove_old_label = tk.Label(root, text="Remove input files after combining:")
remove_old_label.grid(row=1, column=0)
remove_old_var = tk.StringVar(value="0")
remove_old_check = tk.Checkbutton(root, variable=remove_old_var)
remove_old_check.grid(row=1, column=1)
input_label = tk.Label(root, text="Input files:")
input_label.grid(row=2, column=0)
input_entry = tk.Entry(root)
input_entry.grid(row=2, column=1)
output_label = tk.Label(root, text="Output file:")
output_label.grid(row=3, column=0)
output_entry = tk.Entry(root)
output_entry.grid(row=3, column=1)

input_browse_button = tk.Button(root, text="Browse", command=lambda: browse_file(input_entry))
input_browse_button.grid(row=2, column=2)
output_browse_button = tk.Button(root, text="Browse", command=lambda: browse_file(output_entry))
output_browse_button.grid(row=3, column=2)

combine_button = tk.Button(root, text="Combine Files", command=combine_files)
combine_button.grid(row=4, column=1, pady=10)
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)
size_label = tk.Label(root, text="")
size_label.grid(row=6, column=0, columnspan=2)
path_label = tk.Label(root, text="")
path_label.grid(row=7, column=0, columnspan=2)
root.mainloop()
