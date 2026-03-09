import google.generativeai as genai
import os
from datetime import datetime

# 1. 제미나이 설정
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_post():
    # 2. 외국인 타겟 실용 팁 프롬프트 (SEO 강화)
    prompt = """
    Write a high-quality blog post in English for a global audience.
    Topic: A practical and clever 'Life Hack' (e.g., household shortcuts, tech productivity, or money-saving tips).
    
    Target Audience: Global readers looking for quick, effective solutions.
    
    Requirements:
    1. Title: Create a search-friendly title (e.g., '5 Genius Ways to...', 'How to... Like a Pro').
    2. Introduction: Briefly explain the common problem this hack solves.
    3. Body: Provide clear, numbered steps or bullet points. Use natural, engaging English.
    4. Conclusion: Add a final tip or a word of encouragement.
    5. SEO: Include 3-5 relevant keywords naturally throughout the post.
    6. Format: Output MUST be in Jekyll Markdown format with the following Front Matter:
    
    ---
    layout: post
    title: "[Title]"
    date: YYYY-MM-DD HH:MM:SS +0900
    categories: [LifeHacks, PracticalTips]
    tags: [Hacks, Efficiency]
    ---
    """
    
    response = model.generate_content(prompt)
    content = response.text
    
    # 3. 파일 이름 설정
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H%M%S')
    file_name = f"_posts/{date_str}-lifehack-{time_str}.md"
    
    # 4. 저장소의 _posts 폴더에 저장
    os.makedirs("_posts", exist_ok=True)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Global Life Hack Post Created: {file_name}")

if __name__ == "__main__":
    generate_post()
