import os

def set_env():
    """
    从文件 ./env/openai_api_key.txt 中读取 OpenAI API 密钥并设置为环境变量。
    """
    try:
        # 打开文件并读取 API 密钥
        with open('./.env/openai_api_key.txt', 'r') as file:
            api_key = file.read().strip()  # 去掉首尾空白字符

        # 设置环境变量
        os.environ["OPENAI_API_KEY"] = api_key
        print("OPENAI_API_KEY has been set successfully.")
    except FileNotFoundError:
        print("Error: File './.env/openai_api_key.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        # 打开文件并读取 API 密钥
        with open('./.env/deepseek_api_key.txt', 'r') as file:
            api_key = file.read().strip()  # 去掉首尾空白字符

        # 设置环境变量
        os.environ["DEEPSEEK_API_KEY"] = api_key
        print("DEEPSEEK_API_KEY has been set successfully.")
    except FileNotFoundError:
        print("Error: File './.env/deepseek_api_key.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        # 打开文件并读取 API 密钥
        with open('./.env/aws_access_key.txt', 'r') as file:
            api_key = file.read().strip()  # 去掉首尾空白字符

        # 设置环境变量
        os.environ["AWS_ACCESS_KEY"] = api_key
        print("AWS_ACCESS_KEY has been set successfully.")
    except FileNotFoundError:
        print("Error: File './.env/aws_access_key.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


    try:
        # 打开文件并读取 API 密钥
        with open('./.env/aws_secret_access_key.txt', 'r') as file:
            api_key = file.read().strip()  # 去掉首尾空白字符

        # 设置环境变量
        os.environ["AWS_SECRET_ACCESS_KEY"] = api_key
        print("AWS_SECRET_ACCESS_KEY has been set successfully.")
    except FileNotFoundError:
        print("Error: File './.env/aws_secret_access_key.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 示例调用
if __name__ == "__main__":
    set_env()
    # 验证设置
    print(f"OPENAI_API_KEY = {os.environ.get('OPENAI_API_KEY')}")
