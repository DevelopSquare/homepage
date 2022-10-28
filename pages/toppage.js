/** 製品の詳細をアコーディオンパネルとして開閉する */
$('.switching-bar').on('click', function() {
    var findElm = $(this).prev(".hidden-area")
    $(findElm).slideToggle()
      
    if($(this).hasClass('close')){
      $(this).removeClass('close')
    }else{
      $(this).addClass('close')
    }
  });