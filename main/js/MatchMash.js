var match_list_index     = 0;
var match_list_end_index = 50;
var loading_match        = false;
var current_page         = 1;

function toggle_display_match(match_id){
  if($('#match_id_'+match_id).attr('data-loaded') == '1'){
    console.log("Toggle'in match: "+match_id);
    $('#loaded_match_'+match_id+' > .match-node').slideToggle();
    return 0;
  }
  console.log(loading_match);
  if(!loading_match){
    loading_match = true;
    console.log("Loading match: "+match_id);
    $('#match_id_'+match_id).addClass('loading-match');
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
      $('#match_id_'+match_id).attr('data-loaded', '1');
      $('#match_id_'+match_id).after('<td colspan="5" id="loaded_match_'+match_id+'">'+html+'</td>');
      console.log("success getting match data");
    })
    .fail(function() {
      console.log("error getting a match");
      $('#match_id_'+match_id).removeClass('loading-match');
      $('#match_id_'+match_id).addClass('loading-match-failed');
    })
    .always(function() {
      console.log("complete getting match");
    });
    $('#match_id_'+match_id).removeClass('loading-match');
    loading_match = false;
  }
}
  
function get_gents(match_id){
  $.ajax({
    url: 'main/util/getData.php',
    type: 'GET',
    dataType: 'json',
    data: {
      query: 'get_gents',
      match_id: match_id,
    },
  })
  .done(function(gents) {
    console.log(gents);

    $('#list_of_matchs').fadeOut(400, function() {
      $('#gents_row').append(gents["best"]);
      $('#gents_row').append(gents["troll"]);
      console.log("Should hide... maybe the DOM Not ready?");
      $('.player-stats').hide();
      $('.timeline-map').hide();
      $('.full-build').hide();
      $('.toggle_build').click(function(event) {
        $(this).next('.full-build').slideToggle();
      });
      $('.toggle_map').click(function(event) {
        $(this).next(".timeline-map").slideToggle();
      });
      $('.toggle_stats').click(function(event) {
        $(this).next(".player-stats").slideToggle();
      });
    });

    console.log("success getting gents match");
  })
  .fail(function() {
    console.log("error getting gents match");
  })
  .always(function() {
    console.log("complete getting gents match");
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
    $.each(data, function(index, match) {
       $("#match-items").append(''+
        '<tr class="match_row" id="match_id_'+match["match_id"]+'" onclick="toggle_display_match('+match["match_id"]+');" data-loaded="0">'+
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
  
  $('.player-stats').hide();
  $('.timeline-map').hide();
  $('.full-build').hide();
  $('.toggle_build').click(function(event) {
    $(this).next('.full-build').slideToggle();
  });
  $('.toggle_map').click(function(event) {
    $(this).next(".timeline-map").slideToggle();
  });
  $('.toggle_stats').click(function(event) {
    $(this).next(".player-stats").slideToggle();
  });
});