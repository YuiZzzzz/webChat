$(document).ready(function(){
    var socket = io()

    socket.on('connect', function (){
        socket.send('客户端已连接...')
    });

    $('form#join-room').submit(function (event){
        socket.emit('join_room', {
            room:$('#room-number').val()
        })
        return false
    });

    socket.on('joined', function(msg, cb){
        $('ul#text-content').append('<li>' + msg.user + '已加入房间' + msg.room + '</li>')
    });
});