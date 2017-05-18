import webapp2
import os
import jinja2

template_dir = (os.path.dirname(file), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
        autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, a, **kw):
        self.response.out.write(a, kw)

    def render_str(self, template, params):
        t= jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, kw):
        self.write(self.render_str(template, kw))


class MainHandler(Handler):
    def get(self):
        self.redirect('/blog')


class FrontpageHandler(Handler):
    def get(self):
        self.render('frontpage.html')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blog', FrontpageHandler),
], debug=True)