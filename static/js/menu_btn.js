$(function(event){
    $('#new_post_btn').on('click',function(event){
        // 버튼이 눌리면 새 글 쓰기에 대한 request를 전송한다.
        document.location.href = '/bbs/create/' // 자바스크립트에서 경로를 부여하는 내부 함수.
    })
})