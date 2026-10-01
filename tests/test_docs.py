import unittest
from materials_science_indexer import docs

class TestDocsModule(unittest.TestCase):

    def test_get_project_info(self):
        project_info = docs.get_project_info()
        self.assertIn("title", project_info)
        self.assertIn("version", project_info)
        self.assertIn("author", project_info)
        self.assertIn("license", project_info)
        self.assertIn("copyright", project_info)

    def test_get_project_info_values(self):
        project_info = docs.get_project_info()
        self.assertEqual(project_info["title"], "materials_science_indexer")
        self.assertEqual(project_info["version"], "1.0.0")

if __name__ == "__main__":
    unittest.main()
