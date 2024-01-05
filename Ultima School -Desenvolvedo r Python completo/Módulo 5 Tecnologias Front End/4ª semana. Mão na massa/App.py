from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Dados de exemplo para categorias e agendamentos
categorias_animais = ["Cachorro", "Gato"]
agendamentos = []

@app.route('/categorias', methods=['GET'])
def obter_categorias():
    return jsonify({"categorias": categorias_animais})

@app.route('/agendar', methods=['POST'])
def agendar_banho():
    dados_agendamento = request.json

    # Lógica para verificar a disponibilidade de horários
    # (Você pode adicionar mais lógica aqui conforme necessário)

    if len(agendamentos) >= 10:
        return jsonify({"mensagem": "Limite de agendamentos atingido para este dia."}), 400

    # Simplesmente adicionando um agendamento para fins de exemplo
    agendamentos.append({
        "data": dados_agendamento["data"],
        "categoria_animal": dados_agendamento["categoria_animal"],
        "nome_cliente": dados_agendamento["nome_cliente"],
        "telefone_cliente": dados_agendamento["telefone_cliente"],
    })

    return jsonify({"mensagem": "Agendamento realizado com sucesso!"})

@app.route('/agendamentos', methods=['GET'])
def obter_agendamentos():
    data_especifica = request.args.get('data', datetime.today().strftime('%Y-%m-%d'))
    
    agendamentos_do_dia = [agendamento for agendamento in agendamentos if agendamento["data"] == data_especifica]

    return jsonify({"agendamentos": agendamentos_do_dia})

# Adicione mais rotas conforme necessário

if __name__ == '__main__':
    app.run(debug=True, port=8000)