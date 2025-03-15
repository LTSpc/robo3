import rclpy
from rclpy.node import Node
#from std_msgs.msg import Int16
from person_msgs.msg import Person

def cb(msg):
#	node.get_logger().info('listen %d'%msg.data)
	node.get_logger().info('listen %s'%msg)

rclpy.init()
node = Node('listener')
#sub = node.create_subscription(Int16, 'countup',cb,10)
sub = node.create_subscription(Person, 'person',cb,10)
# くりかえす
rclpy.spin(node)
