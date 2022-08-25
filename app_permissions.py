# -*- coding:utf-8 -*-

import requests
import sys


# 权限查询字典
permissions_dict = {
    "android.permission.ACCESS_CHECKIN_PROPERTIES ": "读取或写入登记check-in数据库属性表的权限",
    "android.permission.WRITE_SETTINGS":"修改系统设置",
    "android.permission.WRITE_EXTERNAL_STORAGE":"读取/修改/删除外部存储内容",
    "android.permission.ACCESS_MOCK_LOCATION":"获取模拟定位信息",
    "android.permission.ACCESS_SURFACE_FLINGER":"访问Surface Flinger:Android平台上底层的图形显示支持:一般用于游戏或照相机预览界面和底层模式的屏幕截图",
    "android.permission.WAKE_LOCK":"阻止设备进入休眠状态",
    "android.permission.ACCOUNT_MANAGER":"获取账户验证信息:主要为GMail账户信息:只有系统级进程才能访问的权限",
    "android.permission.AUTHENTICATE_ACCOUNTS":"允许通过账户验证方式访问账户管理ACCOUNT_MANAGER相关信息",
    "android.permission.BATTERY_STATS":"电量统计",
    "android.permission.BIND_APPWIDGET":"绑定小插件",
    "android.permission.BIND_DEVICE_ADMIN":"绑定设备管理:请求系统管理员接收者receiver:只有系统才能使用",
    "android.permission.BIND_INPUT_METHOD ":"绑定输入法:请求InputMethodService服务:只有系统才能使用",
    "android.permission.BIND_REMOTEVIEWS":"绑定RemoteView:必须通过RemoteViewsService服务来请求:只有系统才能用",
    "android.permission.BIND_WALLPAPER":"绑定壁纸:必须通过WallpaperService服务来请求:只有系统才能用",
    "android.permission.VIBRATE":"控制振动",
    "android.permission.BRICK":"变成砖头:能够禁用手机:非常危险:顾名思义就是让手机变成砖头",
    "android.permission.BROADCAST_PACKAGE_REMOVED":"应用删除时广播",
    "android.permission.BROADCAST_SMS":"收到短信时广播",
    "android.permission.BROADCAST_WAP_PUSH":"WAP PUSH广播",
    "android.permission.SYSTEM_ALERT_WINDOW":"在其他应用之上显示内容",
    "android.permission.CALL_PRIVILEGED":"通话权限:允许程序拨打电话:替换系统的拨号器界面",
    "android.permission.CHANGE_COMPONENT_ENABLED_STATE":"改变组件状态",
    "android.permission.CHANGE_CONFIGURATION":"改变配置:允许当前应用改变配置:如定位",
    "android.permission.SET_WALLPAPER":"设置壁纸",
    "android.permission.CHANGE_WIFI_MULTICAST_STATE":"改变WiFi多播状态",
    "android.permission.CLEAR_APP_CACHE":"清除应用缓存",
    "android.permission.CLEAR_APP_USER_DATA":"清除用户数据",
    "android.permission.CWJ_GROUP":"底层访问权限:允许CWJ账户组访问底层信息",
    "android.permission.CELL_PHONE_MASTER_EX":"手机优化大师扩展权限",
    "android.permission.CONTROL_LOCATION_UPDATES":"控制定位更新:允许获得移动网络定位信息改变",
    "android.permission.DELETE_CACHE_FILES":"删除缓存文件",
    "android.permission.DELETE_PACKAGES":"删除应用",
    "android.permission.DEVICE_POWER":"电源管理",
    "android.permission.DIAGNOSTIC":"应用诊断",
    "android.permission.RESTART_PACKAGES":"允许应用程序杀死其他应用程序的后台进程",
    "android.permission.DUMP":"转存系统信息:允许程序获取系统dump信息从系统服务",
    "android.permission.EXPAND_STATUS_BAR":"状态栏控制:允许程序扩展或收缩状态栏",
    "android.permission.FACTORY_TEST":"工厂测试模式",
    "android.permission.FLASHLIGHT":"使用闪光灯",
    "android.permission.FORCE_BACK":"强制后退:允许程序强制使用back后退按键:无论Activity是否在顶层",
    "android.permission.GET_ACCOUNTS":"访问账户Gmail列表",
    "android.permission.GET_PACKAGE_SIZE":"获取应用大小",
    "android.permission.GET_TASKS":"获取任务信息,允许程序获取当前或最近运行的应用",
    "android.permission.GLOBAL_SEARCH":"允许全局搜索",
    "android.permission.HARDWARE_TEST":"硬件测试:访问硬件辅助设备:用于硬件测试",
    "android.permission.INJECT_EVENTS":"注射事件:允许访问本程序的底层事件:获取按键、轨迹球的事件流",
    "android.permission.INSTALL_LOCATION_PROVIDER":"安装定位提供",
    "android.permission.INSTALL_PACKAGES":"安装应用程序",
    "android.permission.INTERNAL_SYSTEM_WINDOW":"内部系统窗口:允许程序打开内部窗口:不对第三方应用程序开放此权限",
    "android.permission.KILL_BACKGROUND_PROCESSES":"结束后台进程:允许程序调用killBackgroundProcesses(String).方法结束后台进程",
    "android.permission.MANAGE_ACCOUNTS":"管理账户:允许程序管理AccountManager中的账户列表",
    "android.permission.MANAGE_APP_TOKENS":"管理程序引用:管理创建、摧毁、Z轴顺序:仅用于系统",
    "android.permission.MTWEAK_USER":"高级权限:允许mTweak用户访问高级系统权限",
    "android.permission.MTWEAK_FORUM":"社区权限:允许使用mTweak社区权限",
    "android.permission.MASTER_CLEAR":"软格式化:允许程序执行软格式化:删除系统配置信息",
    "android.permission.REORDER_TASKS":"允许应用程序将任务移动到前台和后台",
    "android.permission.MODIFY_PHONE_STATE":"修改手机状态:如飞行模式",
    "android.permission.MOUNT_FORMAT_FILESYSTEMS":"格式化文件系统:格式化可移动文件系统:比如格式化清空SD卡",
    "android.permission.NFC":"允许NFC通讯",
    "android.permission.PERSISTENT_ACTIVITY":"永久Activity:创建一个永久的Activity:该功能标记为将来将被移除",
    "android.permission.PROCESS_OUTGOING_CALLS":"处理拨出电话:允许程序监视:修改或放弃播出电话",
    "android.permission.RECORD_AUDIO":"录音",
    "android.permission.READ_CONTACTS":"读取联系人",
    "android.permission.READ_FRAME_BUFFER":"屏幕截图",
    "com.android.browser.permission.READ_HISTORY_BOOKMARKS":"读取浏览器收藏夹和历史记录",
    "android.permission.READ_INPUT_STATE":"读取输入状态:读取当前键的输入状态:仅用于系统",
    "android.permission.RECEIVE_BOOT_COMPLETED":"开机自动启动",
    "android.permission.READ_SMS":"读取短信内容",
    "android.permission.READ_SYNC_SETTINGS":"读取同步设置",
    "android.permission.READ_SYNC_STATS":"读取同步状态",
    "android.permission.REBOOT":"重启设备",
    "android.permission.RECEIVE_MMS":"接收彩信",
    "android.permission.RECEIVE_SMS":"接收短信",
    "android.permission.RECEIVE_WAP_PUSH":"接收Wap Push",
    "android.permission.READ_PHONE_STATE":"读取电话状态",
    "android.permission.READ_LOGS":"读取系统日志",
    "android.permission.SEND_SMS":"发送短信",
    "android.permission.SET_ACTIVITY_WATCHER":"设置Activity观察器一般用于monkey测试",
    "com.android.alarm.permission.SET_ALARM":"设置闹铃提醒",
    "android.permission.SET_ALWAYS_FINISH":"设置程序在后台是否总是退出",
    "android.permission.SET_ANIMATION_SCALE":"设置全局动画缩放",
    "android.permission.SET_DEBUG_APP":"设置调试程序:一般用于开发",
    "android.permission.SET_ORIENTATION":"设置屏幕方向为横屏或标准方式显示:不用于普通应用",
    "android.permission.SET_PROCESS_LIMIT":"设置进程限制",
    "android.permission.SET_TIME":"设置系统时间",
    "android.permission.SET_TIME_ZONE":"设置系统时区",
    "android.permission.SET_WALLPAPER_HINTS":"设置壁纸建议",
    "android.permission.SIGNAL_PERSISTENT_PROCESSES":"发送永久进程信号",
    "android.permission.STATUS_BAR":"状态栏控制:允许程序打开、关闭、禁用状态栏",
    "android.permission.SUBSCRIBED_FEEDS_READ":"访问订阅内容:访问订阅信息的数据库",
    "android.permission.SUBSCRIBED_FEEDS_WRITE":"写入订阅内容:写入或修改订阅内容的数据库",
    "android.permission.READ_CALENDAR":"读取日程信息",
    "android.permission.UPDATE_DEVICE_STATS":"更新设备状态",
    "android.permission.USE_CREDENTIALS":"使用证书:允许程序请求验证AccountManager",
    "android.permission.USE_SIP":"使用SIP视频",
    "android.permission.MOUNT_UNMOUNT_FILESYSTEMS":"挂载文件系统:挂载、反挂载外部文件系统",
    "android.permission.WRITE_APN_SETTINGS":"写入网络GPRS接入点设置",
    "android.permission.WRITE_CALENDAR":"写入日程提醒:但不可读取",
    "android.permission.WRITE_CONTACTS":"写入联系人:但不可读取",
    "android.permission.WRITE_GSERVICES":"写入Google地图数据",
    "com.android.browser.permission.WRITE_HISTORY_BOOKMARKS":"写入浏览器历史记录或收藏夹:但不可读取",
    "android.permission.WRITE_SECURE_SETTINGS":"读写系统敏感设置:允许程序读写系统安全敏感的设置项",
    "android.permission.MODIFY_AUDIO_SETTINGS":"修改声音设置",
    "android.permission.WRITE_SMS":"编写短信",
    "android.permission.WRITE_SYNC_SETTINGS":"写入在线同步设置:写入Google在线同步设置",
    "android.permission.ACCESS_BACKGROUND_LOCATION":"允许应用在后台访问位置",
    "android.permission.INTERNET":"完全互联网访问",
    "android.permission.DISABLE_KEYGUARD":"允许应用程序在不安全的情况下禁用键盘保护",
    "android.permission.CHANGE_WIFI_STATE":"更改WiFi设置",
    "android.permission.READ_EXTERNAL_STORAGE":"测试对受保护存储空间的访问权限",
    "android.permission.CHANGE_NETWORK_STATE":"改变网络状态",
    "android.permission.REQUEST_INSTALL_PACKAGES":"允许应用程序请求安装包",
    "android.permission.CAMERA":"拍照和录像",
    "android.permission.CALL_PHONE":"直接拨打电话号码",
    "android.permission.BROADCAST_STICKY":"连续广播",
    "android.permission.CAPTURE_VIDEO_OUTPUT":"捕获视频输出",
    "android.permission.BLUETOOTH_ADMIN":"蓝牙管理:允许程序进行发现和配对新的蓝牙设备",
    "android.permission.FOREGROUND_SERVICE":"允许常规应用程序使用 Service.startForeground",
    "android.permission.BLUETOOTH":"使用蓝牙",
    "android.permission.ACCESS_WIFI_STATE":"获取WiFi状态",
    "android.permission.SCHEDULE_EXACT_ALARM":"允许应用使用精确的警报",
    "android.permission.ACCESS_NETWORK_STATE":"获取网络状态",
    "com.huawei.android.launcher.permission.CHANGE_BADGE":"在华为手机的应用程序启动图标上显示通知计数",
    "android.permission.ACCESS_LOCATION_EXTRA_COMMANDS":"访问额外的位置提供程序命令",
    "android.permission.ACCESS_FINE_LOCATION":"获取精确位置(GPS)",
    "android.permission.QUERY_ALL_PACKAGES":"允许查询设备上的任何普通应用程序",
    "android.permission.ACCESS_MEDIA_LOCATION":"访问共享存储空间中的媒体文件",
    "android.permission.ACCESS_GPS":"获得GPS位置",
    "android.permission.ACCESS_NOTIFICATION_POLICY":"访问通知策略的应用程序的标记权限",
    "android.permission.CAPTURE_AUDIO_OUTPUT":"录音",
    "android.permission.ACCESS_COARSE_LOCATION":"获取粗略位置(网络)",
    "android.permission.SYSTEM_OVERLAY_WINDOW:":"悬浮窗权限",
    "android.permission.RECEIVE_USER_PRESENT":"允许程序唤醒设备",
    "android.permission.ACCESS_COARSE_UPDATES":"获取当前移动终端附近移动终端的信息",
    "android.permission.INTERACT_ACROSS_USERS_FULL":"多用户互动",
    "android.permission.BROADCAST_PACKAGE_ADDED":"消息推送相关,大多为厂商通道必需权限",
    "android.permission.BROADCAST_PACKAGE_CHANGED":"消息推送相关,大多为厂商通道必需权限",
    "android.permission.BROADCAST_PACKAGE_INSTALL":"消息推送相关,大多为厂商通道必需权限",
    "android.permission.BROADCAST_PACKAGE_REPLACED":"消息推送相关,大多为厂商通道必需权限",
    "android.permission.ACCESS_LOCATION":"访问定位",
    "ANDROID.PERMISSION.CHANGE_CONFIGURATION":"允许修改当前设置,比如语言种类，屏幕方向",
}


# 根据hash获得扫描结果json
def get_json(key, hash):
    url = 'http://192.168.244.162:8000/api/v1/report_json'
    headers = {'Authorization': key}
    data = {'hash': hash}
    r = requests.post(url, headers=headers, data=data)
    return r.json()


# 根据扫描结果json提取权限数据并匹配中文描述
def get_permissions(json):
    app_name = json['app_name']
    version = json['version_name']
    permissions = json['permissions']
    i = 1
    print(app_name + version + '应用权限:')
    for permission in permissions:
        try:
            describe = permissions_dict[permission]
        except:
            describe = json['permissions'][permission]['description']
        print(str(i) + '.' + permission + ':' + describe)
        i = i + 1


def main():
    key = sys.argv[1]
    hash = sys.argv[2]
    get_permissions(get_json(key, hash))
    

if __name__ == '__main__':
    main()
