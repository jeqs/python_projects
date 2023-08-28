from gtts import gTTS 
import os
from newspaper import Article

news = Article("https://www.nytimes.com/2023/07/14/us/politics/defense-bill-house-ndaa.html")
news.download()
news.parse()
print(news.title)

text_speech = gTTS(text=news.title, lang='en', slow=False)
text_speech.save("nytimes_defense-bill-house-ndaa.mp3")
os.system("start nytimes_defense-bill-house-ndaa.mp3")