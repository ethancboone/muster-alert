from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from datetime import date


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def daily_inbox_check():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """

    # Create a dictionary to store our email information
    emails = []

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:

        # This is used so we can query messages for only today 
        today = date.today()

        # Dates have to formatted in YYYY/MM/DD format for gmail
        query = f"after: {today.strftime('%Y/%m/%d')}"

        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages')

        for msg in messages:
            txt = service.users().messages().get(userId='me', id=msg['id']).execute()

            try:
                payload = txt['payload']
                headers = payload['headers']
                # Look for Subject and Sender Email in the headers
                for d in headers:
                    if d['name'] == 'Subject':
                        subject = d['value']
                        emails.append(subject)
            except:
                pass

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')

    return 'Test Virtual Muster' in emails

if __name__ == '__main__':
    response = daily_inbox_check()
    print(response)

