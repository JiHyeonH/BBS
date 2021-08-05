$(function(event){
    $('#del_btn').on('click', function(event) {
        alert('인식 성공')
        if(confirm("정말로 삭제하시겠습니까?")) {
            var delbtn = document.getElementById('del_btn')
            document.location.href = '/bbs/'+ delbtn.dataset.pageid + '/delete/'
        }
    });
});