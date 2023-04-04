import datetime
import unittest


def datos_estudiante_dict(n_estudiantes, nombre, dia_cumpleaños, mes_cumpleaños, año_nacimiento, celuar, correo, direccion):
    lista = []
    for i in range(n_estudiantes):
        nombre = nombre
        mes_cumpleaños = int(mes_cumpleaños)
        dia_cumpleaños = int(dia_cumpleaños)
        año_nacimiento = int(año_nacimiento)
        celular = int(celuar)
        correo = correo
        direccion = direccion

        fecha_nacimiento = datetime.date(año_nacimiento, mes_cumpleaños, dia_cumpleaños)
        fecha_actual = datetime.date.today()


        diferencia = fecha_actual - fecha_nacimiento
        edad = int(diferencia.days / 365.25)

        estudiante_dict = {'nombre': nombre,
                        'dia_cumpleaños': dia_cumpleaños,
                        'mes_cumpleaños': mes_cumpleaños,
                        'año_nacimiento': año_nacimiento,
                        'celular':celular,
                        'correo':correo,
                        'direccion':direccion,
                        'edad': edad
                        }
        lista.append(estudiante_dict)

    return lista

class CajaNegraTest(unittest.TestCase):
    def test_dict_estudiante(self):
        n_estudiantes = 1
        nombre = 'Juan'
        dia_cumpleaños = 26
        mes_cumpleaños = 3
        año_nacimiento = 2006
        celular = 3505913706
        correo = 'jjr20060326@gmail.com'
        direccion = 'Mi casa'

        resultado = datos_estudiante_dict(n_estudiantes, nombre, dia_cumpleaños, mes_cumpleaños, año_nacimiento, celular, correo, direccion)
        self.assertEqual(resultado, [{'nombre': nombre,
                        'dia_cumpleaños': dia_cumpleaños,
                        'mes_cumpleaños': mes_cumpleaños,
                        'año_nacimiento': año_nacimiento,
                        'celular':celular,
                        'correo':correo,
                        'direccion':direccion,
                        'edad': 16
                        }])

if __name__ == '__main__':
    unittest.main()

