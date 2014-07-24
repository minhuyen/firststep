/**
 * Created by shin on 7/17/14.
 */
$(document).ready(function(){
//    $('.category-list .category-item').each(function(){
//        $(this).hover(function(){
//            $(this).children('.sub-category-list').show();
//        },
//        function(){
//            $('.sub-category-list').hide();
//        });
//    });
    if($(window).width()>1024){
        $('.navbar .dropdown').each(function(){
            $(this).hover(
                function(){
                    $(this).children('.dropdown-menu').show();
//                    $(this).children('a').css('color','#000000');
                },
                function(){
                    $('.dropdown-menu').hide();
//                    $(this).children('a').css('color','#ffffff');
                }
            );
        });
    }
    $('.navbar .caret').click(function(){
        $(this).parent('li').children('.dropdown-menu').toggle();
    });
    if($(window).width()>768){
        $('.navbar .navbar-toggle').click(function(){
    //        $('.navbar .collapse').toggle();
            $('.navbar .navbar-nav').toggle();
        });
    };
    if($(window).width()<=768){
        $('.navbar .navbar-toggle').click(function(){
            $('.navbar .navbar-collapse').toggle();
//            $('.navbar .navbar-nav').toggle();
        });
    };

})
