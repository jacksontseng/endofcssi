import webapp2
import os
import jinja2
import json
import random
from random import choice
import urllib2
import logging
from google.appengine.api import users
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
###############Example
# class Artist(ndb.Model):
#     name = ndb.StringProperty()
#     genre = ndb.StringProperty()
#     age = ndb.IntegerProperty()
#
# class Song(ndb.Model):
#     title = ndb.StringProperty()
#     lyrics = ndb.StringProperty()
#     duration = ndb.IntegerProperty()
#     releasedate = ndb.DateProperty()
################Example ends

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render())
        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.write('GET: Hello world!')
############################################ username code
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)

        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))
######################################### username code ends
    def post(self):

        my_vars = {
            "noun1":self.request.get("noun1"),
            "activity":self.request.get("activity"),
            "celebrity":self.request.get("celebrity"),
            "teacher":self.request.get("teacher"),
            "show":self.request.get("show"),
            "fun":self.request.get("fun")
        }
        self.response.out.write("You have submitted your madlib")

        template = jinja_environment.get_template('templates/madlibs.html')
        self.response.out.write(template.render(my_vars))
        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.write('POST: Hello, World!')

# class api(webapp2.RequestHandler):
#     def get(self):
#         noun1s = ['car', 'sandwich', 'plane']
#         activitys = ['swim', 'surf', 'rollerblade']
#         teachers = ['Yasser', 'Josh', 'Kim', 'Zach']
#         celebritys = ['Beyonce', 'Drake', 'Usher']
#         shows = ['breaking bad', 'CSI', 'Archer']
#         fun = ['Fun', 'Funnn!', 'FunnnnnnNnNNn!']
#
#         answer = {
#         "noun1": random.choice(noun1s), "activity":random.choice(activitys),
#         "teacher": random.choice(teachers), "celebrity": choice(celebritys),
#         "show": choice(shows), "fun": choice(fun)
#         }
#         self.response.write(json.dumps(answer))


class gethandler(webapp2.RequestHandler):
    def get(self):
        f = urllib2.urlopen("http://cssi-kir.appspot.com/api")
        x = f.read()
        y = json.loads(x)

        s = (" Once upon a time "+ y['noun1']+ "wanted to learn to"\
         + y['activity'] + " at Google. So " +y['noun1'] +\
         " flew to Google and met " + y['teacher'] + ".To" +  y['noun1']+\
         " 's surprise " + y['celebrity'] +\
         "was also in the class!  Together " + y['noun1'] + " and "+\
         y['celebrity']+ " decided to work on a project about" +\
         y['show'] + ". " + y['noun1']+ "had so much " +\
         y['fun'] + ". ")

        self.response.out.write(s)

# template = jinja_environment.get_template('templates/index.html')
# self.response.out.write(template.render())

# class gethandlertemplate(webapp2.RequestHandler):
#     def get(self):
#         f = urllib2.urlopen("http://cssi-kir.appspot.com/api")
#         x = f.read()
#         y = json.loads(x)

        # s = (" Once upon a time "+ y['noun1']+ "wanted to learn to"\
        #  + y['activity'] + " at Google. So " +y['noun1'] +\
        #  " flew to Google and met " + y['teacher'] + ".To" +  y['noun1']+\
        #  " 's surprise " + y['celebrity'] +\
        #  "was also in the class!  Together " + y['noun1'] + " and "+\
        #  y['celebrity']+ " decided to work on a project about" +\
        #  y['show'] + ". " + y['noun1']+ "had so much " +\
        #  y['fun'] + ". ")
        # self.response.out.write(s)

        # template = jinja_environment.get_template('templates/apitest.html')
        # self.response.out.write(template.render(y))


# class AdminPage(webapp2.RequestHandler): ### testing application
#     def get(self):
#         user = users.get_current_user()
#         if user:
#             if users.is_current_user_admin():
#                 self.response.write('You are an administrator.')
#             else:
#                 self.response.write('You are not an administrator.')
#         else:
#             self.response.write('You are not logged in.')

class MapsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/maps.html')
        self.response.out.write(template.render())

class PositionHandler(webapp2.RequestHandler):
    def post(self):
        logging.info('got a request')
        name = self.request.get('name')
        lat = self.request.get('lat')
        lng = self.request.get('lng')
        if name and lat and lng:
            b = Birthplace(name = name, lat=lat, lng=lng)
            b.put()
            logging.info('test b got instantiated')
#validate types here
class Birthplace(ndb.Model):
    name = ndb.StringProperty()
    lat = ndb.StringProperty()
    lng = ndb.StringProperty()

class GetPositionHandler(webapp2.RequestHandler):
    def get(self):
        result = Birthplace.query().fetch()
        dresult = [i.to_dict() for i in result]
        self.response.write(json.dumps(dresult))
        ##.get query returns first item
        ##.fetch returns all items for query

class MapPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/mapsall.html')
        self.response.out.write(template.render())

        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    # ('/admin', AdminPage),
    ('/maps', MapsHandler),
    ('/postposition', PositionHandler),
    ('/getpos', GetPositionHandler),
    ('/mapall', MapPage)
    # ('/api', api),
    # ('/GET', gethandler),
    # ('/gettemp', gethandlertemplate)
], debug=True)
