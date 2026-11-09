/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
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
      { source: '/hoc', destination: '/xstk/hoc' },
      { source: '/csdl', destination: '/csdl/hoc' },
    ];
  },
};

export default nextConfig;
