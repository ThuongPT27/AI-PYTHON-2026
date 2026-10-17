class Student:
    def __init__(self, student_id, name, scores):
        self.student_id = student_id
        self.name = name
        self.scores = scores 

    @property
    def average(self):
        if not self.scores:
            return 0.0
        return round(sum(self.scores) / len(self.scores), 2)

    def rank(self):
        avg = self.average
        if avg >= 8.0:
            return "Giỏi"
        elif avg >= 6.5:
            return "Khá"
        elif avg >= 5.0:
            return "Đạt"
        else:
            return "Trượt"

    def __str__(self):
        return f"| {self.student_id:<10} | {self.name:<20} | {self.average:<8} | {self.rank():<8} |"
if __name__ == "__main__":
    students = [
        Student("SV001", "Nguyễn Ngọc Anh", [8.5, 9.0, 7.8]),
        Student("SV002", "Trần Thị Bình", [6.0, 5.5, 6.8]),
        Student("SV003", "Lê Minh Cường", [4.5, 5.0, 3.8]),
        Student("SV004", "Phạm Minh Đức", [9.2, 8.8, 9.5]),
        Student("SV005", "Vũ Minh Huyền", [7.5, 7.0, 8.0])
    ]
    students.sort(key=lambda student: student.average, reverse=True)

    print("=" * 59)
    print(f"| {'Mã SV':<10} | {'Họ và Tên':<20} | {'Điểm TB':<8} | {'Xếp loại':<8} |")
    print("=" * 59)
    
    for sv in students:
        print(sv)
        
    print("=" * 59)
