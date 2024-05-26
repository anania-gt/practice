def common_elements(set_1, set_2):
    c_set=([set_1&set_2])
    print(sorted(list(c_set)))



set_1={1,2,3}
set_2={1,2,3,4,5,6}
common_elements(set_1, set_2)