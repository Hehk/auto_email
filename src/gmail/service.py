import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_service(email):
    # TODO eventually use email to actually decide on the creds to get
    print("GETTING SERVICE FOR ", email)

    # TODO figure out a better way to store and get the creds file...
    SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
    if os.path.exists("secrets/token.json"):
        creds = Credentials.from_authorized_user_file("secrets/token.json", SCOPES)
        print(creds)
        return build("gmail", "v1", credentials=creds)
