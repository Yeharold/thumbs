## thumbs 微信朋友圈自动点赞神器
-----------
-----------
- Linux 平台
 - requirement：pillow
 - adb安装：sudo apt-get install adb
 - 手机：设置为USB可以调试状态，适用1080*1920分辨率屏幕手机，其他需要修改源代码（百度设置adb可对手机操作）
 - 命令：adb devices #查看手机连接状态

----------
示例：
首先解压后  进入解压目录安装：sudo pip install ./
第二步  打开微信朋友圈
---
import thumbs

thumbs.run(20)

---
祝你好运--运行成功
