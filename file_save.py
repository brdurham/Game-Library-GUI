#!usr/bin/python3
#Brady Durham
#1/28/20

import pickle
games = { 1: ['FPS', 'Halo3', 'Bungie', 'Microsoft', 'Xbox360', '2007',
              '10', 'either', '$30.00', 'yes', '1/15/2008', 'This game blows chunks!'],
          2: ['FPS', 'Doom', 'id Software', 'Bethesda Softworks', 'XboxOne', '2016',
                  '10', 'either', '$10.00', 'no', '4/8/2018', 'Heavy metal music intensifies'] }


datafile = open("game_lib.pickle", "wb")
pickle.dump(games, datafile)
datafile.close()