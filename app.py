from flask import Flask, request, jsonify
import re
app = Flask(__name__)


def is_valid_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcula os dígitos verificadores
    for i in range(9, 11):
        value = sum((int(cpf[num]) * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != int(cpf[i]):
            return False

    return True


@app.route('/validate', methods=['POST'])
def validate_cpf():
    data = request.get_json()
    cpf = data.get('cpf')

    if not cpf:
        return jsonify({'error': 'CPF is required'}), 400

    if is_valid_cpf(cpf):
        return jsonify({'valid': True}), 200
    else:
        return jsonify({'valid': False}), 400


if __name__ == '__main__':
    app.run()
