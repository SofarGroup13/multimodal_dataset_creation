#! /usr/bin/env python3.5
## @package Smartwatch_node.py
#This node is the node capable of taking specific data (sensor_msgs/Imu) from Smartwatch (or from the fake_node_Imu) and publish a topic with these.

import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import Header



##class FromSmart
class Fromsmart(object):
    def init(self):
        #data from GUI_node
        self.data1 = Header()
        self.flagstart =False
        ##defining frequency
        self.update_rate = 100
        #data from Smartwatch
        self.data = Imu()
        self.dataPublished = False
        ##creation of the topic with the intersting data
        self.pub_imu = rospy.Publisher('/imu_data', Imu, queue_size= 1 )
        ##subscriber to 'smartwatch_status'
        rospy.Subscriber('/smartwatch_status', Header, self.callback1)
        ##subscriber to 'fake_data_imu'
        #rospy.Subscriber('/inertial', Imu, self.callbackImu) #In case there is the link with the Smartwatch sensor.
        rospy.Subscriber('/fake_data_Imu', Imu, self.callbackImu)
##function for callback for message from Gui
    def callback1(self,data):
        self.data1 = data
        if self.data1.frame_id == "1":
            self.flagstart = True
        else:
            self.flagstart = False
##function for callback for message from fakenode
    def callbackImu(self,data):
        self.data = data

        self.dataPublished = True #active bool

    def run(self):
        self.init()
        r = rospy.Rate(self.update_rate)
        while True:
            try:
                if self.dataPublished and self.flagstart:
                    ##publish data from /fake_data_imu to topic /imu_data
                    self.pub_imu.publish(self.data)
                    self.dataPublished =False #disable bool
            except KeyboardInterrupt:
                break
##creation node
def main():
    rospy.init_node('smartnode', disable_signals=True) #create node
    smartnode = Fromsmart()
    smartnode.run()

if __name__ == '__main__':
    main()
