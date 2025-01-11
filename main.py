from flask import Flask, render_template, request, redirect, url_for
from chat import resposta_chat
app = Flask(__name__)
chats = []
mensagens = []


@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        pergunta = request.form['pergunta']
        enviar_chat(pergunta)
        return render_template('pages/index.html', chats=chats)
    
    pergunta = "Olá Chat, tudo bem?"
    enviar_chat(pergunta)
    return render_template('pages/index.html', chats=chats)

@app.route('/login')
def login():
    return render_template('pages/login.html')


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('home')), 404


   
def enviar_chat(pergunta):
    mensagens.append(('user', pergunta))
    resposta = resposta_chat(mensagens) 
    mensagens.append(('assistant', resposta))
    chats.append((pergunta, resposta))

if __name__ == "__main__":
    app.run(debug=True)