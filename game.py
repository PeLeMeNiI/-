#names = ['firewey', 'dewedor','silverde','stupidnames']
#classes = ['amazon','necromancer','paladin','druid']
#levels =[2,2,3,4]
#def get_stats(name,name_list,class_list,level_list):
    #for i in range(len(names)):
        #if name_list[i] == name:
            #char_class = classes[i]
            #char_level = levels[i]

    #return char_class, char_level

#player_3 = get_stats('silverde', names, classes, levels)
#print(player_3)
#player_1 = {}

player_stats = {'firewey': 'amazon', 'dewedor':'necromancer'}

#name = player_stats['firewey']
#print(name)
#player_stats['firewey'] = 'barbarian'

#player_stats['mark'] = 'bard'

#del player_stats['firewey']

#player_stats['ne rabotaet']
#print('ne rabotaet' in player_stats)

#print('firewey' in player_stats)

#print(player_stats)

print(player_stats.keys())
print(player_stats.values())

for key in player_stats.keys():
    print(key)
