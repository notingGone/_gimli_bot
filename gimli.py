import praw
from praw.models import Comment
import re
import secrets

find_and = re.compile(r"^\.*\s*and\b", re.IGNORECASE)
reply = "...and my axe!"
reddit = praw.Reddit(
        user_agent='ruby/praw:gimli_bot:.01 (by /u/_gimli_bot)',
        client_id=secrets.CLIENT_ID, client_secret=secrets.CLIENT_SECRET,
        username=secrets.USERNAME, password=secrets.PASSWORD)
submissions = reddit.front.hot(limit=25)
for submission in submissions:
    submission.comments.replace_more(limit=10)
    print("\"" + submission.title + "\"")
    print("submission: " + str(submission.id) + " comments: " + str(submission.num_comments))
    for comment in submission.comments.list():
        #print(reddit.comment(comment.id).body)
        if find_and.match(comment.body):
            #print(comment.parent_id)
            if comment.parent_id[0:3] != 't3_' and find_and.match(reddit.comment(comment.parent_id[3:]).body):
                    print(comment.parent_id)
                    print("REPLYING!!!")
                    comment.reply(reply)
                    next
