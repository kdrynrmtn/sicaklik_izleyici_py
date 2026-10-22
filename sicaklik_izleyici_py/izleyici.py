import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class IzleyiciDugumu(Node):
    """/sicaklik konusunu dinler; eşik aşılırsa uyarı verir."""

    def __init__(self):
        super().__init__('izleyici')
        self.declare_parameter('esik_degeri', 30.0)
        self.abonelik = self.create_subscription(
            Float32, '/sicaklik', self.sicaklik_geri_cagrisi, 10)
        self.get_logger().info('İzleyici düğümü başlatıldı.')

    def sicaklik_geri_cagrisi(self, mesaj):
        deger = mesaj.data
        esik = self.get_parameter('esik_degeri').get_parameter_value().double_value
        self.get_logger().info(f'Alınan sıcaklık: {deger:.2f} °C')
        if deger > esik:
            self.get_logger().warn(
                f'UYARI: Sıcaklık {esik:.1f} °C eşiğini aştı! ({deger:.2f} °C)')


def main(args=None):
    rclpy.init(args=args)
    dugum = IzleyiciDugumu()
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
