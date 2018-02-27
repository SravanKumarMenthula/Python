
file1 = open("File1.txt",'r')
file2 = open("File2.txt",'r')

file1_line = file1.readline()
file2_line = file2.readline()

#open('f1.txt', 'w').close()
#open('f2.txt', 'w').close()
open('same.txt', 'w').close()

#logic = 0
while file1_line!='' or file2_line != '':
    file1_line = file1_line.strip()
    file2_line = file2_line.strip()

    '''with open('f1.txt','a') as write_file:
        write_file.write(file1_line.lower()+'\n')

    with open('f2.txt','a') as write_file:
        write_file.write(file2_line.lower()+'\n') '''


    if(file1_line == file2_line '''and logic == 0'''):
        with open('Same.txt','a') as write_file:
            write_file.write(file1_line.lower()+'\n')
    else:
        with open('Same.txt','w') as write_file:
            write_file.write("Two Files are not same")
        #logic = 1
        break

    file1_line = file1.readline()
    file2_line = file2.readline()
