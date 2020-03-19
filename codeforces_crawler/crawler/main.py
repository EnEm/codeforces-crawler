from bs4 import BeautifulSoup
import requests
import re
import json
import datetime, time
from collections import Counter
import numpy as np

# def profile(username):
#     source = requests.get('https://codeforces.com/profile/'+username).text
#     soup = BeautifulSoup(source,'lxml')
#     for tag in soup.find_all("div", class_="user-rank"):
# 	    category = tag.find("span").text
#         # return category
    
    
def crawler_1(users):
    api_link = 'https://codeforces.com/api/user.info?handles='
    i = 0
    for j in range(len(users)):
        if i > 0:
            api_link += ';'
        api_link += users[j]
        i += 1
        
    #print(api_link)
    load = json.loads(requests.get(api_link).text)
    result = load['result']
    username = []
    dp = []
    rank = []
    for j in range(len(users)):
        username.append(result[j]['handle'])
        dp.append(result[j]['titlePhoto'])
        rank.append(result[j]['rank'])
    return (username, rank, dp)

def crawler_2(user):
    api_link_1 = 'https://codeforces.com/api/user.rating?handle={}'.format(user)
    load = json.loads(requests.get(api_link_1).text)
    result = load['result']
    user_rating = []
    # label = []
    for item in result:
        temp = {}
        temp['contestId'] = item['contestId']
        temp['contestName'] = item['contestName']
        temp['rank'] = item['rank']
        temp['y'] = item['newRating']
        #date = datetime.datetime.fromtimestamp(item['ratingUpdateTimeSeconds'])
        temp['x']=item['ratingUpdateTimeSeconds']*1000
        temp['ratingChange'] = item['newRating']-item['oldRating']
        user_rating.append(temp)
    return (user_rating)

def crawler_3(user):
    api_link = 'https://codeforces.com/api/user.status?handle={}&from=1&count=6000'.format(user)
    load = json.loads(requests.get(api_link).text)
    result = load['result']
    virtual = []
    contest = []
    unofficial = []
    practice = []
    for item in result:
        if item['verdict'] != 'OK' or 'rating' not in item['problem']:
            continue
        if item['author']['participantType'] == 'VIRTUAL':
            virtual.append(item['problem']['rating'])
        elif item['author']['participantType'] == 'CONTESTANT':
            contest.append(item['problem']['rating'])
        elif item['author']['participantType'] == 'OUT_OF_COMPETITION':
            unofficial.append(item['problem']['rating'])
        else :
            practice.append(item['problem']['rating'])

    virtual = np.bincount(np.array(virtual).astype(np.int64))
    contest = np.bincount(np.array(contest).astype(np.int64))
    unofficial = np.bincount(np.array(unofficial).astype(np.int64))
    practice = np.bincount(np.array(practice).astype(np.int64))
    for i in range(len(virtual), 4000):
        np.append(virtual,0)
    for i in range(len(contest), 4000):
        np.append(contest,0)
    for i in range(len(unofficial), 4000):
        np.append(unofficial, 0)
    for i in range(len(practice), 4000):
        np.append(practice, 0)
    print(virtual[1500])
    print(contest[1500])
    print(unofficial[1500])
    print(practice[1500])
    return (virtual, contest, unofficial, practice)