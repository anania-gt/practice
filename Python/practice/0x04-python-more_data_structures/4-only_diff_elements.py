def only_diff_elements(set_1, set_2):
   od_set=set_1^set_2
   print(sorted(list(od_set)))

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
only_diff_elements(set_1, set_2)