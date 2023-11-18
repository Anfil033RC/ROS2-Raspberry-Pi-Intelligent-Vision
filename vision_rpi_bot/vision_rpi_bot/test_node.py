import rclpy
from geometry_msgs.msg import Quaternion

rclpy.init()
node = rclpy.create_node('my_first_node')
publisher = node.create_publisher(Quaternion,'my_first_publisher_topic',10)
D = Quaternion()
D.x = 1.0
D.y = 2.0
D.z = 3.0
D.w = 1.0

publisher.publish(D)
#print (x,y,z,w)
rclpy.spin(node)

