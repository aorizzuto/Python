import datetime
import pickle
import os.path

import pandas as pd
import numpy as np
import dataframe_image as dfi

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

file_token='.credentials/token.pickle' # File donde se guardará el token de Google una vez autorizado
file_cred='.credentials/credentials.json' # Credenciales de acceso
max_events=10

# NO BORRAR LA SIGUIENTE LINEA
#pylint: disable=maybe-no-member

def plot_image(df):
    df_styled = df #df.style.background_gradient() #adding a gradient based on values in cell
    dfi.export(df_styled,"mytable.png")
    img = Image.open('mytable.png')
    img.show()



def get_meetings():
    """Shows basic usage of the Google Calendar API. Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    lst=[]

    # The file token.pickle stores the user's access and refresh tokens, and is created automatically when the authorization flow completes for the first time.
    if os.path.exists(file_token):
        with open(file_token, 'rb') as token:
            creds = pickle.load(token) # Get credentials

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(file_cred, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(file_token, 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.now().isoformat() + 'Z' # 'Z' indicates UTC time
    print('\nGetting the upcoming events:\n')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=max_events, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        try:
            line=start+" "+event['summary']
            print(line)
            lst.append(line)
        except:
            pass

    print("\nThose were the next {} meetings you have.\n".format(max_events))

    return lst

def create_dataframe(lst):
    df = pd.DataFrame(lst)
    df.rename(columns={0:'info'},inplace=True)
    df['date']=df['info'].apply(lambda x:x[:10])
    df['time']=df['info'].apply(lambda x:x[11:19])
    df['subject']=df['info'].apply(lambda x:x[26:])
    df.drop('info',axis=1,inplace=True)
    return df


def main():
    lst=get_meetings()
    df=create_dataframe(lst)
    plot_image(df)

if __name__ == '__main__':
    main()