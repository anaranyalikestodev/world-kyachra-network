import os,time
import pickle,secrets
from dotenv import load_dotenv
load_dotenv()
import cloudinary,cloudinary.uploader

cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET')    
)

def append_message(session,msg):

    filename=session["file"]

    with open(filename,"ab") as fout:
        pickle.dump(msg,fout)

def finalize_archive(filename):

    if not os.path.exists(filename):return 

    try:
        result=cloudinary.uploader.upload(
            filename,
            resource_type='raw',
            folder="chat_archives"
        )
        print("Upload Ok")

        os.remove(filename)
    except Exception as e:
        print(e)