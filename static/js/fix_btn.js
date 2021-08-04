$(function(event){
    $('#fix_btn').on('click',function(event){
        var fixbtn = document.getElementById('fix_btn')
        document.location.href = '/bbs/'+ fixbtn.dataset.pageid + '/fix/'
    })
})