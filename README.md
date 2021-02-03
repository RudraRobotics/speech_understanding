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

Dependencies:  
1. numpy  
2. ROS noetic  

How to run:  
1. roslaunch speech_understanding speech_understanding.launch  

After this a user can speak and give multiple commands and talk with the robot, offline. 
