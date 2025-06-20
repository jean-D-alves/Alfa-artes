from flask import Flask,render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    numero = '5584996153922'
    mensagem = 'Olá, gataria de saber mais'
    mensagem_formatada =mensagem.replace("","%20)")
    link = f'https://wa.me/{numero}?text={mensagem_formatada}'


    return render_template_string(f'''
       <h1.contato</h1>
       <a href- "{link}" target="_blank">Fale conosco no WhatsApp</a>
       '''
   )
if __name__ == '__main__':
    app.run(debug=True)