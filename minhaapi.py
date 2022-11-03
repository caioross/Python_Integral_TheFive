import pandas as pd
from flask import Flask, jsonify, render_template

app = Flask (__name__)

@app.route('/')
def pagina_inicial():
    return 'Melhor Turma do Mundo'

@app.route('/index/')
def index():
  return 'aqui'

@app.route('/total/')
def total():
    tabela =pd.read_csv('base.csv') 
    total_vendas = tabela['Vendas'].sum()
    resposta = {'Total Vendas': total_vendas}
    return jsonify(resposta)

@app.route('/media/')
def media():
    tabela =pd.read_csv('base.csv') 
    total_vendas = tabela['Vendas'].mean()
    resposta = {'Media Vendas': total_vendas}
    return jsonify(resposta)

@app.route('/composto/')
def composto():
    tabela =pd.read_csv('base.csv') 
    media_vendas = tabela['Vendas'].mean()
    total_vendas = tabela['Vendas'].sum()
    resposta = {'Media Vendas':media_vendas, 'total_vendas': total_vendas}
    return jsonify(resposta)

session = "logado"
@app.route ('/admin/')
def admin_index():
  if ('logado' not in session):
    return redirect(url_('index'))
  return render_template('/admin/index.html')



if __name__ == '__main__':
    app.run('0.0.0.0')
