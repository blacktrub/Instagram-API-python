# coding: utf-8

# Before you start: You need to define constants.py file:
# login = 'login'
# password = 'password'
# test_user_id = 0000000
# test_user_post_id = 0000000

from InstagramAPI import InstagramAPI
from constants import login, password, test_user_id, test_user_post_id

api = InstagramAPI(login, password)
api.login()

api.follow(test_user_id)
api.unfollow(test_user_id)

api.like(test_user_post_id)
api.unlike(test_user_post_id)

api.getUserFollowers(test_user_id)
print api.LastJson

api.getUserFollowings(test_user_id)
print api.LastJson

api.comment(test_user_post_id, 'test comment')

api.getMediaLikers(test_user_post_id)
print api.LastJso

api.getGeoMedia(test_user_id)
print api.LastJson

api.uploadPhoto('12345.jpg', caption='test load photo')

