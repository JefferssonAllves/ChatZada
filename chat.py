import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate


api_key = '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'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='mixtral-8x7b-32768')

def resposta_bot(mensagens):
  mensagem_system = '''Seu nome é ChatZada e eu nao quero que voce seja repetitivo nas suas conversas.'''
                    
  lista_mensagens = [('system', mensagem_system)] 
  lista_mensagens += mensagens
  template = ChatPromptTemplate.from_messages(lista_mensagens)                                                                                                        
  chain = template | chat
  return chain.invoke({}).content


# mensagens = []
# while True:
#   pergunta = input('==> Usuário: ')
#   if pergunta.lower() == 'x':
#     break
  
#   mensagens.append(('user', pergunta))
#   resposta = resposta_bot(mensagens)
#   mensagens.append(('assistant', resposta))
  
#   print(f'\n==> Bot: {resposta}\n')