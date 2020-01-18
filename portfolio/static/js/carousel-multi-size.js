function carouselNormalization() {
    var items = $('.intro-carousel .carousel-item'), //grab all slides
        heights = [], //create empty array to store height values
        smallest; //create variable to make note of the smallest slide

    if (items.length) {
        function normalizeHeights() {
            items.each(function () { //add heights to array
                heights.push($(this).height());
            });
            smallest = Math.min.apply(null, heights); //cache smallest value
            items.each(function () {
                $(this).css('max-height', smallest + 'px');
            });
        };
        normalizeHeights();

        $(window).on('resize orientationchange', function () {
            smallest = 0, heights.length = 0; //reset vars
            items.each(function () {
                $(this).css('max-height', 'unset'); //reset max-height
            });
            normalizeHeights(); //run it again 
        });
    }
}

window.onload = function () { carouselNormalization(); }