import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from turtlesim.msg import Pose
import math

class TurtleDistance(Node):
    def __init__(self):
        super().__init__('turtle_distance')

        # Correct the message type to Pose (from turtlesim.msg)
        self.subscription_ = self.create_subscription(
            Pose,  # Use turtlesim.msg.Pose instead of Float32
            '/turtle1/pose',
            self.pose_pub,
            10
        )
        self.publisher_ = self.create_publisher(Float32, '/turtle1/distance_from_origin', 10)

    def pose_pub(self, msg):
        # msg is of type turtlesim.msg.Pose, so you can access x, y
        x, y = msg.x, msg.y
        dist = math.sqrt(x**2 + y**2)

        distance = Float32()
        distance.data = dist
        self.publisher_.publish(distance)

        self.get_logger().info(f'Turtle Distance: {distance.data:.2f}')

def main(args=None):
    rclpy.init(args=args)
    turtle_distance = TurtleDistance()
    rclpy.spin(turtle_distance)

    turtle_distance.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
