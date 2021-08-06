$(function(event){
    $('#fix_btn').on('click',function(event){
        alert('수정 화면 진입')
        fixbtn = document.getElementById('fix_btn')
        document.location.href = '/bbs/'+ fixbtn.dataset.pageid + '/fix/'
    })
})