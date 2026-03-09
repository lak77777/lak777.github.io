import google.generativeai as genai
import os
from datetime import datetime

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_post():
    # 구글 상위 노출을 위한 3박자(제목, 본문, 태그) 프롬프트
    prompt = """
    Write a high-quality blog post in English for Google Search top ranking.
    Topic: A unique and practical Life Hack.
    Format:
    ---
    layout: post
    title: "[SEO Friendly Title with Keywords]"
    description: "A short summary of this hack for Google search snippets."
    categories: [LifeHacks]
    ---
    # [Main Topic]
    Write a detailed guide with step-by-step instructions. 
    Use bullet points and bold text for readability.
    """
    
    response = model.generate_content(prompt)
    now = datetime.now()
    os.makedirs("_posts", exist_ok=True)
    
    # 구글 로봇이 좋아하는 파일명 형식
    file_name = f"_posts/{now.strftime('%Y-%m-%d')}-best-hack-{now.strftime('%H%M%S')}.md"
    
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(response.text)

if __name__ == "__main__":
    generate_post()
