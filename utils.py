import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def summarize_file(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read(3000)
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ты помощник, который делает краткое содержание учебных материалов."},
                {"role": "user", "content": f"Сделай краткое содержание этого текста:\n\n{content}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Ошибка:", e)
        return None
