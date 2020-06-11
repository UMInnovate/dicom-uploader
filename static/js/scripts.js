/*!
    * Start Bootstrap - Grayscale v6.0.1 (https://startbootstrap.com/themes/grayscale)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/BlackrockDigital/startbootstrap-grayscale/blob/master/LICENSE)
    */
(function ($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
        if (
            location.pathname.replace(/^\//, "") ==
            this.pathname.replace(/^\//, "") &&
            location.hostname == this.hostname
        ) {
            var target = $(this.hash);
            target = target.length
                ? target
                : $("[name=" + this.hash.slice(1) + "]");
            if (target.length) {
                $("html, body").animate(
                    {
                        scrollTop: target.offset().top - 70,
                    },
                    1000,
                    "easeInOutExpo"
                );
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $(".js-scroll-trigger").click(function () {
        $(".navbar-collapse").collapse("hide");
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $("body").scrollspy({
        target: "#mainNav",
        offset: 100,
    });

    // Collapse Navbar
    var navbarCollapse = function () {
        if ($("#mainNav").offset().top > 100) {
            $("#mainNav").addClass("navbar-shrink");
        } else {
            $("#mainNav").removeClass("navbar-shrink");
        }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);

    // When submit button is pressed, hide the form and show the loading message
    $("form").click(function () {
        var f = document.getElementsByTagName("form")[0];
        if (f.checkValidity()) {
            $("#form").addClass("d-none");
            $("#loading").removeClass("d-none");
        }
    });

    $(".quantity").change(function () {
        var num = $(this).val();
        var elementarray = []
        for (let index = 0; index < num; index++) {
            var element = '<dl class="btn btn-secondary" name="model' + index + '">' +
                '<h2 class="text-light mx-auto mt-2 mb-5">' +
                'Please select files and captions for model ' + index + '.' +
                '</h2>' +
                '<input id="files" type="file" name="files[]" multiple="true" autocomplete="off" required>' +
                '<textarea class="form-control" name="caption' + index + '" placeholder="Please enter caption" required></textarea>' +
                '</p>' +
                '</dl>'
            elementarray.push(element)
        }
        $("#models").empty();
        $("#models").append(elementarray);
    });

})(jQuery); // End of use strict
