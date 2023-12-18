export const validateEmail = (email) => {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(String(email).toLowerCase());
};

export function validate(email, password) {
  if (!validateEmail(email)) {
    alert("Invalid Email");
    return false;
  }
  if (password.length < 6) {
    alert("Password must be at least 6 chars long");
    return false;
  }
  return true;
}
