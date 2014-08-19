$(document).ready(function(){
    if($(window).width()>= 1024){
     $( ".left-img" ).hover(
        function() {
            $( this ).find( ".infor-tin" ).css('margin-left', '62%');
            $( this ).find( ".infor-tin" ).css('width', '38%');
        }, function() {
            $( this ).find( ".infor-tin" ).css('margin-left', '66%');
            $( this ).find( ".infor-tin" ).css('width', '34%');
        }
    );

    $( ".right-img" ).hover(
        function() {
            $( this ).find( ".infor-tin" ).css('width', '38%');
        }, function() {
            $( this ).find( ".infor-tin" ).css('width', '34%');
        }
    );
    }
});

