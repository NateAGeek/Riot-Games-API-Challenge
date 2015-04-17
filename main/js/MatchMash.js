var match_list_index = 0;
var match_list_end_index = 50;

function toggle_display_match(match_id){
  alert("Working");
  $.ajax({
    url: 'main/util/getData.php',
    type: 'GET',
    dataType: 'html',
    data: {
      query: 'get_match',
      match_id: match_id,
      html: true
    },
  })
  .done(function(html) {
    console.log(html);
    $('#match_id_'+match_id).after('<td colspan="5">'+html+'</td>');
    console.log("success getting match data");
  })
  .fail(function() {
    console.log("error getting a match");
  })
  .always(function() {
    console.log("complete getting match");
  });
}

function loadMatches(){
  $.ajax({
    url: 'main/util/getData.php',
    type: 'GET',
    dataType: 'json',
    data: {
      query: 'list_matches',
      json:  true,
      start: match_list_index,
      end:   match_list_end_index,
    },
  })
  .done(function(data){
    console.log(data);
    $.each(data, function(index, match) {
       $("#match-items").append(''+
        '<tr class="match_row" id="match_id_'+match["match_id"]+'" onclick="toggle_display_match('+match["match_id"]+');">'+
          '<td>'+match["match_type"]+'</td>'+
          '<td>'+match["match_id"]+'</td>'+
          '<td>'+match["region"]+'</td>'+
          '<td>'+match["duration"]+'</td>'+
          '<td>'+match["creation"]+'</td>'+
        '</tr>'+
        '');
    });
  })
  .fail(function (){
    console.log("Failed to get matches? You doing something sneaky?");
  });
}

jQuery(document).ready(function($) {
  loadMatches();
});