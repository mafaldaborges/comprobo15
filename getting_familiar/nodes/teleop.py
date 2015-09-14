#!/usr/bin/env python

"""A code to control the direction of travel of the Neato using the keys i,k, j, and l"""

import tty
import select
import sys
import termios
import rospy


from geometry_msgs.msg import Twist

rospy.init_node('teleop')

#given code to pick up keystrokes
def getKey():
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

settings = termios.tcgetattr(sys.stdin)
key = None

twist = Twist()
# while key=='k':
# 	print "hey"
	# twist.linear.x = 0.1
	# print twist.linear.x


while key != '\x03':
	key = getKey()
	#i is pressed the robot will move forward linearly with no angular velocity until a new command is given
	while key=="i":
		pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
		twist.linear.x = 0.1
		twist.angular.z = 0
		pub.publish(twist)
		break
	#, for backwards
	while key==",":
		pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
		twist.linear.x = -0.1
		twist.angular.z = 0
		pub.publish(twist)
		break
	#k for stopping
	while key=="k":
		pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
		twist.linear.x = 0
		twist.angular.z=0
		pub.publish(twist)
		break
	#j left turn
	while key=="j":
		pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
		twist.angular.z = 0.5
		twist.linear.z = 0
		pub.publish(twist)
		break
	#l right turn
	while key=="l":
		pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
		twist.angular.z = -0.5
		twist.linear.z = 0
		pub.publish(twist)
		break
