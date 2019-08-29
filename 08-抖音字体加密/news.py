from newspaper import Article 

# A new article from TOI 
url = "http://world.people.com.cn/n1/2019/0308/c1002-30964972.html"

# For different language newspaper refer above table 
toi_article = Article(url, language='zh') # zh for China

# To download the article 
toi_article.download()

# To parse the article 
toi_article.parse() 

# To perform natural language processing ie..nlp 
# toi_article.nlp() 

# To extract title 
print("Article's Title:") 
print(toi_article.title) 
print("*"*80)

# To extract text 
print("Article's Text:") 
print(toi_article.text) 
print("*"*80)

# To extract summary 
print("Article's Summary:") 
print(toi_article.summary) 
print("*"*80)


# To extract keywords 
print("Article's Keywords:") 
print(toi_article.keywords) 