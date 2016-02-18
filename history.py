from collections import Counter
import sys
import praw
import argparse

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


def breakdown_user_comments(username, thing_limit = 100):
    user_agent = "Breakdown of users comments by subreddit"
    r = praw.Reddit(user_agent=user_agent)
    user = r.get_redditor(username)
    c = user.get_comments(limit = thing_limit)


    def countit(comments):
        output = []
        try:
            for x in comments:
                output.append(str(x.subreddit))
        except praw.errors.NotFound, e:
            print "User not found, maybe deleted?"
            sys.exit()
        else:
            raise e

        cnt = Counter()
        for x in output:
            cnt[x] += 1
        if debug:
            print 'output:', output
            print 'cnd:', cnt
        return cnt

    result = countit(c)
    total = sum(result.values())

    print 'Total comments analyzed: {}'.format(total)
    output = []

    percentage_breakdown = {k:(float(v)/float(total)) for k, v in result.items()}
    for k,v in percentage_breakdown.items():
        output.append(["{}: {}%".format(k, v*float(100)), "{}".format("|"*int(float(100)*float(v)))])
    column_width = max([len(x[0]) for x in output]) +4
    print "\nSummary for {}: \n".format(username)
    for row in output:
        print "".join(word.ljust(column_width) for word in row)


def main():
    # If a count is specified, use that, else use 100
    if count is not None:
        breakdown_user_comments(username, count)
    else:
        breakdown_user_comments(username)


if __name__== '__main__':
    main()
