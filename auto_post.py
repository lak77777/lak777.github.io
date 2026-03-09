import google.generativeai as genai
import os
from datetime import datetime

# 1. 제미나이 설정
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_post():
    # 2. 영어 실용 팁 작성을 위한 명령 (프롬프트)
    prompt = """
    Write a practical and helpful 'Life Hack' blog post in English.
    
    Topic: Choose a useful tip (e.g., home organization, cleaning, tech shortcuts, or daily productivity).
    
    Requirements:
    1. Language: English only.
    2. Title: A catchy 'How-to' title for SEO.
    3. Content: Explain the problem and provide a clear, step-by-step solution.
    4. Format: Jekyll Markdown with Front Matter.
    
    Example Format:
    ---
    layout: post
    title: "How to Keep Your Coffee Hot Longer"
    date: YYYY-MM-DD HH:MM:SS +0900
    categories: [LifeHacks, Tips]
    ---
    (Content starts here...)
    """
    
    response = model.generate_content(prompt)
    content = response.text
    
    # 3. 파일 이름 설정 (날짜-시간.md)
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H%M%S')
    file_name = f"_posts/{date_str}-tip-{time_str}.md"
    
    # 4. _posts 폴더 생성 및 저장
    os.makedirs("_posts", exist_ok=True)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Success: {file_name} has been created.")

if __name__ == "__main__":
    generate_post()
