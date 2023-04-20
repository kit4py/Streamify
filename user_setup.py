import tkinter as tk

# Initialize the Tkinter window
window = tk.Tk()
window.title("Configuration Variables")

# Create a label and entry for each variable
variables = {
    "TASK_FIRST": tk.StringVar(),
    "REGISTER_ACCOUNTS_QUANTITY": tk.StringVar(),
    "WEBSITE_LOAD_TIME": tk.StringVar(),
    "USER_START_SLEEP": tk.StringVar(),
    "NUMBER_SKIP": tk.StringVar(),
    "FOLLOW_SAVE_VAR": tk.BooleanVar(),
    "MIN_PLAY_TIME": tk.StringVar(),
    "MAX_PLAY_TIME": tk.StringVar(),
    "USE_NORD_VPN": tk.BooleanVar(),
    "USE_MOUSE_DONT_SLEEP": tk.BooleanVar(),
    "NUM_OF_RUNNING_WINDOWS": tk.StringVar(),
    "STREAM_START_NUM": tk.StringVar(),
    "STREAM1_MAX_USER_NUM": tk.StringVar(),
    "STREAM2_MAX_USER_NUM": tk.StringVar(),
    "STREAM3_MAX_USER_NUM": tk.StringVar(),
    "STREAM4_MAX_USER_NUM": tk.StringVar()
}
row_num = 0
# Create label and entry widgets
for name, var in variables.items():
    # Create label and entry widgets
    label = tk.Label(window, text=name)
    entry = tk.Entry(window, textvariable=var)
    label.grid(row=row_num, column=0, padx=5, pady=5)
    entry.grid(row=row_num, column=1, padx=5, pady=5)

    # Set default values
    if isinstance(var, tk.BooleanVar):
        if name == 'FOLLOW_SAVE_VAR':
            var.set(False)
        elif name == 'USE_NORD_VPN':
            var.set(False)
        else:
            var.set(True)  # set to True by default for BooleanVars
    else:
        if name == 'TASK_FIRST':
            var.set('2')
        elif name == "REGISTER_ACCOUNTS_QUANTITY":
            var.set("80")
        elif name == 'WEBSITE_LOAD_TIME':
            var.set('45')
        elif name == 'USER_START_SLEEP':
            var.set('30')
        elif name == 'NUMBER_SKIP':
            var.set('0')
        elif name == 'MIN_PLAY_TIME':
            var.set('40')
        elif name == 'MAX_PLAY_TIME':
            var.set('120')
        elif name == 'NUM_OF_RUNNING_WINDOWS':
            var.set('1')
        elif name == 'STREAM_START_NUM':
            var.set('0')
        elif name == 'STREAM1_MAX_USER_NUM':
            var.set('20')
        elif name == 'STREAM2_MAX_USER_NUM':
            var.set('40')
        elif name == 'STREAM3_MAX_USER_NUM':
            var.set('60')
        elif name == 'STREAM4_MAX_USER_NUM':
            var.set('80')
        else:
            print(name)
            var.set("10")   # set to empty string by default for other vars

    row_num += 1


# Add a button to save the values
def save_values():
    with open("user_input.py", "r+") as f:
        for name, var in variables.items():
            f.write(f"{name} = {var.get()}\n")

    window.quit()


save_button = tk.Button(window, text="Save", command=save_values)
save_button.grid(row=row_num, column=0, columnspan=2, padx=5, pady=5)

# Start the Tkinter event loop
window.mainloop()
