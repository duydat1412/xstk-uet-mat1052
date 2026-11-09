import { xstkCourse } from "@/data/courses";
import { CourseStudyView } from "@/components/course-study-view";

export const metadata = {
  title: "Học Xác suất Thống kê Tương tác (MAT1052) — UET Study Hub",
  description:
    "26 bài học tương tác Xác suất Thống kê MAT1052 bám sát tuần 1–7 slide UET: Dữ liệu, Xác suất, Rời rạc, Liên tục, Hồi quy.",
};

export default function XstkHocPage() {
  return <CourseStudyView course={xstkCourse} />;
}
