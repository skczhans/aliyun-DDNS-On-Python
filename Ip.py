import requests
import json
import sys

class Ip:
    @staticmethod
    def get_ipv6_addresses():
        # 主接口和备用接口
        urls = [
            ('http://test6.ustc.edu.cn/backend/getIP.php', 'main'),  # 主接口
            ('https://speed.neu6.edu.cn/getIP.php', 'backup')  # 备用接口
        ]

        for url, interface_type in urls:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"请求成功: {url}")
                try:
                    if interface_type == 'main':
                        
                        # 解析JSON数据
                        data = response.json()
                        # 主接口处理逻辑
                        # 假设主接口返回了键 'processedString'
                        ipv6_address = data.get('processedString')
                    elif interface_type == 'backup':
                        # 备用接口处理逻辑
                        # 假设备用接口返回的数据直接是 IP 地址
                        ipv6_address = response.text
                    return ipv6_address
                except json.JSONDecodeError:
                    print("JSON解析失败")
                    continue  # 尝试下一个接口
            else:
                print(f"请求失败，状态码：{response.status_code}, 接口：{url}")

        print("所有接口请求失败")
        sys.exit(1)  # 非零退出码表示错误

    @staticmethod
    def write_addresses(ipv6_addr):
        # 打开（或创建）文件，准备写入
        with open('output.txt', 'w') as file:
            # 将ipv6_addr的值写入文件
            file.write(ipv6_addr)
        print("结果保存成功")

if __name__ == "__main__":
    try:
        ipv6_addresses = Ip.get_ipv6_addresses()
        print(ipv6_addresses)
        Ip.write_addresses(ipv6_addresses)
    except Exception as e:
        print(f"执行中发生错误：{e}")
        sys.exit(1)  # 确保在遇到未处理的异常时也能退出
