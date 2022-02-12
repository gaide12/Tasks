def count_words(sentence):
    punct = "!.,?();' -"
    for p in punct:
        if p in sentence:
            sentence = sentence.replace(p, " ")
    new=sentence.lower().split()
    count_dict={}
    for i in new:
        if i in count_dict:
            counter=count_dict.get(i,0)+1
            count_dict[i]=counter
        else : count_dict[i]=1
    return count_dict
print(count_words("A man, a plan, a canal -- Panama")) # => {"a": 3, "man": 1,"canal": 1, "panama": 1, "plan": 1}
print(count_words("Doo bee doo bee doo")) # => {"doo": 3, "bee": 2}
