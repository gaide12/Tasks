def combine_anagrams(words_array):
    words_array=[i.lower() for i in words_array]
    whole_list=[]
    for i in words_array[::1]:
        new_list = []
        for j in words_array[::1]:
               if sorted(i)==sorted(j) :
                   new_list.append(j)
                   words_array.remove(j)
        if new_list:
            whole_list.append(new_list)
    return whole_list

print(combine_anagrams(["mars", "for", "rams", "racs", "rof", "scar",
"creams", "scream"]))