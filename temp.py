# main.py

from recording import record_audio
from set_env import set_env
from conversation import conversation
from audio2word import transcribe_audio, print_text
from convert_online_gtts import play_english, play_chinese
import time
import os

if __name__ == "__main__":


    # 使用录音函数
    record_audio("active_audio.wav", 5, "hw:3,0")  # 录制 5 秒音频
    set_env()
    # print(os.environ.get("OPENAI_API_KEY"))
    # time.sleep(10)
    prompt = transcribe_audio()
    print(f"User: {prompt}")
    answer = conversation(prompt)
    print(f"gpt-4o: {answer}")
    play_chinese(answer)