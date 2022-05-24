from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10

class NewVsitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_for_one_user(self):
		# Edith ouviu falar que agora a aplicação online de lista de tarefas
		# aceita definir prioridades nas tarefas do tipo baixa, média e alta
		# Ela decide verificar a homepage

		self.browser.get(self.live_server_url)

		# Ela percebe que o título da página e o cabeçalho mencionam
		# listas de tarefas com prioridade (priority to-do)

		self.assertIn('priority to-do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('priority to-do', header_text)

		# Ela é convidada a inserir um item de tarefa e a prioridade da 
		# mesma imediatamente

		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		# Ela digita "Comprar anzol" em uma nova caixa de texto
		# e assinala prioridade alta no campo de seleção de prioridades
		inputbox.send_keys('Comprar anzol')