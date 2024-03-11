#!/usr/bin/python3

import unittest
import uuid
import datetime
from models.base_model import set_attribute, BaseModel

class TestSetAttribute(unittest.TestCase):
    obj = type('TestObject', (), {})()
    set_attribute(obj, 'name', 'John')
    self.assertEqual(obj.name, 'John')

    set_attribute(obj, 'created_at', '2024-03-11T12:00:00.000000')
    self.assertIsInstance(obj.created_at, datetime.datetime)

class TestBaseModel(unittest.TestCase):
     def test_base_model_init_with_kwargs(self):
         kwargs = {'name': 'John', 'created_at': '2024-03-11T12:00:00.000000'}
         obj = BaseModel(**kwargs)
         self.assertEqual(obj.name, 'John')
         self.assertIsInstance(obj.created_at, datetime.datetime)

    def test_base_model_init_without_kwargs(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)

    def setUp(self):
        self.base_model = BaseModel()

    def test_str_method(self):
        self.assertEqual(
                str(self.base_model),
                f"[{self.base_model.__class__.__name__}] ({self.base_model.id}) {self.base_model.__dict__}"
                )
    def test_save_method(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertIn(self.base_model, storage.objects.values())

    def test_to_dict_method(self):
        expected_dict = {
                '__class__': self.base_model.__class__.__name__,
                'id': self.base_model.id,
                'created_at': self.base_model.created_at.isoformat(),
                'updated_at': self.base_model.updated_at.isoformat(),
                }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

    if __name__ == '__main__':
        unittest.main()

