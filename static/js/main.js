$(function () {

    $(window).scroll(function () {
        if ($(window).scrollTop() <= 40) {
            // navbar.removeClass('navbar-scroll');
            $('.navbar').removeClass('navbar-scroll');
        } else {
            // navbar.addClass('navbar-scroll');
            $('.navbar').addClass('navbar-scroll');
        }
    });
});

// paralex js

// end of paralex js

// for image gallery
// jQuery(document).ready(function () {
//     lightbox.option({
//         'resizeDuration': 200,
//         'wrapAround': true,
//         'alwaysShowNavOnTouchDevices': true,
//         'fitImagesInViewport': true,
//     });
// });

// magnigfic gallery javascript
jQuery(document).ready(function () {
    $('.gallerys').magnificPopup({
        type: 'image',
        delegate: 'a',
        gallery: {
            enabled: true
        },
    });
});
// magnigfic gallery javascript end

// To submit contact form data

//end of submit contact form data





