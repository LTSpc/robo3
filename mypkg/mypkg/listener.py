import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def main():
	rclpy.init()
	node = Node('listener')
	client = node.create_client(Query, 'query')
	while not client.wait_for_service(timeout_sec=1.0):
		node.get_logger().info('waiting...')

	req = Query.Request()
	req.name = 'seo-san'
	future = client.call_async(req) # response wo matanai#

	while rclpy.ok():
		rclpy.spin_once(node)
		if future.done():
			try:
				response = future.result()
			except:
				node.get_logger().info('yobidasi shippai')
			else:
				node.get_logger().info('age: {}'.format(response.age))

			break
	node.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()

