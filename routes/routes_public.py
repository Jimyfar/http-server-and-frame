from routes import (
    current_user,
    html_response,
    json_response)
from utils import log


def index(request):
    """
    主页的处理函数, 返回主页的响应
    """
    u = current_user(request)
    return html_response('index.html', username=u.username)


def static(request):
    """
    静态资源的处理函数, 读取图片并生成响应返回
    """
    filename = request.query.get('file', 'doge.gif')
    path = 'static/' + filename
    with open(path, 'rb') as f:
        # header = b'HTTP/1.x 200 OK\r\nContent-Type: image/gif\r\n\r\n'
        header = b'HTTP/1.x 200 OK\r\n\r\n'
        img = header + f.read()
        return img


def ajax_view(request):
    return html_response('ajax.html')


def ajax_test(request):
    log('ajax data', request.body)
    return json_response(dict(response='hello'))


def route_dict():
    """
    路由字典
    key 是路由(路由就是 path)
    value 是路由处理函数(就是响应)
    """
    d = {
        '/': index,
        '/static': static,
        '/ajax/test': ajax_test,
        '/ajax/view': ajax_view,
    }
    return d
