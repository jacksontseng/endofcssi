import jinja2
import os
import webapp2
import random

#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #this is where you reference your HTML file
        names = ["josh", "patrick", "brett", "jackson"]
        person = {"person": {"name": random.choice(names)} #random.choice(names
        template = jinja_environment.get_template('templates/hello.html')
        self.response.out.write(template.render(person))

# creates a WSGIApplication and assigns it to the variable app.
app = webapp2.WSGIApplication([
    ('/', MainHandler)], debug=True)
