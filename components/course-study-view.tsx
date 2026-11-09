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
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";
import { Progress } from "@/components/ui/progress";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
} from "@/components/ui/dialog";
import { GithubIcon } from "@/components/icons";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import {
  Folder,
  FolderOpen,
  ChevronRight,
  ChevronDown,
  CheckCircle2,
  XCircle,
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
  GraduationCap,
  Sparkles,
  BookmarkCheck,
  Info,
  Layers,
  Sigma,
  Database,
  Check,
  CheckCheck,
  ShieldCheck,
  SlidersHorizontal,
  Keyboard,
  Command,
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
  const [isShortcutsOpen, setIsShortcutsOpen] = useState(false);
  const searchInputRef = React.useRef<HTMLInputElement>(null);

  const curLesson: Lesson = course.lessons[curLessonIdx] || course.lessons[0];

  const applyTheme = (targetTheme: "light" | "dark") => {
    setTheme(targetTheme);
    if (targetTheme === "dark") {
      document.documentElement.classList.add("dark");
      document.documentElement.setAttribute("data-theme", "dark");
      document.documentElement.style.colorScheme = "dark";
    } else {
      document.documentElement.classList.remove("dark");
      document.documentElement.setAttribute("data-theme", "light");
      document.documentElement.style.colorScheme = "light";
    }
    try {
      localStorage.setItem("uet_study_theme", targetTheme);
    } catch (e) {}
  };

  const toggleTheme = () => {
    applyTheme(theme === "dark" ? "light" : "dark");
  };

  // Initialize theme & state from localStorage
  useEffect(() => {
    try {
      const savedTheme =
        (localStorage.getItem("uet_study_theme") as "light" | "dark") ||
        (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      applyTheme(savedTheme);

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
    { id: "theory", label: "Lý thuyết", stepNum: 1, icon: BookOpen },
    { id: "examples", label: "3 Ví dụ mẫu", stepNum: 2, icon: GraduationCap },
    { id: "pitfalls", label: "Cạm bẫy thi", stepNum: 3, icon: AlertTriangle },
    { id: "quiz", label: "Bài kiểm tra", stepNum: 4, icon: ShieldCheck },
  ];

  const handleNextSection = () => {
    const tabIdx = subTabs.findIndex((t) => t.id === curSubTab);
    if (tabIdx < subTabs.length - 1) {
      setCurSubTab(subTabs[tabIdx + 1].id);
      window.scrollTo({ top: 160, behavior: "smooth" });
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
      window.scrollTo({ top: 160, behavior: "smooth" });
    } else if (curLessonIdx > 0) {
      handleLessonSelect(curLessonIdx - 1);
    }
  };

  // Global Keyboard Shortcuts (Like Linear, Raycast, Vercel)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      const isInput =
        document.activeElement?.tagName === "INPUT" ||
        document.activeElement?.tagName === "TEXTAREA" ||
        (document.activeElement as HTMLElement)?.isContentEditable;

      // Cmd+K or Ctrl+K -> Focus Search
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        searchInputRef.current?.focus();
        return;
      }

      // Escape -> Clear Search or Close Shortcuts Dialog
      if (e.key === "Escape") {
        if (searchQuery) setSearchQuery("");
        searchInputRef.current?.blur();
        setIsShortcutsOpen(false);
        return;
      }

      // Below shortcuts only when not typing inside an input
      if (isInput) return;

      // '?' -> Toggle Shortcuts Dialog
      if (e.key === "?" || (e.shiftKey && e.key === "/")) {
        e.preventDefault();
        setIsShortcutsOpen((prev) => !prev);
        return;
      }

      // 't' or 'T' -> Toggle Theme
      if (e.key.toLowerCase() === "t" && !e.ctrlKey && !e.metaKey && !e.altKey) {
        e.preventDefault();
        toggleTheme();
        return;
      }

      // '1' - '4' -> Switch Sub Tabs
      if (["1", "2", "3", "4"].includes(e.key)) {
        e.preventDefault();
        const tabMap = ["theory", "examples", "pitfalls", "quiz"];
        const target = tabMap[parseInt(e.key) - 1];
        if (target) {
          setCurSubTab(target);
          window.scrollTo({ top: 160, behavior: "smooth" });
        }
        return;
      }

      // Alt + ArrowRight / Alt + ArrowLeft -> Next / Prev Section
      if (e.altKey && e.key === "ArrowRight") {
        e.preventDefault();
        handleNextSection();
        return;
      }
      if (e.altKey && e.key === "ArrowLeft") {
        e.preventDefault();
        handlePrevSection();
        return;
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [searchQuery, curSubTab, curLessonIdx, isCurrentQuizPassed, course.lessons.length]);

  // Group lessons by cluster
  const groupedLessons = course.lessons.reduce((acc, l, idx) => {
    if (!acc[l.cluster]) acc[l.cluster] = [];
    acc[l.cluster].push({ ...l, globalIdx: idx });
    return acc;
  }, {} as Record<string, (Lesson & { globalIdx: number })[]>);

  const completedCount = Object.keys(completedLessons).filter((id) =>
    course.lessons.some((l) => l.id === id)
  ).length;
  const progressPercent = Math.round((completedCount / course.total_lessons) * 100);

  // Subject vector icon
  const SubjectIcon = course.id === "xstk" ? Sigma : Database;

  // Render Sidebar Tree Content (Used for both Desktop & Mobile Sheet)
  const renderSidebarTree = () => (
    <div className="flex flex-col h-full space-y-3">
      {/* Search Input with Esc Hint */}
      <div className="relative">
        <Search className="absolute left-3 top-2.5 h-3.5 w-3.5 text-muted-foreground" />
        <Input
          ref={searchInputRef}
          placeholder="Tìm bài học..."
          value={searchQuery}
          onChange={(e) => {
            setSearchQuery(e.target.value);
            if (e.target.value) {
              const allOpen: Record<string, boolean> = {};
              Object.keys(course.clusters).forEach((k) => (allOpen[k] = true));
              setOpenFolders(allOpen);
            }
          }}
          className="pl-8.5 pr-14 h-8.5 text-xs bg-slate-50 dark:bg-slate-900 border-border"
        />
        {searchQuery ? (
          <button
            onClick={() => setSearchQuery("")}
            className="absolute right-2.5 top-2.5 text-xs text-muted-foreground hover:text-foreground cursor-pointer"
          >
            ✕
          </button>
        ) : (
          <kbd className="absolute right-2.5 top-2 flex items-center gap-0.5 text-[9px] font-mono text-muted-foreground bg-muted/80 px-1.5 py-0.5 rounded border border-border pointer-events-none">
            <span>⌘</span>
            <span>K</span>
          </kbd>
        )}
      </div>

      {/* Progress Mini Bar */}
      <div className="p-2.5 rounded-lg bg-slate-50 dark:bg-slate-900/60 border border-border/60 space-y-1.5">
        <div className="flex items-center justify-between text-[11px] font-medium text-muted-foreground">
          <span>Tiến độ hoàn thành</span>
          <span className="font-mono text-foreground font-semibold">
            {completedCount}/{course.total_lessons} bài ({progressPercent}%)
          </span>
        </div>
        <Progress value={progressPercent} className="h-1.5 bg-slate-200 dark:bg-slate-800" />
      </div>

      {/* Folders List with Radix ScrollArea */}
      <ScrollArea className="flex-1 pr-1">
        <div className="space-y-1.5 pb-4">
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
            const clusterCompleted = list.filter((l) => !!completedLessons[l.id]).length;

            return (
              <div
                key={clusterKey}
                className="rounded-lg border border-border/60 overflow-hidden bg-card transition-colors"
              >
                <button
                  onClick={() => toggleFolder(clusterKey)}
                  className="w-full flex items-center justify-between px-3 py-2 text-left text-xs font-semibold hover:bg-muted/50 transition-colors"
                >
                  <div className="flex items-center gap-2 overflow-hidden">
                    <ChevronRight
                      className={`h-3.5 w-3.5 shrink-0 text-muted-foreground transition-transform duration-200 ${
                        isOpen ? "rotate-90" : ""
                      }`}
                    />
                    {isOpen ? (
                      <FolderOpen className="h-4 w-4 shrink-0 text-blue-600 dark:text-blue-400" />
                    ) : (
                      <Folder className="h-4 w-4 shrink-0 text-muted-foreground" />
                    )}
                    <span className="truncate text-foreground font-medium">{clusterTitle}</span>
                  </div>
                  <span className="text-[10px] font-mono font-medium text-muted-foreground bg-muted px-1.5 py-0.5 rounded shrink-0 ml-1.5">
                    {clusterCompleted}/{list.length}
                  </span>
                </button>

                {isOpen && (
                  <div className="p-1 space-y-0.5 border-t border-border/40 bg-background/50">
                    {filtered.map((l) => {
                      const isActive = l.globalIdx === curLessonIdx;
                      const isDone = !!completedLessons[l.id];

                      return (
                        <button
                          key={l.id}
                          onClick={() => handleLessonSelect(l.globalIdx)}
                          className={`w-full flex items-center justify-between px-2.5 py-1.5 rounded-md text-xs text-left transition-all relative ${
                            isActive
                              ? "bg-blue-50 text-blue-700 font-semibold dark:bg-blue-950/70 dark:text-blue-300 ring-1 ring-blue-500/20"
                              : "text-muted-foreground hover:bg-muted hover:text-foreground"
                          }`}
                        >
                          <div className="flex items-center gap-1.5 truncate pr-2">
                            <span className="font-mono text-[10px] opacity-75 shrink-0">
                              {l.id}
                            </span>
                            <span className="truncate text-[11.5px]">
                              {l.title.split(":")[1]?.trim() || l.title}
                            </span>
                          </div>
                          {isDone ? (
                            <CheckCircle2 className="h-3.5 w-3.5 shrink-0 text-emerald-500" />
                          ) : (
                            <span className="h-1.5 w-1.5 rounded-full bg-slate-300 dark:bg-slate-700 shrink-0" />
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
      </ScrollArea>

      {/* Pinned Bottom Shortcuts & GitHub Bar */}
      <div className="pt-2.5 mt-auto border-t border-border/80 flex flex-col gap-2 shrink-0 bg-card">
        {/* Quick Actions Row */}
        <div className="grid grid-cols-2 gap-1.5">
          {/* Keyboard Shortcuts Trigger Button */}
          <button
            onClick={() => setIsShortcutsOpen(true)}
            className="flex items-center justify-between px-2.5 py-1.5 rounded-lg border border-border/80 bg-muted/40 hover:bg-muted text-foreground text-xs font-medium transition-colors group cursor-pointer"
            title="Bảng phím tắt (Nhấn ?)"
          >
            <div className="flex items-center gap-1.5">
              <Keyboard className="h-3.5 w-3.5 text-blue-600 dark:text-blue-400 group-hover:scale-110 transition-transform" />
              <span className="text-[11px] font-semibold">Phím tắt</span>
            </div>
            <kbd className="font-mono text-[9px] text-muted-foreground bg-card px-1 py-0.5 rounded border border-border">
              ?
            </kbd>
          </button>

          {/* GitHub Repository Link */}
          <a
            href="https://github.com/duydat1412/xstk-uet-mat1052"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center justify-between px-2.5 py-1.5 rounded-lg border border-border/80 bg-muted/40 hover:bg-muted text-foreground text-xs font-medium transition-colors group"
            title="Xem mã nguồn trên GitHub"
          >
            <div className="flex items-center gap-1.5">
              <GithubIcon className="h-3.5 w-3.5 text-foreground group-hover:scale-110 transition-transform" />
              <span className="text-[11px] font-semibold">GitHub</span>
            </div>
            <ExternalLink className="h-3 w-3 opacity-60 group-hover:opacity-100 transition-opacity" />
          </a>
        </div>

        {/* Developer Profile & Issues Line */}
        <div className="flex items-center justify-between px-1 text-[11px] text-muted-foreground">
          <a
            href="https://github.com/duydat1412"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-1 hover:text-foreground font-mono text-[10.5px] transition-colors"
            title="GitHub cá nhân của tôi"
          >
            <GithubIcon className="h-3 w-3" />
            <span className="hover:underline">@duydat1412</span>
          </a>

          <a
            href="https://github.com/duydat1412/xstk-uet-mat1052/issues"
            target="_blank"
            rel="noopener noreferrer"
            className="text-[10px] hover:text-foreground hover:underline transition-colors flex items-center gap-1"
          >
            <span>Báo lỗi / Góp ý</span>
            <ExternalLink className="h-2.5 w-2.5 opacity-60" />
          </a>
        </div>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 dark:bg-slate-950 dark:text-slate-100 flex flex-col font-sans antialiased selection:bg-blue-500/20">
      {/* Header Bar */}
      <header className="sticky top-0 z-40 w-full border-b border-border/80 bg-background/80 backdrop-blur-md shadow-xs">
        <div className="max-w-7xl mx-auto px-4 h-14 flex items-center justify-between gap-4">
          {/* Logo & Brand Identity */}
          <div className="flex items-center gap-3">
            <Link
              href="/"
              className="flex items-center gap-2.5 text-foreground hover:opacity-85 transition-opacity"
            >
              <div className="h-8 w-8 rounded-lg bg-blue-600 text-white flex items-center justify-center font-bold shadow-xs">
                <GraduationCap className="h-4.5 w-4.5" />
              </div>
              <div className="flex flex-col leading-tight">
                <div className="flex items-center gap-1.5">
                  <span className="font-extrabold text-sm tracking-tight">UET STUDY HUB</span>
                  <Badge variant="outline" className="text-[9px] px-1 py-0 h-3.5 font-mono uppercase">
                    Interactive
                  </Badge>
                </div>
                <span className="text-[10.5px] text-muted-foreground font-medium truncate max-w-[200px] sm:max-w-none">
                  {course.title} ({course.code})
                </span>
              </div>
            </Link>
          </div>

          {/* Center: Course Switcher Segmented Control */}
          <div className="hidden sm:inline-flex items-center bg-muted/80 p-0.5 rounded-lg border border-border">
            <Link
              href="/xstk/hoc"
              className={`flex items-center gap-1.5 px-3 py-1 rounded-md text-xs font-semibold transition-all ${
                course.id === "xstk"
                  ? "bg-card text-blue-600 shadow-xs dark:text-blue-400"
                  : "text-muted-foreground hover:text-foreground"
              }`}
            >
              <Sigma className="h-3.5 w-3.5 text-blue-500" />
              <span>Xác suất (MAT1052)</span>
            </Link>
            <Link
              href="/csdl/hoc"
              className={`flex items-center gap-1.5 px-3 py-1 rounded-md text-xs font-semibold transition-all ${
                course.id === "csdl"
                  ? "bg-card text-blue-600 shadow-xs dark:text-blue-400"
                  : "text-muted-foreground hover:text-foreground"
              }`}
            >
              <Database className="h-3.5 w-3.5 text-indigo-500" />
              <span>Cơ sở dữ liệu (INT2207)</span>
            </Link>
          </div>

          {/* Right Actions: Mobile Switcher, Theme & Hub link */}
          <div className="flex items-center gap-2">
            {/* Mobile Course Dropdown */}
            <div className="sm:hidden">
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button variant="outline" size="sm" className="h-8 gap-1 text-xs px-2">
                    <SubjectIcon className="h-3.5 w-3.5 text-blue-500" />
                    <span className="font-mono">{course.code}</span>
                    <ChevronDown className="h-3 w-3 opacity-60" />
                  </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent align="end" className="w-48 text-xs">
                  <DropdownMenuItem asChild>
                    <Link href="/xstk/hoc" className="flex items-center gap-2">
                      <Sigma className="h-3.5 w-3.5 text-blue-500" />
                      <span>Xác suất Thống kê (MAT1052)</span>
                    </Link>
                  </DropdownMenuItem>
                  <DropdownMenuItem asChild>
                    <Link href="/csdl/hoc" className="flex items-center gap-2">
                      <Database className="h-3.5 w-3.5 text-indigo-500" />
                      <span>Cơ sở Dữ liệu (INT2207)</span>
                    </Link>
                  </DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>
            </div>

            <Link
              href="/"
              className="hidden md:inline-flex items-center gap-1.5 text-xs font-semibold px-2.5 py-1.5 rounded-lg border border-border hover:bg-muted text-muted-foreground hover:text-foreground transition-colors"
            >
              <Layers className="h-3.5 w-3.5 text-muted-foreground" />
              <span>Portal Hub</span>
            </Link>

            {/* GitHub Repo Link */}
            <a
              href="https://github.com/duydat1412/xstk-uet-mat1052"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center h-8 w-8 rounded-lg border border-border hover:bg-muted text-muted-foreground hover:text-foreground transition-colors"
              title="GitHub: duydat1412/xstk-uet-mat1052"
              aria-label="GitHub Repository"
            >
              <GithubIcon className="h-4 w-4" />
            </a>

            {/* Keyboard Shortcuts Trigger Button */}
            <Button
              variant="outline"
              size="icon"
              onClick={() => setIsShortcutsOpen(true)}
              aria-label="Bảng phím tắt"
              title="Bảng phím tắt (Nhấn ?)"
              className="h-8 w-8 rounded-lg"
            >
              <Keyboard className="h-3.5 w-3.5" />
            </Button>

            <Button
              variant="outline"
              size="icon"
              onClick={toggleTheme}
              aria-label="Toggle Theme"
              title={theme === "dark" ? "Chuyển sang Giao diện Sáng (T)" : "Chuyển sang Giao diện Tối (T)"}
              className="h-8 w-8 rounded-lg cursor-pointer"
            >
              {theme === "dark" ? (
                <Sun className="h-3.5 w-3.5 text-amber-400" />
              ) : (
                <Moon className="h-3.5 w-3.5 text-slate-700" />
              )}
            </Button>
          </div>
        </div>
      </header>

      {/* Main Study Workspace */}
      <div className="max-w-7xl mx-auto px-4 py-5 w-full flex-1 flex gap-6">
        {/* Desktop Sidebar: Sticky 310px */}
        <aside className="hidden lg:flex w-76 shrink-0 sticky top-18 h-[calc(100vh-5.5rem)] flex-col rounded-xl border border-border bg-card p-3.5 shadow-xs">
          <div className="flex items-center justify-between pb-3 border-b border-border/80">
            <span className="font-bold text-xs flex items-center gap-2 text-foreground tracking-tight">
              <FolderOpen className="h-4 w-4 text-blue-600 dark:text-blue-400" />
              <span>Mục lục bài học</span>
            </span>
            <Badge variant="blueSoft" className="font-mono text-[10px] px-2 py-0">
              {course.total_lessons} bài
            </Badge>
          </div>
          <div className="mt-3 flex-1 overflow-hidden">{renderSidebarTree()}</div>
        </aside>

        {/* Mobile Header Bar & Drawer Trigger */}
        <div className="lg:hidden w-full flex flex-col gap-3">
          <div className="flex items-center justify-between p-3 rounded-xl border border-border bg-card shadow-xs">
            <div className="flex flex-col truncate pr-2">
              <span className="text-[10px] font-mono font-semibold text-blue-600 dark:text-blue-400 uppercase tracking-wider">
                Bài {curLessonIdx + 1} / {course.total_lessons}
              </span>
              <span className="text-xs font-bold truncate text-foreground">
                {curLesson?.id}: {curLesson?.title}
              </span>
            </div>
            <Sheet open={isMobileOpen} onOpenChange={setIsMobileOpen}>
              <SheetTrigger asChild>
                <Button variant="outline" size="sm" className="gap-1.5 shrink-0 text-xs h-8">
                  <Menu className="h-3.5 w-3.5" />
                  Mục lục
                </Button>
              </SheetTrigger>
              <SheetContent side="left" className="w-[300px] sm:w-[350px] p-4 flex flex-col">
                <SheetHeader className="text-left pb-3 border-b border-border">
                  <SheetTitle className="text-xs font-bold flex items-center gap-2">
                    <SubjectIcon className="h-4 w-4 text-blue-600" />
                    <span>Mục lục {course.title}</span>
                  </SheetTitle>
                </SheetHeader>
                <div className="mt-3 flex-1 overflow-hidden">{renderSidebarTree()}</div>
              </SheetContent>
            </Sheet>
          </div>
        </div>

        {/* Lesson Main Content Area */}
        <main className="flex-1 min-w-0 max-w-4xl space-y-5">
          {/* Lesson Header Card */}
          <Card className="border border-border/80 shadow-xs bg-card overflow-hidden">
            <CardHeader className="p-5 pb-4 space-y-2.5">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <div className="flex flex-wrap items-center gap-1.5">
                  <Badge variant="blueSoft" className="font-semibold text-[11px]">
                    {course.clusters[curLesson?.cluster] || `Cụm ${curLesson?.cluster}`}
                  </Badge>
                  {curLesson?.chapter_badge && (
                    <Badge variant="outline" className="text-[11px] font-mono text-muted-foreground">
                      {curLesson.chapter_badge}
                    </Badge>
                  )}
                </div>

                {isCurrentQuizPassed ? (
                  <Badge variant="success" className="gap-1 text-[11px] font-medium">
                    <CheckCircle2 className="h-3 w-3" /> Đã hoàn thành bài
                  </Badge>
                ) : (
                  <Badge variant="secondary" className="gap-1 text-[11px] font-medium text-muted-foreground">
                    <Lock className="h-3 w-3 opacity-60" /> Chưa hoàn thành
                  </Badge>
                )}
              </div>

              <div>
                <CardTitle className="text-lg sm:text-xl font-bold tracking-tight text-foreground">
                  {curLesson?.title}
                </CardTitle>
                {curLesson?.desc && (
                  <p className="mt-1.5 text-xs sm:text-sm text-muted-foreground leading-relaxed">
                    {curLesson.desc}
                  </p>
                )}
              </div>
            </CardHeader>
          </Card>

          {/* Sequential Section Stepper Tabs */}
          <Tabs value={curSubTab} onValueChange={setCurSubTab} className="w-full">
            <TabsList className="w-full grid grid-cols-2 sm:grid-cols-4 h-auto p-1 bg-muted/80 rounded-xl border border-border">
              {subTabs.map((tab) => {
                const Icon = tab.icon;
                return (
                  <TabsTrigger
                    key={tab.id}
                    value={tab.id}
                    className="flex items-center justify-center gap-1.5 py-2 text-xs font-semibold data-[state=active]:bg-card data-[state=active]:text-foreground data-[state=active]:shadow-xs transition-all"
                  >
                    <span className="w-4.5 h-4.5 rounded-full bg-slate-200/80 dark:bg-slate-700/80 flex items-center justify-center text-[10px] font-mono font-bold shrink-0">
                      {tab.stepNum}
                    </span>
                    <Icon className="h-3.5 w-3.5 shrink-0 opacity-80" />
                    <span className="truncate">{tab.label}</span>
                  </TabsTrigger>
                );
              })}
            </TabsList>

            {/* Sub-tab 1: Theory Steps */}
            <TabsContent value="theory" className="space-y-4 pt-2">
              {curLesson?.theory_steps.map((step, idx) => (
                <Card
                  key={idx}
                  className="border border-border/80 bg-card shadow-xs overflow-hidden"
                >
                  <CardHeader className="bg-muted/40 p-3.5 px-4 border-b border-border/60 flex flex-row items-center justify-between">
                    <span className="font-semibold text-xs sm:text-sm text-foreground flex items-center gap-2">
                      <Badge variant="blueSoft" className="font-mono font-bold text-[10.5px]">
                        Bước {step.step_num || idx + 1}
                      </Badge>
                      <span>{step.title}</span>
                    </span>
                  </CardHeader>
                  <CardContent className="p-4 sm:p-5 text-xs sm:text-sm leading-relaxed text-slate-700 dark:text-slate-300">
                    <div
                      dangerouslySetInnerHTML={{ __html: step.content }}
                      className="prose dark:prose-invert max-w-none space-y-2 [&_p]:mb-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ul]:mb-2 [&_li]:mb-1 [&_b]:text-foreground [&_code]:font-mono [&_code]:text-xs [&_code]:bg-muted [&_code]:px-1 [&_code]:py-0.5 [&_code]:rounded [&_.tip-box]:bg-blue-50/70 dark:[&_.tip-box]:bg-blue-950/30 [&_.tip-box]:border [&_.tip-box]:border-blue-200/80 dark:[&_.tip-box]:border-blue-900/60 [&_.tip-box]:p-3.5 [&_.tip-box]:rounded-xl [&_.tip-box]:my-3"
                    />
                  </CardContent>
                </Card>
              ))}
            </TabsContent>

            {/* Sub-tab 2: 3 Examples */}
            <TabsContent value="examples" className="space-y-4 pt-2">
              <div className="flex items-center gap-2 px-1 text-xs font-semibold text-muted-foreground">
                <GraduationCap className="h-4 w-4 text-blue-600 dark:text-blue-400" />
                <span>3 Ví dụ mẫu phân cấp (100% bám sát Slide bài giảng UET):</span>
              </div>

              {curLesson?.examples.map((ex, idx) => {
                const badgeVariant =
                  idx === 0 ? "emeraldSoft" : idx === 1 ? "amberSoft" : "roseSoft";
                return (
                  <Card
                    key={idx}
                    className="border border-border/80 bg-card shadow-xs overflow-hidden"
                  >
                    <CardHeader className="p-3.5 px-4 border-b border-border/60 bg-muted/40 flex flex-row items-center justify-between">
                      <span className="font-bold text-xs sm:text-sm text-foreground flex items-center gap-2">
                        <span className="h-2 w-2 rounded-full bg-blue-600 dark:bg-blue-400" />
                        Ví dụ {idx + 1}
                      </span>
                      <Badge variant={badgeVariant} className="font-semibold text-[10.5px]">
                        {ex.level}
                      </Badge>
                    </CardHeader>
                    <CardContent className="p-4 sm:p-5 space-y-4 text-xs sm:text-sm">
                      {/* Problem */}
                      <div className="bg-slate-50 dark:bg-slate-900/70 p-3.5 sm:p-4 rounded-xl border border-border/70 text-slate-800 dark:text-slate-200 leading-relaxed">
                        <div className="font-bold text-[11px] text-blue-600 dark:text-blue-400 uppercase tracking-wider mb-1.5 flex items-center gap-1.5">
                          <HelpCircle className="h-3.5 w-3.5" />
                          Đề bài (Trích Slide UET):
                        </div>
                        <div dangerouslySetInnerHTML={{ __html: ex.problem }} />
                      </div>

                      {/* Solution */}
                      <div className="space-y-2 text-slate-700 dark:text-slate-300 leading-relaxed">
                        <div className="font-bold text-[11px] text-muted-foreground uppercase tracking-wider flex items-center gap-1.5">
                          <Sparkles className="h-3.5 w-3.5 text-amber-500" />
                          Hướng dẫn giải chi tiết:
                        </div>
                        <div
                          dangerouslySetInnerHTML={{ __html: ex.solution }}
                          className="space-y-1.5 [&_b]:text-foreground [&_code]:font-mono [&_code]:text-xs [&_code]:bg-muted [&_code]:px-1 [&_code]:py-0.5 [&_code]:rounded"
                        />
                      </div>
                    </CardContent>
                  </Card>
                );
              })}
            </TabsContent>

            {/* Sub-tab 3: Pitfalls (Cạm bẫy) */}
            <TabsContent value="pitfalls" className="space-y-4 pt-2">
              <div className="flex items-center gap-2 px-1 text-xs font-semibold text-muted-foreground">
                <AlertTriangle className="h-4 w-4 text-amber-500" />
                <span>Đối chiếu song song các cạm bẫy kinh điển trong đề thi UET:</span>
              </div>

              {curLesson?.pitfalls.map((p, idx) => (
                <div
                  key={idx}
                  className="grid grid-cols-1 md:grid-cols-2 gap-4 rounded-xl border border-border p-4 bg-card shadow-xs"
                >
                  {/* Wrong Approach */}
                  <div className="p-4 rounded-xl bg-rose-50/50 border border-rose-200/80 dark:bg-rose-950/20 dark:border-rose-900/50 space-y-2">
                    <div className="flex items-center gap-1.5 font-bold text-xs text-rose-600 dark:text-rose-400 uppercase tracking-wider">
                      <XCircle className="h-4 w-4 shrink-0 text-rose-500" />
                      <span>Cách nghĩ sai phổ biến</span>
                    </div>
                    <Separator className="bg-rose-200/60 dark:bg-rose-900/40" />
                    <div
                      dangerouslySetInnerHTML={{ __html: p.bad }}
                      className="text-xs leading-relaxed text-slate-800 dark:text-slate-200 space-y-1 [&_b]:text-rose-950 dark:[&_b]:text-rose-200"
                    />
                  </div>

                  {/* Correct Rule */}
                  <div className="p-4 rounded-xl bg-emerald-50/50 border border-emerald-200/80 dark:bg-emerald-950/20 dark:border-emerald-900/50 space-y-2">
                    <div className="flex items-center gap-1.5 font-bold text-xs text-emerald-600 dark:text-emerald-400 uppercase tracking-wider">
                      <CheckCircle2 className="h-4 w-4 shrink-0 text-emerald-500" />
                      <span>Quy tắc chuẩn thi UET</span>
                    </div>
                    <Separator className="bg-emerald-200/60 dark:bg-emerald-900/40" />
                    <div
                      dangerouslySetInnerHTML={{ __html: p.good }}
                      className="text-xs leading-relaxed text-slate-800 dark:text-slate-200 space-y-1 [&_b]:text-emerald-950 dark:[&_b]:text-emerald-200"
                    />
                  </div>
                </div>
              ))}
            </TabsContent>

            {/* Sub-tab 4: 3-Level Gatekeeper Quiz */}
            <TabsContent value="quiz" className="space-y-5 pt-2">
              {/* Gatekeeper Banner */}
              <div className="bg-blue-50/70 dark:bg-blue-950/30 border border-blue-200/80 dark:border-blue-900/50 p-4 rounded-xl flex items-center justify-between gap-4">
                <div className="flex items-center gap-3">
                  <div className="p-2.5 rounded-lg bg-blue-600 text-white shrink-0 shadow-xs">
                    <ShieldCheck className="h-5 w-5" />
                  </div>
                  <div>
                    <h4 className="font-bold text-xs sm:text-sm text-foreground">
                      Bài kiểm tra 3 cấp độ (Gatekeeper Quiz)
                    </h4>
                    <p className="text-[11px] sm:text-xs text-muted-foreground mt-0.5">
                      Làm đúng cả 3 câu hỏi để hoàn thành bài học và mở khóa bài tiếp theo.
                    </p>
                  </div>
                </div>
                {isCurrentQuizPassed && (
                  <Badge variant="success" className="gap-1 font-semibold text-xs shrink-0">
                    <CheckCheck className="h-3.5 w-3.5" /> Đã vượt qua
                  </Badge>
                )}
              </div>

              {/* 3 Questions */}
              {curLesson?.quizzes.map((quiz, qIdx) => {
                const userChoice = quizAnswers[curLesson.id]?.[qIdx];
                const isAnswered = typeof userChoice === "number";
                const isCorrect = userChoice === quiz.ans;

                const isL1 =
                  quiz.level === 1 ||
                  quiz.level === "1" ||
                  String(quiz.level).toLowerCase().includes("nhận biết");
                const isL2 =
                  quiz.level === 2 ||
                  quiz.level === "2" ||
                  String(quiz.level).toLowerCase().includes("thông hiểu");

                const levelBadge = isL1 ? (
                  <Badge variant="outline" className="border-blue-200 dark:border-blue-900 bg-blue-50/50 dark:bg-blue-950/40 text-blue-700 dark:text-blue-300 gap-1.5 text-[11px] font-medium">
                    <span className="h-1.5 w-1.5 rounded-full bg-blue-500" />
                    Cấp độ 1: Nhận biết
                  </Badge>
                ) : isL2 ? (
                  <Badge variant="outline" className="border-amber-200 dark:border-amber-900 bg-amber-50/50 dark:bg-amber-950/40 text-amber-700 dark:text-amber-300 gap-1.5 text-[11px] font-medium">
                    <span className="h-1.5 w-1.5 rounded-full bg-amber-500" />
                    Cấp độ 2: Thông hiểu
                  </Badge>
                ) : (
                  <Badge variant="outline" className="border-rose-200 dark:border-rose-900 bg-rose-50/50 dark:bg-rose-950/40 text-rose-700 dark:text-rose-300 gap-1.5 text-[11px] font-medium">
                    <span className="h-1.5 w-1.5 rounded-full bg-rose-500" />
                    Cấp độ 3: Vận dụng & Cạm bẫy
                  </Badge>
                );

                return (
                  <Card
                    key={qIdx}
                    className="border border-border/80 bg-card shadow-xs overflow-hidden"
                  >
                    <CardHeader className="p-3.5 px-4 border-b border-border/60 bg-muted/40 flex flex-row items-center justify-between">
                      <div className="flex items-center gap-2">
                        <span className="font-mono text-xs font-semibold text-muted-foreground">
                          Câu {qIdx + 1}
                        </span>
                        {levelBadge}
                      </div>

                      {isAnswered && (
                        <Badge
                          variant={isCorrect ? "success" : "destructive"}
                          className="font-semibold text-[10.5px] gap-1"
                        >
                          {isCorrect ? (
                            <>
                              <Check className="h-3 w-3" /> Đúng
                            </>
                          ) : (
                            <>
                              <XCircle className="h-3 w-3" /> Chưa đúng
                            </>
                          )}
                        </Badge>
                      )}
                    </CardHeader>

                    <CardContent className="p-4 sm:p-5 space-y-4">
                      <div className="font-bold text-xs sm:text-sm text-foreground leading-snug">
                        {quiz.q}
                      </div>

                      {/* Options */}
                      <div className="space-y-2">
                        {quiz.opts.map((opt, optIdx) => {
                          const isSelected = userChoice === optIdx;
                          let optStyle =
                            "border-border bg-card hover:border-blue-400 dark:hover:border-blue-600 text-foreground";

                          if (isAnswered) {
                            if (optIdx === quiz.ans) {
                              optStyle =
                                "border-emerald-500 bg-emerald-50/60 dark:bg-emerald-950/40 text-emerald-950 dark:text-emerald-100 font-medium ring-1 ring-emerald-500/30";
                            } else if (isSelected && !isCorrect) {
                              optStyle =
                                "border-rose-500 bg-rose-50/60 dark:bg-rose-950/40 text-rose-950 dark:text-rose-100 ring-1 ring-rose-500/30";
                            }
                          }

                          return (
                            <button
                              key={optIdx}
                              onClick={() => handleAnswerQuiz(curLesson.id, qIdx, optIdx)}
                              className={`w-full flex items-start gap-3 p-3 sm:p-3.5 rounded-xl border text-left text-xs sm:text-sm transition-all ${optStyle}`}
                            >
                              <span className="w-5 h-5 rounded-md border border-border flex items-center justify-center font-mono font-bold text-xs shrink-0 bg-muted text-muted-foreground">
                                {String.fromCharCode(65 + optIdx)}
                              </span>
                              <span className="flex-1 leading-normal pt-0.5">{opt}</span>
                              {isAnswered && optIdx === quiz.ans && (
                                <CheckCircle2 className="h-4 w-4 text-emerald-600 shrink-0 mt-0.5" />
                              )}
                              {isAnswered && isSelected && !isCorrect && (
                                <XCircle className="h-4 w-4 text-rose-600 shrink-0 mt-0.5" />
                              )}
                            </button>
                          );
                        })}
                      </div>

                      {/* Feedback Box */}
                      {isAnswered && (
                        <div
                          className={`p-3.5 rounded-xl text-xs leading-relaxed border ${
                            isCorrect
                              ? "bg-emerald-50/60 border-emerald-200/80 text-emerald-950 dark:bg-emerald-950/40 dark:border-emerald-900/60 dark:text-emerald-200"
                              : "bg-rose-50/60 border-rose-200/80 text-rose-950 dark:bg-rose-950/40 dark:border-rose-900/60 dark:text-rose-200"
                          }`}
                        >
                          <div className="font-bold mb-1 flex items-center gap-1.5">
                            {isCorrect ? (
                              <>
                                <CheckCircle2 className="h-3.5 w-3.5 text-emerald-600" />
                                <span>Giải thích chính xác:</span>
                              </>
                            ) : (
                              <>
                                <Info className="h-3.5 w-3.5 text-rose-600" />
                                <span>Hướng dẫn giải lại:</span>
                              </>
                            )}
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
            <Card className="border border-border/80 bg-slate-50/70 dark:bg-slate-900/50 rounded-xl overflow-hidden shadow-xs">
              <CardHeader className="p-3.5 px-4 border-b border-border/60 flex flex-wrap items-center justify-between gap-2">
                <span className="font-bold text-xs text-blue-600 dark:text-blue-400 flex items-center gap-1.5 uppercase tracking-wide">
                  <BookmarkCheck className="h-4 w-4" />
                  Dấu Ref Tra cứu Slide Bài Giảng ({course.code})
                </span>
                {curLesson.ref.slide_file && (
                  <a
                    href={`/${curLesson.ref.slide_file}#page=${curLesson.ref.page_start}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-1.5 text-xs font-semibold text-white bg-blue-600 hover:bg-blue-700 px-3 py-1.5 rounded-lg shadow-xs transition-colors"
                  >
                    <span>Mở Slide trang {curLesson.ref.page_start}</span>
                    <ExternalLink className="h-3 w-3" />
                  </a>
                )}
              </CardHeader>
              <CardContent className="p-4 space-y-2 text-xs">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-slate-700 dark:text-slate-300">
                  <div>
                    <span className="font-medium text-muted-foreground">Tập slide: </span>
                    <span className="font-semibold text-foreground">{curLesson.ref.slide_name}</span> (
                    <code className="font-mono text-[11px] bg-muted px-1 py-0.5 rounded">
                      {curLesson.ref.slide_file}
                    </code>
                    )
                  </div>
                  <div>
                    <span className="font-medium text-muted-foreground">Vị trí: </span>
                    <span className="font-semibold text-foreground">{curLesson.ref.pages}</span> —{" "}
                    {curLesson.ref.section}
                  </div>
                </div>
                {curLesson.ref.remind && (
                  <div className="mt-2 p-3 rounded-lg bg-blue-100/40 dark:bg-blue-950/40 border border-blue-200/60 dark:border-blue-900/40 text-slate-800 dark:text-slate-200 leading-relaxed flex items-start gap-2">
                    <Info className="h-4 w-4 text-blue-600 dark:text-blue-400 shrink-0 mt-0.5" />
                    <div>
                      <span className="font-semibold">Lời nhắc khi gặp khó khăn: </span>
                      {curLesson.ref.remind}
                    </div>
                  </div>
                )}
              </CardContent>
            </Card>
          )}

          {/* Bottom Navigation Buttons (Sequential Stepper) */}
          <div className="pt-3 border-t border-border flex items-center justify-between gap-4">
            <Button
              variant="outline"
              onClick={handlePrevSection}
              disabled={curLessonIdx === 0 && curSubTab === "theory"}
              className="font-semibold text-xs sm:text-sm h-9"
            >
              <ArrowLeft className="h-4 w-4 mr-1.5" />
              {curSubTab === "theory" ? "Bài trước" : "Phần trước"}
            </Button>

            <Button
              onClick={handleNextSection}
              disabled={curSubTab === "quiz" && !isCurrentQuizPassed}
              className={`font-semibold text-xs sm:text-sm h-9 shadow-xs ${
                curSubTab === "quiz" && isCurrentQuizPassed
                  ? "bg-emerald-600 hover:bg-emerald-700 text-white"
                  : ""
              }`}
            >
              {curSubTab !== "quiz" ? (
                <>
                  Sang phần tiếp theo
                  <ArrowRight className="h-4 w-4 ml-1.5" />
                </>
              ) : isCurrentQuizPassed ? (
                curLessonIdx < course.lessons.length - 1 ? (
                  <>
                    Mở bài tiếp: {course.lessons[curLessonIdx + 1]?.id}
                    <ArrowRight className="h-4 w-4 ml-1.5" />
                  </>
                ) : (
                  <>
                    <CheckCheck className="h-4 w-4 mr-1.5" />
                    Đã hoàn thành toàn bộ khóa học
                  </>
                )
              ) : (
                <>
                  <Lock className="h-4 w-4 mr-1.5" />
                  Làm đúng trắc nghiệm để mở bài tiếp
                </>
              )}
            </Button>
          </div>
        </main>
      </div>

      {/* Keyboard Shortcuts Dialog Modal (Like Raycast / Linear) */}
      <Dialog open={isShortcutsOpen} onOpenChange={setIsShortcutsOpen}>
        <DialogContent className="max-w-md">
          <DialogHeader className="pb-3 border-b border-border text-left">
            <DialogTitle className="flex items-center gap-2 text-base font-bold text-foreground">
              <Keyboard className="h-4.5 w-4.5 text-blue-600 dark:text-blue-400" />
              <span>Phím tắt bàn phím</span>
            </DialogTitle>
            <DialogDescription className="text-xs text-muted-foreground mt-1">
              Các phím tắt hỗ trợ thao tác nhanh trong không gian học tập tương tác.
            </DialogDescription>
          </DialogHeader>

          <div className="space-y-4 py-2 text-xs">
            {/* Group 1: Điều hướng bài học */}
            <div className="space-y-2">
              <div className="font-semibold text-muted-foreground text-[10.5px] uppercase tracking-wider">
                Điều hướng bài học
              </div>
              <div className="space-y-1.5">
                <div className="flex items-center justify-between p-2.5 rounded-lg bg-muted/40 border border-border/60">
                  <span className="text-foreground font-medium">Nhảy nhanh 4 phần bài học</span>
                  <div className="flex items-center gap-1 font-mono">
                    <kbd className="px-1.5 py-0.5 rounded bg-card border border-border text-[10px] font-bold">1</kbd>
                    <kbd className="px-1.5 py-0.5 rounded bg-card border border-border text-[10px] font-bold">2</kbd>
                    <kbd className="px-1.5 py-0.5 rounded bg-card border border-border text-[10px] font-bold">3</kbd>
                    <kbd className="px-1.5 py-0.5 rounded bg-card border border-border text-[10px] font-bold">4</kbd>
                  </div>
                </div>

                <div className="flex items-center justify-between p-2.5 rounded-lg bg-muted/40 border border-border/60">
                  <span className="text-foreground font-medium">Phần trước / Phần tiếp</span>
                  <div className="flex items-center gap-1 font-mono">
                    <kbd className="px-1.5 py-0.5 rounded bg-card border border-border text-[10px]">Alt</kbd>
                    <span className="text-muted-foreground">+</span>
                    <kbd className="px-1.5 py-0.5 rounded bg-card border border-border text-[10px]">←</kbd>
                    <span className="text-muted-foreground">/</span>
                    <kbd className="px-1.5 py-0.5 rounded bg-card border border-border text-[10px]">→</kbd>
                  </div>
                </div>
              </div>
            </div>

            {/* Group 2: Tìm kiếm & Tiện ích */}
            <div className="space-y-2">
              <div className="font-semibold text-muted-foreground text-[10.5px] uppercase tracking-wider">
                Tìm kiếm & Hệ thống
              </div>
              <div className="space-y-1.5">
                <div className="flex items-center justify-between p-2.5 rounded-lg bg-muted/40 border border-border/60">
                  <span className="text-foreground font-medium">Tìm kiếm bài học</span>
                  <div className="flex items-center gap-1 font-mono">
                    <kbd className="px-1.5 py-0.5 rounded bg-card border border-border text-[10px]">Ctrl / ⌘</kbd>
                    <span className="text-muted-foreground">+</span>
                    <kbd className="px-1.5 py-0.5 rounded bg-card border border-border text-[10px]">K</kbd>
                  </div>
                </div>

                <div className="flex items-center justify-between p-2.5 rounded-lg bg-muted/40 border border-border/60">
                  <span className="text-foreground font-medium">Đổi giao diện Sáng / Tối</span>
                  <div className="flex items-center gap-1 font-mono">
                    <kbd className="px-1.5 py-0.5 rounded bg-card border border-border text-[10px] font-bold">T</kbd>
                  </div>
                </div>

                <div className="flex items-center justify-between p-2.5 rounded-lg bg-muted/40 border border-border/60">
                  <span className="text-foreground font-medium">Mở bảng phím tắt này</span>
                  <div className="flex items-center gap-1 font-mono">
                    <kbd className="px-1.5 py-0.5 rounded bg-card border border-border text-[10px] font-bold">?</kbd>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Dialog Footer */}
          <div className="pt-3 border-t border-border flex items-center justify-between text-xs">
            <a
              href="https://github.com/duydat1412/xstk-uet-mat1052"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 text-muted-foreground hover:text-foreground font-mono text-[11px] transition-colors"
            >
              <GithubIcon className="h-3.5 w-3.5" />
              <span>duydat1412/xstk-uet-mat1052</span>
            </a>

            <Button
              variant="outline"
              size="sm"
              onClick={() => setIsShortcutsOpen(false)}
              className="h-7 text-xs px-2.5"
            >
              Đóng (Esc)
            </Button>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
}
