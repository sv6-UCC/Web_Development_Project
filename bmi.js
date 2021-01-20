let form_element;
let feet_input;
let feet_span;
let inches_input;
let inches_span;
let cm_input;

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    feet_input = document.querySelector('#feet_input');
    feet_span = document.querySelector('#feet_msg');
    inches_input = document.querySelector('#inches_input');
    inches_span = document.querySelector('#inches_msg');
    cm_input = document.querySelector('#cm_input');
    form_element = document.querySelector('form');
    form_element.addEventListener('submit', convert_to_cm, false);
    feet_input.addEventListener('change', validate_input, false);
    inches_input.addEventListener('change', validate_input, false);
}

function check_for_int(text, minimum, maximum) {
    let trimmed_text = text.trim();
    if (trimmed_text === "") {
        return "Required";
    }
    let number = ~~Number(trimmed_text);
    if (String(number) !== trimmed_text) {
        return "Must be a whole number";
    }
    if (number < minimum) {
        return "Must be no less than " + minimum;
    }
    if (number > maximum) {
        return "Must be no greater than " + maximum;
    }
    return '';
}

function validate_input(event) {
    feet_msg = check_for_int(feet_input.value, 0, 8);
    inches_msg = check_for_int(inches_input.value, 0, 11);
    feet_span.innerHTML = feet_msg;
    inches_span.innerHTML = inches_msg;
}

function convert_to_cm(event) {
    feet_msg = check_for_int(feet_input.value, 0, 8);
    inches_msg = check_for_int(inches_input.value, 0, 11);
    feet_span.innerHTML = feet_msg;
    inches_span.innerHTML = inches_msg;
    if (! feet_msg && ! inches_msg) {
        feet_int = Number(feet_input.value);
        inches_int = Number(inches_input.value);
        cm_int = (12 * feet_int + inches_int) * 2.5;
        cm_input.value = cm_int;
    }
    event.preventDefault();
}
