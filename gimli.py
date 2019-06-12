import praw
import re
import secrets

find_and = re.compile(r"^\.*\s*and\b", re.IGNORECASE)
reply = "...and my axe!"
reddit = praw.Reddit(
        user_agent='ruby/praw:gimli_bot:.01 (by /u/_gimli_bot)',
        client_id=secrets.CLIENT_ID,
        client_secret=secrets.CLIENT_SECRET,
        username=secrets.USERNAME, password=secrets.PASSWORD)
submissions = reddit.front.hot(limit=50)

for submission in submissions:
    for comment in submission.comments.replace_more(limit=100).list():
        if comment.author == "_gimli_bot": continue
        if comment.parent_id[0:3] == 't3_': continue
        if find_and.match(comment.body):
        if (find_and.match(comment.body)
        and find_and.match(reddit.comment(comment.parent_id[3:]).body)):
            comment.reply(reply)
            break
