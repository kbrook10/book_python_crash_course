# (1) Using the unittest module to test Classes

class AnonymousSurvey():
	'''Collect anonymous responses to survey questions'''

	def __init__(self, question):
		'''Store questions and prepare to store answers'''

		self.question = question
		self.responses = []

	def show_question(self):
		'''Show the survey question...'''

		print(self.question)

	def store_response(self, new_response):
		'''Store single response'''

		self.responses.append(new_response)

	def show_results(self):
		'''Show all the responses'''

		print('Survey results: ')
		for response in self.responses:
			print('- ' + response)
