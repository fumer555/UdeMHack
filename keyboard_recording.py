from pynput import keyboard
import time

space_pressed = False  # 用于记录空格键的状态

def on_press(key):
    global space_pressed
    if key == keyboard.Key.space and not space_pressed:
        print(f"[{time.time()}] Key pressed: SPACE")
        space_pressed = True  # 标记空格键已按下

def on_release(key):
    global space_pressed
    if key == keyboard.Key.space:
        print(f"[{time.time()}] Key released: SPACE")
        space_pressed = False  # 标记空格键已释放

if __name__ == "__main__":
    try:
        # 启动监听器
        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()

        print("Listening for keyboard events. Hold SPACE to see behavior.")
        
        # 轮询检测长按状态
        while True:
            if space_pressed:
                print(f"[{time.time()}] SPACE is being held.")
            time.sleep(0.1)  # 限制打印频率
    except KeyboardInterrupt:
        print("\nListener stopped by user.")
