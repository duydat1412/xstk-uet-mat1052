import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card";
import { ArrowRight, BookOpen, CheckCircle, GraduationCap, Database, Sigma, FileText, HelpCircle, Compass } from "lucide-react";

export default function HomePage() {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 dark:bg-slate-950 dark:text-slate-50 flex flex-col font-sans">
      {/* Header */}
      <header className="sticky top-0 z-50 w-full border-b border-slate-200 bg-white/90 backdrop-blur-md dark:border-slate-800 dark:bg-slate-900/90 shadow-xs">
        <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <span className="text-2xl">🏛️</span>
            <div className="flex flex-col leading-tight">
              <span className="font-black text-base text-slate-900 dark:text-slate-100">UET STUDY HUB</span>
              <span className="text-[11px] font-bold text-slate-500 dark:text-slate-400">
                Cổng Học Tập & Luyện Thi Tương Tác VNU-UET
              </span>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <Link href="/xstk/hoc">
              <Button variant="outline" size="sm" className="font-bold text-xs">
                🎲 XSTK
              </Button>
            </Link>
            <Link href="/csdl/hoc">
              <Button variant="default" size="sm" className="font-bold text-xs">
                🗄️ CSDL
              </Button>
            </Link>
          </div>
        </div>
      </header>

      {/* Hero */}
      <section className="relative overflow-hidden py-16 px-4 border-b border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
        <div className="max-w-5xl mx-auto text-center space-y-4">
          <Badge variant="blueSoft" className="px-3 py-1 font-bold text-xs uppercase tracking-wide">
            Chuẩn Sư phạm Tương tác UET
          </Badge>
          <h1 className="text-3xl sm:text-5xl font-black tracking-tight text-slate-900 dark:text-slate-50">
            Nền tảng Tự học & Luyện thi <span className="text-blue-600 dark:text-blue-400">UET Chuẩn Barem</span>
          </h1>
          <p className="text-sm sm:text-base text-slate-600 dark:text-slate-300 max-w-2xl mx-auto leading-relaxed">
            Học từng bước (Section Stepper), kiểm tra 3 cấp độ (Gatekeeper Quiz), 100% ví dụ bám sát slide bài giảng của giảng viên trường Đại học Công nghệ.
          </p>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-3xl mx-auto pt-6 text-left">
            <div className="p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950">
              <div className="text-2xl font-black text-blue-600 tabular-nums">40 bài</div>
              <div className="text-xs text-slate-500 font-semibold">Bài giảng chi tiết</div>
            </div>
            <div className="p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950">
              <div className="text-2xl font-black text-emerald-600 tabular-nums">120 ví dụ</div>
              <div className="text-xs text-slate-500 font-semibold">100% bám sát Slide</div>
            </div>
            <div className="p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950">
              <div className="text-2xl font-black text-amber-600 tabular-nums">120 câu</div>
              <div className="text-xs text-slate-500 font-semibold">Quiz 3 cấp độ chặn bài</div>
            </div>
            <div className="p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950">
              <div className="text-2xl font-black text-purple-600 tabular-nums">100%</div>
              <div className="text-xs text-slate-500 font-semibold">Có dấu Ref tra cứu slide</div>
            </div>
          </div>
        </div>
      </section>

      {/* Primary Courses Grid */}
      <section className="max-w-6xl mx-auto px-4 py-12 w-full space-y-8">
        <div className="flex flex-col gap-1 text-center sm:text-left">
          <h2 className="text-2xl font-black text-slate-900 dark:text-slate-50 tracking-tight">
            Chọn Môn Học Bắt Đầu
          </h2>
          <p className="text-sm text-slate-500 dark:text-slate-400">
            Mỗi môn học gồm đầy đủ 5 công cụ học tập và thi thử tương tác.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Card 1: XSTK */}
          <Card className="border border-slate-200 dark:border-slate-800 hover:border-blue-400 dark:hover:border-blue-600 transition-all shadow-xs hover:shadow-md bg-white dark:bg-slate-900 flex flex-col justify-between">
            <CardHeader className="p-6 pb-4">
              <div className="flex items-center justify-between mb-2">
                <Badge variant="blueSoft" className="font-bold text-xs">
                  MAT1052
                </Badge>
                <span className="text-2xl">🎲</span>
              </div>
              <CardTitle className="text-xl font-black text-slate-900 dark:text-slate-100">
                Xác suất Thống kê
              </CardTitle>
              <CardDescription className="text-xs text-slate-500 dark:text-slate-400">
                26 bài học chia làm 5 cụm (Dữ liệu, Xác suất, Rời rạc, Liên tục, Hồi quy) bám sát tuần học 1–7 của UET.
              </CardDescription>
            </CardHeader>
            <CardContent className="p-6 pt-0 space-y-3">
              <ul className="text-xs space-y-2 text-slate-600 dark:text-slate-300">
                <li className="flex items-center gap-2">
                  <CheckCircle className="h-4 w-4 text-emerald-500 shrink-0" />
                  <span>26 bài tương tác, 78 ví dụ slide có lời giải</span>
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle className="h-4 w-4 text-emerald-500 shrink-0" />
                  <span>Trắc nghiệm, tự luận chuẩn barem, mẹo bấm Casio</span>
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle className="h-4 w-4 text-emerald-500 shrink-0" />
                  <span>Tra cứu slide PDF tuần 1 đến tuần 7</span>
                </li>
              </ul>
            </CardContent>
            <CardFooter className="p-6 pt-0 flex gap-2">
              <Link href="/xstk/hoc" className="flex-1">
                <Button className="w-full font-bold text-xs shadow-sm">
                  Vào Học Tương Tác
                  <ArrowRight className="h-4 w-4 ml-1" />
                </Button>
              </Link>
              <Link href="/tuluan">
                <Button variant="outline" className="font-bold text-xs">
                  Tự Luận
                </Button>
              </Link>
            </CardFooter>
          </Card>

          {/* Card 2: CSDL */}
          <Card className="border border-slate-200 dark:border-slate-800 hover:border-blue-400 dark:hover:border-blue-600 transition-all shadow-xs hover:shadow-md bg-white dark:bg-slate-900 flex flex-col justify-between">
            <CardHeader className="p-6 pb-4">
              <div className="flex items-center justify-between mb-2">
                <Badge variant="amberSoft" className="font-bold text-xs">
                  INT2207
                </Badge>
                <span className="text-2xl">🗄️</span>
              </div>
              <CardTitle className="text-xl font-black text-slate-900 dark:text-slate-100">
                Cơ sở Dữ liệu
              </CardTitle>
              <CardDescription className="text-xs text-slate-500 dark:text-slate-400">
                14 bài học chia làm 4 chương (Tổng quan, Mô hình ER, Đại số quan hệ & SQL, Phụ thuộc hàm & Chuẩn hóa BCNF/3NF).
              </CardDescription>
            </CardHeader>
            <CardContent className="p-6 pt-0 space-y-3">
              <ul className="text-xs space-y-2 text-slate-600 dark:text-slate-300">
                <li className="flex items-center gap-2">
                  <CheckCircle className="h-4 w-4 text-emerald-500 shrink-0" />
                  <span>14 bài tương tác chuẩn UET.IS2099</span>
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle className="h-4 w-4 text-emerald-500 shrink-0" />
                  <span>42 ví dụ slide, 42 câu trắc nghiệm 3 cấp độ</span>
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle className="h-4 w-4 text-emerald-500 shrink-0" />
                  <span>Tra cứu slide PPTX Chương 1, 2, 3, 4</span>
                </li>
              </ul>
            </CardContent>
            <CardFooter className="p-6 pt-0 flex gap-2">
              <Link href="/csdl/hoc" className="flex-1">
                <Button className="w-full font-bold text-xs shadow-sm bg-blue-600 hover:bg-blue-700">
                  Vào Học Tương Tác
                  <ArrowRight className="h-4 w-4 ml-1" />
                </Button>
              </Link>
            </CardFooter>
          </Card>
        </div>
      </section>
    </div>
  );
}
