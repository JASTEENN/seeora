document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form");
  const firstName = document.getElementById("firstname-input");
  const lastName = document.getElementById("lastname-input");
  const email = document.getElementById("email-input");
  const password = document.getElementById("password-input");
  const rePassword = document.getElementById("re-password-input");

  function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  }

  form.addEventListener("submit", (e) => {
    let errors = [];

    if (firstName.value.trim() === "") {
      errors.push("First name is required.");
    }

    if (lastName.value.trim() === "") {
      errors.push("Last name is required.");
    }

    if (!validateEmail(email.value)) {
      errors.push("Enter a valid email address.");
    }

    if (password.value.length < 6) {
      errors.push("Password must be at least 6 characters long.");
    }

    if (password.value !== rePassword.value) {
      errors.push("Passwords do not match.");
    }

    if (errors.length > 0) {
      e.preventDefault();
      alert(errors.join("\n"));
    }
  });
});
