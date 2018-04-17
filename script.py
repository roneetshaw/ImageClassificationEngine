'''
Created on 13-Apr-2018

@author: kumarro
'''

from flask import Flask,render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from distutils.log import debug
import label_image as label

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
   if request.method == 'POST' and 'photo' in request.files:
       filename = photos.save(request.files['photo'])
       res = label.runInit(app.config['UPLOADED_PHOTOS_DEST']+'/'+filename)
       return res
   return 'Send a POST request'

@app.route("/")
def hello():
   return "Hello World!"
if __name__ == "__main__":
   app.run()