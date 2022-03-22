#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

def take_action(regions):
    msg = Twist()
    linear_x = 0

    if regions > 1 :
        state_description = 'No_obstacle'
        linear_x = 1
    
    else:
        state_description = 'Obstacle_detected'
        linear_x = 0

    rospy.loginfo(state_description)
    msg.linear.x = linear_x
    pub.publish(msg)

def lidar_read(msg):
    regions = round(min(msg.ranges[288:431]),2)
    take_action(regions)

def main():
    global pub

    rospy.init_node('obstacledetection')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    sub = rospy.Subscriber("/scout/laser/scan", LaserScan, lidar_read)
    rospy.spin()

if __name__ == '__main__':
    main()