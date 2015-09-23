#!/usr/bin/env python

from neato_node.msg import Bump
from geometry_msgs.msg import Twist
import rospy

twist = Twist()



def process_bump(msg)
	bumped = false
	if leftFront == 1 or rightFront == 1 or leftSide == 1 or rightSide == 1:
		bumped = true
	while bumped == true:
		twist.linear.x = 0



rospy.init_node('emergency_stop')

rospy.Subscriber("/bump",Bump, process_bump)


pub =rospy.Publisher('cmd_vel', Twist, queue_size =10)

twist.linear.x = 0.2


r = rospy.Rate(10)
while not rospy.is_shutdown():
	r.sleep()
	pub.publish(twist)