"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { Course, Lesson } from "@/types/course";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { Sheet, SheetContent, SheetTrigger, SheetHeader, SheetTitle } from "@/components/ui/sheet";
import { MathBlock } from "@/components/math-block";
import {
  Folder,
  FolderOpen,
  ChevronRight,
  CheckCircle2,
  Lock,
  ArrowLeft,
  ArrowRight,
  Search,
  BookOpen,
  AlertTriangle,
  HelpCircle,
  Menu,
  Sun,
  Moon,
  ExternalLink,
  GraduationCap
} from "lucide-react";

interface CourseStudyViewProps {
  course: Course;
}

export function CourseStudyView({ course }: CourseStudyViewProps) {
  const [curLessonIdx, setCurLessonIdx] = useState<number>(0);
  const [curSubTab, setCurSubTab] = useState<string>("theory");
  const [openFolders, setOpenFolders] = useState<Record<string, boolean>>({});
  const [searchQuery, setSearchQuery] = useState<string>("");
  const [completedLessons, setCompletedLessons] = useState<Record<string, boolean>>({});
  const [quizAnswers, setQuizAnswers] = useState<Record<string, Record<number, number>>>({});
  const [theme, setTheme] = useState<"light" | "dark">("light");
  const [isMobileOpen, setIsMobileOpen] = useState(false);

  const curLesson: Lesson = course.lessons[curLessonIdx] || course.lessons[0];

  // Initialize theme & state from localStorage
  useEffect(() => {
    try {
      const savedTheme = (localStorage.getItem("uet_study_theme") as "light" | "dark") ||
        (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      setTheme(savedTheme);
      document.documentElement.setAttribute("data-theme", savedTheme);

      const storageKey = `${course.id}_progress`;
      const saved = JSON.parse(localStorage.getItem(storageKey) || "{}");
      if (saved.done) setCompletedLessons(saved.done);
      if (typeof saved.curIdx === "number" && saved.curIdx >= 0 && saved.curIdx < course.lessons.length) {
        setCurLessonIdx(saved.curIdx);
      }
    } catch (e) {}
  }, [course.id, course.lessons.length]);

  // Open the folder containing the current lesson
  useEffect(() => {
    if (curLesson) {
      setOpenFolders((prev) => ({ ...prev, [curLesson.cluster]: true }));
    }
  }, [curLesson]);

  const toggleTheme = () => {
    const next = theme === "dark" ? "light" : "dark";
    setTheme(next);
    document.documentElement.setAttribute("data-theme", next);
    try {
      localStorage.setItem("uet_study_theme", next);
    } catch (e) {}
  };

  const toggleFolder = (clusterKey: string) => {
    setOpenFolders((prev) => ({ ...prev, [clusterKey]: !prev[clusterKey] }));
  };

  const handleLessonSelect = (idx: number) => {
    setCurLessonIdx(idx);
    setCurSubTab("theory");
    setIsMobileOpen(false);
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleAnswerQuiz = (lessonId: string, qIdx: number, optIdx: number) => {
    setQuizAnswers((prev) => {
      const lessonAns = { ...(prev[lessonId] || {}) };
      lessonAns[qIdx] = optIdx;
      const updated = { ...prev, [lessonId]: lessonAns };

      // Check if all quizzes answered correctly
      const totalQuizzes = curLesson.quizzes.length;
      let allCorrect = true;
      for (let i = 0; i < totalQuizzes; i++) {
        if (lessonAns[i] !== curLesson.quizzes[i].ans) {
          allCorrect = false;
          break;
        }
      }

      if (allCorrect) {
        setCompletedLessons((prevDone) => {
          const nextDone = { ...prevDone, [lessonId]: true };
          try {
            localStorage.setItem(
              `${course.id}_progress`,
              JSON.stringify({ done: nextDone, curIdx: curLessonIdx })
            );
          } catch (e) {}
          return nextDone;
        });
      }

      return updated;
    });
  };

  const isCurrentQuizPassed = !!completedLessons[curLesson?.id];

  const subTabs = [
    { id: "theory", label: "1. Lý thuyết", icon: BookOpen },
    { id: "examples", label: "2. Ba Ví dụ", icon: GraduationCap },
    { id: "pitfalls", label: "3. Cạm bẫy", icon: AlertTriangle },
    { id: "quiz", label: "4. Kiểm tra", icon: HelpCircle },
  ];

  const handleNextSection = () => {
    const tabIdx = subTabs.findIndex((t) => t.id === curSubTab);
    if (tabIdx < subTabs.length - 1) {
      setCurSubTab(subTabs[tabIdx + 1].id);
      window.scrollTo({ top: 180, behavior: "smooth" });
    } else {
      if (isCurrentQuizPassed && curLessonIdx < course.lessons.length - 1) {
        handleLessonSelect(curLessonIdx + 1);
      }
    }
  };

  const handlePrevSection = () => {
    const tabIdx = subTabs.findIndex((t) => t.id === curSubTab);
    if (tabIdx > 0) {
      setCurSubTab(subTabs[tabIdx - 1].id);
      window.scrollTo({ top: 180, behavior: "smooth" });
    } else if (curLessonIdx > 0) {
      handleLessonSelect(curLessonIdx - 1);
    }
  };

  // Group lessons by cluster
  const groupedLessons = course.lessons.reduce((acc, l, idx) => {
    if (!acc[l.cluster]) acc[l.cluster] = [];
    acc[l.cluster].push({ ...l, globalIdx: idx });
    return acc;
  }, {} as Record<string, (Lesson & { globalIdx: number })[]>);

  // Render Sidebar Tree Content (Used for both Desktop & Mobile Sheet)
  const renderSidebarTree = () => (
    <div className="flex flex-col h-full space-y-4">
      {/* Search Bar */}
      <div className="relative">
        <Search className="absolute left-3 top-2.5 h-4 w-4 text-slate-400" />
        <Input
          placeholder="Tìm kiếm bài học..."
          value={searchQuery}
          onChange={(e) => {
            setSearchQuery(e.target.value);
            if (e.target.value) {
              // Expand all folders on search
              const allOpen: Record<string, boolean> = {};
              Object.keys(course.clusters).forEach((k) => (allOpen[k] = true));
              setOpenFolders(allOpen);
            }
          }}
          className="pl-9 h-9 text-xs"
        />
      </div>

      {/* Folders List */}
      <div className="flex-1 overflow-y-auto pr-1 space-y-2">
        {Object.entries(course.clusters).map(([clusterKey, clusterTitle]) => {
          const list = groupedLessons[clusterKey] || [];
          const filtered = list.filter(
            (l) =>
              !searchQuery ||
              l.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
              l.id.toLowerCase().includes(searchQuery.toLowerCase())
          );
          if (filtered.length === 0 && searchQuery) return null;

          const isOpen = !!openFolders[clusterKey];

          return (
            <div key={clusterKey} className="rounded-lg border border-slate-200/60 dark:border-slate-800/60 overflow-hidden bg-slate-50/50 dark:bg-slate-900/50">
              <button
                onClick={() => toggleFolder(clusterKey)}
                className="w-full flex items-center justify-between p-2.5 text-left font-bold text-xs hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
              >
                <div className="flex items-center gap-2 overflow-hidden">
                  <ChevronRight
                    className={`h-3.5 w-3.5 shrink-0 text-slate-400 transition-transform duration-200 ${
                      isOpen ? "rotate-90" : ""
                    }`}
                  />
                  {isOpen ? (
                    <FolderOpen className="h-4 w-4 shrink-0 text-blue-500" />
                  ) : (
                    <Folder className="h-4 w-4 shrink-0 text-slate-400" />
                  )}
                  <span className="truncate text-slate-900 dark:text-slate-100">{clusterTitle}</span>
                </div>
                <Badge variant="secondary" className="text-[10px] px-1.5 py-0 h-4">
                  {list.length} bài
                </Badge>
              </button>

              {isOpen && (
                <div className="p-1 space-y-0.5 border-t border-slate-200/60 dark:border-slate-800/60 bg-white dark:bg-slate-950">
                  {filtered.map((l) => {
                    const isActive = l.globalIdx === curLessonIdx;
                    const isDone = !!completedLessons[l.id];

                    return (
                      <button
                        key={l.id}
                        onClick={() => handleLessonSelect(l.globalIdx)}
                        className={`w-full flex items-center justify-between px-2.5 py-2 rounded-md text-xs font-medium text-left transition-all ${
                          isActive
                            ? "bg-blue-50 text-blue-700 font-bold dark:bg-blue-950/70 dark:text-blue-300 border-l-2 border-blue-600"
                            : "text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-900 hover:text-slate-900 dark:hover:text-slate-100"
                        }`}
                      >
                        <span className="truncate pr-2">
                          <span className="font-semibold text-slate-500 mr-1">{l.id}:</span>
                          {l.title.split(":")[1]?.trim() || l.title}
                        </span>
                        {isDone && (
                          <CheckCircle2 className="h-3.5 w-3.5 shrink-0 text-emerald-500" />
                        )}
                      </button>
                    );
                  })}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 dark:bg-slate-950 dark:text-slate-100 flex flex-col font-sans antialiased">
      {/* Header Bar */}
      <header className="sticky top-0 z-40 w-full border-b border-slate-200 bg-white/90 backdrop-blur-md dark:border-slate-800 dark:bg-slate-900/90 shadow-xs">
        <div className="max-w-7xl mx-auto px-4 h-14 flex items-center justify-between gap-4">
          {/* Logo & Course */}
          <div className="flex items-center gap-3">
            <Link
              href="/"
              className="flex items-center gap-2 text-slate-900 dark:text-slate-100 font-extrabold text-base tracking-tight hover:opacity-80 transition-opacity"
            >
              <span className="text-xl">{course.icon}</span>
              <div className="flex flex-col leading-tight">
                <span className="font-black text-sm">{course.title}</span>
                <span className="text-[10px] text-slate-500 dark:text-slate-400 font-bold">
                  {course.code} • UET Study Hub
                </span>
              </div>
            </Link>
          </div>

          {/* Course Switcher */}
          <div className="inline-flex items-center bg-slate-100 dark:bg-slate-800 p-1 rounded-lg border border-slate-200 dark:border-slate-700">
            <Link
              href="/xstk/hoc"
              className={`flex items-center gap-1.5 px-3 py-1 rounded-md text-xs font-bold transition-all ${
                course.id === "xstk"
                  ? "bg-white text-blue-600 shadow-xs dark:bg-slate-900 dark:text-blue-400"
                  : "text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-slate-100"
              }`}
            >
              <span>🎲</span> XSTK
            </Link>
            <Link
              href="/csdl/hoc"
              className={`flex items-center gap-1.5 px-3 py-1 rounded-md text-xs font-bold transition-all ${
                course.id === "csdl"
                  ? "bg-white text-blue-600 shadow-xs dark:bg-slate-900 dark:text-blue-400"
                  : "text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-slate-100"
              }`}
            >
              <span>🗄️</span> CSDL
            </Link>
          </div>

          {/* Right Actions: Theme & Hub link */}
          <div className="flex items-center gap-2">
            <Link
              href="/"
              className="hidden sm:inline-flex items-center text-xs font-semibold px-2.5 py-1.5 rounded-lg border border-slate-200 dark:border-slate-800 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-600 dark:text-slate-300 transition-colors"
            >
              🏛️ Trang chủ Hub
            </Link>
            <Button
              variant="outline"
              size="icon"
              onClick={toggleTheme}
              aria-label="Toggle Theme"
              className="h-8 w-8"
            >
              {theme === "dark" ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
            </Button>
          </div>
        </div>
      </header>

      {/* Main Study Container */}
      <div className="max-w-7xl mx-auto px-4 py-6 w-full flex-1 flex gap-6">
        {/* Desktop Sidebar: Sticky 320px */}
        <aside className="hidden lg:flex w-80 shrink-0 sticky top-20 h-[calc(100vh-6rem)] flex-col rounded-xl border border-slate-200 bg-white p-4 shadow-xs dark:border-slate-800 dark:bg-slate-900">
          <div className="flex items-center justify-between pb-3 border-b border-slate-200 dark:border-slate-800">
            <span className="font-extrabold text-sm flex items-center gap-2 text-slate-900 dark:text-slate-100">
              📁 Mục Lục Bài Học
            </span>
            <Badge variant="blueSoft" className="tabular-nums">
              {course.total_lessons} bài
            </Badge>
          </div>
          <div className="mt-3 flex-1 overflow-hidden">{renderSidebarTree()}</div>
        </aside>

        {/* Mobile Header Bar & Drawer Trigger */}
        <div className="lg:hidden w-full flex flex-col gap-4">
          <div className="flex items-center justify-between p-3 rounded-xl border border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-900 shadow-xs">
            <div className="flex flex-col truncate pr-2">
              <span className="text-[11px] font-bold text-blue-600 dark:text-blue-400">
                Bài {curLessonIdx + 1} / {course.total_lessons}
              </span>
              <span className="text-xs font-extrabold truncate text-slate-900 dark:text-slate-100">
                {curLesson?.id}: {curLesson?.title}
              </span>
            </div>
            <Sheet open={isMobileOpen} onOpenChange={setIsMobileOpen}>
              <SheetTrigger asChild>
                <Button variant="outline" size="sm" className="gap-1.5 shrink-0 text-xs">
                  <Menu className="h-3.5 w-3.5" />
                  Mục lục
                </Button>
              </SheetTrigger>
              <SheetContent side="left" className="w-[300px] sm:w-[360px] p-4 flex flex-col">
                <SheetHeader className="text-left pb-3 border-b border-slate-200 dark:border-slate-800">
                  <SheetTitle className="text-sm font-bold flex items-center gap-2">
                    <span>{course.icon}</span> Mục Lục {course.title}
                  </SheetTitle>
                </SheetHeader>
                <div className="mt-4 flex-1 overflow-hidden">{renderSidebarTree()}</div>
              </SheetContent>
            </Sheet>
          </div>
        </div>

        {/* Lesson Main Content Area */}
        <main className="flex-1 min-w-0 max-w-4xl space-y-6">
          {/* Lesson Header Card */}
          <Card className="border border-slate-200 shadow-xs bg-white dark:border-slate-800 dark:bg-slate-900">
            <CardHeader className="p-6 pb-4 space-y-2">
              <div className="flex flex-wrap items-center gap-2">
                <Badge variant="blueSoft" className="font-bold text-xs">
                  {course.clusters[curLesson?.cluster] || `Cụm ${curLesson?.cluster}`}
                </Badge>
                {curLesson?.chapter_badge && (
                  <Badge variant="secondary" className="text-xs">
                    {curLesson.chapter_badge}
                  </Badge>
                )}
                {isCurrentQuizPassed && (
                  <Badge variant="success" className="gap-1 text-xs font-bold">
                    <CheckCircle2 className="h-3 w-3" /> Đã hoàn thành
                  </Badge>
                )}
              </div>
              <CardTitle className="text-xl sm:text-2xl font-black tracking-tight text-slate-900 dark:text-slate-50">
                {curLesson?.title}
              </CardTitle>
              {curLesson?.desc && (
                <p className="text-sm text-slate-600 dark:text-slate-400 leading-relaxed max-w-3xl">
                  {curLesson.desc}
                </p>
              )}
            </CardHeader>
          </Card>

          {/* Sequential Section Stepper Tabs */}
          <Tabs value={curSubTab} onValueChange={setCurSubTab} className="w-full">
            <TabsList className="w-full grid grid-cols-2 sm:grid-cols-4 h-auto p-1 bg-slate-100 dark:bg-slate-800/80 rounded-xl">
              {subTabs.map((tab) => {
                const Icon = tab.icon;
                return (
                  <TabsTrigger
                    key={tab.id}
                    value={tab.id}
                    className="flex items-center justify-center gap-1.5 py-2 text-xs sm:text-sm font-bold"
                  >
                    <Icon className="h-4 w-4" />
                    <span>{tab.label}</span>
                  </TabsTrigger>
                );
              })}
            </TabsList>

            {/* Sub-tab 1: Theory Steps */}
            <TabsContent value="theory" className="space-y-4 pt-2">
              {curLesson?.theory_steps.map((step, idx) => (
                <Card
                  key={idx}
                  className="border border-slate-200/80 bg-white dark:border-slate-800/80 dark:bg-slate-900 shadow-xs overflow-hidden"
                >
                  <CardHeader className="bg-slate-50/70 dark:bg-slate-800/50 p-4 border-b border-slate-200/60 dark:border-slate-800/60 flex flex-row items-center justify-between">
                    <span className="font-bold text-sm text-slate-900 dark:text-slate-100 flex items-center gap-2">
                      <Badge variant="outline" className="font-black text-blue-600 dark:text-blue-400">
                        Bước {step.step_num || idx + 1}
                      </Badge>
                      {step.title}
                    </span>
                  </CardHeader>
                  <CardContent className="p-5 text-sm leading-relaxed text-slate-700 dark:text-slate-300">
                    <div
                      dangerouslySetInnerHTML={{ __html: step.content }}
                      className="prose dark:prose-invert max-w-none space-y-2 [&_p]:mb-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ul]:mb-2 [&_li]:mb-1 [&_b]:text-slate-900 dark:[&_b]:text-slate-100 [&_.tip-box]:bg-blue-50/80 dark:[&_.tip-box]:bg-blue-950/40 [&_.tip-box]:border-l-4 [&_.tip-box]:border-blue-500 [&_.tip-box]:p-3 [&_.tip-box]:rounded-r-lg [&_.tip-box]:my-3"
                    />
                  </CardContent>
                </Card>
              ))}
            </TabsContent>

            {/* Sub-tab 2: 3 Examples */}
            <TabsContent value="examples" className="space-y-4 pt-2">
              <div className="text-xs font-semibold text-slate-500 dark:text-slate-400 mb-2">
                📌 100% Ví dụ mẫu trích xuất trực tiếp từ Slide bài giảng UET:
              </div>
              {curLesson?.examples.map((ex, idx) => {
                const badgeVariant =
                  idx === 0 ? "emeraldSoft" : idx === 1 ? "amberSoft" : "roseSoft";
                return (
                  <Card
                    key={idx}
                    className="border border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-900 shadow-xs"
                  >
                    <CardHeader className="p-4 border-b border-slate-200 dark:border-slate-800 flex flex-row items-center justify-between">
                      <span className="font-bold text-sm text-slate-900 dark:text-slate-100">
                        Ví dụ {idx + 1}
                      </span>
                      <Badge variant={badgeVariant} className="font-bold">
                        {ex.level}
                      </Badge>
                    </CardHeader>
                    <CardContent className="p-5 space-y-4 text-sm">
                      <div className="bg-slate-50 dark:bg-slate-800/60 p-3.5 rounded-lg border-l-4 border-blue-500 text-slate-800 dark:text-slate-200 leading-relaxed">
                        <div className="font-bold text-xs text-blue-600 dark:text-blue-400 mb-1">
                          ĐỀ BÀI:
                        </div>
                        <div dangerouslySetInnerHTML={{ __html: ex.problem }} />
                      </div>
                      <div className="space-y-2 text-slate-700 dark:text-slate-300 leading-relaxed">
                        <div className="font-bold text-xs text-slate-500 dark:text-slate-400">
                          HƯỚNG DẪN GIẢI CHI TIẾT:
                        </div>
                        <div
                          dangerouslySetInnerHTML={{ __html: ex.solution }}
                          className="space-y-1.5 [&_b]:text-slate-900 dark:[&_b]:text-slate-100"
                        />
                      </div>
                    </CardContent>
                  </Card>
                );
              })}
            </TabsContent>

            {/* Sub-tab 3: Pitfalls (Cạm bẫy) */}
            <TabsContent value="pitfalls" className="space-y-4 pt-2">
              <div className="text-xs font-semibold text-slate-500 dark:text-slate-400 mb-2">
                ⚠️ Đối chiếu song song các lỗi sai kinh điển trong đề thi UET:
              </div>
              {curLesson?.pitfalls.map((p, idx) => (
                <div
                  key={idx}
                  className="grid grid-cols-1 md:grid-cols-2 gap-4 rounded-xl border border-slate-200 dark:border-slate-800 p-4 bg-white dark:bg-slate-900"
                >
                  {/* Sai */}
                  <div className="p-4 rounded-lg bg-red-50/70 border border-red-200/80 dark:bg-red-950/40 dark:border-red-900/60 space-y-2">
                    <div className="flex items-center gap-2 font-bold text-xs text-red-600 dark:text-red-400 uppercase tracking-wider">
                      <span>❌</span> Cách nghĩ sai phổ biến
                    </div>
                    <div
                      dangerouslySetInnerHTML={{ __html: p.bad }}
                      className="text-xs leading-relaxed text-slate-800 dark:text-slate-200"
                    />
                  </div>

                  {/* Đúng */}
                  <div className="p-4 rounded-lg bg-emerald-50/70 border border-emerald-200/80 dark:bg-emerald-950/40 dark:border-emerald-900/60 space-y-2">
                    <div className="flex items-center gap-2 font-bold text-xs text-emerald-600 dark:text-emerald-400 uppercase tracking-wider">
                      <span>✅</span> Quy tắc chuẩn thi UET
                    </div>
                    <div
                      dangerouslySetInnerHTML={{ __html: p.good }}
                      className="text-xs leading-relaxed text-slate-800 dark:text-slate-200"
                    />
                  </div>
                </div>
              ))}
            </TabsContent>

            {/* Sub-tab 4: 3-Level Gatekeeper Quiz */}
            <TabsContent value="quiz" className="space-y-6 pt-2">
              <div className="bg-blue-50 dark:bg-blue-950/40 border border-blue-200 dark:border-blue-900/60 p-4 rounded-xl flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="p-2 rounded-lg bg-blue-600 text-white">
                    <HelpCircle className="h-5 w-5" />
                  </div>
                  <div>
                    <h4 className="font-extrabold text-sm text-slate-900 dark:text-slate-50">
                      Bài kiểm tra 3 cấp độ (Gatekeeper Quiz)
                    </h4>
                    <p className="text-xs text-slate-500 dark:text-slate-400">
                      Làm đúng cả 3 câu hỏi để hoàn thành bài học và mở khóa bài tiếp theo.
                    </p>
                  </div>
                </div>
                {isCurrentQuizPassed && (
                  <Badge variant="success" className="font-bold text-xs">
                    🎉 Đã hoàn thành bài
                  </Badge>
                )}
              </div>

              {curLesson?.quizzes.map((quiz, qIdx) => {
                const userChoice = quizAnswers[curLesson.id]?.[qIdx];
                const isAnswered = typeof userChoice === "number";
                const isCorrect = userChoice === quiz.ans;
                const levelNames = [
                  "🟢 Cấp độ 1 — Nhận biết",
                  "🟡 Cấp độ 2 — Thông hiểu",
                  "🔴 Cấp độ 3 — Vận dụng & Cạm bẫy",
                ];

                return (
                  <Card
                    key={qIdx}
                    className="border border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-900 shadow-xs"
                  >
                    <CardHeader className="p-4 border-b border-slate-200 dark:border-slate-800 flex flex-row items-center justify-between">
                      <span className="font-extrabold text-xs text-slate-700 dark:text-slate-300">
                        {levelNames[quiz.level - 1] || `Câu hỏi ${qIdx + 1}`}
                      </span>
                      {isAnswered && (
                        <Badge
                          variant={isCorrect ? "success" : "destructive"}
                          className="font-bold text-[10px]"
                        >
                          {isCorrect ? "Chính xác ✓" : "Chưa đúng ✕"}
                        </Badge>
                      )}
                    </CardHeader>

                    <CardContent className="p-5 space-y-4">
                      <div className="font-bold text-sm text-slate-900 dark:text-slate-100 leading-snug">
                        {quiz.q}
                      </div>

                      {/* Options */}
                      <div className="space-y-2">
                        {quiz.opts.map((opt, optIdx) => {
                          const isSelected = userChoice === optIdx;
                          let optStyle =
                            "border-slate-200 dark:border-slate-800 hover:border-blue-400 bg-white dark:bg-slate-950";

                          if (isAnswered) {
                            if (optIdx === quiz.ans) {
                              optStyle =
                                "border-emerald-500 bg-emerald-50/80 dark:bg-emerald-950/60 text-emerald-900 dark:text-emerald-100 font-bold";
                            } else if (isSelected && !isCorrect) {
                              optStyle =
                                "border-red-500 bg-red-50/80 dark:bg-red-950/60 text-red-900 dark:text-red-100";
                            }
                          }

                          return (
                            <button
                              key={optIdx}
                              onClick={() => handleAnswerQuiz(curLesson.id, qIdx, optIdx)}
                              className={`w-full flex items-start gap-3 p-3.5 rounded-lg border text-left text-xs sm:text-sm transition-all ${optStyle}`}
                            >
                              <span className="w-5 h-5 rounded-full border border-slate-300 dark:border-slate-700 flex items-center justify-center font-bold text-xs shrink-0 bg-slate-100 dark:bg-slate-800">
                                {String.fromCharCode(65 + optIdx)}
                              </span>
                              <span className="flex-1 leading-normal">{opt}</span>
                            </button>
                          );
                        })}
                      </div>

                      {/* Feedback Box */}
                      {isAnswered && (
                        <div
                          className={`p-3.5 rounded-lg text-xs leading-relaxed border ${
                            isCorrect
                              ? "bg-emerald-50 border-emerald-200 text-emerald-900 dark:bg-emerald-950/60 dark:border-emerald-900 dark:text-emerald-200"
                              : "bg-red-50 border-red-200 text-red-900 dark:bg-red-950/60 dark:border-red-900 dark:text-red-200"
                          }`}
                        >
                          <div className="font-bold mb-1">
                            {isCorrect ? "✅ GIẢI THÍCH CHÍNH XÁC:" : "💡 HƯỚNG DẪN GIẢI LẠI:"}
                          </div>
                          <div>{quiz.fb}</div>
                        </div>
                      )}
                    </CardContent>
                  </Card>
                );
              })}
            </TabsContent>
          </Tabs>

          {/* Lecture Reference Metadata Box (Dấu Ref) */}
          {curLesson?.ref && (
            <Card className="border border-slate-200 dark:border-slate-800 bg-slate-50/80 dark:bg-slate-900/60 rounded-xl overflow-hidden shadow-xs">
              <CardHeader className="p-4 border-b border-slate-200/80 dark:border-slate-800/80 flex flex-wrap items-center justify-between gap-2">
                <span className="font-extrabold text-xs text-blue-600 dark:text-blue-400 flex items-center gap-1.5 uppercase tracking-wide">
                  📌 Dấu Ref Tra cứu Slide Bài Giảng ({course.code})
                </span>
                {curLesson.ref.slide_file && (
                  <a
                    href={`/${curLesson.ref.slide_file}#page=${curLesson.ref.page_start}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-1.5 text-xs font-bold text-white bg-blue-600 hover:bg-blue-700 px-3 py-1.5 rounded-lg shadow-xs transition-colors"
                  >
                    📄 Mở Slide trang {curLesson.ref.page_start}
                    <ExternalLink className="h-3 w-3" />
                  </a>
                )}
              </CardHeader>
              <CardContent className="p-4 space-y-2 text-xs">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-slate-700 dark:text-slate-300">
                  <div>
                    <span className="font-bold text-slate-500">File Slide: </span>
                    <span className="font-semibold">{curLesson.ref.slide_name}</span> (<code>{curLesson.ref.slide_file}</code>)
                  </div>
                  <div>
                    <span className="font-bold text-slate-500">Vị trí: </span>
                    <span className="font-semibold">{curLesson.ref.pages}</span> — {curLesson.ref.section}
                  </div>
                </div>
                {curLesson.ref.remind && (
                  <div className="mt-2 p-2.5 rounded-md bg-blue-100/60 dark:bg-blue-950/60 border border-blue-200 dark:border-blue-900 text-slate-800 dark:text-slate-200 leading-relaxed">
                    <b>💡 Lời nhắc khi đọc không hiểu:</b> {curLesson.ref.remind}
                  </div>
                )}
              </CardContent>
            </Card>
          )}

          {/* Bottom Navigation Buttons (Sequential Stepper) */}
          <div className="pt-4 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between gap-4">
            <Button
              variant="outline"
              onClick={handlePrevSection}
              disabled={curLessonIdx === 0 && curSubTab === "theory"}
              className="font-bold text-xs sm:text-sm"
            >
              <ArrowLeft className="h-4 w-4 mr-1" />
              {curSubTab === "theory" ? "Bài trước" : "Phần trước"}
            </Button>

            <Button
              onClick={handleNextSection}
              disabled={curSubTab === "quiz" && !isCurrentQuizPassed}
              className="font-bold text-xs sm:text-sm shadow-md"
            >
              {curSubTab !== "quiz" ? (
                <>
                  Sang phần tiếp theo
                  <ArrowRight className="h-4 w-4 ml-1" />
                </>
              ) : isCurrentQuizPassed ? (
                curLessonIdx < course.lessons.length - 1 ? (
                  <>
                    Mở bài tiếp: {course.lessons[curLessonIdx + 1]?.id}
                    <ArrowRight className="h-4 w-4 ml-1" />
                  </>
                ) : (
                  "🏆 Bạn đã hoàn thành toàn bộ khóa học!"
                )
              ) : (
                <>
                  <Lock className="h-4 w-4 mr-1" />
                  Làm đúng trắc nghiệm để mở bài tiếp
                </>
              )}
            </Button>
          </div>
        </main>
      </div>
    </div>
  );
}
