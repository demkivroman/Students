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

function initGroupSelector(){
$("#group-selector select").change(function(event){
  var group = $(this).val();

  if(group){
    $.cookie('current_group',group,{'path':'/','expires':365});
  }
  else{
        $.removeCookie('current_group',{'path':'/'});
  } 
 
 location.reload(true);

return true;  
 
});
}


function initDateFields(){
  $("input.dateinput").datetimepicker({
    'format': 'YYYY-MM-DD' 
}).on('dp.hide',function(event){
   $(this).blur(); 
});
}

function initEditStudentPage(){
$('a.student-edit-form-link').click(function(event){
   var link = $(this);
   $.ajax({
     'url': link.attr('href'),
     'dataType': 'html',
     'type': 'get',
     'success': function(data,status,xhr){
         // check if we got successfull response from the server
         if(status != 'success'){
             alert('Помилка на сервері. Сробуйте будь-ласка пізніше.');
             return false;
         }
         // update modal window with arrived content from the server
         var modal = $('#myModal'), html = $(data), form = html.find('form');
         modal.find('.modal-title').html(html.find('#content-column h2').text());
         modal.find('.modal-body').html(form);
        // init our edit form
         initEditStudentForm(form, modal);
        // setup and show modal window finally 
         modal.modal({
             'keyboard': false,
             'backdrop': false,
             'show': true 
         });
     },
     'error': function(){
         alert('Помилка на сервері. Сробуйте будь-ласка пізніше.');
         return false;
      }
   });
 
   return false;  

});
}

function initEditStudentForm(form, modal){
    // atach datepicker
    initDateFields();
    
    // close modal window on Cansel button click
    form.find('button[name=cancel_button]').click(function(event){
        modal.modal('hide');
        return false;
    });

    // make form work in AJAX mode
    form.ajaxForm({
        'dataType': 'html',
        'error': function(){
             alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
             return false;},
        'beforeSend': function(xhr, settings){
         $('#alertModal').show();
         },
        'success': function(data, status, xhr){
            var html = $(data), newform = html.find('#content-column form');
      
            // copy alert to modal window
            modal.find('.modal-body').html(html.find('.alert'));  
            
            // copy form to modal if we found it in server response
            if (newform.length > 0){
                modal.find('.modal-body').append(newform);
                // initialize form fields and buttons
                initEditStudentForm(newform, modal);
            }
            else{
                // if no form it mean success and we need to reload a page
                // to get updated student list;
                // reload after two seconds, so that user can read 
                // success mesage
                setTimeout(function(){
                    location.reload(true);},500);
            }
          }
         
    });
}

function initTabs(){
    $('#ajax_journal').click(function(event){
    var jour = $(this);
    $.ajax({
     'url': jour.data('url'),
     'method':'get',
     'dataType': 'html',
     'success': function(data,status,xhr){
          var content = $('#content-columns'), html = $(data);
          var conJour = html.find('#content-columns');
              content.html(conJour);
          initJournal();
              
         },
     'error': function(){
         alert('Помилка на сервері. Сробуйте будь-ласка пізніше.');
         return false;
      }
   });
    return false;
    });
/*
    $("#ajax_group").click(function(event){
        var groupTab = $(this);
        $.ajax({
            'url': groupTab('url'),
            'method': 'get',
            'dataType': 'html',
            'success': function(data, status, xhr){
                var content = $('#content-columns'), html = $(data);
                //var conGroup = 
             alert(data);
            }
        });
       return false;
    });
*/
}


$(document).ready(function(){
initJournal();
initGroupSelector();
initDateFields();
initEditStudentPage();
initTabs();
});
