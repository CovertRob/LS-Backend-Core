import unittest
import os
import sys
import shutil
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app


class AppTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.data_path = os.path.join(os.path.dirname(__file__), 'data')
        os.makedirs(self.data_path, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.data_path, ignore_errors=True)

    def create_document(self, name, contents=""):
        with open(os.path.join(self.data_path, name), 'w') as file:
            file.write(contents)

    def test_index(self):

        self.create_document("about.md")
        self.create_document("changes.txt")
        with self.client.get("/") as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "text/html; charset=utf-8")

            files = [os.path.basename(file) for file in os.listdir(self.data_path)]
            in_response = all([True if file in response.get_data(as_text=True) else False for file in files])

            self.assertTrue(in_response)

    def test_get_file(self):
        self.create_document('history.txt', "Python 0.9.0 (initial release) is released.")
        with self.client.get('/history.txt') as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "text/plain; charset=utf-8")
            self.assertIn("Python 0.9.0 (initial release) is released.", response.get_data(as_text=True))

    def test_document_not_found(self):
        # Attempt to access a nonexistent file and verify a redirect happens
        with self.client.get("/notafile.ext") as response:
            self.assertEqual(response.status_code, 302)

        # Verify redirect and message handling works
        with self.client.get(response.headers['Location']) as response:
            self.assertEqual(response.status_code, 200)
            self.assertIn("notafile.ext does not exist",
                          response.get_data(as_text=True))

        # Assert that a page reload removes the message
        with self.client.get("/") as response:
            self.assertNotIn("notafile.ext does not exist",
                             response.get_data(as_text=True))
            
    def test_view_markdown(self):
        self.create_document('about.md', "# Python is...")
        response = self.client.get('/about.md')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertIn("<h1>Python is...</h1>", response.get_data(as_text=True))

    def test_edit_file(self):
        self.create_document("changes.txt")
        response = self.client.get('/changes.txt/edit')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertIn("<textarea", response.get_data(as_text=True))

    def test_updating_file(self):
        self.create_document("changes.txt")
        response = self.client.post('/changes.txt/edit', data={'content': "new content"})
        self.assertEqual(response.status_code, 302)

        follow_response = self.client.get(response.headers['Location'])
        self.assertIn("changes.txt has been updated.", follow_response.get_data(as_text=True))

        with self.client.get("/changes.txt") as content_response:
            self.assertEqual(content_response.status_code, 200)
            self.assertIn("new content", content_response.get_data(as_text=True))      

    def test_enter_new_document(self):
        response = self.client.get('/new')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
        self.assertIn("<form action=\"/new\" method=\"post\">", response.get_data(as_text=True))

    def test_save_new_document(self):
        response = self.client.post("/new", data={'new_file': "new_file.txt"})
        self.assertEqual(response.status_code, 302)
        follow_response = self.client.get(response.headers['Location'])
        self.assertIn("new_file.txt has been created.", follow_response.get_data(as_text=True))

        with self.client.get("/new_file.txt") as content_response:
            self.assertEqual(content_response.status_code, 200)

    def test_create_new_document_without_filename(self):
        response = self.client.post('/new', data={'new_file': ''})
        self.assertEqual(response.status_code, 422)
        self.assertIn("A name is required.", response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()