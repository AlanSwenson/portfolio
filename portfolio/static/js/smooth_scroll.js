// Smooth scrolling to links in the page

var headerHeight = 68;

$('.nav-link, #book-button, #top-logo').click(function () {
    var sectionTo = $(this).attr('href');
    if (sectionTo != '#') {
        $('html, body').animate({
            scrollTop: $(sectionTo).offset().top - headerHeight
        }, 800);
    }
    else {
        // Special Case for a single '#' as the href
        // Scroll to top of body
        $('body,html').animate({
            scrollTop: 0
        }, 500);
    }

    return false;
});

