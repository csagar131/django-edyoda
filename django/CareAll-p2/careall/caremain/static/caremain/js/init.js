(function($){
  $(function(){

    $('.sidenav').sidenav();

  }); // end of document ready
})(jQuery); // end of jQuery name space


$(document).ready(function(){
  $(".dropdown-trigger").dropdown();
  $('.modal').modal();
  
})

function toggleModal(){
  var instance  = M.Modal.getInstance($('#modal3'))
  instance.open()
}
