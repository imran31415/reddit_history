# reddit_history

Get a breakdown of a users comments by subreddit in the terminal.

### Example

Example breakdown of Zach Braff's commenting:

`$ python history.py zachinoz`
```
Total comments analyzed: 100

Summary for zachinoz: 

photoshopbattles: 1.0%  
movies: 2.0%            |
funny: 8.0%             ||||
IAmA: 89.0%             ||||||||||||||||||||||||||||||||||||||||||||||||||
```

By default 100 (most recent I think) comments are analized. To analize more, use the -c flag or --count option:

`$ python history.py zachinoz -c 1000`
```
Total comments analyzed: 319

Summary for zachinoz: 

IAmA: 81.0%             ||||||||||||||||||||||||||||||||||||||||||||||
television: 0.0%        
funny: 8.0%             ||||
videos: 4.0%            ||
photoshopbattles: 0.0%  
AskReddit: 1.0%         
WTF: 2.0%               |
pics: 1.0%              
movies: 3.0%            |
```