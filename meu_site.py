from flask import Flask

app = Flask(__name__) 

#criar a primeira pagina do projeto
# route -> hashtagtreinamentos.com/( o que eu quiser por exemplo "usuario" )
#função -> o que voce vai quer exibir naquela página 

@app.route("/")
def homepage():
    return "Esse é meu primeiro site"

#colocar o site no ar 
app.rum()