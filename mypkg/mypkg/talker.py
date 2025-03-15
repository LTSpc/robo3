import rclpy
from rclpy.node import Node
#from  std_msgs.msg import Int16
#from person_msgs.msg import Person
from person_msgs.srv import Query

def cb(request, response):
	if request.name == 'seo-san':
		response.age = 32
	else:
		response.age = 255
	return response

rclpy.init()
node = Node('talker')
srv = node.create_service(Query, 'query', cb)
rclpy.spin(node)
