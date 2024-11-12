import { setCookie } from 'cookies-next';

export default async function handler(req, res) {
  if (req.method === 'POST') {
    const { username, password } = req.body;
    // Autenticar al usuario aquí (por ejemplo, usando un servicio externo o base de datos)
    if (username === 'admin' && password === 'password') {
      // Establecer cookie de sesión
      setCookie('token', 'your-auth-token', { req, res, maxAge: 60 * 60 * 24 });
      return res.status(200).json({ message: 'Login successful' });
    } else {
      return res.status(401).json({ message: 'Invalid credentials' });
    }
  } else {
    res.setHeader('Allow', ['POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
