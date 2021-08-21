
# -*- coding: utf-8 -*-
"""
@author: Sahibzada Salman
"""

from flask import Flask, render_template
from newsapi import NewsApiClient
import requests



app = Flask(__name__)                   ## http://127.0.0.1:5000/  for USA news
                                        ## http://127.0.0.1:5000/bbc for BBC News
                                        ## http://127.0.0.1:5000/reddit for getting news from reddit

@app.route('/')         ##Getting top headlines from the US 
def Index():
    newsapi = NewsApiClient(api_key="a3374fd7f3e94155b0123501f2717351") ## api key from NewsApi Website
    topheadlines = newsapi.get_top_headlines(country="us", q = 'news')    ## Top headlines from USA, q for  searching in this case q is set to new 


    articles = topheadlines['articles']         ## Extracting articles from the top headlines
    
    headline = []           # creating empty lists to store the information as mentioned in the assessment
    link = []           
    source = []     
    a = 'NewsApi'             
    
   
    for i in range(len(articles)):          ## Creating for loop to extract the required information from all articles
        myarticles = articles[i]


        headline.append(myarticles['title'])
        link.append(myarticles['url'])
        source.append(a)
        



    mylist = zip(headline, link, source)        #Combining all lists into single


    return render_template('USA.html', context = mylist)  ## this will render the html file which will show the 
                                                            ## required content on our webpage

@app.route('/bbc')          ##Getting top headlines from BBC News
def bbc():
    newsapi1 = NewsApiClient(api_key="a3374fd7f3e94155b0123501f2717351")   ##   Same api key from the NewsApi
    topheadlines1 = newsapi1.get_top_headlines(sources="bbc-news")  ##getting top headlines from BBC news

    articles1 = topheadlines1['articles']       ## Extracting the articles from the top headlines

    headline1 = []                      ## empty lists to group all the relevant headlines, links and sources 
    link1 = []
    source1 = []
    a1 = 'NewsApi'
    for j in range(len(articles1)):     ## reading and extracting headline, link and source info from the articles 
        myarticles1 = articles1[j]

        headline1.append(myarticles1['title'])
        link1.append(myarticles1['url'])
        source1.append(a1)
    

    mylist1 = zip(headline1, link1, source1)        ## Grouping all the lists into singe 

    return render_template('BBC-NEWS.html', context=mylist1)     ##rendering the html file to show the extracted content 
                                                            ## on the web page "/bbc"




@app.route('/reddit')   ##Getting top News from Reddit

def reddit():
    subreddit = 'news'    ##Sub category from the Reddit website, we have selected "news" because of the requirements
    limit = 100         ## maximum of 100 news will be retrieved 
    timeframe = 'day' ## hour, day, week, month, year, all
    listing = 'new' ## controversial, best, hot, new, random, rising, top ##we can select any of the type mentioned 
                    ## this implies 100 new news of the day will be retrieved from the reddit website
     
    def get_reddit(subreddit,listing,limit,timeframe):  ##function to extract the infos
        try:                                        ## will try to retirive news from the mentioned url in json format
            base_url = f'https://www.reddit.com/r/{subreddit}.json?limit={limit}&t={timeframe}'
            request = requests.get(base_url, headers = {'User-agent': 'yourbot'})  ## sending request
        except:                                     ## the above code will run and constantly update news unless 
            print('An Error Occured')               ## an error occus
        return request.json()                       ## will return request in json format 
     
    r = get_reddit(subreddit,listing,limit,timeframe)   ## now calling the above function and according the data provided
    
    news = r['data']['children']            ## extracting relevant info from the retrieved news
    # news = news[0]
    # news = news['data']

    title2 = []                     ## again empty arrays to store the required fields
    link2 = []
    Source2 = []
    headline2 = []
    ss = []
    
    for z in range (len(news)):     #using for loop to extract required information from the retrieved news 
        mynews = news[z]
        #mynews = mynews[0]
        mynews = mynews['data']
        ti = mynews['title']                ## title will store the headline of the news
        li = mynews['url']                  ## link of the news
        he = mynews['selftext']             ## description of the news
        source = 'Reddit'                   ## source of the news which is Reddit ofcourse
        title2.append(ti)
        link2.append(li)                    ## Appending each extracted headline, link and source in their respective lists
        headline2.append(headline2)
        Source2.append(source)   
        
        
    reddit_list = zip(title2, link2, headline2, Source2)    ## again combining all the lists using zip()
    
    return render_template('reddit.html', context=reddit_list)  ## Now this will render the reddit html file and our zipped list

if __name__ == "__main__":      ## will run only if the file is directly run and not imported
    app.run(debug=True)         ## Run the app and if there is an eroor debug = True will show the details of that error
    
    
    
    ############################## Thank You ########################
    
