$(document).ready(function() {
    $('input[type=radio][value="0"]').click(
        function () {
            console.log(js_vars.TYPE, js_vars.ORDER)
            if ((js_vars.TYPE == 0 && js_vars.ORDER == 1) || (js_vars.TYPE == 1 && js_vars.ORDER == 0)) {
                console.log("DESCENDING")
                let radios = document.querySelectorAll('input[type=radio]')
                let after = false
                let i = 0
                while (after === false && i <= radios.length) {
                    if (radios[i].id === this.id) {
                        radios[i].checked = true;
                        after = true;
                    }
                    if (radios[i].value == 1) {
                        radios[i].checked = true;
                    }
                    i++;
                }
                radios[i].checked = false;
                i++;
                while (i < radios.length) {
                    if (radios[i].value == 0) {
                        radios[i].checked = true;
                    }
                    i++;
                }
            }
            if ((js_vars.TYPE == 0 && js_vars.ORDER == 0) || (js_vars.TYPE == 1 && js_vars.ORDER == 1)) {
                console.log("ASCENDING")
                let radios = document.querySelectorAll('input[type=radio]')
                let after = false
                let i = 0
                while (after === false && i <= radios.length) {
                    if (radios[i].id === this.id) {
                        radios[i].checked = true;
                        after = true;
                    }
                    if (radios[i].value == 0) {
                        radios[i].checked = true;
                    }
                    i++;
                }
                radios[i].checked = false;
                i++;
                while (i < radios.length) {
                    if (radios[i].value == 1) {
                        radios[i].checked = true;
                    }
                    i++;
                }
            }
        }
    );

    $('input[type=radio][value="1"]').click(
        function () {
            console.log(js_vars.TYPE, js_vars.ORDER)
            if ((js_vars.TYPE == 0 && js_vars.ORDER == 1) || (js_vars.TYPE == 1 && js_vars.ORDER == 0)) {
                console.log("DESCENDING")
                let radios = document.querySelectorAll('input[type=radio]')
                let after = false
                let i = 0
                while(after === false && i <= radios.length) {
                    if(radios[i].id === this.id) {
                        radios[i].checked = true;
                        after = true;
                    }
                    if(radios[i].value == 1) {
                        radios[i].checked = true;
                    }
                    i++;
                }
                while(i<radios.length) {
                    if(radios[i].value == 0) {
                        radios[i].checked = true;
                    }
                    i++;
                }
            }
            if ((js_vars.TYPE == 0 && js_vars.ORDER == 0) || (js_vars.TYPE == 1 && js_vars.ORDER == 1)) {
                console.log("ASCENDING")
                let radios = document.querySelectorAll('input[type=radio]')
                let after = false
                let i = 0
                while(after === false && i <= radios.length) {
                    if(radios[i].id === this.id) {
                        radios[i].checked = true;
                        after = true;
                    }
                    if(radios[i].value == 0) {
                        radios[i].checked = true;
                    }
                    i++;
                }
                while(i <radios.length) {
                    if(radios[i].value == 1) {
                        radios[i].checked = true;
                    }
                    i++;
                }
            }
        }
    );
});