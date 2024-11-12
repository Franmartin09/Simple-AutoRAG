import { deleteCookie } from 'cookies-next';

export default async function handler(req, res) {
  // Eliminar la cookie de sesión
  deleteCookie('token', { req, res });
  return res.status(200).json({ message: 'Logout successful' });
}
