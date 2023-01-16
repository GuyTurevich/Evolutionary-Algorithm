import multiprocessing
import threading
import time
import tkinter as tk
from tkinter import ttk
import sys
from EvolutionaryAlgorithm import EvolutionaryAlgorithm

class StdoutRedirector(object):
    def __init__(self, text_area):
        self.text_area = text_area

    def write(self, str):
        self.text_area.insert(tk.END, str)
        self.text_area.see(tk.END)

def update_mutation_bit_flips_max(val):
    mutation_bit_flips_scale.config(to=int(val))

def start_algorithm():
    start_button.config(state='disable')
    graph_size = graph_size_var.get()
    edge_prob = edge_prob_var.get()
    population_size = population_size_var.get()
    elitism_rate = elitism_rate_var.get()
    mutation_prob = mutation_prob_var.get()
    mutation_bit_flips = mutation_bit_flips_var.get()
    tournament_size = tournament_size_var.get()
    tournament_prob = tournament_prob_var.get()
    crossover_type = crossover_var.get()
    max_generation = max_generation_var.get()
    num_generations_unchanged = num_generations_unchanged_var.get()

    tab = tk.Text(notebook)
    notebook.add(tab, text="Run " + str(notebook.index("end")))
    notebook.select(tab)
    sys.stdout = StdoutRedirector(tab)
    algo = EvolutionaryAlgorithm(graph_size, edge_prob, population_size, elitism_rate, mutation_prob, mutation_bit_flips, tournament_size, tournament_prob, crossover_type , max_generation, num_generations_unchanged)
    algo.run()
    sys.stdout = sys.__stdout__
    start_button.config(state='normal')



root = tk.Tk()
root.title("Evolutionary Algorithm")


main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True)

left_frame = tk.Frame(main_frame)
left_frame.pack(side='left', fill='both', expand=True)

right_frame = tk.Frame(main_frame)
right_frame.pack(side='right', fill='both', expand=True)


# Graph Size
graph_size_label = tk.Label(left_frame, text="Graph Size:")
graph_size_label.grid(row=0, column=0, padx=5, pady=5)
graph_size_var = tk.IntVar()
graph_size_var.set(30)
graph_size_scale = tk.Scale(left_frame, from_=10, to=200, variable=graph_size_var, orient='horizontal', command=update_mutation_bit_flips_max)
graph_size_scale.grid(row=0, column=1, padx=5, pady=5)

graph_size_entry = tk.Entry(left_frame)
graph_size_entry.grid(row=0, column=2, padx=5, pady=5)
graph_size_entry.insert(0, graph_size_var.get())

def on_entry_change(event):
    graph_size_var.set(int(graph_size_entry.get()))

graph_size_entry.bind("<Return>", on_entry_change)
graph_size_var.trace("w",lambda *args: graph_size_entry.delete(0,tk.END))
graph_size_var.trace("w",lambda *args: graph_size_entry.insert(0, graph_size_var.get()))


# Graph Edge Probability
edge_prob_label = tk.Label(left_frame, text="Graph Edge Probability:")
edge_prob_label.grid(row=1, column=0, padx=5, pady=5)
edge_prob_var = tk.DoubleVar()
edge_prob_var.set(0.5)
edge_prob_scale = tk.Scale(left_frame, from_=0.01, to=0.99, variable=edge_prob_var, orient='horizontal',resolution = 0.01)
edge_prob_scale.grid(row=1, column=1, padx=5, pady=5)

# Population Size
population_size_label = tk.Label(left_frame, text="Population Size:")
population_size_label.grid(row=2, column=0, padx=5, pady=5)
population_size_var = tk.IntVar()
population_size_var.set(120)
population_size_scale = tk.Scale(left_frame, from_=20, to=1000, variable=population_size_var, orient='horizontal')
population_size_scale.grid(row=2, column=1, padx=5, pady=5)

population_size_entry = tk.Entry(left_frame)
population_size_entry.grid(row=2, column=2, padx=5, pady=5)
population_size_entry.insert(0, population_size_var.get())

def on_entry_change(event):
    population_size_var.set(int(population_size_entry.get()))

population_size_entry.bind("<Return>", on_entry_change)
population_size_var.trace("w",lambda *args: population_size_entry.delete(0,tk.END))
population_size_var.trace("w",lambda *args: population_size_entry.insert(0, population_size_var.get()))


# Elitism Rate
elitism_rate_label = tk.Label(left_frame, text="Elitism Rate:")
elitism_rate_label.grid(row=3, column=0, padx=5, pady=5)
elitism_rate_var = tk.DoubleVar()
elitism_rate_var.set(0.05)
elitism_rate_scale =  tk.Scale(left_frame, from_=0.01, to=1, variable=elitism_rate_var, orient='horizontal',resolution=0.01)
elitism_rate_scale.grid(row=3, column=1, padx=5, pady=5)


# Mutation Probability
mutation_prob_label = tk.Label(left_frame, text="Mutation Probability:")
mutation_prob_label.grid(row=4, column=0, padx=5, pady=5)
mutation_prob_var = tk.DoubleVar()
mutation_prob_var.set(0.1)
mutation_prob_scale =  tk.Scale(left_frame, from_=0.01, to=1, variable=mutation_prob_var, orient='horizontal',resolution=0.01)
mutation_prob_scale.grid(row=4, column=1, padx=5, pady=5)

# Mutation Bit-flips
mutation_bit_flips_label = tk.Label(left_frame, text="Mutation Bit-flips:")
mutation_bit_flips_label.grid(row=5, column=0, padx=5, pady=5)
mutation_bit_flips_var = tk.IntVar()
mutation_bit_flips_var.set(1)
mutation_bit_flips_scale = tk.Scale(left_frame, from_=1, to=10, variable=mutation_bit_flips_var, orient='horizontal')
mutation_bit_flips_scale.grid(row=5, column=1, padx=5, pady=5)

# Tournament Size
tournament_size_label = tk.Label(left_frame, text="Tournament Size:")
tournament_size_label.grid(row=6, column=0, padx=5, pady=5)
tournament_size_var = tk.IntVar()
tournament_size_var.set(4)
tournament_size_flips_scale = tk.Scale(left_frame, from_=1, to=10, variable=tournament_size_var, orient='horizontal')
tournament_size_flips_scale.grid(row=6, column=1, padx=5, pady=5)

# Tournament Probability
tournament_prob_label = tk.Label(left_frame, text="Tournament Probability:")
tournament_prob_label.grid(row=7, column=0, padx=5, pady=5)
tournament_prob_var = tk.DoubleVar()
tournament_prob_var.set(1)
tournament_prob_scale =  tk.Scale(left_frame, from_=0.01, to=1, variable=tournament_prob_var, orient='horizontal',resolution=0.01)
tournament_prob_scale.grid(row=7, column=1, padx=5, pady=5)

# Crossover Type
crossover_label = tk.Label(left_frame, text="Crossover Type:")
crossover_label.grid(row=8, column=0, padx=5, pady=5)
crossover_var = tk.StringVar()
crossover_var.set("Uniform")
crossover_dropdown = ttk.Combobox(left_frame, textvariable=crossover_var, values=["uniform", "one_point", "two_point"])
crossover_dropdown.grid(row=8, column=1, padx=5, pady=5)

# Max generation
max_generation_label = tk.Label(left_frame, text="Max generation:")
max_generation_label.grid(row=9, column=0, padx=5, pady=5)
max_generation_var = tk.IntVar()
max_generation_var.set(50)
max_generation_scale = tk.Scale(left_frame, from_=10, to=500, variable=max_generation_var, orient='horizontal')
max_generation_scale.grid(row=9, column=1, padx=5, pady=5)

max_generation_entry = tk.Entry(left_frame)
max_generation_entry.grid(row=9, column=2, padx=5, pady=5)
max_generation_entry.insert(0, max_generation_var.get())

def on_entry_change(event):
    max_generation_var.set(int(max_generation_entry.get()))

max_generation_entry.bind("<Return>", on_entry_change)
max_generation_var.trace("w",lambda *args: max_generation_entry.delete(0,tk.END))
max_generation_var.trace("w",lambda *args: max_generation_entry.insert(0, max_generation_var.get()))

# Number of generations unchanged before stopping
num_generations_unchanged_label = tk.Label(left_frame, text="Unchanged generations termination:")
num_generations_unchanged_label.grid(row=10, column=0, padx=5, pady=5)
num_generations_unchanged_var = tk.IntVar()
num_generations_unchanged_var.set(15)
num_generations_unchanged_scale = tk.Scale(left_frame, from_=5, to=100, variable=num_generations_unchanged_var, orient='horizontal')
num_generations_unchanged_scale.grid(row=10, column=1, padx=5, pady=5)


# Start button
start_button = tk.Button(left_frame, text="Start", command=start_algorithm)
start_button.grid(row=11, column=0, columnspan=2, padx=5, pady=5, ipadx=50)

# # stdout text box
# stdout_text = tk.Text(right_frame)
# stdout_text.pack(fill='both', expand=True)
notebook = ttk.Notebook(right_frame)
notebook.pack(fill='both', expand=True)
tab = tk.Text(notebook)
notebook.add(tab, text="default")
notebook.select(notebook.tabs()[0])


root.mainloop()


