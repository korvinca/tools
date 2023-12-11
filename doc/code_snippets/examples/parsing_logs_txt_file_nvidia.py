GIT_LOG = """
commit e8e65233f50c16b1739
Author: korvinca <ivan.korolevskiy@gmail.com>
Date:   Tue Aug 1 21:20:00 2023 -0700

add imput

commit 8a1a43d0f173853d42
Author: korvinca <ivan.korolevskiy@gmail.com>
Date:   Tue Aug 1 13:08:08 2023 -0700

    update

commit 68e2b7cc3ce7889bcf
Author: korvinca <ivan.korolevskiy@gmail.com>
Date:   Tue Aug 1 12:55:02 2023 -0700

    Update    

commit 460831fc6c68206243
Author: korvinca <ivan.korolevskiy@gmail.com>
Date:   Tue Aug 1 11:42:01 2023 -0700

clear
"""

def get_content(l):
    line_con = l.split()
    return str(" ".join(line_con[1:]))

"""
a = "  hello  apple  "
b = "  hello  apple  "
c = "  hello  apple  "

print(a.strip()) # > 'hello  apple'
print(a.replace(" ", "")) # > 'helloapple'
print(" ".join(a.split())) # > 'hello  apple'
"""

def parcing_logs_to_array(logs_txt):
    lines = logs_txt.splitlines()
    data = []
    for line in lines:
        if line.startswith("commit"):
            data_sub = []
            arr_line = line.split()
            comm_id = str(arr_line[1])
            data_sub.append(comm_id)
        else:
            if not line:
                continue
            if "Author:" in line:
                data_sub.append(get_content(line))
            elif "Date:" in line:
                data_sub.append(get_content(line))
            else:
                #Trims characters from both ends of a string.
                data_sub.append(line.strip())
                data.append(data_sub)
    print(data)

def parcing_logs_to_dictionary(logs_txt):
    lines = logs_txt.splitlines()
    # data = [] # to add in Array
    data = {} # to add in Dictionary
    count = 1
    for line in lines:
        if line.startswith("commit"):
            data_sub = {}
            arr_line = line.split()
            comm_id = str(arr_line[1])
            data_sub["commit"] = comm_id
        else:
            if not line:
                continue
            if "Author:" in line:
                data_sub["Author"] = get_content(line)
            elif "Date:" in line:
                data_sub["Date"] = get_content(line)
            else:
                data_sub["Comment"] = line
                # data.append(data_sub) # to add in Array
                data[count] = data_sub # to add in Dictoary
                count += 1
    print(data)

print("Parsing to Array:")
parcing_logs_to_array(GIT_LOG)

print("Parsing to Dictionary:")
parcing_logs_to_dictionary(GIT_LOG)
