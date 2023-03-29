/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ["images.dog.ceo"], //ここにドメインを指定
  },
};

module.exports = nextConfig;
