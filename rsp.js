let bill;
let tip_type;
let tip_entry;
let message;
let form_element;


document.addEventListener('DOMContentLoaded', init, false);

function init() {
    bill= document.querySelector('#bill');
    message= document.querySelector('#message');
    tip_type= document.querySelector('#tip_type');
    tip_entry= document.querySelector('#tip');
    form_element = document.querySelector('#form');
    form_element.addEventListener('submit', check_for_pos_int, false);
}

function check_for_pos_int(text) {
let bill_error = '';
let trimmed_text = text.trim();
if (trimmed_text === "") {
    bill_error = "The bill must be a whole number greater than 0";
}else{
    let number = Number(trimmed_text);
    if (String(number) !== trimmed_text) {
      bill_error = "The bill must be a whole number greater than 0";
    }
    if (number < 0) {
      bill_error = "The bill must be a whole number greater than 0";
    }
}
message.innerHTML =bill_error;
if (bill_error === '' && tip_type.value = 'small'){
  tip_entry.value =((bill.value/100) * 10).toFixed(2)
}
if (bill_error === '' && tip_type.value = 'large'){
  tip_entry.value =((bill.value/100) * 15).toFixed(2)
}
event.preventDefault();
}
