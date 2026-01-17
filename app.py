from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'clave_secreta'


@app.route('/')
def index():
    title = "IDGS804 - Intro Flask"
    listado = {"juana", "Ana", "pedro", "luisa"}

    return render_template('index.html', title=title, listado=listado)



@app.route("/saludo1")
def saludo():
    return render_template('saludo1.html')


@app.route("/saludo2")
def saludo2():
    return render_template('saludo2.html')

@app.route("/user/<string:user>")
def usuario(user):
    return f'Hola, {user}'


@app.route("/numero/<int:n>")
def numero(n):
    return f'<h1> Numero:  {n}</h1>'


@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f'<h1> Hola: {username} Tu ID es: {id} </h1>'


@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1> La suma es: {n1+n2}</h1>"


@app.route("/default/")
@app.route("/default/<string:parm>")
def func2(param="Jiovani"):
    return f"<h1> Hola, {param}</h1>"



@app.route("/operas")
def operas():
    return '''
    <form>
    <label form="name">Name:</label>
    <input type="text" id="name" name="name" required>
    </br>
    <label form="name">paterno:</label>
    <input type="text" id="name" name="name" required>
    </br>
    <input type="submit" value="submit">
    '''

@app.route('/operasBas')
def operasbas():
    return render_template('operasBas.html')


@app.route('/resultado', methods=['GET', 'POST'])
def resul1():
    n1=request.form.get('num1')
    n2=request.form.get('num2')
    return f"<h1> la suma es: {float(n1)+float(n2)}</h1>"




if __name__==  '__main__':
    app.run(debug=True)