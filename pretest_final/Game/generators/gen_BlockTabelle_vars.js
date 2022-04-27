$(document).ready(function() {
    $('input[type=radio]').click(
        function () {

            // get Values
            const OPTION = this.value
            const DECISION = this.name.substr(6)

            // set Values
            document.getElementById('id_BLOCK' + js_vars.BLOCK_NUMBER + '_TABLE' + js_vars.TABLE_NUMBER + '_SP_OPTION').value = OPTION
            document.getElementById('id_BLOCK' + js_vars.BLOCK_NUMBER + '_TABLE' + js_vars.TABLE_NUMBER + '_SP_DECISION').value = DECISION
        }
    );
});