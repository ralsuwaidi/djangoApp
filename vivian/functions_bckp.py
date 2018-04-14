import praw

def reddit(value):
    story={}
    reddit = praw.Reddit(client_id='T1mKRsAWXfGfzA',
                         client_secret='9I0sxWA2kmIDi4TIaP7LLvON0zA',
                         user_agent='my user agent')

                         #print(reddit.read_only)  # Output: True

    stickies = [reddit.subreddit("writingprompts").sticky(i).id for i in range(1,4)]

    for submission in reddit.subreddit('writingprompts').hot(limit=4):
        if submission.id not in stickies:
            if value=="show title":
                return(submission.title)  # Output: the submission's title
            if value =='show score':
                return(submission.score)  # Output: the submission's score
            #print(submission.id)     # Output: the submission's ID
            #print(submission.url)
            #print(submission.comments)    # Output: the URL the submission points to
            top_comment = [comment.body for comment in submission.comments if (hasattr(comment, "body") and comment.distinguished==None)][0]
            story[submission.title]=top_comment
            if value=="show comment":
                return(top_comment)
    if value=="show as story":
        return(story[submission.title])
    if value=="show as title":
        return(story)
