from models.todo_ajax import TodoAjax
from routes import (
    current_user,
    html_response,
    json_response)
from utils import log


def index(request):
    """
    todo 首页的路由函数
    """
    u = current_user(request)
    # 替换模板文件中的标记字符串
    return html_response('todo_ajax_index.html')


def all(request):
    log('ajax request json', request.body)
    todos = TodoAjax.all()
    todos = [t.__dict__ for t in todos]
    # log('todos all <{}>'.format(todos))
    return json_response(todos)


def add(request):
    """
    用于增加新 todo 的路由函数
    """
    u = current_user(request)
    form = request.json()
    log('ajax todo add', form, u)
    t = TodoAjax.add(form, u.id)
    # 浏览器发送数据过来被处理后, 重定向到首页
    # 浏览器在请求新首页的时候, 就能看到新增的数据了
    message = dict(message='成功添加 {}'.format(t.title))
    return json_response(message)


def route_dict():
    """
    路由字典
    key 是路由(路由就是 path)
    value 是路由处理函数(就是响应)
    """
    d = {
        '/todo/ajax/add': add,
        '/todo/ajax/index': index,
        '/todo/ajax/all': all,
    }
    return d
