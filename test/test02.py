from PrintWithColor import print as print

print.change_settings(1, True)

print('Line 1 with nice green', f='green')
print('But this line is brighter!', s='bright') 

print.clear_settings()