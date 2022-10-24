import requests
import json


def print_hi(name):
    page_id_1 = 'insick.son@gmail.com'
    access_token = 'EAAQpEDvYaccBAEP9cZANmZBiFMJJAFZCt4nJ3Ltvrh3HJrZB3XUHMVeqUSKoDHuUpP2LZArL1ZAKmovMU1oymYuUmdu9LI1ZBYkKAzAviJ4JvDDa7uL9L1rkEsa3ZCXxac9sJPXmNxKZBJXJ7ZCo2blWEIIAiyReZBcKsD1G8UnfZA0moZCbhvddwoRxFzSmrFwIkZAbcRO9QDLkXQuIuhZCvHxQwWp'

    post_url = 'https://graph.facebook.com/v15.0/' + str(page_id_1) + '?fields=instagram_business_account&access_token=' + str(access_token)

    r = requests.get(post_url)

    print(r.text)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')