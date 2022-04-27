$(document).ready(function() {
    $('input[type=radio]').click(
        function () {

            // get Values
            const LOTTERY = js_vars.LOTTERY
            const TYPE = js_vars.TYPE
            const ORDER = js_vars.ORDER
            const OPTION = this.value
            const DECISION = this.name.substr(6)

            // set Values
            document.getElementById('id_BLOCK' + js_vars.BLOCK_NUMBER + '_TABLE' + js_vars.TABLE_NUMBER + '_LOTTERY').value = LOTTERY
            document.getElementById('id_BLOCK' + js_vars.BLOCK_NUMBER + '_TABLE' + js_vars.TABLE_NUMBER + '_TYPE').value = TYPE
            document.getElementById('id_BLOCK' + js_vars.BLOCK_NUMBER + '_TABLE' + js_vars.TABLE_NUMBER + '_ORDER').value = ORDER
            document.getElementById('id_BLOCK' + js_vars.BLOCK_NUMBER + '_TABLE' + js_vars.TABLE_NUMBER + '_SP_OPTION').value = OPTION
            document.getElementById('id_BLOCK' + js_vars.BLOCK_NUMBER + '_TABLE' + js_vars.TABLE_NUMBER + '_SP_DECISION').value = DECISION
        }
    );
});