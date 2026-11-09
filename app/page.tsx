import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card";
import {
  ArrowRight,
  BookOpen,
  CheckCircle2,
  GraduationCap,
  Database,
  Sigma,
  FileText,
  HelpCircle,
  Layers,
  Sparkles,
  ShieldCheck,
  BookmarkCheck,
  ChevronRight,
} from "lucide-react";

export const metadata = {
  title: "UET Study Hub — Cổng Học Tập & Luyện Thi Tương Tác VNU-UET",
  description:
    "Nền tảng tự học tương tác chuẩn Sư phạm UET cho Xác suất Thống kê MAT1052 và Cơ sở Dữ liệu INT2207 bám sát slide bài giảng giảng viên.",
};

export default function HomePage() {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 dark:bg-slate-950 dark:text-slate-100 flex flex-col font-sans antialiased selection:bg-blue-500/20">
      {/* Top Navbar */}
      <header className="sticky top-0 z-50 w-full border-b border-border/80 bg-background/80 backdrop-blur-md shadow-xs">
        <div className="max-w-7xl mx-auto px-4 h-14 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="h-8 w-8 rounded-lg bg-blue-600 text-white flex items-center justify-center font-bold shadow-xs">
              <GraduationCap className="h-4.5 w-4.5" />
            </div>
            <div className="flex flex-col leading-tight">
              <span className="font-extrabold text-sm tracking-tight text-foreground">
                UET STUDY HUB
              </span>
              <span className="text-[10px] text-muted-foreground font-medium">
                Cổng Học Tập & Luyện Thi Tương Tác VNU-UET
              </span>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <Link href="/xstk/hoc">
              <Button variant="outline" size="sm" className="font-semibold text-xs h-8 gap-1.5">
                <Sigma className="h-3.5 w-3.5 text-blue-500" />
                <span className="hidden sm:inline">Xác suất</span>
                <span className="font-mono text-[10px] opacity-75">MAT1052</span>
              </Button>
            </Link>
            <Link href="/csdl/hoc">
              <Button size="sm" className="font-semibold text-xs h-8 gap-1.5 shadow-xs">
                <Database className="h-3.5 w-3.5 text-blue-200" />
                <span className="hidden sm:inline">Cơ sở dữ liệu</span>
                <span className="font-mono text-[10px] opacity-75">INT2207</span>
              </Button>
            </Link>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative overflow-hidden py-14 sm:py-20 px-4 border-b border-border bg-card">
        <div className="max-w-4xl mx-auto text-center space-y-4">
          <Badge variant="blueSoft" className="px-3 py-1 font-semibold text-xs gap-1.5">
            <Sparkles className="h-3.5 w-3.5 text-blue-600 dark:text-blue-400" />
            <span>Chuẩn Sư phạm Tương tác UET</span>
          </Badge>

          <h1 className="text-3xl sm:text-5xl font-extrabold tracking-tight text-foreground leading-[1.15]">
            Nền tảng Tự học & Luyện thi <br className="hidden sm:inline" />
            <span className="text-blue-600 dark:text-blue-400">Chuẩn Barem VNU-UET</span>
          </h1>

          <p className="text-sm sm:text-base text-muted-foreground max-w-2xl mx-auto leading-relaxed">
            Học tuần tự từng bước (Section Stepper), kiểm tra 3 cấp độ chặn chuyển bài (Gatekeeper Quiz), và 100% ví dụ mẫu trích xuất trực tiếp từ slide bài giảng giảng viên.
          </p>

          {/* Metric Highlights */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-3xl mx-auto pt-6 text-left">
            <div className="p-4 rounded-xl border border-border/80 bg-muted/40">
              <div className="text-2xl font-bold font-mono text-blue-600 dark:text-blue-400 tabular-nums">
                40 bài
              </div>
              <div className="text-xs text-muted-foreground font-medium mt-0.5">Bài giảng chi tiết</div>
            </div>
            <div className="p-4 rounded-xl border border-border/80 bg-muted/40">
              <div className="text-2xl font-bold font-mono text-emerald-600 dark:text-emerald-400 tabular-nums">
                120 ví dụ
              </div>
              <div className="text-xs text-muted-foreground font-medium mt-0.5">100% bám sát Slide</div>
            </div>
            <div className="p-4 rounded-xl border border-border/80 bg-muted/40">
              <div className="text-2xl font-bold font-mono text-amber-600 dark:text-amber-400 tabular-nums">
                120 câu
              </div>
              <div className="text-xs text-muted-foreground font-medium mt-0.5">Quiz 3 cấp độ</div>
            </div>
            <div className="p-4 rounded-xl border border-border/80 bg-muted/40">
              <div className="text-2xl font-bold font-mono text-indigo-600 dark:text-indigo-400 tabular-nums">
                100%
              </div>
              <div className="text-xs text-muted-foreground font-medium mt-0.5">Dấu Ref tra cứu slide</div>
            </div>
          </div>
        </div>
      </section>

      {/* Primary Courses Grid */}
      <section className="max-w-6xl mx-auto px-4 py-12 w-full space-y-6 flex-1">
        <div className="flex flex-col gap-1 text-center sm:text-left">
          <h2 className="text-xl sm:text-2xl font-bold text-foreground tracking-tight flex items-center justify-center sm:justify-start gap-2">
            <Layers className="h-5 w-5 text-blue-600 dark:text-blue-400" />
            <span>Môn Học Đã Tích Hợp</span>
          </h2>
          <p className="text-xs sm:text-sm text-muted-foreground">
            Chọn môn học bên dưới để vào không gian học tập tương tác phân đoạn.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Card 1: XSTK */}
          <Card className="border border-border hover:border-blue-300 dark:hover:border-blue-700 transition-all shadow-xs hover:shadow-md bg-card flex flex-col justify-between overflow-hidden">
            <CardHeader className="p-6 pb-4">
              <div className="flex items-center justify-between mb-3">
                <Badge variant="blueSoft" className="font-mono font-semibold text-xs">
                  MAT1052
                </Badge>
                <div className="h-10 w-10 rounded-xl bg-blue-50 dark:bg-blue-950/60 border border-blue-200 dark:border-blue-900/60 flex items-center justify-center text-blue-600 dark:text-blue-400 shadow-2xs">
                  <Sigma className="h-5 w-5" />
                </div>
              </div>
              <CardTitle className="text-lg sm:text-xl font-bold text-foreground">
                Xác suất Thống kê
              </CardTitle>
              <CardDescription className="text-xs text-muted-foreground leading-relaxed mt-1">
                26 bài học chia làm 5 cụm (Dữ liệu, Xác suất, Rời rạc, Liên tục, Hồi quy) bám sát tuần học 1–7 của UET.
              </CardDescription>
            </CardHeader>
            <CardContent className="p-6 pt-0 space-y-3">
              <ul className="text-xs space-y-2 text-slate-700 dark:text-slate-300">
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="h-4 w-4 text-emerald-500 shrink-0" />
                  <span>26 bài tương tác, 78 ví dụ slide có lời giải</span>
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="h-4 w-4 text-emerald-500 shrink-0" />
                  <span>Trắc nghiệm, tự luận chuẩn barem, mẹo bấm Casio</span>
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="h-4 w-4 text-emerald-500 shrink-0" />
                  <span>Tra cứu slide PDF tuần 1 đến tuần 7</span>
                </li>
              </ul>
            </CardContent>
            <CardFooter className="p-6 pt-0 flex gap-2.5">
              <Link href="/xstk/hoc" className="flex-1">
                <Button className="w-full font-semibold text-xs h-9 shadow-xs">
                  Vào Học Tương Tác
                  <ArrowRight className="h-3.5 w-3.5 ml-1" />
                </Button>
              </Link>
              <Link href="/tuluan">
                <Button variant="outline" className="font-semibold text-xs h-9">
                  Tự Luận
                </Button>
              </Link>
            </CardFooter>
          </Card>

          {/* Card 2: CSDL */}
          <Card className="border border-border hover:border-indigo-300 dark:hover:border-indigo-700 transition-all shadow-xs hover:shadow-md bg-card flex flex-col justify-between overflow-hidden">
            <CardHeader className="p-6 pb-4">
              <div className="flex items-center justify-between mb-3">
                <Badge variant="outline" className="font-mono font-semibold text-xs border-indigo-200 dark:border-indigo-900 bg-indigo-50/50 dark:bg-indigo-950/40 text-indigo-700 dark:text-indigo-300">
                  INT2207
                </Badge>
                <div className="h-10 w-10 rounded-xl bg-indigo-50 dark:bg-indigo-950/60 border border-indigo-200 dark:border-indigo-900/60 flex items-center justify-center text-indigo-600 dark:text-indigo-400 shadow-2xs">
                  <Database className="h-5 w-5" />
                </div>
              </div>
              <CardTitle className="text-lg sm:text-xl font-bold text-foreground">
                Cơ sở Dữ liệu
              </CardTitle>
              <CardDescription className="text-xs text-muted-foreground leading-relaxed mt-1">
                14 bài học chia làm 4 chương (Tổng quan, Mô hình ER, Đại số quan hệ & SQL, Phụ thuộc hàm & Chuẩn hóa BCNF/3NF).
              </CardDescription>
            </CardHeader>
            <CardContent className="p-6 pt-0 space-y-3">
              <ul className="text-xs space-y-2 text-slate-700 dark:text-slate-300">
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="h-4 w-4 text-emerald-500 shrink-0" />
                  <span>14 bài tương tác chuẩn UET.IS2099</span>
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="h-4 w-4 text-emerald-500 shrink-0" />
                  <span>42 ví dụ slide, 42 câu trắc nghiệm 3 cấp độ</span>
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="h-4 w-4 text-emerald-500 shrink-0" />
                  <span>Tra cứu slide PPTX Chương 1, 2, 3, 4</span>
                </li>
              </ul>
            </CardContent>
            <CardFooter className="p-6 pt-0 flex gap-2.5">
              <Link href="/csdl/hoc" className="flex-1">
                <Button className="w-full font-semibold text-xs h-9 shadow-xs bg-indigo-600 hover:bg-indigo-700 text-white">
                  Vào Học Tương Tác
                  <ArrowRight className="h-3.5 w-3.5 ml-1" />
                </Button>
              </Link>
            </CardFooter>
          </Card>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-border py-6 px-4 text-center text-xs text-muted-foreground bg-card">
        <p>UET Study Hub • Hệ thống Tự học & Luyện thi Tương tác Đại học Công nghệ (VNU - UET)</p>
      </footer>
    </div>
  );
}
