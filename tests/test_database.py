import copy
import csv
import config
import helpers
import unittest
import database as db

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('15J', 'Ana', 'Pons'),
            db.Cliente('48H', 'Pere', 'Carretero'),
            db.Cliente('28Z', 'Adri', 'Abad')
        ]
    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('15J')
        cliente_inexistente = db.Clientes.buscar('11J')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)
    
    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('39X', 'Hector', 'Costa')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '39X')
        self.assertEqual(nuevo_cliente.nombre, 'Hector')
        self.assertEqual(nuevo_cliente.apellido, 'Costa')
    
    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('15J'))
        cliente_a_modificado = db.Clientes.modificar('15J', 'Amor', 'Etern')
        self.assertEqual(cliente_a_modificar.nombre, 'Ana')
        self.assertEqual(cliente_a_modificado.nombre, 'Amor')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('28Z')
        cliente_rebuscado = db.Clientes.buscar('28Z')
        self.assertEqual(cliente_borrado.dni, '28Z')
        self.assertIsNone(cliente_rebuscado)

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('21Z', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('2222B', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F45', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('28Z', db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar('15J')
        db.Clientes.borrar('48H')
        db.Clientes.modificar('28Z', 'Pau', 'Ciruelos')

        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)
        self.assertEqual(dni, '28Z')
        self.assertEqual(nombre, 'Pau')
        self.assertEqual(apellido, 'Ciruelos')