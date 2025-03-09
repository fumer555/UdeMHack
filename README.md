## VocalDoc: An AI-Powered Voice Health Assistant

### Project Overview
This project introduces a health assistant that takes in users' vocal input, analyzes the provided symptoms and 
provides possible disease name as a response. 

### Repositories Content
- **`audio2word.py`**: Converts speech to text using **OpenAI Whisper**.
- **`conversation.py`**: AI symptom analysis using **GPT-4**.
- **`conversation_ds.py`**: AI symptom analysis using **DeepSeek AI**.
- **`convert_online_gtts.py`**: Converts text-based diagnosis into speech.
- **`main.py`**: The core script that records, processes, and plays back the diagnosis.
- **`press_recording.py`**: Manages the voice recording process.
- **`set_env.py`**: Loads API keys from the `.env` directory.


### Installation

#### 1. Clone the project
Download the Project as a Zip File or Clone the Repository

#### 2. Install dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

#### 3.Run the assistant
To use GPT-4 for AI diagnosis:
```bash
python main.py --model gpt-4o
```
To use DeepSeek AI instead:
```bash
python main.py --model deepseek
```


