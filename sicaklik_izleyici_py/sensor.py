import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SensorDugumu(Node):
    """Her saniye 20-40 °C arasında rastgele sıcaklık üretip yayınlar."""

    def __init__(self):
        super().__init__('sensor')
        self.publisher_ = self.create_publisher(Float32, '/sicaklik', 10)
        self.timer = self.create_timer(1.0, self.zamanlayici_geri_cagrisi)
        self.get_logger().info('Sensör düğümü başlatıldı.')

    def zamanlayici_geri_cagrisi(self):
        mesaj = Float32()
        mesaj.data = random.uniform(20.0, 40.0)
        self.publisher_.publish(mesaj)
        self.get_logger().info(f'Yayınlanan sıcaklık: {mesaj.data:.2f} °C')


def main(args=None):
    rclpy.init(args=args)
    dugum = SensorDugumu()
    try:
        rclpy.spin(dugum)
    except KeyboardInterrupt:
        pass
    finally:
        dugum.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()

