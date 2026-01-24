from flask import Flask, render_template, request
import math
import forms
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'clave_secreta'
csrf=CSRFProtect()


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

@app.route('/operasBas', methods=['GET', 'POST'])
def operasbas():
        res=None
        if request.method == 'POST':
            n1=request.form.get('num1')
            n2=request.form.get('num2')

            if request.form.get('operacion')=='suma':
                res=float(n1)+float(n2)
            if request.form.get('operacion')=='resta':
                res=float(n1)-float(n2)
            if request.form.get('operacion')=='multiplicacion':
                res=float(n1)*float(n2)
            if request.form.get('operacion')=='division':
                res=float(n1)/float(n2)

        return render_template('operasBas.html', res=res)    

    


@app.route('/resultado', methods=['GET', 'POST'])
def resul1():
    n1=request.form.get('num1')
    n2=request.form.get('num2')
    return f"<h1> la suma es: {float(n1)+float(n2)}</h1>"





@app.route('/distancia', methods=['GET', 'POST'])
def distancia():
    resultado = None
    if request.method == 'POST':
        
            
            x1 = float(request.form.get('x1'))
            y1 = float(request.form.get('y1'))
            x2 = float(request.form.get('x2'))
            y2 = float(request.form.get('y2'))
            
            
            resultado = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
        

    return render_template('distancia.html', res=resultado)


@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    mat=0
    nom=''
    ape=''
    email=''
    alumno_clas=forms.UserForm(request.form)
    if request.method=='POST' and alumno_clas.validate():
        mat=alumno_clas.matricula.data
        nom=alumno_clas.nombre.data
        ape=alumno_clas.apellido.data
        email=alumno_clas.correo.data
    return render_template("alumnos.html", form=alumno_clas,mat=mat,nom=nom,ape=ape,email=email)

if __name__==  '__main__':
    csrf.init_app(app)
    app.run(debug=True)