class Student:
    name = str()
    reg_no = str()
    marks_list = list()

class Marks:
    sub_code = str()
    internal = int()
    theory = int()
    sem = int()


import PyPDF2
import os
from datetime import datetime
def coversion(file,seme):

    print("Running")

    #extraction of received pdf file
    obj = open(file,'rb')
    read=PyPDF2.PdfFileReader(obj)
    t=str()
    for i in range(1,read.numPages):
    	pobj=read.getPage(i)
    	t+=pobj.extractText()
    obj.close()
    
    file_name = datetime.now().strftime("%y%m%d_%H%M%S")

    #creating text file and saving
    handle = open(file_name +".txt", "w")
    handle.write(t)
    handle.close()

    sem = seme

    # opening file in read mode
    handle = open(file_name +".txt", "r")

    sub_list = list()
    d = dict()


    #exceptional marks handling function
    def int_convert(x):
    	try:
    		return int(x)
    	except:
    		return 0





    # finding paper codes available
    for lines in handle:
        if 'Paper Code :' in lines:
            ri = lines.index("Paper Code :")
            sub_list = lines[ri+12:ri+100].split()
            break

    # assigning everything to a dictionary
    for lines in handle:
        if 'Register No.' in lines:
            ri = lines.index("Register No.")
            reg = lines[ri+13:ri+23]
            d[reg] = {'Name': lines[ri+34:ri+70].strip()}
        if 'Total Marks:' in lines:
            ri = lines.index("Total Marks:")
            sum1 = sum(list(map(int_convert, lines[ri+12:ri+100].split())))
            d[reg]['Theory marks'] = list(map(int_convert, lines[ri+12:ri+100].split()))
        if 'I.A.Marks  :' in lines:
            ri = lines.index("I.A.Marks  :")
            sum2 = sum1+sum(list(map(int_convert, lines[ri+12:ri+100].split())))
            d[reg]['Internal marks'] = list(map(int_convert, lines[ri+12:ri+100].split()))
            d[reg]['Marks'] = sum2
    handle.close()


    S_list=[]


    #assing everything in dictionary to student class objects
    for i,j in d.items():
        s1 = Student()
        s1.reg_no = i
        s1.name = j['Name']
        m = []
        
        for k in range(len(j['Internal marks'])):
            m1 = Marks()
            m1.sub_code = sub_list[k]
            m1.internal = j['Internal marks'][k]
            try:
                m1.theory = j['Theory marks'][k]
            except:
                m1.theory = 0
            m1.sem = sem
            m.append(m1)
        s1.marks_list = m
        S_list.append(s1)
    
    # deleting created file
    if os.path.exists(file_name+".txt"):
      os.remove(file_name+".txt")
    else:
      print("The file does not exist")

    return S_list

#calling conversion function with file and semester



#printing the result for cross verification






