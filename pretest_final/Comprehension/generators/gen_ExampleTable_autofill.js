$(document).ready(function() {
    $('input[type=radio][value="1"]').click(
        function () {
            let type;
            if ($(this)[0].name.includes('GAIN')) {
                type = 'GAIN';
                let radios = document.querySelectorAll('input[type=radio][name*=' + type + ']')

                let after = false
                let i = 0
                while(after === false && i <= radios.length) {
                    if(radios[i].id === this.id) {
                        radios[i].checked = true;
                        after = true;
                    }
                    if(radios[i].value == 2) {
                        radios[i].checked = true;
                    }
                    i++;
                }
                radios[i].checked = false;
                i++;
                while(i<radios.length) {
                    if(radios[i].value == 1) {
                        radios[i].checked = true;
                    }
                    i++;
                }
            }
            if ($(this)[0].name.includes('LOSS')) {
                type = 'LOSS';

                let radios = document.querySelectorAll('input[type=radio][name*=' + type + ']')
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
                radios[i].checked = false;
                i++;
                while(i <radios.length) {
                    if(radios[i].value == 2) {
                        radios[i].checked = true;
                    }
                    i++;
                }
            }
        }
    );


    $('input[type=radio][value="2"]').click(
        function () {
            let type;
            if ($(this)[0].name.includes('GAIN')) {
                type = 'GAIN';
                let radios = document.querySelectorAll('input[type=radio][name*=' + type + ']')
                let after = false
                let i = 0
                while(after === false && i <= radios.length) {
                    if(radios[i].id === this.id) {
                        radios[i].checked = true;
                        after = true;
                    }
                    if(radios[i].value == 2) {
                        radios[i].checked = true;
                    }
                    i++;
                }
                while(i<radios.length) {
                    if(radios[i].value == 1) {
                        radios[i].checked = true;
                    }
                    i++;
                }
            }
            if ($(this)[0].name.includes('LOSS')) {
                type = 'LOSS';
                let radios = document.querySelectorAll('input[type=radio][name*=' + type + ']')
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
                while(i <radios.length) {
                    if(radios[i].value == 2) {
                        radios[i].checked = true;
                    }
                    i++;
                }
            }


        }
    );
});