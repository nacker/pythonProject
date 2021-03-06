# coding:utf-8
__author__ = 'nacker'

import tornado.web
import tornado.ioloop
import tornado.httpserver

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        """对应http的get请求方式"""
        self.write("Hello Itcast!")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    # -----------修改----------------
    http_server.bind(8000)
    http_server.start(0)
    # ------------------------------
    tornado.ioloop.IOLoop.current().start()