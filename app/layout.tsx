import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "UET Study Hub — Nền tảng Tự học & Luyện thi Tương tác UET",
  description:
    "Hệ thống tự học và ôn thi tương tác Đại học Công nghệ (VNU - UET): Xác suất Thống kê MAT1052 và Cơ sở dữ liệu INT2207.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="vi" data-theme="light">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=Fira+Code:wght@400;600&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="antialiased min-h-screen bg-slate-50 text-slate-900 dark:bg-slate-950 dark:text-slate-50 selection:bg-blue-100 selection:text-blue-900 dark:selection:bg-blue-900 dark:selection:text-blue-100 font-sans">
        {children}
      </body>
    </html>
  );
}
