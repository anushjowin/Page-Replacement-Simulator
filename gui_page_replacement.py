import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



# ---------- ALGORITHMS ----------

def fifo(reference_string, frames):
    memory = []
    page_faults = 0
    states = []

    for page in reference_string:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1

        states.append(memory.copy())

    return states, page_faults


def lru(reference_string, frames):
    memory = []
    page_faults = 0
    states = []
    recent_use = []

    for page in reference_string:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = recent_use.pop(0)
                memory.remove(lru_page)
                memory.append(page)
            page_faults += 1
        else:
            recent_use.remove(page)

        recent_use.append(page)
        states.append(memory.copy())

    return states, page_faults


def optimal(reference_string, frames):
    memory = []
    page_faults = 0
    states = []

    for i in range(len(reference_string)):
        page = reference_string[i]

        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                future = reference_string[i+1:]
                replace_page = None
                farthest = -1

                for m in memory:
                    if m not in future:
                        replace_page = m
                        break
                    else:
                        index = future.index(m)
                        if index > farthest:
                            farthest = index
                            replace_page = m

                memory.remove(replace_page)
                memory.append(page)

            page_faults += 1

        states.append(memory.copy())

    return states, page_faults


# ---------- GUI FUNCTIONS ----------

def animate_steps(states, faults):
    result_text.delete(1.0, tk.END)
    step = 0

    def show():
        nonlocal step
        if step < len(states):
            result_text.insert(tk.END, f"Step {step+1}  ➜  {states[step]}\n")
            result_text.see(tk.END)
            step += 1
            root.after(500, show)
        else:
            result_text.insert(tk.END, f"\nTotal Page Faults: {faults}")

    show()


def run_simulation():
    try:
        reference_string = list(map(int, entry_ref.get().split()))
        frames = int(entry_frames.get())
        algo = algo_choice.get()

        if algo == "FIFO":
            states, faults = fifo(reference_string, frames)
        elif algo == "LRU":
            states, faults = lru(reference_string, frames)
        elif algo == "Optimal":
            states, faults = optimal(reference_string, frames)
        else:
            messagebox.showerror("Error", "Select Algorithm")
            return

        animate_steps(states, faults)

    except:
        messagebox.showerror("Error", "Invalid Input")


def reset_all():
    entry_ref.delete(0, tk.END)
    entry_frames.delete(0, tk.END)
    result_text.delete(1.0, tk.END)
    algo_choice.set("")


def show_comparison_graph(reference_string, frames):
    fifo_states, fifo_faults = fifo(reference_string, frames)
    lru_states, lru_faults = lru(reference_string, frames)
    opt_states, opt_faults = optimal(reference_string, frames)

    algorithms = ["FIFO", "LRU", "Optimal"]
    faults = [fifo_faults, lru_faults, opt_faults]

    plt.figure()
    plt.bar(algorithms, faults)
    plt.xlabel("Algorithms")
    plt.ylabel("Number of Page Faults")
    plt.title("Page Replacement Algorithm Comparison")
    plt.show()

def compare_all():
    try:
        reference_string = list(map(int, entry_ref.get().split()))
        frames = int(entry_frames.get())
        animated_comparison_graph(reference_string, frames)
    except:
        messagebox.showerror("Error", "Invalid Input")


def animated_comparison_graph(reference_string, frames):
    fifo_states, fifo_faults = fifo(reference_string, frames)
    lru_states, lru_faults = lru(reference_string, frames)
    opt_states, opt_faults = optimal(reference_string, frames)

    algorithms = ["FIFO", "LRU", "Optimal"]
    final_faults = [fifo_faults, lru_faults, opt_faults]

    fig, ax = plt.subplots()
    bars = ax.bar(algorithms, [0, 0, 0])

    ax.set_ylim(0, max(final_faults) + 2)
    ax.set_xlabel("Algorithms")
    ax.set_ylabel("Page Faults")
    ax.set_title("Real-Time Page Fault Comparison")

    def update(frame):
        for i in range(len(bars)):
            if bars[i].get_height() < final_faults[i]:
                bars[i].set_height(bars[i].get_height() + 1)

    ani = FuncAnimation(fig, update, frames=max(final_faults)+2, interval=400, repeat=False)
    plt.show()

def show_algorithm_info():
    algo = algo_choice.get()

    if algo == "FIFO":
        info_text = (
            "FIFO (First-In-First-Out)\n\n"
            "• Replaces the oldest page in memory.\n"
            "• Uses queue principle.\n"
            "• Simple to implement.\n"
            "• May suffer from Belady’s Anomaly."
        )

    elif algo == "LRU":
        info_text = (
            "LRU (Least Recently Used)\n\n"
            "• Replaces the least recently used page.\n"
            "• Uses past usage history.\n"
            "• Better performance than FIFO.\n"
            "• Requires tracking of recent usage."
        )

    elif algo == "Optimal":
        info_text = (
            "Optimal Page Replacement\n\n"
            "• Replaces the page that will not be used "
            "for the longest time in future.\n"
            "• Gives minimum possible page faults.\n"
            "• Not practical in real systems.\n"
            "• Used for performance comparison."
        )

    else:
        messagebox.showerror("Error", "Select an Algorithm First")
        return

    messagebox.showinfo("Algorithm Explanation", info_text)


# ---------- WINDOW DESIGN ----------

root = tk.Tk()
root.title("Page Replacement Simulator")
root.geometry("800x600")
root.configure(bg="#0f172a")

# Title
title = tk.Label(root,
                 text="Page Replacement Simulator",
                 font=("Segoe UI", 24, "bold"),
                 bg="#0f172a",
                 fg="#38bdf8")
title.pack(pady=20)

# Card Frame
card = tk.Frame(root, bg="#1e293b", bd=0)
card.pack(padx=40, pady=10, fill="both", expand=True)

# Input Section
input_frame = tk.Frame(card, bg="#1e293b")
input_frame.pack(pady=20)

label_style = {"bg": "#1e293b", "fg": "white", "font": ("Segoe UI", 12)}

tk.Label(input_frame, text="Reference String:", **label_style).grid(row=0, column=0, padx=10, pady=10)
entry_ref = tk.Entry(input_frame, width=40, font=("Segoe UI", 11))
entry_ref.grid(row=0, column=1, padx=10)

tk.Label(input_frame, text="Number of Frames:", **label_style).grid(row=1, column=0, padx=10, pady=10)
entry_frames = tk.Entry(input_frame, font=("Segoe UI", 11))
entry_frames.grid(row=1, column=1)

tk.Label(input_frame, text="Select Algorithm:", **label_style).grid(row=2, column=0, padx=10, pady=10)
algo_choice = ttk.Combobox(input_frame,
                           values=["FIFO", "LRU", "Optimal"],
                           state="readonly",
                           font=("Segoe UI", 11))
algo_choice.grid(row=2, column=1)

# Buttons
button_frame = tk.Frame(card, bg="#1e293b")
button_frame.pack(pady=15)

run_btn = tk.Button(button_frame,
                    text="Run Simulation",
                    command=run_simulation,
                    bg="#22c55e",
                    fg="white",
                    font=("Segoe UI", 12, "bold"),
                    width=15)
run_btn.grid(row=0, column=0, padx=10)

reset_btn = tk.Button(button_frame,
                      text="Reset",
                      command=reset_all,
                      bg="#ef4444",
                      fg="white",
                      font=("Segoe UI", 12, "bold"),
                      width=10)
reset_btn.grid(row=0, column=1, padx=10)

compare_btn = tk.Button(button_frame,
                        text="Compare All",
                        command=lambda: compare_all(),
                        bg="#3b82f6",
                        fg="white",
                        font=("Segoe UI", 12, "bold"),
                        width=12)
compare_btn.grid(row=0, column=2, padx=10)

info_btn = tk.Button(button_frame,
                     text="Explain",
                     command=show_algorithm_info,
                     bg="#f59e0b",
                     fg="white",
                     font=("Segoe UI", 12, "bold"),
                     width=10)
info_btn.grid(row=0, column=3, padx=10)



# Output Section
result_text = tk.Text(card,
                      height=15,
                      width=80,
                      bg="#0f172a",
                      fg="#f8fafc",
                      font=("Consolas", 11),
                      bd=0)
result_text.pack(pady=20)

root.mainloop()
