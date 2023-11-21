from flask import Flask, render_template, request,redirect

app = Flask(__name__)


competidores = []


@app.route('/criar', methods=['GET', 'POST'])
def criar():
    nome = request.form['nome']
    jogo = request.form['jogo']
    posicao = request.form['posicao']
    ranking = request.form['ranking']
    competidores.append({'nome': nome, 'jogo': jogo, 'posicao': posicao, 'ranking': ranking})
    return redirect('/competidores')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/competidores')
def lista_competidores():
    return render_template('competidores.html', competidores=competidores)

if __name__ == '_main_':
    app.run(debug=True)