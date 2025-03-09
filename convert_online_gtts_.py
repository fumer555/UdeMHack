import os
from gtts import gTTS
from pydub import AudioSegment
from pygame import mixer

def text_to_speech_and_play(text, lang='zh', output_file='output.wav'):
    """
    Full process: Generate speech with gTTS, adjust volume with pydub, and save the file as WAV.
    """
    try:
        # Step 1: Generate speech with gTTS
        tts = gTTS(text=text, lang=lang, slow=False)
        temp_file = "temp_low_mp3.mp3"
        tts.save(temp_file)
        print(f"gTTS audio saved to {temp_file}.")

        # Step 2: Load and adjust volume with pydub
        audio = AudioSegment.from_file(temp_file)
        print(f"Loaded audio file: {temp_file}")
        louder_audio = audio + 8  # Increase volume
        louder_audio.export(output_file, format="wav")
        print(f"Processed audio saved to {output_file}.")

        # 播放生成的音频文件
        print("Playing audio...")
        mixer.init()
        mixer.music.load(output_file)
        mixer.music.play()
        while mixer.music.get_busy():  # Wait for playback to finish
            pass

    except Exception as e:
        print(f"Error during processing: {e}")

def play_english(text):
    text_to_speech_and_play(text, lang='en', output_file='english.wav')

def play_chinese(text):
    text_to_speech_and_play(text, lang='zh', output_file='chinese.wav')

# 示例调用
if __name__ == "__main__":
    play_chinese("你好，世界")
    play_english("Hello, world")