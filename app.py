from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista inicial de topiks
topiks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar-topiks')
def listar_topiks():
    return render_template('listar_topiks.html', topiks=topiks)

@app.route('/adicionar-topik', methods=['GET', 'POST'])
def adicionar_topik():
    if request.method == 'POST':
        horario = request.form['horario']
        motorista = request.form['motorista']
        destino = request.form['destino']

        topik = {
            'horario': horario,
            'motorista': motorista,
            'destino': destino
        }
        topiks.append(topik)

        return redirect(url_for('listar_topiks'))
    return render_template('adicionar_topik.html')

@app.route('/editar-topik/<int:id>', methods=['GET', 'POST'])
def editar_topik(id):
    topik = topiks[id]

    if request.method == 'POST':
        topik['horario'] = request.form['horario']
        topik['motorista'] = request.form['motorista']
        topik['destino'] = request.form['destino']

        return redirect(url_for('listar_topiks'))
    return render_template('editar_topik.html', id=id, topik=topik)

@app.route('/excluir-topik/<int:id>', methods=['POST'])
def excluir_topik(id):
    del topiks[id]
    return redirect(url_for('listar_topiks'))

if __name__ == '__main__':
    app.run(debug=True)
