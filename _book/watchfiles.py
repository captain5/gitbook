import time,os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 定义事件处理器类
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".md"):
            print(f"文件 {event.src_path} 被修改！")
            os.system("gitbook build")

    def on_created(self, event):
        print(f"文件 {event.src_path} 被创建！")

    def on_deleted(self, event):
        print(f"文件 {event.src_path} 被删除！")

# 设置监控路径
path = "./"# 你要监控的文件夹路径
event_handler = MyHandler()  # 绑定事件处理器
observer = Observer()
observer.schedule(event_handler, path, recursive=True)

# 开始监控
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
