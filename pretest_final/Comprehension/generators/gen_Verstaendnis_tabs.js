function bootstrapButtonControl(buttonDirection){
    let i;
    let items = $('.nav-link');
    let pane = $('.tab-pane');

    for(i = 0; i < items.length; i++){
        if($(items[i]).hasClass('active') == true){
            break;
        }
    }
    if(buttonDirection === 'next'){
        $(items[i]).removeClass('active');
        $(pane[i]).removeClass('show active');
        $(items[i+1]).addClass('active');
        $(pane[i+1]).addClass('show active');
    }
    if(buttonDirection === 'back') {
        $(items[i]).removeClass('active');
        $(pane[i]).removeClass('show active');
        $(items[i-1]).addClass('active');
        $(pane[i-1]).addClass('show active');
    }
}

function bootstrapTabControl(nextTab) {
    let i;
    let items = $('.nav-link');
    let pane = $('.tab-pane');
    for(i = 0; i < items.length; i++){
        if($(items[i]).hasClass('active') == true){
            break;
        }
    }
    // for tab
    $(items[i]).removeClass('active');
    $(items[nextTab-1]).addClass('active');
    // for pane
    $(pane[i]).removeClass('show active');
    $(pane[nextTab-1]).addClass('show active');
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}