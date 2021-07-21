import dropbox 

class Cloudstorage: 
    def __init__(self, accesstoken):
        self.accesstoken = accesstoken 
    
    def uploadfile(self, file_from, file_to ):
        dbx = dropbox.Dropbox(self.accesstoken)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)
    
def main() :
    accesstoken ='cRVAzqD-tw0AAAAAAAAAAaA4ovgyU90ws1x-SJM3OMQ_0Sag5WiNGsubdf0GsOWd'
    transferdata = Cloudstorage(accesstoken)
    file_from = input('enter the location: ')
    file_to = input('enter full path to upload: ')
    transferdata.uploadfile(file_from, file_to)
    print("The file has benn uploaded")
main()
