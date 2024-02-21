function generateAppointment(){
  first-name-input = document.getElementById("first_name");
  first-name = first-name-input.value();
  last-name-input = document.getElementById("last_name");
  last-name = last-name-input.value();
  contact-input = document.getElementById("contact");
  contact = contact-input.value();
  email-input = document.getElementById("email");
  email = email-input.value();
  pet-name-input = document.getElementById("pet_name");
  pet-name = pet-name-input.value();
  document.getElementById("your_appointment").innerHTML = "Thanks for making an appointment with PupSpa" + first-name + "." + pet-name + " is the king and we are its servants!";
}
