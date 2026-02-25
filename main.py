import tkinter as tk
from tkinter import messagebox

# ---------------- LOGIN ---------------- #

def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "admin" and senha == "1234":
        janela.destroy()  # Fecha login
        abrir_tela_principal()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")


# ---------------- TELA PRINCIPAL ---------------- #

def abrir_tela_principal():
    principal = tk.Tk()
    principal.title("Sistema Frota de Carros")
    principal.geometry("600x400")
    principal.configure(bg="#1e1e2f")

    # ----- MENU -----
    barra_menu = tk.Menu(principal)

    menu_cadastro = tk.Menu(barra_menu, tearoff=0)
    menu_cadastro.add_command(label="Cadastrar Veículo", command=lambda: mensagem("Cadastro de Veículo"))
    menu_cadastro.add_command(label="Listar Veículos", command=lambda: mensagem("Lista de Veículos"))
    menu_cadastro.add_separator()
    menu_cadastro.add_command(label="Sair", command=principal.destroy)

    barra_menu.add_cascade(label="Cadastro", menu=menu_cadastro)

    menu_ajuda = tk.Menu(barra_menu, tearoff=0)
    menu_ajuda.add_command(label="Sobre", command=lambda: mensagem("Sistema Frota v1.0"))
    barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)

    principal.config(menu=barra_menu)

    # ----- Título -----
    titulo = tk.Label(principal,
                      text="Bem-vindo ao Sistema de Frota",
                      font=("Arial", 18, "bold"),
                      bg="#1e1e2f",
                      fg="white")
    titulo.pack(pady=50)

    principal.mainloop()


def mensagem(texto):
    messagebox.showinfo("Menu", texto)


# ---------------- JANELA LOGIN ---------------- #

janela = tk.Tk()
janela.title("Login")
janela.geometry("400x300")
janela.configure(bg="#1e1e2f")
janela.resizable(False, False)

frame = tk.Frame(janela, bg="#2c2c3e", padx=30, pady=30)
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="LOGIN",
         font=("Arial", 18, "bold"),
         bg="#2c2c3e",
         fg="white").pack(pady=10)

tk.Label(frame, text="Usuário",
         bg="#2c2c3e",
         fg="white").pack()

entry_usuario = tk.Entry(frame)
entry_usuario.pack(pady=5)

tk.Label(frame, text="Senha",
         bg="#2c2c3e",
         fg="white").pack()

entry_senha = tk.Entry(frame, show="*")
entry_senha.pack(pady=5)

tk.Button(frame,
          text="Entrar",
          bg="#4CAF50",
          fg="white",
          width=15,
          command=verificar_login).pack(pady=15)

janela.mainloop()
