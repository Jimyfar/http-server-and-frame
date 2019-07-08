
基于 Socket 的 HTTP 服务器和 Web 框架
=====================

## 简介

- 实现底层为 Socket 的 HTTP 服务器，在性能上使用多线程实现并发访问，在功能方面，服务器负责转发请求数据到 Web 框架和将返回的响应结果发往客户端。
- 在整个 MVC 架构中，Model 层实现基于 MySQL 的 ORM，除了支持使用数据对象的实例化形式数据外，还通过将 SQL 语句抽象为对象，实现支持 JOIN 子句的数据库语句拼接，解决 ORM n + 1 问题。
- View 层使用 Jinja2 模板，简化网页生成，加速开发。
- Control 层为自制 Web 框架，核心功能是利用高阶函数实现的注册路由和路由分发。辅助功能包括请求数据实例化，响应头组装接口，重定向，支持返回 HTML 、JSON和静态资源的响应结果。
- 基于这个框架实现了一个类微博应用，功能包括用户登录注册，密码加盐 Hash，博文和留言的 CRUD，使用装饰器实现用户对内容删除修改的权限验证。
Todo 列表功能使用了原生 JS 封装的 AJAX，前后端使用 JSON 格式文本通信。


## 运行环境

Windows10

python 3.6

```
pip install pymysql jinja2
```
## 本地测试

```
python reset.py
python server.py
```

## 详细
### 主页
![主页](images/主页.png)

### 登录界面
![登录界面](images/登录界面.png)

### ajax todo 前端和后端发送请求接收响应
![ajax](images/ajax.jpg)

### weibo CRUD gif
微博增删改查，微博权限控制（博主可以修改博文和删除博文，博主可以删除评论但不可以修改评论。评论楼主可以修改和删除评论）
![weibo CRUD gif](https://github.com/Jimyfar/http-server-and-frame/blob/master/images/Animation%204.gif)

### 注册登录 gif
![注册登录](https://github.com/Jimyfar/http-server-and-frame/blob/master/images/Animation%202.gif)

### ajax gif
![注册登录](https://github.com/Jimyfar/http-server-and-frame/blob/master/images/Animation%203.gif)

