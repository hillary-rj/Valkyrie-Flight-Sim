print('''
************************************************************************
     .  . '    .                                             
      '   .            . '            .                +           
              `                          '    . '
        .                         ,'`.                         .
   .                  .."    _.-;'    `.              .    
              _.-"`.##%"_.--" ,'        `.           "#"     ___,,od000
           ,'"-_ _.-.--"\   ,'            `-_       '%#%',,/////00000HH
         ,'     |_.'     )`/-     __..--""`-_`-._    J L/////00000HHHHM
 . +   ,'   _.-"        / /   _-""           `-._`-_/___\///0000HHHHMMM
     .'_.-""      '    :_/_.-'                 _,`-/__V__\0000HHHHHMMMM
 . _-""                         .        '   _,////\  |  /000HHHHHMMMMM
_-"   .       '  +  .              .        ,//////0\ | /00HHHHHHHMMMMM
       `                                   ,//////000\|/00HHHHHHHMMMMMM
.             '       .  ' .   .       '  ,//////00000|00HHHHHHHHMMMMMM
     .             .    .    '           ,//////000000|00HHHHHHHMMMMMMM
                  .  '      .       .   ,///////000000|0HHHHHHHHMMMMMMM
  '             '        .    '         ///////000000000HHHHHHHHMMMMMMM
                    +  .  . '    .     ,///////000000000HHHHHHHMMMMMMMM
     '      .              '   .       ///////000000000HHHHHHHHMMMMMMMM
   '                  . '              ///////000000000HHHHHHHHMMMMMMMM
                           .   '      ,///////000000000HHHHHHHHMMMMMMMM
       +         .        '   .    .  ////////000000000HHHHHHHHMMMMMMhs
************************************************************************
''')
print("Welcome to Valkyrie Flight Sim!\n")
print("Absalom Station has been under Azlanti Star Empire occupation for too long - today, the fight for a free Pact Worlds begins! Your mission, Captain Rosco, is to navigate the space battle and reach the Station in one piece. Good luck, soldier!\n") 

start = input("          Type 'y' to continue. ").lower()
print("\n")
if start == "y":
  print("The Valkyrie thwomps out of FTL, immediately faced with an Azlanti dreadnaught. Pilot instincts kicking in, you attempt to barrel roll to safety - but which way?\n")
  left_right = input("          Type 'left' or 'right'. ").lower()
  print("\n")
  if left_right == "left":
    print("Left is always right! You corkscrew away from danger as Chuk bumps his head on the ceiling - better buckle up, Chuk...\n\nThere's a frantic beeping on the targeting system - a missile heading straight for you! Perea can divert power to one system, but which?\n")
    system = input("          Type 'engine' or 'shields'. ").lower()
    print("\n")
    if system == "shields":
      print("Perea taps his omnitool without hesitation - there's a satisfying hum as the ship's shields stengthen. The missile explodes against the shield with a muffled boom, leaving the ship unharmed.\n\nThe landing zone is in sight, but dogfighters are in your way. Brut's ready on the guns - should he open up?\n")
      shoot = input("          Type 'attack' or 'refrain'. ").lower()
      print("\n")
      if shoot == "attack":
        print("Of course he should! Brut grins with devilish glee as he grips the triggers and shatters the fighters into pieces of shrapnel.\n\nRosco, the landing zone is close, but not close enough. The bay doors are closing. You've got time to give one command - should Rishek biotically lift the door, should Brut shoot it from the gunner's nest, or should you put your foot down and thread the needle?\n")
        door = input("          Type 'lift', 'shoot', or 'pilot'. ").lower()
        print("\n")
        if door == "lift":
          print("Rishek gathers biotic energy at his fingertips, concentrating as he channels the Element Zero through his L5x implant. He thrusts his hands upward as the energy ripples through the Valkyrie windshield, to the closing door... but it's not enough. The heavy door slams shut before the Valkyrie can land. Looks like you'll have to find another way... Game over.\n")
        elif door == 'shoot':
          print("High on his decimation of the dogfighters, Brut gets greedy. He unleashes an ungodly barrage on the heavy hangar door - rapidfire laser cannons, rockets, and plasma blasts. But the door is made of stern stuff, and the Valkyrie is far too close. The splash damage from Brut's attacks cripples the Valkyrie's shields, leaving it open to an Azlanti onslaught... Game over\n")
        elif door == 'pilot':
          print("Captain Rosco pushes the thrusters to full capacity. He grits his teeth as the ship draws closer to its goal, the rest of the crew bracing for a bumpy landing. The front of the Valkyrie ducks under the closing door, scraping along the metal floor of the hangar, the back half chewed up by the heavy door. A wing buckles and flies off, bisecting a squad of Greens as the ship grinds to a painful screeching halt.\n\nThough in poor condition, the Valkyrie has successfully made it onto Absalom Station. Now... it's time to end this war.\n\n\nCongratulations, Captain - you win! Thank you for playing this Virtua game, and have a pleasant day.\n")
          print('''
                                        _.oo.
                 _.u[[/;:,.         .odMMMMMM'
              .o888UU[[[/;:-.  .o@P^    MMM^
             oN88888UU[[[/;::-.        dP^
            dNMMNN888UU[[[/;:--.   .o@P^
           ,MMMMMMN888UU[[/;::-. o@^
           NNMMMNN888UU[[[/~.o@P^
           888888888UU[[[/o@^-..
          oI8888UU[[[/o@P^:--..
       .@^  YUU[[[/o@^;::---..
     oMP     ^/o@P^;:::---..
  .dMMM    .o@^ ^;::---...
 dMMMMMMM@^`       `^^^^
YMMMUP^
 ^^
          ''')
        else:
          print("You got this far into the game and chose not to go with one of the options? Or maybe you just fucked it with a typo. Ah well, guess you'll have to start all over again. Uhhh... let's say the Doomlurker comes back and swallows the Valkyrie whole. Shame. Game over.\n")
      elif shoot == "refrain":
        print("Refrain?! This is Brutimius Mauraka we're talking about, here... Alas, his past traumas resurface at the worst moment, and Brut cannot bring himself to pull the trigger. The fighters swarm the Valkyrie, barraging it with lasers until all systems are critical. Unresponsive to any controls, the Valkyrie drifts off into empty space. Eventually the crew starves to death, alone in the dark abyss. Game over.\n")
      else:
        print("That wasn't one of the options I gave you! Ander walks out of the cargo bay and casts a ninth level fireball on the whole crew. I bet Brut would still survive, but for the rest of them... Game over.\n")
    elif system == "engine":
      print("The engines scream as Perea overclocks them, and the Valkyrie's speed doubles. Unfortunately, the missile has an advanced homing system. With no power to shields, it collides with the ship's drift drive, instigating a nuclear chain reaction that vapourises the Valkyrie and all its inhabitants. Game over.\n")
    else:
      print("This is a multiple choice game, my friend. And that wasn't one of the choices. Perea panics, all engineering knowledge gone from his mind. He accepts his fate. With his final act, he removes his suit to reveal Luke Beavan underneath. Klep cries. Game over.\n")
  elif left_right == "right":
    print("Wrong choice, friend. You spin away from the dreadnaught, directly into the path of some high-velocity debris. Metal plating breaches the hull, and the Valkyrie's oxygen leaks into space. You and the crew suffocate before you can get your helmets on. Game over.\n")
  else:
    print("That wasn't one of the options, amigo. You hesitate a moment too long, and collide with the dreadnaught. Hard. The Valkyrie explodes in an inferno of incompetence. Game over.\n")
else:
  print("Wow, seriously? Fine, the Greens blow Absalom up. They take over the galaxy and the emperor personally teabags your corpses. Game over.\n")
