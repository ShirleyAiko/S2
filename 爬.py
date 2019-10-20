import jieba
import numpy
import re
import pandas as pd  
import matplotlib.pyplot as plt
from urllib import request
from bs4 import BeautifulSoup as bs
import matplotlib
from wordcloud import WordCloud

matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)

def getComments(pageNum): 
    
    """
    A function to get movie comments
    input: page number of movie comments
    output: each comment list
    
    """
    eachCommentList = [] # An empty list of each comment list
    
    # A reminder for the user to input proper page numbers
    if pageNum>0: 
         start = (pageNum-1) * 20 
    else: 
        return False 
    
    requrl = 'https://movie.douban.com/subject/26426056/comments' +'?' +'start=' + str(start) + '&limit=20' # The actual website for movie comments
    print(requrl)
    resp = request.urlopen(requrl) 
    html_data = resp.read().decode('utf-8') 
    soup = bs(html_data, 'html.parser') 
    comment_div_lits = soup.find_all('div', class_='comment')
    
    # paraphrase source code and add the result(each comment) into eachCommentList
    for item in comment_div_lits: 
        if item.find_all('p')[0].string is not None:     
            eachCommentList.append(item.find_all('span', class_='short')[0].string)
    
    return eachCommentList

def main():
    
    """
    main programme that supports the whole work
    input: none
    ouput: the wordcloud of Maleficent: Mistress of Evil movie reviews
    
    """
    filehandle = open("WS.txt", "w") # A file that stores comments; open to write
    commentList = [] # A list to store comments
    
    # repeat twenty times to acquire movie comments
    for i in range(20):    
        num = i + 1 
        commentList_temp = getComments(20)
        commentList.append(commentList_temp) #add comments into commentList

    # Change item in list into type STRING
    comments = ''
    for i in range(len(commentList)):
        comments = comments + (str(commentList[i])).strip()
    
    filehandle.write(comments) # write in comments
    filehandle.close()

    # Erase puntuation
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comments)
    cleaned_comments = ''.join(filterdata)

    # Divide by Jieba
    segment = jieba.lcut(cleaned_comments)
    words_df=pd.DataFrame({'segment':segment})

    # Erase Stopwords
    stopwords = pd.read_csv("stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')#quoting=3全不引用
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

    # generate word frequency
    words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
    words_stat = words_stat.reset_index().sort_values(by=["计数"],ascending=False)
    
    # use word cloud to show word frequency
    wordcloud = WordCloud(font_path="simhei.ttf",background_color="white",max_font_size=80)
    word_frequence = {x[0]:x[1] for x in words_stat.head(1000).values}

    word_frequence_list = []
    for key in word_frequence:
        temp = (key,word_frequence[key])
        word_frequence_list.append(temp)

    wordcloud=wordcloud.fit_words(word_frequence_list)
    plt.imshow(wordcloud)

main()