const containers = document.getElementById('container');
const signupBtn = document.getElementById('signup');
const loginBtn = document.getElementById('login');

signupBtn.addEventListener('click', () => {
    containers.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    containers.classList.remove("active");
});