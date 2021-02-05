# speech_understanding

This is the speech recognition ros module  
Features:  
1. Text to speech conversion with picovoice cheetah  
2. rasa-nlu and rasa-core for NLP features    
3. text to speech conversion   
4. ros nav_msgs/Goal [] publisher as a mission with voice commands  
5. Offiline speech recongition features
6. Supports multiple plateform like embedded, desktop etc  
7. Mission cancelation feature   
8. Mission changing feature  
9. wake up word detection for voice commanded system startup  

Dependencies:  
1. numpy  
2. ROS noetic  
3. pyaudio_ros package https://github.com/RudraRobotics/pyaudio_ros  

How to run:  
1. roslaunch speech_understanding speech_understanding.launch  

After this a user can speak and give multiple commands and talk with the robot, offline. 
Online API documentation of this module:  https://rudrarobotics.github.io/speech_understanding/html/index.html
