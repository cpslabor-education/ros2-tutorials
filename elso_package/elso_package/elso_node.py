import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64, String, Int32

import random

class ElsoNode(Node):

    def __init__(self):
        super().__init__("elso_node")
        # Publisher
        self.pub_elso_topic = self.create_publisher(String, "/elso_topic", 0)
        self.pub_masodik_topic = self.create_publisher(Float64, "/masodik_topic", 0)
        # Timer
        self.pub_timer = self.create_timer(0.1, self.cb_timer)
        # Értesítjük a felhasználót
        self.get_logger().info("Kész az inicializálás!")

    def cb_timer(self):
        msg = String()
        msg.data = "Szevasz!"
        self.pub_elso_topic.publish(msg)
        # Random szamok
        msg_random = Float64()
        msg_random.data = random.random()
        self.pub_masodik_topic.publish(msg_random)




def main(args=None):
    rclpy.init(args=args)
    elso_node = ElsoNode()
    rclpy.spin(elso_node)
    elso_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
