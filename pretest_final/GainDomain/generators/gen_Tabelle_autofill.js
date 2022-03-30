$(document).ready(function() {
    $('input[type=radio][value="1"]').click(
        function () {
            console.log('A')
            let radios = document.querySelectorAll('input[type=radio]')
            let after = false
            for(let i = 0; i<radios.length; i++) {
                if(after === false && radios[i].value == 2 && radios[i].id !== this.id) {
                    radios[i].checked = true
                }
                else if (radios[i].id === this.id) {
                    after = true
                }
                else if (after === true && radios[i].value == 1) {
                    radios[i].checked = true
                }
            }
        }
    );
    $('input[type=radio][value="2"]').click(
        function () {
            console.log('B')
            let radios = document.querySelectorAll('input[type=radio]')
            let after = false
            for(let i = 0; i<radios.length; i++) {
                if(after === false && radios[i].value == 2 && radios[i].id !== this.id) {
                    radios[i].checked = true
                }
                else if (radios[i].id === this.id) {
                    after = true
                }
                else if (after === true && radios[i].value == 1) {
                    radios[i].checked = true
                }
            }
        }
    );
});