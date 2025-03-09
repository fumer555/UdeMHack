import subprocess
import signal
import os

class AudioRecorder:
    def __init__(self, device="Microphone (Realtek Audio)"):
        """
        Initialize the AudioRecorder.
        :param device: Name of the audio input device (use the exact name from `ffmpeg -list_devices true -f dshow -i dummy`).
        """
        self.device = device
        self.process = None
        self.output_file = None

    def start_recording(self, filename):
        """
        Start recording audio.
        """
        self.output_file = filename
        command = [
            "ffmpeg",
            "-f", "dshow",  # Use DirectShow for Windows
            "-i", f"audio={self.device}",  # Specify the audio input device
            "-ar", "44100",  # Set sample rate to 44.1 kHz (CD quality)
            "-ac", "1",  # Set number of channels to 1 (mono)
            "-sample_fmt", "s16",  # Set sample format to 16-bit
            self.output_file  # Output file
        ]
        try:
            self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Recording started: {self.output_file}")
            
            # Capture and print ffmpeg's stderr output
            _, stderr = self.process.communicate()
            if stderr:
                print("ffmpeg stderr:", stderr.decode())
        except FileNotFoundError:
            print("Error: ffmpeg not found. Please install ffmpeg and ensure it's in your PATH.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def stop_recording(self):
        """
        Stop recording audio.
        """
        if self.process:
            self.process.terminate()  # Terminate the ffmpeg process
            self.process.wait()  # Wait for the process to finish
            print(f"Recording stopped. File saved as {self.output_file}")
            
            # Debug: Check if the file exists
            if os.path.exists(self.output_file):
                print(f"File {self.output_file} exists and is ready for processing.")
            else:
                print(f"Error: File {self.output_file} was not created.")