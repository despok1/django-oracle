from django.test import TestCase


class IndexViewTests(TestCase):
    def test_renders_index_template(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "oracle/index.html")
        self.assertContains(response, "1233231231231232312312312")
