print "a)"
stud_sport = {"Inattag" : ["Kabaddi", "Chess"], "Alasatnahg" : ["Cricket", "Chess"], "Inenigog" : ["Cricket", "Chess"], "Uparavakog" : ["Cricket", "Football"], "Yttesirwog" : ["Kabaddi", "Basketball"], "Knamih" : ["Kabaddi", "Basketball"], "Sayerhs" : ["Kabaddi", "Basketball"], "Ihuj" : ["Cricket", "Football"], "Hsihsak" : ["Chess"], "Radek" : ["Kabaddi", "Basketball"]}
print stud_sport
print
print "b)"
stud_numsports = {"Inattag" : "", "Alasatnahg" : "", "Inenigog" : "", "Uparavakog" : "", "Yttesirwog" : "", "Knamih" : "", "Sayerhs" : "", "Ihuj" : "", "Hsihsak" : "", "Radek" : ""}
for i in stud_sport:
    stud_numsports[i] = len(stud_sport[i])
print stud_numsports        
print

print "c)"
sport_stud = {}
for i in stud_sport:
    for j in stud_sport[i]:
        if not j in sport_stud:
            sport_stud[j] = []
        sport_stud[j].append(i)
print sport_stud
