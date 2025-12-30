import pytest
pytestmark = pytest.mark.no_db
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class BaseE2ETest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_base_page_loads(self):
        self.driver.get(self.live_server_url)
        self.assertIn("Consultorio", self.driver.title)

    def test_nav_links_exist(self):
        self.driver.get(self.live_server_url)

        nav_links = self.driver.find_elements(By.TAG_NAME, "a")
        texts = [link.text for link in nav_links]

        self.assertIn("Inicio", texts)
        self.assertIn("Servicios", texts)
        self.assertIn("Información", texts)

    def test_phone_visible(self):
        self.driver.get(self.live_server_url)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("0988605465", body_text)

    def test_logo_is_visible(self):
        self.driver.get(self.live_server_url)
        logo = self.driver.find_element(By.TAG_NAME, "img")
        self.assertTrue(logo.is_displayed())