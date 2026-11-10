export interface TheoryStep {
  step_num: number;
  title: string;
  content: string;
}

export interface Example {
  level: "Cơ bản" | "Trung bình" | "Vận dụng" | string;
  problem: string;
  solution: string;
  image?: string;
  caption?: string;
}

export interface Pitfall {
  bad: string;
  good: string;
}

export interface GatekeeperQuiz {
  level: 1 | 2 | 3 | string | number;
  q: string;
  opts: string[];
  ans: number;
  fb: string;
  image?: string;
  caption?: string;
}

export interface LectureRef {
  slide_file: string;
  slide_name: string;
  page_start: number;
  page_end: number;
  pages: string;
  section: string;
  remind: string;
  stat20?: string;
  key_points?: string[];
}

export interface Illustration {
  title: string;
  src: string;
  caption: string;
  slide_ref?: string;
  drawing_guide?: string[];
}

export interface Lesson {
  id: string;
  cluster: string;
  title: string;
  desc: string;
  chapter_badge?: string;
  slide_badge?: string;
  theory_steps: TheoryStep[];
  examples: Example[];
  pitfalls: Pitfall[];
  quizzes: GatekeeperQuiz[];
  ref: LectureRef;
  illustrations?: Illustration[];
}

export interface Course {
  id: "xstk" | "csdl" | string;
  code: string;
  title: string;
  subtitle: string;
  icon: string;
  total_lessons: number;
  clusters: Record<string, string>;
  lessons: Lesson[];
}
