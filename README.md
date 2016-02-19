# reddit_history

Get a breakdown of a users comments by subreddit in the terminal.

### Example

Example breakdown of Zach Braff's commenting:

`$ python history.py zachinoz`
```
Total comments analyzed: 100

Summary for zachinoz: 

movies: 2.0%             ▀
funny: 8.0%              ▀▀▀▀
IAmA: 89.0%              ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
photoshopbattles: 1.0%   

```

By default 100 (most recent I think) comments are analized. To analize more, use the -c flag or --count option:

`$ python history.py zachinoz -c 1000`
```
Total comments analyzed: 319

Summary for zachinoz: 

hotoshopbattles: 0.31%  
funny: 7.52%             ▀▀▀▀
television: 0.31%        
videos: 4.39%            ▀▀
movies: 2.82%            ▀
IAmA: 80.88%             ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
WTF: 1.57%               
pics: 0.94%              
AskReddit: 1.25%         
```