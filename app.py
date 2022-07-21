from flask import Flask,url_for
from markupsafe import escape

# 从 flask 包导入 Flask 类，通过实例化这个类，创建一个程序对象 app
app = Flask(__name__)

# 注册一个处理函数
@app.route('/')
def hello():
    return 'Hello'

# 用户输入的数据可能会包含恶意代码，使用 MarkupSafe 提供的 escape() 函数对 name 变量进行转义处理
@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'

# 对于 URL 变量，Flask 支持在 URL 规则字符串里对变量设置处理器，对变量进行预处理
@app.route('/user/<int:number>')
def test_number(number):
    return f'User: {escape(type(number))}'

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 生成 hello 视图函数对应的 URL，将会输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'