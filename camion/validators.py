from django.core.exceptions import ValidationError


def validar_cuatro_cifras(value):
    if value < 1000 :
        raise ValidationError(
            '%(value)s no hay placas menores a 1000',
            params={'value': value},
        )

def validar_no_cero(value):
    if value < 1 :
        raise ValidationError(
            '%(value)s El valor NO puede ser menor a 1',
            params={'value': value},
        )