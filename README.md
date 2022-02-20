# paitient_monitoring_coding_test

# Setup Steps
- Clone repository using the repo url
- in the project folder run the following commands
``python manage.py makemigrations``
``python manage.py migrate``
``python manage.py createsuperuser``
``python manage.py runserver``
- these steps should start running the app with a url provided to access it

# Completed User Stories
1. Clinicians can register new patient accounts into the system
2. Administrators can register new clinician accounts into the system
6. Clinicians can view a patient dashboard showing history of patient measurements and (not) alerts
10. Clinicians can only see patients that they registered themselves or are otherwise assigned to
them
11. User management should be managed in a separate Django app
12. Measurements/Thresholds/Alerts should be managed in another separate Django app

# Additional Questions
1. If you had more time, what would you change or focus more on?
With a little more time I could setup the client thresholds and associated risk dashboards for the clients. This would include the completion of user story 5,6,7 and 8. I believe I demostrated my ability to be able to program these features, but I just didn't have the time available to push them through.

I was never planning to address items regarding API's and Emails as I have never built anything like this in Django. If I was to complete these parts I would have preferred to discuss with someone who is more expierenced in Django or done some research online to make sure I complete them in a manner that was time efficient.

2. Which part of the solution consumed the most amount of time?
I think most of the time was relearning some Django shortcuts and refactoring the project. For example, my initial view.py files were very basic, but once I looked at the LoginRequiredMixin, I realised the view classes were much more approproiate.

3. What suggestions do you have for stakeholders in this context that they may not have
thought of?
I think giving the clinicians the ability to easily sort measurements by patients is vital. Long term overview of the patients measurements would help give them a make better diagnosises and see declines in patient health. This could easily be displayed in line graphs on the patient dashboard.

I think thresholds for patient submission frequency would also be benefitial, since alerts are only being logged for entered measurements. If a patient is unreliable, unwell or there is technical issues, the clinicians currently has no oversite of the patients health.

I think once we would move out of the prototype stage the clinician would need an expansion of the patient information in the system. For the measurements to provide the most use, the clinician should be able to see the patients age, medical history and recent communicatinos to help evaluate measurements. 
