$(function(){
    $('#comment_btn').on('click',function(){
        //alert('댓글 등록 버튼 인식')
        $.ajax({
            async : true,   // default : true. 비동기화 시킬 것인가? 네
                            // 일처리 중에 다른 일처리의 접수도 가능.
            url : '/bbs/<board_objects.id>/detail/',
            type : 'POST',
            timeout : 3000, // 단위는 ms
            data : {
                // c_author : $('#c_writer').var(),
                // c_content : $('#c_content').var(),
                csrfmiddlewaretoken : '{{csrf_token}}'
            }, // 서버쪽 프로그램에게 전달할 데이터를 명시(key, targetDt)
            dataType : 'json', // 문자열인 JSON을 JavaScript객체로 변환
            success : function(jsondata){ // 위에서 변환된 객체를 인자로 받음. 인자명은 우리가 정한대로 사용가능.
                let tr = $('<tr></tr>')
                let title = $('<td></td>').text($('#c_writer').var())
                let content = $('<td></td>').text($('#c_content').var())
                let delBtnTd = $('<td></td>')
                let delBtn = $('<button></button>').text('삭제')
                delBtn.addClass('btn btn-dark')
                delBtn.on('click', function (event) {
                    /*
                    <tr> ->parent
                        <td> -> parent
                            <button> -> this
                                삭제
                            </button>
                        </td>
                    </tr> 의 계층*/
                    $(this).parent().parent().remove()
                })
                delBtnTd.append(delBtn)
                /*---------------------------------------------------------------표 구성요소 변수들 만들기*/

                tr.append(title)
                tr.append(content)
                tr.append(delBtnTd)

                $('#TbodyPart').append(tr)
            },
            error : function(){
                // 어떤 이유로든 호출 실패시 이 함수가 자동으로 호출
                alert('실패했어요!')
            }
        })
    })
})