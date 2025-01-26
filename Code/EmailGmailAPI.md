Requirements:
Set Up a Google Cloud Project
	1.	Go to Google Cloud Console:
	    •	Navigate to Google Cloud Console.
	    •	If you don’t have a Google Cloud account, create one.
	2.	Create a new project:
	    •	Click on the “Select a Project” dropdown at the top of the screen.
	    •	Click on “New Project”.
	    •	Give your project a name and click Create.

Enable Gmail API
	1.	Go to the API Library:
	    •	In the Google Cloud Console, go to the “APIs & Services” section and select “Library”.
	2.	Search for Gmail API:
	    •	In the search bar, type Gmail API and select the Gmail API from the list.
	3.	Enable the Gmail API:
	    •	Click Enable to activate the Gmail API for your project.

Set Up OAuth 2.0 Credentials
	1.	Go to the Credentials page:
	    •	In the Google Cloud Console, go to the “APIs & Services” section and select “Credentials”.
	2.	Create OAuth 2.0 credentials:
	    •	Click on “Create Credentials” and select OAuth 2.0 Client ID.
	    •	Configure the consent screen with necessary details (application name, email, etc.).
	3.	Set Application Type:
	    •	Under Application type, select Desktop app.
	4.	Download the credentials JSON file:
	    •	After creating the credentials, you will be able to download the client_secret.json file.
	    •	Save it to your local machine because you’ll need it in the Python code.

You will need the following Python libraries:
	•	google-auth
	•	google-auth-oauthlib
	•	google-auth-httplib2
	•	google-api-python-client
	•	google-api-core

To install these dependencies, run the following commands:
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client google-api-core
