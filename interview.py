import datetime
cache = [
    {
        "token": "asasfsdfdf",
        "expiration-date":"2024-04-25 14:30:03.588921"
    },
    {
        "token": "asasfsdfde",
        "expiration-date":"2024-04-26 14:30:03.588921"
    },
    {
        "token": "asasfsdfdg",
        "expiration-date":"2024-04-20 14:30:03.588921"
    }
]
"""
   token: expiraition-date
   key: {
        token: asdfadfsdf
        expriation-date: date
   }
   1- The expire function can only be manually run to expire cache, but we want to continuously check if the cache should expire when the time comes. How would you do this?
        Run a cronjob or a schedular to check continuously everyday if the key needs to expire
        
        at 4am everyday check and see if the session needs to expire then run the check_expiration function
        cronjob-time = 0 4 * * * 
        crontab cronjob interview.py

   2- Re - Step 1, when you do this, what rudimentary optimizations could you make to make this more performant? (Checking 100m keys all the time would be really slow)
   when a session token is created have another key called created-at that will record the moment the token is created. Then when the check_expiration function runs you get both the expiration and created at time
   subtract both and if it is less then or equal to 0 you delete it

   look up time for expiration and created-at O(1)

"""
def access(key):
    return cache[key]

def setVal(value):
    key = {
        "token": value,
        "expiration-date": datetime.datetime.now() + datetime.timedelta(days=7),
        "created-at": datetime.datetime.now()

    }
    global cache
    cache.append(key)

def expire(key):
    if key in cache:
        exp = key.get("expiration-date")
        date_exp = datetime.datetime.strptime(exp,"%Y-%m-%d %H:%M:%S.%f")
        date_now = datetime.datetime.now()
        if date_exp >= date_now:
            del key
            return True
        else:
            return False
    else:
        return False
    
def check_expiration():
    for session in cache:
        if expire(session):
            return f"{session} removed"
        else:
            return f"{session} still valid"

setVal("sdfsdfsdfsfsdfds")
print(check_expiration())
