# Aliyun DDNS on Python

## 概述
这个项目是在阿里云提供的模板基础上添加一个自动获取当前的IPv6地址的函数，从而简化动态域名解析 (DDNS) 的设置过程。通过借助中科大测速站的功能，我们能够自动获取当前IPv6地址，而不需要手动添加。

## 如何使用

### 1. 准备工作
确保你已经拥有一个阿里云账号，并且已经创建了一个域名解析服务，并且该服务已经配置了相应的域名记录。

### 2. 安装依赖
在运行代码之前，你需要确保你的环境中安装了以下依赖：
- Python 3.x
- 阿里云 Python SDK
- Requests 库

你可以使用以下命令来安装所需的 Python 库：

```bash
pip install requests alibabacloud-tea-console alibabacloud-darabonba-env alibabacloud_alidns20150109
```

### 3. 配置
在开始之前，你需要进行一些配置：
- 在阿里云控制台中创建一个 RAM 用户，并为其分配域名解析的相关权限。然后获取该用户的 Access Key ID 和 Access Key Secret。
- 在环境变量中添加RAM用户的Access Key ID 和 Access Key Secret。添加方法参考[配置环境变量](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)
- 
| 变量 | 示例值 |
|------|--------|
| AccessKey ID | 变量名：ALIBABA_CLOUD_ACCESS_KEY_ID<br>变量值：LTAI4GDty\**\**W4Y1D**** |
| AccessKey Secret | 变量名：ALIBABA_CLOUD_ACCESS_KEY_SECRET<br>变量值：IrVTNZNy5yQe\**\**g0cZML3TQn**** |



### 4. 运行
运行 `sample.py` 文件，它将会获取当前的 IPv6 地址，并更新指定域名的解析记录。

```bash
python sample.py cn-guangzhou 你的域名 主机记录 记录类型
```

## 注意事项
- 请确保你的阿里云账号信息和域名信息配置正确，否则可能导致更新失败。
- 请注意阿里云 API 的调用频率限制，避免频繁调用而触发限制。
- 中科大测速站的稳定性和可用性可能会影响到获取 IPv6 地址的成功率，建议定期检查代码以确保功能正常运行。

## 贡献
如果你发现了任何问题或者有改进建议，欢迎提交 Issue 或者 Pull Request，让我们一起改进这个项目！

## 许可证
本项目采用 GNU Affero General Public License v3.0 许可证。详细信息请参阅 [LICENSE](LICENSE) 文件。
