import tweepy

consumer_key = 'consumer key'
consumer_secret = 'consumer secrets'
access_token = 'access token'
access_token_secret = 'access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()

# Follow everyone back
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()


# def NeedHelp(message):
#     return model.predict(message)


# Define keywords
search = 'desanimado hoje foda'
numberOfTweets = 10

phrase = ', tá tudo bem, você precisa de ajuda? Você pode falar com alguém pelo chat do @CVVBrasil em https://www.cvv.org.br/chat/ ou ligando para 188. Fique bem!'

def search_reply():
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            # if NeedHelp(tweet):
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break

    # Follow user who needs help
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            # if NeedHelp(tweet):      
                tweet.user.follow()
        
        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break       

search_reply()

# Retweet ?

# if True: 
#     for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
#         try:
#             #Retweet
#             tweet.retweet()
#             print('Retweeted the tweet')   

#         except tweepy.TweepError as e:
#             print(e.reason)

#         except StopIteration:
#             break

# Favorite tweet

# for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
#     try:
#         #Favorite
#         tweet.favorite()
#         print('Favorited the tweet')   

#     except tweepy.TweepError as e:
#         print(e.reason)

#     except StopIteration:
#         break