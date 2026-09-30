"""
Database interface for materials science data.

This module provides a basic database interface to store and retrieve materials science data.
It uses the built-in `dict` type as an in-memory database, but can be easily replaced with a real database backend.
"""

class MaterialsDatabase:
    """
    Database interface for materials science data.

    This class provides methods to add, update and delete materials from the database,
    as well as retrieve specific materials by their ID or properties.
    """

    def __init__(self):
        """
        Initialize an empty database.
        """
        self.database = {}

    def add_material(self, material_id, name, lattice_constants, alloy_properties=None):
        """
        Add a new material to the database.

        Args:
            material_id (str): Unique identifier for the material.
            name (str): Name of the material.
            lattice_constants (dict): Lattice constants of the material.
            alloy_properties (dict, optional): Alloy properties of the material. Defaults to None.

        Returns:
            None
        """
        self.database[material_id] = {
            'name': name,
            'lattice_constants': lattice_constants,
            'alloy_properties': alloy_properties if alloy_properties else {}
        }

    def update_material(self, material_id, **kwargs):
        """
        Update an existing material in the database.

        Args:
            material_id (str): Unique identifier for the material.
            **kwargs: Keyword arguments to update. Supported keys are 'name', 'lattice_constants', and 'alloy_properties'.

        Returns:
            None
        """
        if material_id in self.database:
            for key, value in kwargs.items():
                self.database[material_id][key] = value

    def delete_material(self, material_id):
        """
        Delete a material from the database.

        Args:
            material_id (str): Unique identifier for the material.

        Returns:
            None
        """
        if material_id in self.database:
            del self.database[material_id]

    def get_material_by_id(self, material_id):
        """
        Retrieve a material by its ID.

        Args:
            material_id (str): Unique identifier for the material.

        Returns:
            dict: Material data or None if not found.
        """
        return self.database.get(material_id)

    def get_materials_by_name(self, name):
        """
        Retrieve materials with a specific name.

        Args:
            name (str): Name of the material(s).

        Returns:
            list: List of material IDs matching the name.
        """
        return [material_id for material_id, data in self.database.items() if data['name'] == name]

    def get_materials_by_lattice_constants(self, lattice_constants):
        """
        Retrieve materials with specific lattice constants.

        Args:
            lattice_constants (dict): Lattice constants to search for.

        Returns:
            list: List of material IDs matching the lattice constants.
        """
        return [material_id for material_id, data in self.database.items() if data['lattice_constants'] == lattice_constants]

# Example usage
db = MaterialsDatabase()
db.add_material('mat1', 'Material 1', {'a': 1.0, 'b': 2.0})
print(db.get_material_by_id('mat1'))  # Output: {'name': 'Material 1', 'lattice_constants': {'a': 1.0, 'b': 2.0}, 'alloy_properties': {}}
