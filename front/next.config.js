
const nextConfig = {

    reactStrictMode: true,
    // swcMinify: true,
  
    i18n: {
      locales: ['en', 'es', 'fr'], // Idiomas soportados
      defaultLocale: 'en',         // Idioma por defecto
    },

    async headers() {
      return [
        {
          source: '/(.*)',
          headers: [
            {
              key: 'X-Content-Type-Options',
              value: 'nosniff', 
            },
            {
              key: 'X-Frame-Options',
              value: 'DENY',
            },
            {
              key: 'Content-Security-Policy',
              value: "default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src;",
            },
          ],
        },
      ];
    },
  
    webpack: (config, { isServer }) => {
      if (!isServer) {
        config.resolve.fallback = {
          ...config.resolve.fallback,
          fs: false,
        };
      }
      return config;
    },
  
  };
  
  module.exports = nextConfig;
  