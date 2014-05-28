'''
Created on May 6, 2014

@author: jasonbaer
'''
import SportLeague.League
import datetime
import os

if __name__ == '__main__':
    
    #Remove previous output files
    folder = 'output'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e

    #Gather basic duration stat
#    starttime = datetime.datetime.now()

    myLeague = SportLeague.League.League()
    myLeague.createLeague()

#    endtime = datetime.datetime.now()
#    diff = endtime - starttime
#    print "DURATION::"+str(diff.total_seconds())
    print "FIN"