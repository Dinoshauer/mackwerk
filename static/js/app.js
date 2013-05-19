jQuery(document).ready(function ($) {

    //DEVELOPMENT
    $('.lipsum').lorem({ type: 'paragraphs', amount: '8', ptags: true });

    var winHeight = $(window).height();   // returns height of browser viewport
    var docHeight = $(document).height(); // returns height of HTML document

    var width = $(window).width();

    var headerBG = $('#blog-post-header').data('header-bg-img');
    if (headerBG != '') {
        $('#blog-post-header').css('background-image', 'url(' + headerBG + ')');
    }

    var footerBG = $('#blog-post-header').data('header-bg-img');
    if (footerBG != '') {
        $('#blog-post-header').css('background-image', 'url(' + footerBG + ')');
    }

    if (width < 481) {
        $('body').addClass('mobile');
        $('.work > .span12 > a').text('Work');
        $('.blog > .span12 > a').text('Blog');
        $('.photo > .span12 > a').text('Photo');
        $('nav > ul > li > a:contains("About")').text('About');
    }

    // Align the nav element to the top of the viewport
    $('nav').css('left', width / 2 - ($('nav > ul').width() / 2));

    console.log("Window height - " + winHeight);
    console.log("Document height - " + docHeight);

    // Set the header to the height of the viewport
    //$('header').css('height', winHeight);
    $('header').css('height', winHeight + 35);
    // Set when the nav element should show again.
    if (!$('body').hasClass('mobile')) {
        $('nav').attr('data-spy', 'affix').attr('data-offset-top', winHeight).addClass('affix-top');
    }

    //initialise Stellar.js
    $(window).stellar();

    // Scroll to top
    $('#back-to-top').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });
});