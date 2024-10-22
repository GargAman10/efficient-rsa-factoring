from flask import Flask, request, render_template
from factors import pollards_rho
from rsa import rsa_factoring

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/factor', methods=['POST'])
def factor():
    numbers = request.form['numbers'].splitlines()
    results = []

    for n in numbers:
        n = n.strip()
        if n.isdigit():
            n = int(n)
            p_rho = pollards_rho(n)
            p_rsa, q_rsa = rsa_factoring(n)
            results.append((n, p_rho, p_rsa, q_rsa))
        else:
            results.append((n, "Invalid input", "", ""))

    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
