function initJournal(){
   var indicator = $('#ajax-progress-indicator');

$('.day-box input[type="checkbox"]').click(function(event){

   var box = $(this);
   $.ajax(box.data('url'), {
   'type': 'POST',
   'async': true,
   'dataType': 'json',
   'data': {
      'pk': box.data('student-id'),
      'date': box.data('date'),
      'present': box.is(':checked'),
      'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').prop('value')},
   'beforeSend': function(xhr, settings){
            indicator.show();
         },
   'error': function(xhr,status,error){
            alert(error);
            indicator.hide(); 
         },
   'success': function(data, status, xhr){
            indicator.hide();
         }
});
});
}

$(document).ready(function(){
initJournal();
});
