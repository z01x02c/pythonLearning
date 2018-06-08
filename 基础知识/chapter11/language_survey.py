from survey import AnonynousSurvey

question = "What language did first learn to speak?"
my_survey = AnonynousSurvey(question)

my_survey.show_question()
print("Enter 'q' at ant time to quit.")
while True:
	response = input('Language: ')
	if response == 'q':
		break
	my_survey.store_response(response)

print("\nThank you to everyone who participant in the survey!")
my_survey.show_results()
	
	
