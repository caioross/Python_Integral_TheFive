import pandas as pd
from flask import Flask, jsonify

app = Flask (__name__)

@app.route('/')
def pagina_inicial():
  return 'Melhor turma do mundo'

@app.route('/total/')
def total():
  tabela = pd.read_csv('base.csv')
  tabela_vendas = tabela['Vendas'].sum()
  resposta = {'Total Vendas:': total_vendas}
  return jsonify(resposta)

if __name__ == '__main__':
  app.run('0.0.0.0')
