import unittest
from materials_science_indexer import materials_database

class TestMaterialsDatabase(unittest.TestCase):
    def test_add_material(self):
        db = materials_database.MaterialsDatabase()
        db.add_material('mat1', 'Material 1', {'a': 1, 'b': 2})
        self.assertEqual(db.get_material_by_id('mat1'), {'name': 'Material 1', 'lattice_constants': {'a': 1, 'b': 2}, 'alloy_properties': {}})

    def test_update_material(self):
        db = materials_database.MaterialsDatabase()
        db.add_material('mat1', 'Material 1', {'a': 1, 'b': 2})
        db.update_material('mat1', name='New Name')
        self.assertEqual(db.get_material_by_id('mat1'), {'name': 'New Name', 'lattice_constants': {'a': 1, 'b': 2}, 'alloy_properties': {}})

    def test_delete_material(self):
        db = materials_database.MaterialsDatabase()
        db.add_material('mat1', 'Material 1', {'a': 1, 'b': 2})
        db.delete_material('mat1')
        self.assertIsNone(db.get_material_by_id('mat1'))

if __name__ == '__main__':
    unittest.main()
