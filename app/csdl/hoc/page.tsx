import { csdlCourse } from "@/data/courses";
import { CourseStudyView } from "@/components/course-study-view";

export const metadata = {
  title: "Học Cơ sở Dữ liệu Tương tác (INT2207) — UET Study Hub",
  description:
    "14 bài học tương tác Cơ sở dữ liệu UET.IS2099: Kiến trúc 3 mức, Mô hình ER, Đại số quan hệ & SQL, Phụ thuộc hàm & Chuẩn hóa.",
};

export default function CsdlHocPage() {
  return <CourseStudyView course={csdlCourse} />;
}
