import shelve
hg_file = shelve.open('high_score')
hg_score = 0
hg_file['hg_score'] = hg_score
hg_file.close()
