import subprocess

def record_audio(filename, duration, device="hw:3,0"):
    """
    使用 arecord 从指定设备录制音频。
    :param filename: 保存的文件名
    :param duration: 录音时长（秒）
    :param device: 音频设备标识，默认 hw:3,0
    """
    command = [
        "arecord",
        "-D", device,           # 指定设备
        "-f", "cd",             # 设置 CD 质量录音 (44100 Hz, 16 位, 立体声)
        "-c", "1",              # 单声道
        "-d", str(duration),    # 设置录音时长
        filename                # 输出文件名
    ]
    try:
        print(f"Recording {duration} seconds of audio to {filename}...")
        subprocess.run(command, check=True)  # 执行命令
        print("Recording complete.")
    except subprocess.CalledProcessError as e:
        print(f"Error during recording: {e}")
    except FileNotFoundError:
        print("arecord command not found. Please make sure ALSA is installed.")

if __name__ == "__main__":
    record_audio("test.wav", 10, "hw:3,0")  # 调用函数，录音 10 秒
