from collections import Counter
import sys
import praw
import argparse
from getscreensize import get_terminal_size

# Parse parameters/arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help="Add extra output to help debug a problem", action="store_true")
parser.add_argument("username", help="The reddit username (without /u/)")
parser.add_argument("-c", "--count", help="The number of comments to fetch", type=int)
args = parser.parse_args()

# Assign arguments to variables
debug = True if args.debug else False
username = args.username
count = args.count


def breakdown_user_comments(username, thing_limit=100):
    user_agent = "Breakdown of users comments by subreddit"
    r = praw.Reddit(user_agent=user_agent)
    user = r.get_redditor(username)
    comments = user.get_comments(limit=thing_limit)

    def countit(comments):
        output = []
        try:
            for x in comments:
                output.append(str(x.subreddit))
        except praw.errors.NotFound:
            print("User not found, maybe deleted?")
            sys.exit()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        if debug:
            print('output:', output)

        # Add up the number of posts in each subreddit
        cnt = Counter()
        for x in output:
            cnt[x] += 1
        if debug:
            print('cnt:', cnt)
        return cnt

    result = countit(comments)
    total = sum(result.values())

    print('Total comments analyzed: {}'.format(total))
    output = []

    percentage_breakdown = {k:round((float(v)/float(total)), 2) for k, v in result.items()}
    if debug:
        print("percentage_breakdown:", percentage_breakdown)

    max_subreddit_length = 0
    for k,v in percentage_breakdown.items():
        if len(k) > max_subreddit_length:
            max_subreddit_length = len(k)
        output.append(["{}: {}%".format(k, v * float(100)), v])
    if debug:
        print("max_subreddit_length", max_subreddit_length)
        print("output:", output)
    print("\nSummary for {}: \n".format(username))
    terminal_width = get_terminal_size()[0]
    if debug:
        print('terminal width:', terminal_width)
    for row in output:
        print(row[0].ljust(max_subreddit_length + 7) + ' ' + '|' * int((row[1] * (terminal_width - (max_subreddit_length + 7)))))


def main():
    # If a count is specified, use that, else use 100
    if count is not None:
        breakdown_user_comments(username, count)
    else:
        breakdown_user_comments(username)


if __name__== '__main__':
    main()
