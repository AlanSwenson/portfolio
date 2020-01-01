// Smooth scrolling to links in the page

$('.nav-link').click(function () {
    var sectionTo = $(this).attr('href');
    $('html, body').animate({
        scrollTop: $(sectionTo).offset().top
    }, 800);
    return false;
});