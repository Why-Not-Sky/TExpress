type="text/javascript">jQuery(document).ready(function () {
!function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    p = /^http:/.test(d.location) ? 'http' : 'https';
    if (!d.getElementById(id)) {
        js = d.createElement(s);
        js.id = id;
        js.src = p + '://platform.twitter.com/widgets.js';
        fjs.parentNode.insertBefore(js, fjs);

    }
}
(document, "script", "twitter-wjs");

$(function () {
    $("[data-toggle=\'tooltip\']").tooltip();
});;
$(function () {
    $("[data-toggle=\'popover\']").popover();
});
$('body').on('click', function (e) {
    //did not click a popover toggle or popover
    if ($(e.target).data('toggle') !== 'popover'
        && $(e.target).parents('.popover.in').length === 0) {
        $('[data-toggle="popover"]').popover('hide');
    }
});
setTimeout(function() {
    $('.kv-webtips').removeClass('kv-animated-bell').addClass('kv-animated-bell');
}, 3000);
});