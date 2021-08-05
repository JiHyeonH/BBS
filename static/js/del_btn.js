$(document).ready(function(){
    $('#del_btn').on('click', function() {
        alert('인식 좀 돼라')
        if(confirm("정말로 삭제하시겠습니까?")) {
            location.href = $(this).data('uri');
        }
    });
});