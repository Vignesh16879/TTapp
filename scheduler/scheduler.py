import random
from pathlib import Path

from .models import teacher, student
from .utils import Xlsx_extractor

# # Scheduler
# class Scheduler():
#     teachers = list()
#     error = ""
    
#     def __init__(self):
#         pass
    
    
#     def fetch_teacher_details(self):
#         try:
#             self.teachers = teacher.get_objects()
#         except:
#             self.error = "Unable to fetch teachers details."
    
    
#     def make_tt(self):
#         self.fetch_teacher_details()
        
#         if not self.teacher:
#             return False, self.error


# Scheduler
class Scheduler():
    timetable = []
    n = 6
    m = 6
    k = 4
    teachers_data = []
    subject_list = []

    
    def __init__(self, n, m, k):
        self.n = n
        self.m = m
        self.k = k
    
    
    def fetch_teacher_details_from_xlsx(self):
        
        FILE = Path.cwd() / "sample.xlsx"
        temp = Xlsx_extractor()
        self.teachers_data = temp.get_teachers_data(FILE)
        
        return self.teachers_data
    
    
    def fetch_subject_details_from_xlsx(self):
        FILE = Path.cwd() / "subject.xlsx"
        temp = Xlsx_extractor()
        self.subject_list = temp.get_subject_list_data(FILE)
        
        return self.subject_list
    
    
    def fetch_teacher_details(self, c, s, subject):        
        for i in range(0, len(self.teachers_data)):
            try:                
                if "," not in subject:
                    l = self.teachers_data[i]["Subjects"][subject]
                    for sub in l:
                        if str(c) in sub and s in sub:
                            return [i]
                else:
                    lt = subject.split(",")
                    ff = []
                    
                    for xx in lt:
                        ff.append(self.fetch_teacher_details(c, s, xx)[0])                    
                        
                    return ff
            except:
                pass
        
        return []
    
    
    def can_teacher_be_assigned(self, index, i, j):
        periods = self.teachers_data[index]["Time Table"]
        
        return periods[i][j]["isFree"]        
    
    
    def generate_time_table(self, subject_list):
        timetable = []
        pt = []

        for i in range(0, self.n):
            xt = []
            
            for j in range(0, self.m):
                xt.append({"isFree" : True, "Class" : "Free", "Section" : "Period"})
                
            pt.append(xt)
        
        for i in self.teachers_data:
            i["Time Table"] = pt
        
        fg = []

        for i in range(0, self.n):
            xt = []
            
            for j in range(0, self.m):
                xt.append({"Subject" : None,"Teacher" : ""})
            
            fg.append(xt)

        temp_subject_list = subject_list
        
        for classes in temp_subject_list:
            clas = classes["Class"]
            sections = classes["Sections"]
            
            for section in sections:
                period = fg
                subjects = section["Subjects"]
                min_per = section["min"]
                max_per = section["max"]
                teachers = []
                print(clas, section["Section"])
                
                for sub in subjects:
                    index = self.fetch_teacher_details(clas, section["Section"], sub)
                    teachers.append(index)
                    try:
                        print(sub, index, self.teachers_data[index[0]]["Name"])
                    except:
                        pass
                
                arr = list(range(len(subjects)))
                random.shuffle(arr)
                
                for j in range(0, self.m):
                    for i in range(0, self.n):
                        itr = 1
                        
                        while(itr < 2*len(arr)):
                            itr += 1
                            rand = random.randint(0, len(arr)-1)
                            
                            if max_per[rand] <= 0:
                                continue
                            
                            teach = ""
                            isTeacher_free = False
                            
                            for xx in teachers[rand]:
                                teach += self.teachers_data[xx]["Name"] + (", " if xx != teachers[len(teachers)-1] else "")
                                teach = teach[:-2]
                                
                                if self.teachers_data[xx]["Time Table"][i][j]["isFree"]:
                                    isTeacher_free = True
                                else:
                                    isTeacher_free = False
                                    continue
                                
                            if isTeacher_free:
                                for xx in teachers[rand]:
                                    self.teachers_data[xx]["Time Table"][i][j]["isFree"] = False
                                    self.teachers_data[xx]["Time Table"][i][j]["Class"] = clas
                                    self.teachers_data[xx]["Time Table"][i][j]["Section"] = section["Section"]
                                    
                                period[i][j]["Subject"] = subjects[rand]                                                            
                                period[i][j]["Teacher"] = teach
                                max_per[rand] -= 1
                                
                                arr = [x for x in arr if max_per[x] > 0]
                                break
                            else:
                                continue
                
                for x in period:
                    print(x)
                
                timetable.append({
                    "Class" : clas,
                    "Section" : section["Section"],
                    "Time Table" : period
                })
                            
                
            #     for j in range(0, self.m):
            #         for i in range(0, self.n):
            #             for xx in arr:
            #                 if max_per[xx] / self.n > 1 and xx >= 0:
            #                     def itr(i, k1 = 0):
            #                         rand = random.randint(0, self.m - 2)
            #                         k1 += 1
                                    
            #                         if k1 == self.m:
            #                             return
                                    
            #                         if period[i][rand]["Subject"] == None and period[i][rand+1]["Subject"] == None:
            #                             isValid = False
            #                             teach = []
            #                             teachs = ""
                                        
            #                             for tx in teachers[xx]:
            #                                 if self.teachers_data[tx]["Time Table"][i][rand]["isFree"] and self.teachers_data[tx]["Time Table"][i][rand+1]["isFree"]:
            #                                     tt55 = {}
            #                                     tt55["isFree"] = False
            #                                     tt55["Class"] = clas
            #                                     tt55["Section"] = section["Section"]
            #                                     teach.append(tt55)
            #                                     isValid = True
            #                                 else:
            #                                     isValid = False
            #                                     break
                                            
            #                             if isValid:
            #                                 min_per[xx] -= 2
            #                                 j -= 1
                                            
            #                                 for i in range(0, len(teachers[xx])):
            #                                     teachs += self.teachers_data[teachers[xx][i]]["Name"] + (", "if i != len(teachers[xx])-1 else "")
            #                                     self.teachers_data[teachers[xx][i]]["Time Table"][i][rand] = teach[i]
            #                                     self.teachers_data[teachers[xx][i]]["Time Table"][i][rand+1] = teach[i]
                                            
            #                                 period[i][rand] = {"Subject" : subjects[xx], "Teacher" : teachs}
            #                                 period[i][rand+1] = {"Subject" : subjects[xx], "Teacher" : teachs}
            #                             else:
            #                                 itr(i, k1)
            #                         else:
            #                             itr(i, k1)
            #                     itr(i)
            #                 else:
            #                     def itr(i, k1 = 0):
            #                         rand = random.randint(0, self.m - 1)
            #                         k1 += 1
                                    
            #                         if k1 == self.m+1:
            #                             return
                                    
            #                         if period[i][rand]["Subject"] == None:
            #                             isValid = False
            #                             teach = []
            #                             teachs = ""
                                        
            #                             for tx in teachers[xx]:
            #                                 if self.teachers_data[tx]["Time Table"][i][rand]["isFree"]:
            #                                     tt55 = {}
            #                                     tt55["isFree"] = False
            #                                     tt55["Class"] = CLASS
            #                                     tt55["Section"] = section["Section"]
            #                                     teach.append(tt55)
            #                                     isValid = True
            #                                 else:
            #                                     isValid = False
            #                                     break
                                            
            #                             if isValid:
            #                                 min_per[xx] -= 1
                                            
            #                                 for i in range(0, len(teachers[xx])):    
            #                                     teachs += self.teachers_data[teachers[xx][i]]["Name"] + (", "if i != len(teachers[xx])-1 else "")
            #                                     self.teachers_data[teachers[xx][i]]["Time Table"][i][rand] = teach[i]
            #                                     # print(self.teachers_data[teachers[xx][i]]["Time Table"])
                                            
            #                                 period[i][rand] = {"Subject" : subjects[xx], "Teacher" : teachs}
            #                             else:
            #                                 itr(i, k1)
            #                         else:
            #                             itr(i, k1)
            #                     itr(i) 
                            
            #                 if min_per[xx] == 0:
            #                     arr = [x for x in arr if min_per[x] != 0]
                    
            #         # print(f"Day-{i+1}")
            #         # print(period[i])
                
            #     break
            #     timetable.append({
            #         "Class" : CLASS,
            #         "Section" : section["Section"],
            #         "Time Table" : period
            #     })
                
            #     # for fdg in timetable:
            #     #     for ty in fdg["Time Table"]:
            #     #         for tx in ty:
            #     #             print(tx)
            #     #         print("next")
       
        return True, self.teachers_data, timetable


# FILE = "subject.xlsx"
# temp = Xlsx_extractor()
# subject_list = temp.get_subject_list_data(FILE)

# ff = Scheduler(6, 7, 3) 
# teachers_data = ff.fetch_teacher_details_from_xlsx()
# # ff.generate_time_table(subject_list)
# success, teachers_data, timetable = ff.generate_time_table(subject_list)
# print(ff.fetch_teacher_details(6, "A", "Science"))

# if success:
#     print("Timetable generated successfully!")
#     # You can print or use the timetable as needed
#     for i in timetable:
#         if i["Class"] == 6:
#             print(i["Time Table"])
# else:
#     print("Error generating timetable:", timetable)