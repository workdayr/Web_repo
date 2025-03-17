import CryptoJS from 'crypto-js';

// Genera una cadena aleatoria de 16 bytes
const generateSalt = () => {
  // Genera una cadena aleatoria en base64 para usarla como salt
  return CryptoJS.lib.WordArray.random(16).toString(CryptoJS.enc.Base64);
};

// Función para hashear la contraseña con SHA-256 y una sal
export function hashPassword(password) {
  const salt = generateSalt();
  
  // Concatenar la sal con la contraseña
  const saltedPassword = salt + password;
  
  // Hashear la contraseña con SHA-256 usando CryptoJS
  const hashedPassword = CryptoJS.SHA256(saltedPassword).toString(CryptoJS.enc.Hex);
  
  return `${salt}$${hashedPassword}`; // Se concatena la sal y el hash para guardarlos juntos
}
