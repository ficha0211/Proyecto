import unittest
from flask import json
from app import create_app, db
from app.models import Data

class TestDataRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app("testing")
        cls.client = cls.app.test_client()

        # Establecer el contexto de la aplicación
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

        # Crear las tablas en la base de datos
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Eliminar las tablas de la base de datos y sacar el contexto de la aplicación
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()
        cls.app_context.pop()

    def test_insert_data(self):
        data = {"name": "Test Data"}
        response = self.client.post("/data", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Data inserted successfully", response.data)

    def test_get_all_data(self):
        response = self.client.get("/data")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_delete_data(self):
        # Insertar un dato primero
        data = Data(name="Test Data")
        db.session.add(data)
        db.session.commit()

        # Eliminar el dato insertado
        response = self.client.delete(f"/data/{data.id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Data deleted successfully", response.data)

if __name__ == "__main__":
    unittest.main()
