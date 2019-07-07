var log = console.log.bind(console, new Date().toLocaleString())

var e = function (selector) {
    return document.querySelector(selector)
}

var isLetter = function(char) {
    return (char.codePointAt() >= 65 && char.codePointAt() <= 90) || (char.codePointAt() >= 97 && char.codePointAt() <= 122)
}

var isNumber = function(char) {
    return char.codePointAt() >= 48 && char.codePointAt() <= 57
}

var isLetterOrNumber = function (char) {
     return isLetter(char) || isNumber(char)
}

var isUnderline = function (char) {
    return char === '_'
}

var usernameValid = function (validResult) {
    var e = document.querySelector('#id-username-valid')
    e.innerText = validResult
}

var bindEvents = function () {
    var b = e('#id-button-login')
    b.addEventListener('click', function (){
        log('click')
        var input = e('#id-input-username')
        log(input)
        log(input.value)
        var username = input.value
        // 最小长度2，最大长度10
        if (username.length >= 2 && username.length <= 10) {
            // 字母开头，字母或数字结尾
            if (isLetter(username[0]) && isLetterOrNumber(username[username.length - 1])) {
                // 只能包含字母、数字、下划线
                for (var i = 0; i < username.length; i++) {
                    log(username[i])
                    if (isLetterOrNumber(username[i]) || isUnderline(username[i])) {
                    } else {
                        return usernameValid('用户名错误')
                    }
                }
                log('用户名正确')
                return usernameValid('检查合格')
            }
        }
        log ('用户名错误')
        return usernameValid('用户名错误')
        // ajax('POST', '/todo/ajax/add', data, function (json) {
        //     log('拿到ajax响应')
        //     var message = json.message
        //     alert(message)
        //     insertTodo(todoCell)
        // })
    })
}

var main = function () {
    bindEvents()

}

main()