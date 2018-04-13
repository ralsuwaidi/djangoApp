import praw
from .models import Writingprompt

def reddit(value):
    story={}
    reddit = praw.Reddit(client_id='T1mKRsAWXfGfzA',
                         client_secret='9I0sxWA2kmIDi4TIaP7LLvON0zA',
                         user_agent='my user agent')

                         #print(reddit.read_only)  # Output: True

    stickies = [reddit.subreddit("writingprompts").sticky(i).id for i in range(1,4)]

    for submission in reddit.subreddit('writingprompts').hot(limit=4):
        if submission.id not in stickies:
            top_comment = [comment.body for comment in submission.comments if (hasattr(comment, "body") and comment.distinguished==None)][0]
            Writingprompt.objects.create(title=submission.title, comment=top_comment, score=submission.score)
    if value=="show as story":
        return(Writingprompt.objects)
