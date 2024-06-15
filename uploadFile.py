import os
import dropbox
from dropbox.files import WriteMode
#
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
        
            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.join(root, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, "rb") as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))


def main():
    access_token = 'sl.B3MNh6UJkUGYgkzyGvDp75oG7eM43O_9EHJC2kBsEoV1ngotvWFoILDLvdDHUQ3IvGfbu3gewczDuV0iZqxUTgzAUe3VlEyicT_4lHs0U3LRu9C1IGZZ_voWv8ZrJzx8f5PXCsXFbaP3'
    transferData = TransferData(access_token)

    file_from = str(input("enter the folder path to transfer: -"))
    file_to = input("enter the full path to upload to dropbox: -")

    transferData.upload_files(file_from, file_to)
    print("file has been moved!!")
main()