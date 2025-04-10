# this is a node to publish HCSR-04 asensor data.
# the ros2 run name is: move
# this are the main libraries
import rclpy
from rclpy.node import Node

# I use gpio zero for the sensor control for more info about gpiozero is here below:

from gpiozero import DistanceSensor # The DistanceSensor class is  used to control the sensor
# https://gpiozero.readthedocs.io/en/latest/index.html#

from std_msgs.msg import Float64


class Ultrasonic_publisher(Node):

    def __init__(self):
        super().__init__('sonic_publisher')
        self.publisher_ = self.create_publisher(Float64, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        sensor = DistanceSensor(echo=4, trigger=17) # sets the echo and triggering pin.
        sense = sensor.distance *100 # is the value thats is send over the msg data.
        msg = Float64()
        msg.data = sense # send the data as a float
        
        self.publisher_.publish(msg) # publish msg
        self.get_logger().info('Publishing: "%f"' % msg.data) # logs msg data
        self.i += 1

        
#the rest is just the node spinning
def main(args=None):
    rclpy.init(args=args)

    ultrasonic_publisher = Ultrasonic_publisher()

    rclpy.spin(ultrasonic_publisher) # and now it spins

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    ultrasonic_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()