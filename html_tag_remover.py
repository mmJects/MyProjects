string = input("Please input the string: ")       # objective string which html tags will be deleted

# function to remove html tag of a string (start_index of tag,end_index of tag, string)
def delete_tags(start,end,obj_string):
    if start != end:                                # to check not to remove single angle brackets "<" or ">"
        first_partition = obj_string[:start]        # get the text in front of the tags
        second_partition = obj_string[end+1:]       # get the text behind the tags
        return first_partition + second_partition   # concatenate two portions and return as a string

# trckers for the indexs of a tag
start , end = 0 , 0
# tracker string to know we deleted the tags or not
track_string = string

for idx,char in enumerate(string):              # loop through the index,item of string
    if string != track_string:                  # if some tags are removed from orginal string 
        idx = 0                                 # reset the first_index to 0
    if char == "<":                             # if we find the the opening angle bracket
        start = idx                             # mark the index of that bracket as start_index
        end = idx                               # mark also as end_index
        while True:                             # loopthrough all characters behind a single opening angle bracket
            if string[end] == ">":              # if we find the closing bracket : the html tag
                break                           # break the while loop
            elif string[end] == "<":            # if we find the second opening angle bracket 
                start = end                     # 
            elif end == len(string)-1 and string[end] != ">":  # if there are not closing anlge bracket in the string      
                end = idx                       #  set the end_index as start_index because it is not a html tag
                break                           # break the loop
            end += 1                            # increae the end_indx by one
        string = delete_tags(start,end,string)  # reassign the tags deleted string to the original string 
        continue                                # restart the loop with new deleted tags string

print(f"Original String : {track_string}")          # compare the original string
print(f"No-tags  String : {string}")                # and new string