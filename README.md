# app_permissions

### 简介
基于MobSF API测试安卓app权限的工具，用于app合规检查，查看敏感权限是否在隐私政策中说明

内置权限对应中文描述的字典，如字典无该条目则采用MobSF英文描述（欢迎补充或纠错）

MobSF传送门:https://github.com/MobSF/Mobile-Security-Framework-MobSF

### 使用方式
apk安卓包丢到MobSF扫描分析后，通过此次扫描的hash值查询
```
python3 app_permissions.py <MobSF api key> <扫描结果hash>
```

### 示例
运行
```
python3 app_permissions.py 02880522857f4ae4943a55b6f960d375fb6655487f24e9ffd0de2054169d3deb 9e8efe63a8119a5108d2f6ea53841de4
```
输出
```
某应用2.0.2应用权限:
1.android.permission.RECEIVE_USER_PRESENT:允许程序唤醒设备
2.android.permission.INTERNET:完全互联网访问
3.android.permission.WAKE_LOCK:阻止设备进入休眠状态
4.android.permission.WRITE_EXTERNAL_STORAGE:读取/修改/删除外部存储内容
5.android.permission.READ_EXTERNAL_STORAGE:测试对受保护存储空间的访问权限
6.android.permission.VIBRATE:控制振动
7.android.permission.ACCESS_NETWORK_STATE:获取网络状态
8.android.permission.ACCESS_WIFI_STATE:获取WiFi状态
9.android.permission.CHANGE_NETWORK_STATE:改变网络状态
10.android.permission.CAMERA:拍照和录像
11.android.permission.RECEIVE_BOOT_COMPLETED:开机自动启动
14.android.permission.MODIFY_AUDIO_SETTINGS:修改声音设置
15.android.permission.BROADCAST_STICKY:连续广播
16.android.permission.SCHEDULE_EXACT_ALARM:允许应用使用精确的警报
```
