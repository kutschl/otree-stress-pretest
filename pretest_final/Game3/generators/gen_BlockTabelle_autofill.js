$(document).ready(function() {
    $('input[type=radio][value="1"]').click(
        function () {
            let asc = document.querySelector('table[id=ASC]').getAttribute('name')
            // ASCENDING
            if (asc === "True") {
                console.log("ASCENDING")
                let radios = document.querySelectorAll('input[type=radio]')
                let after = false
                let i = 0
                while(after === false && i <= radios.length) {
                    if(radios[i].id === this.id) {
                        radios[i].checked = true;
                        after = true;
                        console.log("1")
                    }
                    if(radios[i].value == 1) {
                        radios[i].checked = true;
                        console.log("1")
                    }
                    i++;
                }
                radios[i].checked = false;
                console.log("2")
                i++;
                while(i <radios.length) {
                    if(radios[i].value == 2) {
                        console.log("2")
                        radios[i].checked = true;
                    }
                    i++;
                }
            }
            // DESCENDING
            if (asc === "False") {
                console.log("DESCENDING")
                let radios = document.querySelectorAll('input[type=radio]')
                let after = false
                let i = 0
                while(after === false && i <= radios.length) {
                    if(radios[i].id === this.id) {
                        radios[i].checked = true;
                        after = true;
                        console.log("2")
                    }
                    if(radios[i].value == 2) {
                        radios[i].checked = true;
                        console.log("2")
                    }
                    i++;
                }
                radios[i].checked = false;
                console.log("2")
                i++;
                while(i<radios.length) {
                    if(radios[i].value == 1) {
                        console.log("1")
                        radios[i].checked = true;
                    }
                    i++;
                }
            }
            // else {
            //     let radios = document.querySelectorAll('input[type=radio]')
            //     let after = false
            //     for(let i = 0; i<radios.length; i++) {
            //         if(after === false && radios[i].value == 2 && radios[i].id !== this.id) {
            //             radios[i].checked = true
            //         }
            //         else if (radios[i].id === this.id) {
            //             radios[i].checked = true
            //             after = true
            //         }
            //         else if (after === true && radios[i].value == 1 && radios[i].id !== this.id) {
            //             radios[i].checked = true
            //         }
            //     }
            // }



        }
    );
    $('input[type=radio][value="2"]').click(
        function () {
            let asc = document.querySelector('table[id=ASC]').getAttribute('name')
            // ASCENDING
            if (asc === "True") {
                console.log("ASCENDING")
                let radios = document.querySelectorAll('input[type=radio]')
                let after = false
                let i = 0
                while(after === false && i <= radios.length) {
                    if(radios[i].id === this.id) {
                        radios[i].checked = true;
                        after = true;
                        console.log("1")
                    }
                    if(radios[i].value == 1) {
                        radios[i].checked = true;
                        console.log("1")
                    }
                    i++;
                }
                while(i <radios.length) {
                    if(radios[i].value == 2) {
                        console.log("2")
                        radios[i].checked = true;
                    }
                    i++;
                }
            }
            // DESCENDING
            if (asc === "False") {
                console.log("DESCENDING")
                let radios = document.querySelectorAll('input[type=radio]')
                let after = false
                let i = 0
                while(after === false && i <= radios.length) {
                    if(radios[i].id === this.id) {
                        radios[i].checked = true;
                        after = true;
                        console.log("2")
                    }
                    if(radios[i].value == 2) {
                        radios[i].checked = true;
                        console.log("2")
                    }
                    i++;
                }
                while(i<radios.length) {
                    if(radios[i].value == 1) {
                        console.log("1")
                        radios[i].checked = true;
                    }
                    i++;
                }
            }
            // else {
            //     let radios = document.querySelectorAll('input[type=radio]')
            //     let after = false
            //     for(let i = 0; i<radios.length; i++) {
            //         if(after === false && radios[i].value == 2 && radios[i].id !== this.id) {
            //             radios[i].checked = true
            //         }
            //         else if (radios[i].id === this.id) {
            //             radios[i].checked = true
            //             after = true
            //         }
            //         else if (after === true && radios[i].value == 1 && radios[i].id !== this.id) {
            //             radios[i].checked = true
            //         }
            //     }
            // }



        }
    );
});