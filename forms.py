from wtforms import Form
from wtforms import StringField, IntegerField, RadioField
from wtforms import validators
from wtforms import ValidationError

class UserForm(Form):
    matricula = IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido")
    ])

    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido")
    ])
    
    apellido = StringField("Apellido", [
        validators.DataRequired(message="El campo es requerido")
    ])
    
    correo = StringField("Correo", [
        validators.Email(message="Ingresa correo valido")
    ])

# cinepolis-------------------------------------------------------------
class CinepolisForm(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El nombre es requerido')
    ])
    compradores = IntegerField('Cantidad de Compradores', [
        validators.DataRequired(message='Requerido'),
        validators.NumberRange(min=1, message='Mínimo 1 persona')
    ])
    
    tarjeta = RadioField('Tarjeta Cineco', choices=[('Si', 'Si'), ('No', 'No')], default='No')
    
    boletas = IntegerField('Cantidad Boletas', [
        validators.DataRequired(message='Requerido'),
        validators.NumberRange(min=1, message='Mínimo 1 boleto')
    ])

    
    def validate_boletas(self, field):
    
        if field.data is not None and self.compradores.data is not None:
            limite = self.compradores.data * 7
            if field.data > limite:
                raise ValidationError(f'Máximo 7 boletas por persona (Límite para {self.compradores.data} personas: {limite})')