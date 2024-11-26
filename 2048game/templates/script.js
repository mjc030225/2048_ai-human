// $(document).ready(function () {
//     let gameId = $("#game_id").val(); // 从隐藏字段或初始配置中获取 game_id

//     // console.log(gameId)
//     function updateGameBoard(response) {
//         $(".grid-cell").each(function (index) {
//             var row = Math.floor(index / 4);
//             var col = index % 4;
//             $(this).text(response.data[row][col] !== '0' ? response.data[row][col] : '');
//         });
//         $('#score').text(response.score);
//     }

//     function sendCommand(command) {
//         var new_data = [];
//         var res_line = [];
//         var new_score = $('#score').text();

//         // 获取当前棋盘数据
//         $('.grid-cell').each(function () {
//             res_line.push($(this).text());
//         });
//         for (var i = 0; i < 4; i++) {
//             var res_per = [];
//             for (var j = 0; j < 4; j++) {
//                 res_per.push(res_line[i * 4 + j]);
//             }
//             new_data.push(res_per);
//         }

//         // 发送请求到后端
//         $.ajax({
//             type: 'POST',
//             url: '/move',
//             contentType: 'application/json',
//             data: JSON.stringify({
//                 game_id: gameId, // 添加 game_id
//                 command: command,
//                 data: new_data,
//                 score: new_score,
//             }),
//             success: function (response) {
//                 updateGameBoard(response);
//                 console.log("指令已发送: ", command);
//             },
//             error: function (error) {
//                 console.error("发送指令时出错: ", error);
//             }
//         });
//     }

//     // 监听方向键事件
//     $(document).keydown(function (event) {
//         const keyMap = { 87: 'w', 38: 'w', 83: 's', 40: 's', 65: 'a', 37: 'a', 68: 'd', 39: 'd' };
//         var command = keyMap[event.which];
//         if (command) {
//             sendCommand(command);
//         }
//         console.log("按下的键码：", event.which);
//     });

//     // 新游戏按钮
//     $('#new-game-btn').click(function () {
//         $.ajax({
//             type: 'POST',
//             url: '/submit',
//             data: { command: 'reset', game_id: gameId  }, // 添加 game_id
//             success: function (response) {
//                 gameId = response.game_id; // 更新 game_id
//                 updateGameBoard(response);
//                 console.log("新游戏已创建");
//             },
//             error: function (error) {
//                 console.error("重置游戏时出错:", error);
//             }
//         });
//     });

//     // AI 模式
//     function sendDataToBackend() {
//         var new_data = [];
//         var res_line = [];
//         var new_score = $('#score').text();

//         // 获取当前棋盘数据
//         $('.grid-cell').each(function () {
//             res_line.push($(this).text());
//         });
//         for (var i = 0; i < 4; i++) {
//             var res_per = [];
//             for (var j = 0; j < 4; j++) {
//                 res_per.push(res_line[i * 4 + j]);
//             }
//             new_data.push(res_per);
//         }

//         $.ajax({
//             url: "/ai-mode",
//             type: "POST",
//             contentType: "application/json",
//             data: JSON.stringify({
//                 game_id: gameId, // 添加 game_id
//                 data: new_data,
//                 score: new_score,
//             }),
//             success: function (response) {
//                 updateGameBoard(response);
//                 console.log("AI 模式响应数据:", response);
//             },
//             error: function (xhr, status, error) {
//                 console.error("AI 模式发送数据时出错:", status, error);
//             }
//         });
//     }

//     // 每2秒检查是否进入 AI 模式
//     setInterval(function () {
//         var isAI = $('#game-mode').val();
//         if (isAI === 'ai') {
//             sendDataToBackend();
//         }
//     }, 2000);
// });
$(document).ready(function () {
    let gameId = $("#game_id").val(); // 从隐藏字段或初始配置中获取 game_id

    function updateGameBoard(response) {
        $(".grid-cell").each(function (index) {
            var row = Math.floor(index / 4);
            var col = index % 4;
            var newValue = response.data[row][col] !== '0' ? response.data[row][col] : '';
            var oldValue = $(this).text();
    
            // 如果数字发生变化，添加动画效果
            if (newValue !== oldValue) {
                animateMove($(this), oldValue, newValue);
            }
    
            $(this).text(newValue);
    
            // 根据数字更新背景颜色
            if (newValue === '') {
                $(this).css('background-color', '#cdc1b4');  // 恢复为初始背景颜色
            } else {
                setCellBackgroundColor($(this), newValue);
            }
        });
        $('#score').text(response.score);
    }

    // 为每个格子添加移动动画
    function animateMove($cell, oldValue, newValue) {
        var animationDuration = 300; // 动画时长

        // 根据新的值设置背景颜色
        setCellBackgroundColor($cell, newValue);

        // 清除现有动画类
        $cell.removeClass('move-animation');

        // 重置格子的状态
        $cell.stop(true, true);
        $cell.css('transform', 'scale(0)');
        setTimeout(function () {
            $cell.css('transform', 'scale(1)');
        }, 50);

        // 动画效果，首先缩小然后恢复大小
        $cell.addClass('move-animation');
    }
    // 设置格子的背景颜色
function setCellBackgroundColor($cell, value) {
    switch (value) {
        case '':
            $cell.css('background-color', '#cdc1b4'); 
            break;
        case '2':
            $cell.css('background-color', '#eee4da');
            break;
        case '4':
            $cell.css('background-color', '#ede0c8');
            break;
        case '8':
            $cell.css('background-color', '#f2b179');
            break;
        case '16':
            $cell.css('background-color', '#f59563');
            break;
        case '32':
            $cell.css('background-color', '#f67c5f');
            break;
        case '64':
            $cell.css('background-color', '#f65e3b');
            break;
        case '128':
            $cell.css('background-color', '#edcf72');
            break;
        case '256':
            $cell.css('background-color', '#edcc61');
            break;
        case '512':
            $cell.css('background-color', '#edc850');
            break;
        case '1024':
            $cell.css('background-color', '#edc53f');
            break;
        case '2048':
            $cell.css('background-color', '#edc22e');
            break;
        default:
            $cell.css('background-color', '#cdc1b4'); // 背景颜色恢复到初始状态
    }
}


    // 发送指令到后端
    function sendCommand(command) {
        var new_data = [];
        var res_line = [];
        var new_score = $('#score').text();

        // 获取当前棋盘数据
        $('.grid-cell').each(function () {
            res_line.push($(this).text());
        });
        for (var i = 0; i < 4; i++) {
            var res_per = [];
            for (var j = 0; j < 4; j++) {
                res_per.push(res_line[i * 4 + j]);
            }
            new_data.push(res_per);
        }

        // 发送请求到后端
        $.ajax({
            type: 'POST',
            url: '/move',
            contentType: 'application/json',
            data: JSON.stringify({
                game_id: gameId, // 添加 game_id
                command: command,
                data: new_data,
                score: new_score,
            }),
            success: function (response) {
                updateGameBoard(response);
                console.log("指令已发送: ", command);
            },
            error: function (error) {
                console.error("发送指令时出错: ", error);
            }
        });
    }

    // 监听方向键事件
    $(document).keydown(function (event) {
        const keyMap = { 87: 'w', 38: 'w', 83: 's', 40: 's', 65: 'a', 37: 'a', 68: 'd', 39: 'd' };
        var command = keyMap[event.which];
        if (command) {
            sendCommand(command);
        }
        console.log("按下的键码：", event.which);
    });

    // 新游戏按钮
    $('#new-game-btn').click(function () {
        $.ajax({
            type: 'POST',
            url: '/submit',
            data: { command: 'reset', game_id: gameId }, // 添加 game_id
            success: function (response) {
                gameId = response.game_id; // 更新 game_id
                updateGameBoard(response);
                console.log("新游戏已创建");
            },
            error: function (error) {
                console.error("重置游戏时出错:", error);
            }
        });
    });

    // AI 模式
    function sendDataToBackend() {
        var new_data = [];
        var res_line = [];
        var new_score = $('#score').text();

        // 获取当前棋盘数据
        $('.grid-cell').each(function () {
            res_line.push($(this).text());
        });
        for (var i = 0; i < 4; i++) {
            var res_per = [];
            for (var j = 0; j < 4; j++) {
                res_per.push(res_line[i * 4 + j]);
            }
            new_data.push(res_per);
        }

        $.ajax({
            url: "/ai-mode",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                game_id: gameId, // 添加 game_id
                data: new_data,
                score: new_score,
            }),
            success: function (response) {
                updateGameBoard(response);
                console.log("AI 模式响应数据:", response);
            },
            error: function (xhr, status, error) {
                console.error("AI 模式发送数据时出错:", status, error);
            }
        });
    }

    // 每2秒检查是否进入 AI 模式
    setInterval(function () {
        var isAI = $('#game-mode').val();
        if (isAI === 'ai') {
            sendDataToBackend();
        }
    }, 2000);
});