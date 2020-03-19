from bs4 import BeautifulSoup
import requests
import re
import json
import datetime, time

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
        
    print(api_link)
    request_object = requests.get(api_link).text
    json_data = json.loads(request_object)
    result = json_data['result']
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
    request_object = requests.get(api_link_1).text
    json_data = json.loads(request_object)
    result = json_data['result']
    user_rating = []
    # label = []
    for item in result:
        temp = {}
        temp['contestId'] = item['contestId']
        temp['contestName'] = item['contestName']
        temp['rank'] = item['rank']
        temp['y'] = item['newRating']
        date = datetime.datetime.fromtimestamp(item['ratingUpdateTimeSeconds'])
        temp['label']="{}".format(date.strftime("%m-%Y"))
        temp['ratingChange'] = item['newRating']-item['oldRating']
        user_rating.append(temp)
    return (user_rating)