$(function(){
    $('#b_del_btn').on('click', function() {
        //alert('삭제 인식')
        if(confirm("정말로 삭제하시겠습니까?")) {
            location.href = $(this).data('b_del_url');
        }
    });
});