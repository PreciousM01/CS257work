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

function shrinkBox() {
  const boxes = document.getElementsByClassName("box");
  
  for (let box of boxes) {
    box.addEventListener('mouseover', () => {
      box.style.backgroundColor = 'slategray';
      box.style.color = '#db6363';
      box.style.heigth = '100px';
      box.style.width = '200px';
      box.style.fontSize = '18px';
    });
    
    box.addEventListener('mouseout', () => {
      box.style.backgroundColor = '';
    });
  }
}

  
