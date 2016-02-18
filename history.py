import praw
from collections import Counter
import sys



def breakdown_user_comments(username, thing_limit = 100):
    user_agent = "breakdown of subreddit posts"
    r = praw.Reddit(user_agent=user_agent)

    user = r.get_redditor(username)

    c = user.get_comments(limit = thing_limit)


    def countit(comments):
        output = []
        for x in comments:
            output.append(str(x.subreddit))
        cnt = Counter()
        for x in output:
            cnt[x] +=1 

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
#test
#breakdown_user_comments('CATfixer', thing_limit = 100)
def main():
    if len(sys.argv) <2:
        print 'Error: Must pass a username when running script'
    elif len(sys.argv) == 2:
       # print "History of {} for max 100 comments:\n".format(sys.argv[1])
        breakdown_user_comments(sys.argv[1])

    elif len(sys.argv) == 3:
        #print "History of {} for last {} comments:\n".format(sys.argv[1], sys.argv[2])
        breakdown_user_comments(sys.argv[1], int(sys.argv[2]))
    else:
        print 'Error: too many arguments running with first 2...\n'
        breakdown_user_comments(sys.argv[1], sys.argv[2])



if __name__== '__main__':
    main()
