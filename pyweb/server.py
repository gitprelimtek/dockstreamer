import cherrypy
import sys

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"


if __name__ == '__main__':
    cherrypy.log("Starting ------>")
    cherrypy.quickstart(HelloWorld(), '/pyapp', {'global': {'server.socket_host':'0.0.0.0','server.socket_port': 8080}})
    cherrypy.log("Stopping ------>")
