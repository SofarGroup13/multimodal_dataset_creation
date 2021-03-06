import rospy, sys
from multimodal_dataset_creation.srv import GestureSequence

## class Gesture_Sequence_Client
#  Client class for the service "gesture sequence generator"
class Gesture_Sequence_Client:
    def __init__(self,num_of_gestures):
        self.num_of_gestures = num_of_gestures
        self.gesture_sequence = self.gesture_sequence_request(self.num_of_gestures)

    ## method gesture_sequence_request
    #  Request to the service for the gesture sequence
    #  @param self The object pointer
    #  @param num_of_gestures
    def gesture_sequence_request(self,num_of_gestures):
        rospy.wait_for_service('gesture_sequence_generator')
        try:
            self.gesture_sequence_generator = rospy.ServiceProxy('gesture_sequence_generator', GestureSequence)
            self.response = self.gesture_sequence_generator(self.num_of_gestures)
            return self.response
        except rospy.ServiceException as e:
            print("Service did not process request: " + str(e))