# Police_Interrogation_Text_Game
This is a text based game in which assuming the role of a police officer you engage in interracting 3 suspects to find the one that is lying. 
There are 3 stages (cases) all of which share the same gameplay loop:
I) The player is presented with the available information of that case, which should always be taken as valid
II) The play is presented with a list of questions for the suspects. Each time they picks one the three different responses can be instantly juxtaposed.
III) If the player spots a logical or factual contradiction between a suspect's response, a previous response, any of the available information or common knowledge they can move to the accusatory phase, or the can ask more questions.
IV) During the accusatory phase the player types the number corresponding to the suspect they deem guilty and they are immediatly informed whether they were right and move on to the next case.
There are only 3 stages, but the file can be very easily updated because all stages are ran by the same function that takes as parameter the information , questions , answers and correct solution of each corresponding case.
