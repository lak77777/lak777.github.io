import google.generativeai as genai
import os
from datetime import datetime

# 1. 제미나이 설정 (깃허브 시크릿에 등록된 API 키 사용)
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_post():
    # 2. 외국인 타겟 & 개별 페이지 노출을 위한 강화된 프롬프트
    prompt = """
    Write a high-quality, SEO-optimized blog post in English for a global audience.
    
    Topic: A practical and clever 'Life Hack' (e.g., household tips, tech shortcuts, or productivity hacks).
    
    Target Audience: Global readers searching on Google for quick solutions.
    
    Requirements:
    1. Title: Create a catchy, search-friendly 'How-to' title.
    2. Content: Explain the problem and provide clear, step-by-step instructions in natural English.
    3. Formatting: You MUST include the following Front Matter at the very top of the post to ensure it renders as an individual page:
    
    ---
    layout: post
    title: "[Insert Your Catchy Title Here]"
    date: YYYY-MM-DD HH:MM:SS +0900
    categories: [LifeHacks]
    tags: [Tips, Efficiency]
    ---
    
    (Then start the body content here...)
    """
    
    # 글 생성
    response = model.generate_content(prompt)
    content = response.text
    
    # 3. 파일 이름 설정 (날짜-제목 형식으로 검색에 유리하게 설정)
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H%M%S')
    
    # _posts 폴더가 없으면 생성
    os.makedirs("_posts", exist_ok=True)
    
    # 파일 저장 (이 파일들이 각각 하나의 웹페이지가 됩니다)
    file_name = f"_posts/{date_str}-hack-{time_str}.md"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"✅ Individual Post Created: {file_name}")

if __name__ == "__main__":
    generate_post()
