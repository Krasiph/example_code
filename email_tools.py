import os
import base64
import httplib2
import oauth2client

from oauth2client import client
from oauth2client import tools
from apiclient import discovery
from email.mime.text import MIMEText
from urllib.error import HTTPError

SCOPES = 'https://www.googleapis.com/auth/gmail.modify'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'GMail API Quickstart'

def get_credentials():
    """
    Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    :return: the obtained credentials
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')

    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)

    credential_path = os.path.join(credential_dir, 'gmail-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()

    if not credentials or credentials.invalid:
        if not os.path.exists(CLIENT_SECRET_FILE):
            print('No secrets file in working directory.')

            credentials = None

        else:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)

            flow.user_agent = APPLICATION_NAME

            credentials = tools.run_flow(flow, store, None)

            print('Stored credentials to {}'.format(credential_path))

    return credentials


def create_message(sender, to, subject, message_text):
    """
    Create a message for an email.

    :param sender: email address of the sender
    :param to: email address of the receiver
    :param subject: the subject of the email message
    :param message_text: the text of the email message

    :return: an object containing a base64url encoded email object
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    # @TODO might have to decode the final result into a string, not sure
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode('utf-8')}


def send_message(service, user_id, message):
    """
    Send an email message.

    :param service: authorized Gmail API service instance
    :param user_id: user's email address (the special value "me" can be used to indicate the authenticated user
    :param message: message to be sent

    :return: the sent message
    """
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())

        print('Message ID: {}'.format(message['id']))

        return message

    except HTTPError as e:
        print('An error occurred: {}'.format(e))


def main():
    credentials = get_credentials()

    if credentials is None:
        return

    http = credentials.authorize(httplib2.Http())

    service = discovery.build('gmail', 'v1', http=http)

    # results = service.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])

    # if not labels:
    #     print('No labels found.')
    #
    # else:
    #     print('Labels:')
    #     for label in labels:
    #         print('\t{}'.format(label['name']))

    msg = create_message('krasiph@gmail.com', 'matthew-best@utulsa.edu', 'TEST', 'This is a test!')
    send_message(service, 'me', msg)

    return


if __name__ == '__main__':
    main()
