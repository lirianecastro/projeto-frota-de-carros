from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ==========================
# TELA DE LOGIN
# ==========================
@app.route('/')
def login():
    return render_template('login.html')


# ==========================
# AUTENTICAÇÃO
# ==========================
@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    # Usuário fixo para teste
    if usuario == "admin" and senha == "1234":
        return redirect(url_for('principal'))
    else:
        return "Usuário ou senha inválidos!"


# ==========================
# TELA PRINCIPAL (MENU)
# ==========================
@app.route('/principal')
def principal():
    return render_template('index.html')


# ==========================
# TELA DE CADASTRO
# ==========================
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    if request.method == 'POST':
        nome = request.form.get('nome')
        modelo = request.form.get('modelo')
        placa = request.form.get('placa')

        # Aqui você pode salvar no banco depois
        print("Nome:", nome)
        print("Modelo:", modelo)
        print("Placa:", placa)

        return redirect(url_for('principal'))

    return render_template('cadastro.html')


# ==========================
# EXECUTAR SISTEMA
# ==========================
if __name__ == '__main__':
    app.run(debug=True)

