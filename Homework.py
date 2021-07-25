import os


class Homework:
    def __init__(self, student_data_file="./StudentData.csv", subject_data_file="./SubjectData.csv"):
        self.students_info = list()
        self.subjects_info = list()
        self.class_info = list()
        self.student_data_file = student_data_file
        self.subject_data_file = subject_data_file

    def read_student_info(self):
        f = open(self.student_data_file, 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            student_info = {
                'Student_Name': None,
                'Class': None,
                'Section': None
            }
            if "Student_Name" in line:
                pass
            else:
                line = line.rstrip("\n")
                line = line.split(",")
                student_info['Student_Name'] = line[0]
                student_info['Class'] = line[1]
                student_info['Section'] = line[2]
                self.students_info.append(student_info)
        return self.students_info

    def read_subject_info(self):
        f = open(self.subject_data_file, 'r')
        lines = f.readlines()
        f.close()
        subjects = list()
        for line in lines:
            subject_info = {
                'Class': None,
                'Subjects': list()
            }
            if "Class" in line:
                line = line.rstrip("\n")
                line = line.split(",")
                for item in line:
                    if item != "Class":
                        subjects.append(item)
            else:
                line = line.rstrip("\n")
                line = line.split(",")
                subject_info['Class'] = line.pop(0)
                index = 0
                for item in line:
                    if "Yes" in item or "yes" in item:
                        subject_info['Subjects'].append(subjects[index])
                    index += 1
                self.subjects_info.append(subject_info)
        return self.subjects_info

    def prep_class_info(self):
        c = set()
        for student in self.students_info:
            c.add(student['Class'])
        for item in c:
            s = set()
            class_info = {'Class': item,
                          'Sections': set()
                          }
            for student in self.students_info:
                if student['Class'] == item:
                    s.add(student['Section'])
            class_info['Sections'] = s
            self.class_info.append(class_info)
        return self.class_info

    def init_homework_dir(self, root="./homework"):
        for c in self.class_info:
            path = root + "/" + str(c['Class'])
            for s in c['Sections']:
                s_path = path + "/" + str(s)
                for student in self.students_info:
                    if student['Class'] == c['Class'] and student['Section'] == s:
                        n_path = s_path + "/" + str(student['Student_Name'])
                        for item in self.subjects_info:
                            if item['Class'] == student['Class']:
                                for subject in item['Subjects']:
                                    sub_path = n_path + "/" + str(subject)
                                    try:
                                        os.makedirs(sub_path)
                                    except FileExistsError:
                                        pass


if __name__ == '__main__':
    Test = Homework()
    Test.read_subject_info()
    Test.read_student_info()
    Test.prep_class_info()
    Test.init_homework_dir()
