$(document).ready(function() {
    $('#new-game-btn').click(function() {
        var new_data=[];
        var res_line=[];
        var new_score=0;
        $('.grid-cell').each(function(){
            var res=$(this).text();
            res_line.push(res);
        });
        for(var i=0;i<4;i++)
            {res_per=[]
            for(var j=0;j<4;j++)
            {
                res_per.push(res_line[i*4+j]);
            }
            new_data.push(res_per);
        };
        // console.log(new_data);
        $.ajax({
            type: 'POST',
            url: '/submit',  // 后端接收请求的URL
            // contentType: 'application/json',
            data: {command:'reset',
                    data:new_data,
                    score:new_score},  // 要发送的指令数据
            success: function(response) {
                // 请求成功后的处理
                console.log(response.data)
                // console.log(response.score);
                $(".grid-cell").each(function(index) {
                    var row = Math.floor(index / 4);
                    var col = index % 4;
                    if (response.data[row][col]!='0')
                    $(this).text(response.data[row][col]);
                    else
                    $(this).text('');
                  });
                $('#score').text(response.score);
                console.log('指令已发送');
            },
            error: function(error) {
                // 请求失败后的处理
                console.error('发送指令时出错:', error);
            }
        });
    });
});


$(document).ready(function() {
    $(document).keydown(function(event) {
        var key = event.which || event.keyCode;
        if(key==87 ||key==38)
        {
            var new_data=[];
        var res_line=[];
        var new_score = $('#score').text();
        $('.grid-cell').each(function(){
            var res=$(this).text();
            res_line.push(res);
        });
        for(var i=0;i<4;i++)
            {res_per=[]
            for(var j=0;j<4;j++)
            {
                res_per.push(res_line[i*4+j]);
            }
            new_data.push(res_per);
        };
        console.log(new_data);
        $.ajax({
            type: 'POST',
            url: '/move',  // 后端接收请求的URL
            contentType: 'application/json',
            data: JSON.stringify({
                command: 'w',
                data: new_data,
                score: new_score
            }),  // 要发送的指令数据
            success: function(response) {
                // 请求成功后的处理
                console.log(response.data)
                // console.log(response.score);
                $(".grid-cell").each(function(index) {
                    var row = Math.floor(index / 4);
                    var col = index % 4;
                    if (response.data[row][col]!='0')
                    $(this).text(response.data[row][col]);
                    else
                    $(this).text('');
                  });
                $('#score').text(response.score);
                console.log('指令已发送');
            },
            error: function(error) {
                // 请求失败后的处理
                console.error('发送指令时出错:', error);
            }
        })};
        if(key==83||key==40)
        {
            var new_data=[];
        var res_line=[];
        var new_score = $('#score').text();
        $('.grid-cell').each(function(){
            var res=$(this).text();
            res_line.push(res);
        });
        for(var i=0;i<4;i++)
            {res_per=[]
            for(var j=0;j<4;j++)
            {
                res_per.push(res_line[i*4+j]);
            }
            new_data.push(res_per);
        };

        $.ajax({
            type: 'POST',
            url: '/move',  // 后端接收请求的URL
            contentType: 'application/json',
            data: JSON.stringify({
                command: 's',
                data: new_data,
                score: new_score
            }),  // 要发送的指令数据
            success: function(response) {
                // 请求成功后的处理
                console.log(response.data)
                // console.log(response.score);
                $(".grid-cell").each(function(index) {
                    var row = Math.floor(index / 4);
                    var col = index % 4;
                    if (response.data[row][col]!='0')
                    $(this).text(response.data[row][col]);
                    else
                    $(this).text('');
                  });
                $('#score').text(response.score);
                console.log('指令已发送');
            },
            error: function(error) {
                // 请求失败后的处理
                console.error('发送指令时出错:', error);
            }
        })};
        if(key==68||key==39)
        {
            var new_data=[];
        var res_line=[];
        var new_score = $('#score').text();
        $('.grid-cell').each(function(){
            var res=$(this).text();
            res_line.push(res);
        });
        for(var i=0;i<4;i++)
            {res_per=[]
            for(var j=0;j<4;j++)
            {
                res_per.push(res_line[i*4+j]);
            }
            new_data.push(res_per);
        };
        console.log(new_data);
        $.ajax({
            type: 'POST',
            url: '/move',  // 后端接收请求的URL
            contentType: 'application/json',
               data: JSON.stringify({
        command: 'd',
        data: new_data,
        score: new_score
    }),  // 要发送的指令数据
            success: function(response) {
                // 请求成功后的处理
                console.log(response.data)
                // console.log(response.score);
                $(".grid-cell").each(function(index) {
                    var row = Math.floor(index / 4);
                    var col = index % 4;
                    if (response.data[row][col]!='0')
                    $(this).text(response.data[row][col]);
                    else
                    $(this).text('');
                  });
                $('#score').text(response.score);
                console.log('指令已发送');
            },
            error: function(error) {
                // 请求失败后的处理
                console.error('发送指令时出错:', error);
            }
        })};
        if(key==65||key==37)
        {
        var new_data=[];
        var res_line=[];
        var new_score = $('#score').text();
        $('.grid-cell').each(function(){
            var res=$(this).text();
            res_line.push(res);
        });
        for(var i=0;i<4;i++)
            {res_per=[]
            for(var j=0;j<4;j++)
            {
                res_per.push(res_line[i*4+j]);
            }
            new_data.push(res_per);
        };
        console.log(new_data);
        $.ajax({
            type: 'POST',
            url: '/move',  // 后端接收请求的URL
            contentType: 'application/json',
            data: JSON.stringify({
                command: 'a',
                data: new_data,
                score: new_score
            }),  // 要发送的指令数据
            success: function(response) {
                // 请求成功后的处理
                console.log(response.data)
                // console.log(response.score);
                $(".grid-cell").each(function(index) {
                    var row = Math.floor(index / 4);
                    var col = index % 4;
                    if (response.data[row][col]!='0')
                    $(this).text(response.data[row][col]);
                    else
                    $(this).text('');
                  });
                $('#score').text(response.score);
                console.log('指令已发送');
            },
            error: function(error) {
                // 请求失败后的处理
                console.error('发送指令时出错:', error);
            }
        })};
        // 在控制台输出按键的键码
        console.log('按下的键码：', key);
  })});


$(document).ready(function() {
    $('#new-game-btn').click(function() {
        var new_data=[];
        var res_line=[];
        var new_score=0;
        $('.grid-cell').each(function(){
            var res=$(this).text();
            res_line.push(res);
        });
        for(var i=0;i<4;i++)
            {res_per=[]
            for(var j=0;j<4;j++)
            {
                res_per.push(res_line[i*4+j]);
            }
            new_data.push(res_per);
        };
        // console.log(new_data);
        $.ajax({
            type: 'POST',
            url: '/submit',  // 后端接收请求的URL
            // contentType: 'application/json',
            data: {command:'reset',
                    data:new_data,
                    score:new_score},  // 要发送的指令数据
            success: function(response) {
                // 请求成功后的处理
                console.log(response.data)
                // console.log(response.score);
                $(".grid-cell").each(function(index) {
                    var row = Math.floor(index / 4);
                    var col = index % 4;
                    if (response.data[row][col]!='0')
                    $(this).text(response.data[row][col]);
                    else
                    $(this).text('');
                  });
                $('#score').text(response.score);
                console.log('指令已发送');
            },
            error: function(error) {
                // 请求失败后的处理
                console.error('发送指令时出错:', error);
            }
        });
    });
});
$(document).ready(function () {
    function sendDataToBackend() {
        var new_data=[];
        var res_line=[];
        var new_score = $('#score').text();
        $('.grid-cell').each(function(){
            var res=$(this).text();
            res_line.push(res);
        });
        for(var i=0;i<4;i++)
            {res_per=[]
            for(var j=0;j<4;j++)
            {
                res_per.push(res_line[i*4+j]);
            }
            new_data.push(res_per);
        };
        // 获取要发送的数据，可以从表单元素中获取，或者根据页面逻辑自行组织数据
        var dataToSend = {
            data: new_data,
            score: new_score,
            command:' '
        };

        // 使用jQuery的ajax方法发送POST请求
        $.ajax({
            url: "/ai-mode",  // 替换为实际的后端URL
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(dataToSend),
            success: function (response) {
                // 请求成功，可以在这里处理后端返回的响应数据
                $(".grid-cell").each(function(index) {
                    var row = Math.floor(index / 4);
                    var col = index % 4;
                    if (response.data[row][col]!='0')
                    $(this).text(response.data[row][col]);
                    else
                    $(this).text('');
                  });
                $('#score').text(response.score);
                console.log(data);
            },
            error: function (xhr, status, error) {
                console.error("Error sending data:", status, error);
            }
        });
    }
    var isTrue=document.getElementById("game-mode").value;
    console.log(isTrue);

    if (isTrue=='ai') {
        sendDataToBackend();
    }

    // 每2秒发送一次数据
    setInterval(function () {
        var isTrue=document.getElementById("game-mode").value;
         console.log(isTrue);
        if (isTrue=='ai') {
            sendDataToBackend();
        }
    }, 2000);
});
