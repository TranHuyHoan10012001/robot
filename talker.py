from pipes import Template
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(data):
    pub1 = rospy.Publisher("/Robot1/cmd_vel", Twist , queue_size =10)
    pub2 = rospy.Publisher("/Robot2/cmd_vel", Twist , queue_size =10)
    
    rospy.loginfo(rospy.get_caller_id () + "I heard %s", data.ranges[0])
    msg = Twist()
    msg.linear.x = 0.5
    msg.angular.z = 0.2
    rospy.loginfo(msg)
    pub1.publish(msg)
    pub2.publish(msg)
def talker ():
    rospy.init_node("talker", anonymous=True)
    rospy.Subscriber("/Robot1/scan", LaserScan , callback)
    rospy.spin()

    rate = rospy.Rate (10) # 10hz
if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
