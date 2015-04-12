jQuery(document).ready(function($) {
  $(".timeline-spot").mouseover(function(event) {
    $(this).css("z-index","1000");
  });
  $(".timeline-spot").mouseout(function(event) {
    $(this).css("z-index","1");
  });
});