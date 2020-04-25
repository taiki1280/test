import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def upload_gd_image(filename, folder_id):
    # folder_id = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    # folder_id = '1CDiMHnxzQxzVzFf7ghMiUDO_1fbmk2hM'
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth)
    f = drive.CreateFile(
        {'title': filename,
         'mimeType': 'image/png',
         'parents': [{'kind': 'drive#fileLink', 'id': folder_id}]}
    )
    f.SetContentFile(filename)
    f.Upload()
    print(f)
    url = 'http://drive.google.com/uc?export=view&id=' + f['id']
    return url


if __name__ == '__main__':
    url = upload_gd_image("球体.png", "1iSl19xZs_GZtfDFCVACtq2E7rz9veja6")
    print(url)
