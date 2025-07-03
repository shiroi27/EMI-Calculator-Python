import tkinter as tk
from tkinter import messagebox

def calculate_emi():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())

        monthly_rate = rate / (12 * 100)
        months = time * 12
        emi = (principal * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
        emi = round(emi, 2)

        result_label.config(text=f"Monthly EMI: ₹{emi}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Setup GUI
root = tk.Tk()
root.title("EMI Calculator")
root.geometry("420x410+600+300")
root.resizable(False, False)
root.config(bg="#F2F2F2")

# Fake Header Frame
header_frame = tk.Frame(root, width=440, height=60, bg="#FFB6C1")
header_frame.place(x=0, y=0)

# Header Title
header = tk.Label(header_frame, text="EMI CALCULATOR", font=("Times New Roman", 20, "bold"), bg="#FFB6C1", fg="#000000")
header.place(relx=0.5, rely=0.5, anchor="center")

# Decorative Line
decorative_line = tk.Frame(root, height=6, width=440, bg="#FF69B4")
decorative_line.place(x=0, y=60)

# Principal
tk.Label(root, text="Loan Amount (₹):", font=("Times New Roman", 14, "bold"), bg="#F2F2F2", fg="#000000").place(x=20, y=90)
principal_entry = tk.Entry(root, font=("Times New Roman", 14, "bold"))
principal_entry.place(x=240, y=90, width=160)

# Interest Rate
tk.Label(root, text="Annual Interest Rate (%):", font=("Times New Roman", 14, "bold"), bg="#F2F2F2", fg="#000000").place(x=20, y=140)
rate_entry = tk.Entry(root, font=("Times New Roman", 14, "bold"))
rate_entry.place(x=240, y=140, width=160)

# Time
tk.Label(root, text="Loan Tenure (Years):", font=("Times New Roman", 14, "bold"), bg="#F2F2F2", fg="#000000").place(x=20, y=190)
time_entry = tk.Entry(root, font=("Times New Roman", 14, "bold"))
time_entry.place(x=240, y=190, width=160)

# Button
calculate_btn = tk.Button(root, text="Calculate EMI", command=calculate_emi, font=("Times New Roman", 13, "bold"), bg="#4CAF50", fg="#000000")
calculate_btn.place(x=140, y=240, width=140, height=35)

# Result Frame and Label
result_frame = tk.Frame(root, bg="white", highlightbackground="#000000", highlightthickness=3)
result_frame.place(x=60, y=290, width=300, height=50)

result_label = tk.Label(result_frame, text="", font=("Times New Roman", 14, "bold"), bg="white", fg="#000000")
result_label.place(relx=0.5, rely=0.5, anchor="center")

# Footer
footer = tk.Label(root, text="© 2025 Finance Tools by Shiroi", font=("Times New Roman", 10, "bold"), bg="#F2F2F2", fg="#000000")
footer.place(relx=0.5, y=370, anchor="n")

root.mainloop()