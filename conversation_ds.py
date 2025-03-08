import os
from openai import OpenAI

def conversation(input_text):
    """
    使用 OpenAI API 进行对话，并限制回答为 5 个单词以内。
    :param input_text: 用户输入内容
    :return: 模型的回复
    """
    # 确保 API 密钥已设置
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("DEEPSEEK_API_KEY is not set in environment variables.")
    
    client = OpenAI(
        api_key=os.environ.get("DEEPSEEK_API_KEY"), 
        base_url="https://api.deepseek.com", 
    )

    try:
        # 调用 OpenAI Chat Completion API
        chat_completion = client.chat.completions.create(
            model="deepseek-chat",  # 使用 GPT-4 模型
            messages=[
                {"role": "system", "content": "Answer in English, be concise: in less than 50 words"},
                {"role": "user", "content": input_text}
            ],
            max_tokens=30,  # 限制返回的 Token 数
        )
        
        # 获取回复内容
        response = chat_completion.choices[0].message.content.strip()


        return response
    except Exception as e:
        return f"Error: {e}"

# 示例调用
if __name__ == "__main__":
    user_input = "Tell me something about AI."
    reply = conversation(user_input)
    print(f"Model reply: {reply}")
