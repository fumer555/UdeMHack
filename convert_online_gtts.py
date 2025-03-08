import os
from gtts import gTTS
from pydub import AudioSegment

def text_to_speech_and_play(text, lang='zh', output_file='output.mp3'):
    """
    将文本转换为语音并播放。
    :param text: 要转换的文本
    :param lang: 语言代码，例如 'zh'（中文）或 'en'（英文）
    :param output_file: 输出文件名
    """
    # 使用 gTTS 生成语音
    tts = gTTS(text=text, lang=lang, slow=False)
    temp_file = "temp_low_mp3.mp3"
    tts.save(temp_file)
    print(f"Audio saved to {output_file}")


    
    # 使用 pydub 调整音量
    volume_increase_db=8
    audio = AudioSegment.from_file(temp_file)
    louder_audio = audio + volume_increase_db  # 增加音量
    louder_audio.export(output_file, format="mp3")
    print(f"Audio saved to {output_file} with increased volume.")

    # 播放生成的音频文件
    try:
        print("Playing audio...")
        if os.name == 'posix':  # Linux 或 macOS
            os.system(f"mpg123 {output_file} || aplay {output_file}")
        elif os.name == 'nt':  # Windows
            os.system(f"start {output_file}")
        else:
            print("Unsupported OS for playback.")
    except Exception as e:
        print(f"Error during playback: {e}")
def play_english(text):
    text_to_speech_and_play(text, lang='en', output_file='output.mp3')

def play_chinese(text):
    text_to_speech_and_play(text, lang='zh', output_file='output.mp3')

# 示例调用
if __name__ == "__main__":
    text_to_speech_and_play("你好，世界", lang='zh', output_file='chinese.mp3')
    text_to_speech_and_play("Hello, world", lang='en', output_file='english.mp3')
