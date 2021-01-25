document.addEventListener('DOMContentLoaded', ()=>{
  
  document.getElementById('password').onchange=()=>{
    let password1 = document.getElementById('password1');
    
    if(password1.value.length !==0){
      passwordCheck();
    }
  }
  
  
  document.getElementById('password').onkeyup=() =>{
    let password1 = document.getElementById('password1');
    if(password1.value.length!==0){
      passwordCheck();
    }
  }
  
  document.getElementById('password1').onchange=passwordCheck;
  document.getElementById('password1').onkeyup=passwordCheck;
  
});

const passwordCheck=function() {
  let password = document.getElementById('password');
  let password1 = document.getElementById('password1');
  let register = document.getElementById('register');
  let msg = document.getElementById('msg');
  if (password1.value !== password.value) {
    msg.innerHTML = 'password mismatch';
    register.disabled=true;
  }
  else {
    msg.innerHTML = '';
    register.disabled=false;
  }
}