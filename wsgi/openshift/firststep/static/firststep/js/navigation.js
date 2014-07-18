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
    $('.navbar .dropdown').each(function(){
        $(this).hover(
            function(){
                $(this).children('.dropdown-menu').show();
                $(this).children('a').css('color','#000000');
            },
            function(){
                $('.dropdown-menu').hide();
                $(this).children('a').css('color','#ffffff');
            }
        );
    });

    $('.navbar .navbar-toggle').click(function(){
        $('.navbar .navbar-collapse').toggle();
    });
})
