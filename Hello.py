"""
1、创建 Python Web 应用
2、在你的项目根目录下创建一个 requirements.txt，我们使用 requirements.txt 来安装 Flask 及其他依赖项
3、

"""

from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis',port=6379)

@app.route("/")
def hello():
    cache.incr('hits')
    return "Hello Python! this is a flask web project. You have seen this page %s times." % cache.get('hits')
    # return "Hello Python! this is a flask web project."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

