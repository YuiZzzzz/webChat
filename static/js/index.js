$(document).ready(function () {
    var socket = io()
    var id = 0
    socket.on("connect", function (){
       socket.send("客户端已连接")
       id += 1;
    });


    $('form#send').submit(function () {
        socket.emit('sendMsg', {
            msg:$('#chatMsg').val(),
            user_id: id
        });
        $('#chatMsg').val("");
        console.log("已发送 " + $('#chatMsg').val())
        return false
    });

})