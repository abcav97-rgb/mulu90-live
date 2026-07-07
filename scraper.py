import requests
import re

# 1. ጨዋታው ያለበት ዋና ገጽ
url = "https://a13.kora-plus.app/live/max2"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://a13.kora-plus.app/"
}

try:
    # ገጹን አንብቦ ቶከኑን መፈለግ
    response = requests.get(url, headers=headers, timeout=10)
    html = response.text
    
    # በኮዱ ውስጥ ያለውን የ .m3u8 ሊንክ ከነቶከኑ መፈለፊያ (Regex)
    match = re.search(r'(https://[^\s"\']+\.m3u8\?token=[^\s"\']+)', html)
    
    if match:
        live_link = match.group(1)
        # አፕክሪየተር በቀጥታ እንዲያጫውተው Headers መግለጫ መጨመር
        formatted_link = f"{live_link}|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36&Referer=https://a13.kora-plus.app/&Origin=https://a13.kora-plus.app"
        
        # M3U ፕሌይሊስት ፋይል መጻፍ
        m3u_content = f"#EXTM3U\n#EXTINF:-1,Mulu 90 Live\n{formatted_link}"
        
        with open("live.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("M3U Playlist successfully updated!")
    else:
        print("Token or M3U8 link not found in HTML.")
except Exception as e:
    print(f"Error occurred: {e}")
