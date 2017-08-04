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
import logging


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("<html><body><h1>Hello Mundo!</h1></body></html>")
        logging.info('Hello, doing some logging!')
        logging.warning('warning!')
        #print "<html><body><h1>Hello Mundo!</h1></body></html>"

class GoodBye(webapp2.RequestHandler):
    def get(self):
        self.response.write("<html><body><h1>GoodBye!!!</h1></body></html>")

class cake(webapp2.RequestHandler):
    def get(self):
        self.response.write("<html><body><h1>CSSI DAY!!!</h1></body></html>")
        self.response.write('<html><body><img src="/resources/cupcake.png" height="250" width="250"></body></html>')

class CountHandler(webapp2.RequestHandler):
    def get(self):
        for i in range(1, 101):
            self.response.write(str(i) + "<br>")
            #print "<div>" + str(i) "</div>"

def is_prime(n):
    """A simple (but inefficient) check to see whether a number is prime."""
    for possible_factor in range(2, n):
        if n % possible_factor == 0:
            logging.info('Found a factor: %d', possible_factor)
            return False
    return True

class MainHandler2(webapp2.RequestHandler):
    def get(self):
        n = 5
        if is_prime(n):
            self.response.write('%d is prime' % n)
        else:
            self.response.write('%d is not prime' % n)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/2', MainHandler2),
    ('/count', CountHandler),
    ('/goodbye', GoodBye),
    ('/cake', cake)
], debug=True)
