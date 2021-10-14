import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64, String, Int32

class MasodikNode(Node):

    def __init__(self):
        super().__init__("masodik_node")
        # Subscriber
        self.sub = self.create_subscription(Float64, "/masodik_topic", self.cb_sub_masodik_topik, 0)
        # Publisher
        self.pub_transformed = self.create_publisher(Float64, "/transformed_masodik_topic", 0)
        self.get_logger().info("Inicializálás kész")

    def cb_sub_masodik_topik(self, data: Float64):
        msg = Float64()
        msg.data = 2 * data.data
        self.get_logger().info(f"Transzformált érték: {msg.data}")
        self.pub_transformed.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    masodik_node = MasodikNode()
    rclpy.spin(masodik_node)
    masodik_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

    