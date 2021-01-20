let feet;
let inches;
let metres;
let message1;
let message2;
let form_element;


document.addEventListener('DOMContentLoaded', init, false);

function init() {
    //initialize variables
    //query selecter to find stuff
    //register event listners
    feet= document.querySelector('#feet');
    message1= document.querySelector('#message1');
    inches= document.querySelector('#inches');
    message2= document.querySelector('#message2');
    metres= document.querySelector('#metres');
    //form_element = document.querySelector('#form');

    //form_element = document.querySelector('#form');
    form_element =document.getElementById('clicky')
    form_element.addEventListener('click', convert, false);
    //form_element.addEventListener('submit', convert, false);
}

function convert(event) {
  //get users data
  //validate;display error messages in the spanspec
  //if no errors
      //do the calc
      //display answer
  let feet_error = '';
  let feet_text =feet.value.trim();
  if (feet_text === '') {
      feet_error = 'Required';
  } else {
       let feet_number =Number(feet_text);
       if (String(feet_number) !== feet_text){
         feet_error = 'Must be a whole number';
       } else if (feet_number < 0) {
           feet_error ='Must be greater than 0';
       } else if (feet_number > 10){
           feet_error ='Must be less than 11';
       }

  }
  let inches_error = '';
  let inches_text =inches.value.trim();
  if (inches_text === '') {
      inches_error = 'Required';
  } else {
       let inches_number =Number(inches_text);
       if (String(inches_number) !== inches_text){
         inches_error = 'Must be a whole number';
       } else if (inches_number < 0) {
           inches_error ='Must be greater than 0';
       } else if (inches_number > 10){
           inches_error ='Must be less than 11';
       }

  }
  message1.innerHTML =feet_error;
  message2.innerHTML =inches_error;
  if (feet_error === '' && inches_error === ''){
    metres.value =(feet.value + (inches.value/10)) / 3.281;
  }
  event.preventDefault();
}
