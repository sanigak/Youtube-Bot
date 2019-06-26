import praw


reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='sanigak')




for submission in reddit.subreddit('askreddit').hot(limit=10):
    print(submission.title)