
def read_schedules():
    instructors = open("instructors.txt", "r")
    data_file2 = open("locations.txt", "r")
    data_file3= open("times.txt", "r")

    data = {}
    dataloc = {}
    datatime = {}
    
    
    for line in data_file2:
        line = line.strip().split(",")
        courseID = line[0].strip(' ')
        location = line[1].strip(' ')
        dataloc[courseID] = {'Location': location}
        
    for line in data_file3:
            line = line.strip().split(",")
            courseID = line[0].strip(' ')
            days = line[1].strip(' ')
            start_time = line[2].strip(' ')
            end_time = line[3].strip(' ') 
            datatime[courseID] = {'Days': days, 'Start Time': start_time, 'End Time': end_time}
   
    for line in instructors:
        line = line.strip().split(",")
        courseID = line[1].strip(' ')
        name = line[0].strip(' ')
        instructor = line[2].strip(' ')
        data[courseID] = {'Name' : name,'Instructor': instructor}
  
    for key in data:
         for keyloc in dataloc:
              if key == keyloc:
                  data[key]["Location"] = dataloc[keyloc]["Location"]
                  
    for key in data:
         for keytime in datatime:
              if key == keytime:
                  data[key]["Days"] = datatime[keytime]["Days"]
                  data[key]["Start Time"] = datatime[keytime]["Start Time"]
                  data[key]["End Time"] = datatime[keytime]["End Time"]
                  
    return data

def find_unscheduled(data):
    crs_without_locations=[]
    crs_without_times=[]
    for courseID in data:
        if not 'Location' in data[courseID]:
            crs_without_locations.append(courseID)
            
    for courseID in data:
        if not 'Days' in data[courseID]:
            crs_without_times.append(courseID)
    return crs_without_locations, crs_without_times

def clean_schedule(data, courses_to_remove):
 
    for courseID in courses_to_remove:
        del data[courseID]
    return data

def find_instructor(data, courseID):
    
    if courseID in data:
        return data[courseID]['Instructor']
    else:
     return "NA"
 
def find_subj_courses(data, subject):
    newsub = []
    for dataID in data:
        if dataID.startswith(subject):
            newsub.append(dataID)
    return newsub

def build_schedule(data, courses):
    
    student_text = open("student.txt","w+")
    program = []
    time_conflict = False  
    
    for firstcourse in courses:
        for secondc in courses:
           if firstcourse != secondc:
             if data[firstcourse]['Days'] == data[secondc]['Days']:
               if data[firstcourse]['Start Time'] == data[secondc]['Start Time']:
                  time_conflict = True

    for courseID in courses:
        if courseID in data:
            course_info = courseID, data[courseID]
            program.append(course_info)
            
    program = str(program)
    ", ".join(program)
              
              
    if time_conflict == True:
       student_text.write('***Time Conflict***') 
    else: 
       for i in range(len(courses)):
          student_text.write ("".join(courses[i])+','+str(data[courses[i]]['Location'])+','+str(data[courses[i]]['Days'])+','+str(data[courses[i]]['Start Time'])+','+str(data[courses[i]]['End Time'])+'\n')

    pass

def main():

    # part A
    data = read_schedules()
    find_unscheduled(data)
    # part B
    crs_without_locations, crs_without_times = find_unscheduled(data)
    # part C
    data = clean_schedule(data, crs_without_locations) 
    data = clean_schedule(data, crs_without_times)
    # part D
    print(find_instructor(data, "COMP304"))
    print(find_instructor(data, "ELEC202"))
    print(find_instructor(data, "COMP430"))
    # part E
    print(find_subj_courses(data, "COMP"))
    print(find_subj_courses(data, "CHBI"))
    print(find_subj_courses(data, "MECH"))
    print(find_subj_courses(data, "WRNG"))
    # part F
    build_schedule(data, ["COMP125", "MECH301", "COMP305", "ELEC301"])

    
    
        
################################################################ 
"""
DO NOT EDIT BELOW THIS LINE
"""
if __name__ == '__main__':
    main()
