/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  async redirects() {
    return [
      { source: '/hoc', destination: '/xstk/hoc', permanent: false },
      { source: '/csdl', destination: '/csdl/hoc', permanent: false },
      { source: '/xstk', destination: '/xstk/hoc', permanent: false },
    ];
  },
  async rewrites() {
    return [
      { source: '/tuluan', destination: '/site/tuluan.html' },
      { source: '/tracnghiem', destination: '/site/tracnghiem.html' },
      { source: '/congthuc', destination: '/site/congthuc.html' },
      { source: '/dethi', destination: '/site/dethi.html' },
      { source: '/xstk/tuluan', destination: '/site/tuluan.html' },
      { source: '/xstk/tracnghiem', destination: '/site/tracnghiem.html' },
      { source: '/xstk/congthuc', destination: '/site/congthuc.html' },
      { source: '/xstk/dethi', destination: '/site/dethi.html' },
    ];
  },
};

export default nextConfig;
