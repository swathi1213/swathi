import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "jYE7ES66UefUWL7HCbowpHUEM",
    "consumer_secret"     : "FlNbLoTCKjiprMjVggjaLyclOvgzbqPqAOgLSLQDYWHaJFEVfa",
    "access_token"        : "966203062892290048-6zh3Argqd6LYCZvPwa9edpCbqFTxNvr",
    "access_token_secret" : "Q0Unr4w2S4R7W4GHNHwzNMJiWOBDAu33mHemhZm7XBdbW"
 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
