import google.generativeai as genai
import os
from datetime import datetime

# 1. 제미나이 설정
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_post():
    # 2. 실용적인 영어 팁을 위한 프롬프트 (영어 블로그 최적화)
    prompt = """
    Write a helpful and practical 'Life Hack' blog post in English.
    
    Topic: Choose one specific, small but essential life hack (e.g., how to remove stains, organization tips, tech shortcuts, etc.)
    
    Requirements:
    1. Language: Perfect English.
    2. Title: Catchy and search-friendly (e.g., "How to...", "5 Minutes to...").
    3. Structure: 
       - Introduction (Why this is useful)
       - Step-by-step instructions or tips
       - Conclusion
    4. Format: Jekyll Markdown with Front Matter.
    5. SEO: Include relevant keywords naturally.
    
    Format:
    ---
    layout: post
    title: "[Your Catchy Title Here]"
    date: YYYY-MM-DD HH:MM:SS +0900
    categories: [LifeHacks, Tips]
    ---
    (Content starts here...)
    """
    
    response = model.generate_content(prompt)
    content = response.text
    
    # 3. 파일 이름 만들기 (날짜-시간.md)
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H%M%S')
    file_name = f"_posts/{date_str}-tip-{time_str}.md"
    
    # 4. _posts 폴더에 저장
    os.makedirs("_posts", exist_ok=True)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Successful! New English Life Hack posted: {file_name}")

if __name__ == "__main__":
    generate_post()
