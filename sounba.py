from urllib import quote_plus
import praw

QUESTIONS = ['thread']
REPLY_TEMPLATE = '**HD** |  [ NBA  Stream   720p ](http://www.sportstreamsgalaxy.xyz/2019/03/newcastle-united-vs-everton.html) | MISR:1mbps |  Clicks:2 | Mobile: Yes | English'



def main(): 
    reddit = praw.Reddit(user_agent='istream4all (by /u/istream4all)',
                         client_id='HooTUcj5dKeCpA', client_secret='iUPbliaVhWU2C0fH2Jsiz1mdS54',
                         username='istream4all', password='5119051190Aa')


     
 


    subreddit = reddit.subreddit('nbastreams')
    for submission in subreddit.stream.submissions():
        process_submission(submission)


def process_submission(submission):
    # Ignore titles with more than 10 words as they probably are not simple
    # questions.
    if (((str(submission .author)) == 'NHLStreamsBot') ):
     return

    normalized_title = submission.title.lower()
    for question_phrase in QUESTIONS:
        if question_phrase in normalized_title:
            url_title = quote_plus(submission.title)
            reply_text = REPLY_TEMPLATE.format(url_title)
            print('Replying to: {}'.format(submission.title))
            submission.reply(reply_text)
            # A reply has been made so do not attempt to match other phrases.
            break
     



if __name__ == '__main__':
    main()

