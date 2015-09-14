#!/usr/bin/env python
# import roslib; roslib.load_manifest('robot_mover')

""" a program to make the robot travel in a 1m x 1m square using time to calculate distances"""
import rospy

from geometry_msgs.msg import Twist

rospy.init_node('square')

def mover():

    pub = rospy.Publisher('cmd_vel', Twist)

    twist = Twist()
    #setting a linear travel speed to .1 m/s
    twist.linear.x = .1
    pub.publish(twist)
    #setting the duration of sleep to allow the robot to travel forward
    rospy.sleep(10)

    twist.angular.z = 1
    #having the robot turn left
    pub.publish(twist)
    rospy.sleep(1.5);


r=rospy.Rate(10)
#mover will continue to run if rospy is not shut down
while not rospy.is_shutdown(): 
    mover()
