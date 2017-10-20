#!/usr/bin/env python
"""
    Listener
    Subscriber
"""
import rospy
from std_msgs.msg import String


def callback(data):
    """
    Callback
    """
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.data)


def listener():
    """
    Listener
    """
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
