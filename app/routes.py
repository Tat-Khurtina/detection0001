from werkzeug.utils import secure_filename #
from flask import render_template, flash, redirect, url_for, request, jsonify, Response
from werkzeug.urls import url_parse
from app import app

import os

import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import cv2
import torch
import numpy as np


from app.camera import VideoCamera

model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model = model.eval()

@app.route('/')
@app.route('/str')
def str():
    # rendering webpage
    return render_template('str.html')
def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame(model=model)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



