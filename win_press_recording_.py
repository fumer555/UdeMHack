import subprocess
import signal
import os

class AudioRecorder:
    def __init__(self, device="Microphone (Realtek Audio)"):
        self.device = device
        self.process = None
        self.output_file = None

    def start_recording(self, filename):
        """
        启动录音。
        """
        self.output_file = filename
        command = [
            "ffmpeg",
            "-f", "dshow",
            "-i", f"audio={self.device}",
            "-ar", "44100",  # Set sample rate to 44.1 kHz (CD quality)
            "-ac", "1",  # Set number of channels to 1 (mono)
            self.output_file
        ]
        self.process = subprocess.Popen(command)
        print(f"Recording started: {filename}")

    def stop_recording(self):
        """
        停止录音。
        """
        if self.process:
            # self.process.send_signal(signal.SIGINT)  # 发送中断信号停止录音
            # self.process.wait()                     # 等待进程结束
            # print(f"Recording stopped: {self.output_file}")
            # self.process = None
            # self.process.terminate()  # 先尝试终止
            # self.process.wait()
            # subprocess.run(["pkill", "-f", "arecord"])  # 确保没有残留进程
            # print(f"Recording stopped: {self.output_file}")
            # self.process = None
            self.process.terminate()  # 发送 SIGTERM，正常结束进程
            self.process.wait()        # 确保进程结束
            print(f"Recording stopped: {self.output_file}")
            self.process = None