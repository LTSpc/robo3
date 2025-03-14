import rclpy
from rclpy.node import Node
from  std_msgs.msg import Int16


rclpy.init()
node = Node('talker')

pub= node.create_publisher(Int16,'countup', 10)
n = 0

def cb():
	global n
	# talkerがlistenerに送るmsgの
	# 内容にあたる変数を型を指定して作成
	msg = Int16()
	# msgに内容を入れる
	msg.data = n
	# 送る
	pub.publish(msg)
	n += 1

node.create_timer(0.5, cb)
# くりかえす
rclpy.spin(node)
