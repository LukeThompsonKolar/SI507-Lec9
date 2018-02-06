
from requests_oauthlib import OAuth1Session
import secrets
import json
import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

search = sys.argv[1]

client_key = secrets.client_key
client_secret = secrets.client_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':search}
r = oauth.get(protected_url, params=params)
#print (r.text)

tweets = json.loads(r.text)

for d in tweets["statuses"]:
	print("{}:\n{}\n".format(d["user"]["name"],d["text"]))