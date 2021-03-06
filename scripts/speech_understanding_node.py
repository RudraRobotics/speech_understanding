#!/usr/bin/env python3
import rospy
import sys
from audio_common_msgs.msg import AudioData
import os
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '../binding/python'))

from cheetah import Cheetah

class SpeechUnderstanding:

  def __init__(self):
    self.library_path = rospy.get_param("/speech_understanding/library_path")
    self.acoustic_model_path = rospy.get_param("/speech_understanding/acoustic_model_path")
    self.language_model_path = rospy.get_param("/speech_understanding/language_model_path")
    self.license_path = rospy.get_param("/speech_understanding/license_path")

    self.cheetah = Cheetah(
        library_path=self.library_path,
        acoustic_model_path=self.acoustic_model_path,
        language_model_path=self.language_model_path,
        license_path=self.license_path,
        endpoint_duration_sec=1)

    self.sub = rospy.Subscriber("audio", AudioData, self.callback)

  def callback(self,data):
    try:
        pcm = data.data
        #print('len:', len(pcm))
        #print('type of tuple data and data:', type(pcm[0]), pcm[0])
        partial_transcript, is_endpoint = self.cheetah.process(pcm)
        if is_endpoint:
            print(self.cheetah.flush())
    except Exception as e:
        print(e)

if __name__ == '__main__':
  rospy.init_node('speech_understanding', anonymous=True)
  speechUnderStanding = SpeechUnderstanding()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
