# coding:utf-8

__author__ = 'nacker'

import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""

    def get(self):
    # def post(self):
        """对应http的get post请求方式"""
        self.write("hello word!")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()