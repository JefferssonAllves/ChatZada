from flask import Flask
from flask import render_template
from flask import request
from chat import resposta_bot




app = Flask(__name__)
chats = []
mensagens = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == 'POST':
        pergunta = request.form['pergunta']
    
        mensagens.append(('user', pergunta))
        resposta = resposta_bot(mensagens) 
        mensagens.append(('assistant', resposta))
        
        chats.append((pergunta, resposta))
        return render_template('pages/index.html', chats=chats)
    return render_template('pages/index.html', teste='sem perguntas')




if __name__ == "__main__":
    app.run(debug=True)