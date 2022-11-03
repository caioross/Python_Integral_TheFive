import pandas as pd
from flask import Flask, jsonify, render_template

app = Flask (__name__)

@app.route('/')
def pagina_inicial():
  return 'Melhor turma do mundo'

@app.route('/index/')
def index():
  return 'aqui'

@app.route('/total/')
def total():
  tabela = pd.read_csv('base.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'Total Vendas:': total_vendas}
  return jsonify(resposta)


  
@app.route('/media/')
def media():
  tabela = pd.read_csv('base.csv')
  media_vendas = tabela['Vendas'].mean()
  resposta = {'media Vendas:': media_vendas}
  return jsonify(resposta)



@app.route('/composto/')
def composto():
  tabela = pd.read_csv('base.csv')
  media_vendas = tabela['Vendas'].mean()
  total_vendas = tabela['Vendas'].sum()
  resposta = {'media Vendas:': media_vendas, 'Total Vendas:':total_vendas}
  return jsonify(resposta)


  session = 'logado'
  @app.route('/admin/')
  def admin_index():
    if('logado' not in session):
      return redirect(url_for('index'))
    return render_template('index.html')
    
if __name__ == '__main__':
  app.run('0.0.0.0')
