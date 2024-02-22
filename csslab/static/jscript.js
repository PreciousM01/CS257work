function generateAppointment(){
  var firstNameInput = document.getElementById("first_name");
  var firstName = firstNameInput.value;
  var lastNameInput = document.getElementById("last_name");
  var lastName = lastNameInput.value;
  var contactInput = document.getElementById("contact");
  var contact = contactInput.value;
  var emailInput = document.getElementById("email");
  var email = emailInput.value;
  var petNameInput = document.getElementById("pet_name");
  var petName = petNameInput.value;
  document.getElementById("your_appointment").innerHTML = "Thanks for making an appointment with PupSpa " + firstName + " :-) " + petName + " is the king and we are its servants!";
}

function shrinkBox(){
  const box = document.getElementsByClassName("box");
  box.addEventListener('mouseover', () => {
  box.style.backgroundcolor = 'slategray'  
  })
  box.addEventListener('mouseout', () => {
  box.style.backgroundcolor = ''  
  })
}
  
