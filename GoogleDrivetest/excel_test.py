from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# check auth
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

downloaded = drive.CreateFile({'id': '1VCfUC...'})

# Download the file to a local disk as 'sample.csv'.
downloaded.GetContentFile('softbank_9984.csv')

import pandas as pd
data = pd.read_csv('softbank_9984.csv', encoding='CP932', header=-1)
data.head()