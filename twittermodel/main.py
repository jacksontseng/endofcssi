#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import logging
import json
from google.appengine.api import users
from google.appengine.ext import ndb


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):


        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
            logging.warning('test if user gets runs')

        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)

        template = jinja_environment.get_template('templates/twitterindex.html')
        self.response.out.write(template.render({'greeting':greeting}))

class PostRequestHandler(webapp2.RequestHandler):
    def post(self):
        result = User.query().fetch()
        dresult = [i.to_dict() for i in result]
        self.response.write(json.dumps(dresult))


class User(ndb.Model):
    name = ndb.StringProperty()
    age = ndb.IntegerProperty()
    tweet = ndb.StringProperty(repeated=True)

class Tweet(ndb.Model):
    message = ndb.StringProperty()
    LengthOfMessage = ndb.IntegerProperty()
    Media = ndb.BlobProperty()
    Timestamp = ndb.DateProperty()
    # Author_key = ndb.StringProperty()

class newUser(webapp2.RequestHandler):
    logging.info('got a request, newUser')
    name = self.request.get('name')
    age = self.request.get('age')
    tweets = self.request.get('tweets')

    if name and age:
        new_user = user(name=name, age=age)
        new_user.put()
        logging.info('ayy it worked')



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/postrequest', PostRequestHandler),
    ('/newuser', newUser)
], debug=True)
