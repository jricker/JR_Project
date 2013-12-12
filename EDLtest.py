# EDL TEST
with open('C:\Users\jricker\Desktop\ghost_temp2.edl') as fp:
    for line in fp:
        print line
        if 'test_preview.mov' in line:
        	print line