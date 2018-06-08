import unittest
from survey import AnonynousSurvey

class TestAnonymouSurvey(unittest.TestCase):

	def setUp(self):
		question = "What language did you first learn to speak?"
		self.my_survey = AnonynousSurvey(question)
		self.responses = ['english','chinese','japanese']
	
	def test_store_single_response(self):
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0].title(),self.my_survey.responses)


	def test_store_three_response(self):
		for response in self.responses:
			self.my_survey.store_response(response)

		for response in self.responses:
			self.assertIn(response.title(),self.my_survey.responses)

unittest.main()
