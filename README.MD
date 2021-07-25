This is a simple python3 script to generate a homework folder for a school. 

The script prepares a folder structure as shown under sample output using two csv files as input data

**StudentData.csv** 
This file contains a list of students in following format
Student_Name,Class,Section
Student_1,1,A
Student_2,2,B
Student_3,3,C
Student_4,4,A
Student_5,5,B

**SubjectData.csv**
This file contains a list of subjects in following format
Class,Subject-1,Subject-2,Subject-3,Subject-4,Subject-5,Subject-6,Subject-7,Subject-8,Subject-9,Subject-10,Subject-11
1,Yes ,Yes ,Yes ,Yes ,Yes ,Yes ,No,No,No,No,No
2,Yes ,Yes ,Yes ,Yes ,No,No,No,No,No,Yes ,Yes 
3,No,No,No,No,Yes ,Yes ,Yes ,Yes ,Yes ,Yes ,Yes 


**Sample output**
output of tree ./homework 
./homework
├── 1
│   ├── A
│   │   ├── Student_1
│   │   │   ├── Subject-1
│   │   │   ├── Subject-2
│   │   │   ├── Subject-3
│   │   │   ├── Subject-4
│   │   │   ├── Subject-5
│   │   │   └── Subject-6
│   │   ├── Student_121
│   │   │   ├── Subject-1
│   │   │   ├── Subject-2
│   │   │   ├── Subject-3
│   │   │   ├── Subject-4
│   │   │   ├── Subject-5
│   │   │   └── Subject-6
│   │   ├── Student_31
│   │   │   ├── Subject-1
│   │   │   ├── Subject-2
│   │   │   ├── Subject-3
│   │   │   ├── Subject-4
│   │   │   ├── Subject-5
│   │   │   └── Subject-6
│   │   ├── Student_61
│   │   │   ├── Subject-1
│   │   │   ├── Subject-2
│   │   │   ├── Subject-3
│   │   │   ├── Subject-4
│   │   │   ├── Subject-5
│   │   │   └── Subject-6
│   │   └── Student_91
│   │       ├── Subject-1
│   │       ├── Subject-2
│   │       ├── Subject-3
│   │       ├── Subject-4
│   │       ├── Subject-5
│   │       └── Subject-6
│   ├── B
│   │   ├── Student_101
│   │   │   ├── Subject-1
│   │   │   ├── Subject-2
│   │   │   ├── Subject-3
│   │   │   ├── Subject-4
│   │   │   ├── Subject-5
│   │   │   └── Subject-6
│   │   ├── Student_11
│   │   │   ├── Subject-1
│   │   │   ├── Subject-2
│   │   │   ├── Subject-3
│   │   │   ├── Subject-4
│   │   │   ├── Subject-5
│   │   │   └── Subject-6
│   │   ├── Student_131
│   │   │   ├── Subject-1
│   │   │   ├── Subject-2
│   │   │   ├── Subject-3
│   │   │   ├── Subject-4
│   │   │   ├── Subject-5
│   │   │   └── Subject-6
│   │   ├── Student_41
│   │   │   ├── Subject-1
│   │   │   ├── Subject-2
│   │   │   ├── Subject-3
│   │   │   ├── Subject-4
│   │   │   ├── Subject-5
│   │   │   └── Subject-6
│   │   └── Student_71
│   │       ├── Subject-1
│   │       ├── Subject-2
│   │       ├── Subject-3
│   │       ├── Subject-4
│   │       ├── Subject-5
│   │       └── Subject-6
│   └── C
│       ├── Student_111
│       │   ├── Subject-1
│       │   ├── Subject-2
│       │   ├── Subject-3
│       │   ├── Subject-4
│       │   ├── Subject-5
│       │   └── Subject-6
│       ├── Student_141
│       │   ├── Subject-1
│       │   ├── Subject-2
│       │   ├── Subject-3
│       │   ├── Subject-4
│       │   ├── Subject-5
│       │   └── Subject-6
│       ├── Student_21
│       │   ├── Subject-1
│       │   ├── Subject-2
│       │   ├── Subject-3
│       │   ├── Subject-4
│       │   ├── Subject-5
│       │   └── Subject-6
│       ├── Student_51
│       │   ├── Subject-1
│       │   ├── Subject-2
│       │   ├── Subject-3
│       │   ├── Subject-4
│       │   ├── Subject-5
│       │   └── Subject-6
│       └── Student_81
│           ├── Subject-1
│           ├── Subject-2
│           ├── Subject-3
│           ├── Subject-4
│           ├── Subject-5
│           └── Subject-6
├── 10
│   ├── A
│   │   ├── Student_10
│   │   │   ├── Subject-1
│   │   │   ├── Subject-10
│   │   │   ├── Subject-11
│   │   │   ├── Subject-2
│   │   │   ├── Subject-3
│   │   │   ├── Subject-4
│   │   │   ├── Subject-5
│   │   │   └── Subject-6
│   │   ├── Student_100
│   │   │   ├── Subject-1
│   │   │   ├── Subject-10
│   │   │   ├── Subject-11
│   │   │   ├── Subject-2
│   │   │   ├── Subject-3
│   │   │   ├── Subject-4
│   │   │   ├── Subject-5
│   │   │   └── Subject-6
│   │   ├── Student_130
│   │   │   ├── Subject-1
│   │   │   ├── Subject-10
│   │   │   ├── Subject-11
│   │   │   ├── Subject-2
│   │   │   ├── Subject-3
│   │   │   ├── Subject-4
│   │   │   ├── Subject-5
│   │   │   └── Subject-6
│   │   ├── Student_40
│   │   │   ├── Subject-1
│   │   │   ├── Subject-10
│   │   │   ├── Subject-11
│   │   │   ├── Subject-2
│   │   │   ├── Subject-3
│   │   │   ├── Subject-4
│   │   │   ├── Subject-5
│   │   │   └── Subject-6
│   │   └── Student_70
│   │       ├── Subject-1
│   │       ├── Subject-10
│   │       ├── Subject-11
│   │       ├── Subject-2
│   │       ├── Subject-3
│   │       ├── Subject-4
│   │       ├── Subject-5
│   │       └── Subject-6
│   ├── B
│   │   ├── Student_110



		
	



