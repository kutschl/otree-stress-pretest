$(document).ready(function() {
    document.getElementById('otree-next').setAttribute('style', 'display: none')
    $('input[type=radio][value="True"]').click(
        function () {
            document.getElementById('otree-next').removeAttribute('style')
        }
    );
    $('input[type=radio][value="False"]').click(
        function () {
            document.getElementById('otree-next').setAttribute('style', 'display: none')
        }
    );
});