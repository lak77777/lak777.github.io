import google.generativeai as genai
import os
from datetime import datetime

# 설정
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def generate():
    # 영어로 '사소하지만 중요한 문제 해결 팁' 요청
    prompt = """
    Write a helpful blog post in English about 'Small but Essential Life Hacks or Problem-Solving Tips'. 
    Focus on practical solutions for everyday minor issues (e.g., tech tips, organizing, or productivity). 
    The post should be professional, at least 1,500 words, including:
    1. A catchy title.
    2. An introduction.
    3. 3-4 subheadings with detailed explanations.
    4. A conclusion.
    Format everything in Markdown for a Jekyll blog.
    """
    response = model.generate_content(prompt)
    
    now = datetime.now().strftime('%Y-%m-%d-%H-%M')
    filename = f"_posts/{now}-post.md"
    
    # 지킬(Jekyll) 헤더 설정
    header = f"---\nlayout: post\ntitle: \"Daily Tip: {now}\"\n---\n\n"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(header + response.text)

if __name__ == "__main__":
    generate()
