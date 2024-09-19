

import sympy as sp
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import tkinter as tk

matplotlib.use('TkAgg')

print("Abrindo a tela, por favor aguarde")

def plot_function(func_input, valA, valB, valN):
    x = sp.symbols('x')

    try:
        f_x = sp.sympify(func_input)
    except sp.SympifyError:
        print("Função inválida. Certifique-se de usar a sintaxe correta.")
        return

    f_numeric = sp.lambdify(x, f_x, "numpy")

    x_vals = np.linspace(valA, valB+2, 400)

    y_vals = f_numeric(x_vals)

    plt.plot(x_vals, y_vals, label=f'f(x) = {func_input}')

    intervalo = (valB - valA) / valN

    aproximacao = 0
    for iteration in range(valN):
        x_interval = valA + ((iteration+1) * intervalo)
        y_interval = f_numeric(x_interval)

        coord_x = valA + (iteration * intervalo)
        plt.gca().add_patch(patches.Rectangle((coord_x, 0), intervalo, y_interval, linewidth=1, edgecolor='r', facecolor='none'))
        aproximacao += intervalo * y_interval

    plt.grid(False)

    plt.axhline(0, color='black', linewidth=0.5)  # Linha horizontal no y = 0
    plt.axvline(0, color='black', linewidth=0.5)  # Linha vertical no x = 0

    plt.axvline(valA, color='red', linewidth=0.3)  # Linha vertical no x = 0
    plt.axvline(valB, color='red', linewidth=0.3)  # Linha vertical no x = 0


    plt.xlim(valA - 2, valB + 2)
    plt.ylim(min(0, min(y_vals)) - 2, max(y_vals) + 2)
    plt.title(f"Aproximação da região com {valN} intervalos: {aproximacao}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()

    plt.show()


def get_user_input(): 
    root = tk.Tk()
    root.withdraw()  # Esconder a janela principal

    input_dialog = tk.Toplevel(root)
    input_dialog.title("Entrada de Dados")

    tk.Label(input_dialog, text="Digite a função f(x) em termos de x (ex: sqrt(x) + 2*x + 1):").pack()
    func_entry = tk.Entry(input_dialog)
    func_entry.pack()

    tk.Label(input_dialog, text="Digite o limite inferior A:").pack()
    val_a = tk.Entry(input_dialog)
    val_a.pack()

    tk.Label(input_dialog, text="Digite o limite superior B:").pack()
    val_b = tk.Entry(input_dialog)
    val_b.pack()

    tk.Label(input_dialog, text="Digite a quantidade de intervalos:").pack()
    val_n = tk.Entry(input_dialog)
    val_n.pack()

    def submit():
        try:
            func_input = func_entry.get()
            valA = int(val_a.get())
            valB = int(val_b.get())
            valN = int(val_n.get())
            #input_dialog.destroy()  # Fechar o diálogo

            if func_input and valA >= 0 and valA < valB and valN > 0:
                plt.close()
                plot_function(func_input, valA, valB, valN)
            else:
                print("Entradas inválidas. Certifique-se de que A < B e N > 0.")
                root.quit()
        except ValueError:
            print("Valores inválidos. Certifique-se de inserir números inteiros válidos.")

    submit_button = tk.Button(input_dialog, text="Submeter", command=submit)
    submit_button.pack() 

    root.wait_window(input_dialog)


get_user_input()
