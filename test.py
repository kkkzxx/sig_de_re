# -*- coding: utf-8 -*-
'''
__author__ = 'kongzixiang'
'''
import sys
sys.path.append('signature_detect/')
sys.path.append('signature_recognition/')
from signature_detect.yolo import YOLO
from signature_detect.yolo import detect_img
from signature_recognition.sig_match_test import sig_recog
from signature_recognition.sig_match_test_v2 import sig_recog2


img_path=detect_img(YOLO())
sig_recog(img_path)