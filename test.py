# coding: utf-8

# Before you start: You need to define constants.py file:
# login = 'login'
# password = 'password'
# test_user_id = 0000000
# test_user_post_id = 0000000
from pprint import pprint

from InstagramAPI import InstagramAPI
from constants import login, password, test_user_id, test_user_post_id

api = InstagramAPI(login, password)
api.login()

api.follow(test_user_id)
api.unfollow(test_user_id)

api.like(test_user_post_id)
api.unlike(test_user_post_id)

print '## Followers ##'
api.getUserFollowers(test_user_id)
pprint(api.LastJson)

print '## Following ##'
api.getUserFollowings(test_user_id)
pprint(api.LastJson)

api.comment(test_user_post_id, 'test comment')

print '## Media likers ##'
api.getMediaLikers(test_user_post_id)
pprint(api.LastJson)

print '## Geo media ##'
api.getGeoMedia(test_user_id)
pprint(api.LastJson)

api.uploadPhoto('test_photo.jpg', caption='test load photo')

