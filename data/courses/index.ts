import { Course, Lesson } from "@/types/course";
import csdlRaw from "./csdl.json";
import xstkRaw from "./xstk.json";

function normalizeLesson(raw: any): Lesson {
  // Normalize theory steps
  const theory_steps = (raw.steps || raw.theory_steps || []).map((s: any, idx: number) => ({
    step_num: s.step_num || idx + 1,
    title: s.t || s.title || `Bước ${idx + 1}`,
    content: s.c || s.content || "",
  }));

  // Normalize examples
  const examples = (raw.examples || []).map((ex: any) => ({
    level: ex.level || "Cơ bản",
    problem: ex.problem || ex.q || "",
    solution: ex.solution || ex.sol || "",
  }));

  // Normalize pitfalls
  const pitfalls = (raw.pitfalls || []).map((p: any) => ({
    bad: p.bad || "",
    good: p.good || "",
  }));

  // Normalize quizzes
  const quizzes = (raw.quizzes || (raw.final_quiz ? [raw.final_quiz] : [])).map((q: any, idx: number) => ({
    level: q.level || idx + 1,
    q: q.q || "",
    opts: q.opts || [],
    ans: typeof q.ans === "number" ? q.ans : 0,
    fb: q.fb || "",
  }));

  return {
    id: raw.id,
    cluster: String(raw.cluster),
    title: raw.title,
    desc: raw.desc || "",
    chapter_badge: raw.chapter_badge || raw.sources || "",
    slide_badge: raw.slide_badge || "",
    theory_steps,
    examples,
    pitfalls,
    quizzes,
    ref: raw.ref || {
      slide_file: "",
      slide_name: "",
      page_start: 1,
      page_end: 1,
      pages: "",
      section: "",
      remind: "",
    },
  };
}

export const csdlCourse: Course = {
  id: "csdl",
  code: "INT2207",
  title: "Cơ sở dữ liệu",
  subtitle: "Nền tảng Tự học & Luyện thi Tương tác UET (UET.IS2099)",
  icon: "🗄️",
  total_lessons: csdlRaw.length,
  clusters: {
    "1": "Chương 1: Tổng quan về Hệ CSDL",
    "2": "Chương 2: Mô hình ER & Quan hệ",
    "3": "Chương 3: Đại số quan hệ & SQL",
    "4": "Chương 4: Lý thuyết thiết kế CSDL & Phụ thuộc hàm",
  },
  lessons: (csdlRaw as any[]).map(normalizeLesson),
};

export const xstkCourse: Course = {
  id: "xstk",
  code: "MAT1052",
  title: "Xác suất Thống kê",
  subtitle: "Luyện thi Giữa kỳ Tương tác Chuẩn Barem UET (MAT1052)",
  icon: "🎲",
  total_lessons: xstkRaw.length,
  clusters: {
    "A": "Cụm A: Dữ liệu & Thống kê Mô tả",
    "B": "Cụm B: Xác suất & Biến ngẫu nhiên",
    "C": "Cụm C: Phân phối Xác suất Rời rạc",
    "D": "Cụm D: Tổng biến & Biến Liên tục",
    "E": "Cụm E: Thống kê Suy luận & Hồi quy",
  },
  lessons: (xstkRaw as any[]).map(normalizeLesson),
};

export const COURSES: Record<string, Course> = {
  xstk: xstkCourse,
  csdl: csdlCourse,
};

export function getCourse(id: string): Course | null {
  return COURSES[id.toLowerCase()] || null;
}

export function getLesson(courseId: string, lessonId: string): Lesson | null {
  const course = getCourse(courseId);
  if (!course) return null;
  return course.lessons.find((l) => l.id.toLowerCase() === lessonId.toLowerCase()) || null;
}
