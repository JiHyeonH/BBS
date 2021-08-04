$(function(event){
    $('#like_btn').on('click', function(board_objects){
        $.ajax({
            async : true,   // default : true. 비동기화 시킬 것인가? 네
                            // 일처리 중에 다른 일처리의 접수도 가능.
            url : 'http://localhost:8000/bbs/<board_objects.id>/detail/',
            url : 'http://127.0.0.1:8000/bbs/<board_objects.id>/detail/',
            type : 'POST',
            timeout : 3000, // 단위는 ms
            data : {
                'b_like_count' : board_objects.b_like_count,
                'csrfmiddlewaretoken' : '{{csrf_token}}'
            }, // 서버쪽 프로그램에게 전달할 데이터를 명시(key, targetDt)
            dataType : 'json', // 문자열인 JSON을 JavaScript객체로 변환
            success : function(jsondata){ // 위에서 변환된 객체를 인자로 받음. 인자명은 우리가 정한대로 사용가능.
                alert(jsondata.message)
            },
            error : function(){
                // 어떤 이유로든 호출 실패시 이 함수가 자동으로 호출
                alert('실패했어요!')
            }
        })
    })
})