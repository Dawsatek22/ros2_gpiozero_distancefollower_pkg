
 # this is a node to control a 2 dc motors with a h-bridge using gpiozero and ros2 jazzy
# the ros2 run name is: move
from time import sleep # for sleep function
# this are the main libraries
import rclpy
from rclpy.node import Node
# this node uses the gpiozero library to control the  h_bridge more info on gpiozero here below:
# https://gpiozero.readthedocs.io/en/latest/index.html#
from gpiozero import Robot, Motor # this is to control the dc motor
from std_msgs.msg import Float64 # receive and respond to the sensor node 
robot = Robot(left=Motor(15,14), right=Motor(23, 18)) # the Pins for the robot are setup with the gpio pins

class Motorsubscriber(Node):

    def __init__(self):
        super().__init__('motor_subscriber')
        self.subscription = self.create_subscription(
          Float64,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%i"' % msg.data) 
        # here the motors changes position depending on the publisher value received
        if msg.data < 5: # if value is lower than 5 than it goes backwards and then leftwards
            robot.backward()
            
            sleep(2)
            robot.left()
            sleep(1)
            print('reposition')
            
            
        else: # else it moves forward
            robot.forward()
            print('forwards')
            sleep(0.2)
            
        
            
        
#the rest is just the node spinning

def main(args=None):
    rclpy.init(args=args)

    motorsubscriber = Motorsubscriber()

    rclpy.spin(motorsubscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    motorsubscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()