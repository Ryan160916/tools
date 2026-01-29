import fs

str_taifeng = 'D:/work/study_python/ryan/Tropical_Storm.csv'
list_taifeng = fs.read_file(str_taifeng)
print(list_taifeng)


import ryan.object.storm_utils as storm_utils
i_jyl = int(input('请输入降雨量：'))
str_bydj = storm_utils.baoyu(i_jyl)
print(str_bydj)

