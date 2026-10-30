from django.test import TestCase


class IndexViewTests(TestCase):
    def test_renders_index_template(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "oracle/index.html")
        self.assertContains(response, 'lang="uk"')
        self.assertContains(response, 'id="home-tab"')
        self.assertContains(response, 'id="info-tab"')
        self.assertContains(response, "Як працювати з Django")
        self.assertContains(response, "python -m pip install Django")
        self.assertContains(response, "python manage.py runserver")
        self.assertContains(response, "python manage.py makemigrations")
        self.assertContains(response, "Для чого потрібен Makefile")
        self.assertContains(response, "make migrate")
        self.assertContains(response, "Що шукати:")

    def test_info_link_opens_info_page(self):
        response = self.client.get("/")

        self.assertContains(response, 'href="/info/"')

    def test_info_page_links_back_to_index(self):
        response = self.client.get("/info/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "oracle/info.html")
        self.assertContains(response, 'href="/"')
        self.assertContains(response, "Цей сайт створено на Django.")
