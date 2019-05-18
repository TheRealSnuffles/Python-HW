import pickle
January = {'Activision':['Call of duty'],
            'Ubisoft':['Assassin\'s Creed'],
            'EA': ['Star Wars Project']}
February = {'Activision':'Spyro, Skylanders', 
            'Ubisoft':'Far Cry',
            'EA':'Need For Speed'}
March = {'Activision':['None'], 
          'Ubisoft':['Assassin\'s Creed 2'],
          'EA':['Anthem']}
April = {'Activison':['Call of Duty 2'],
          'Ubisoft':['Watch Dogs'], 
          'EA':['Madden NFL']}
May = {'Activison':['Ghost Busters'],
          'Ubisoft':['Far Cry 2'], 
          'EA':['FIFA 2018']}
June = {'Activison':['Call of Duty 2'],
          'Ubisoft':['Tom Clancy\'s Rainbow Six'], 
          'EA':['Apex Legends']}
July = {'Activison':['Call of Duty 2'],
          'Ubisoft':['Watch Dogs'], 
          'EA':['Madden NFL']}
August = {'Activison':['Call of Duty 2'],
          'Ubisoft':['Watch Dogs'], 
          'EA':['Madden NFL']}
September = {'Activison':'Call of Duty 2',
          'Ubisoft':'Watch Dogs', 
          'EA':'Madden NFL'}
October = {'Activison':'Call of Duty 2',
          'Ubisoft':'Watch Dogs', 
          'EA':'Madden NFL'}
November = {'Activison':'Call of Duty 2',
          'Ubisoft':'Watch Dogs', 
          'EA':'Madden NFL'}
December = {'Activison':'Call of Duty 2',
          'Ubisoft':'Watch Dogs', 
          'EA':'Madden NFL'}
output_file = open('Game_Releases.dat','wb')        
pickle.dump(January,output_file)
pickle.dump(February,output_file)
output_file.close()

#for key in months:
#  pickle.dump(key:value, output_file)
