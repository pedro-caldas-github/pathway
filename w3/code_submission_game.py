print("Welcome to the Amazon Forest Adventure!")
print("You're dropped by parachute in the forest. When you finally touch the ground, you see two paths ahead.")
print("You hear water and you see what you think is a boat, but also there is a path that goes inside the jungle. What do you do?")

choice1 = input("Choice (BOAT/TRAIL): ").upper()

if choice1 == "BOAT":
    print("\nYou are now at the river. The water is really dark and the river current starts to drag you.")
    print("Do you try to SWIM against the current or GRAB onto nearby roots?")

    choice2 = input("Choice (SWIM/GRAB): ").upper()

    if choice2 == "SWIM":
        print("\nThe current is too strong! You struggle to stay afloat.")
        print("Do you try to reach a distant LOG or give up and DRIFT?")

        choice3 = input("Choice (LOG/DRIFT): ").upper()

        if choice3 == "LOG":
            print("\nYou manage to reach the log, but it's slippery and unstable. You fall back into the raging river.")
            print("--- GAME OVER!!! ---")
        elif choice3 == "DRIFT":
            print("\nYou give up fighting and let the river carry you. It eventually leads you to a hidden waterfall.")
            print("--- GAME OVER!!! ---")
        else:
            print("\nInvalid choice.")
            print("--- GAME OVER!!! ---")

    elif choice2 == "GRAB":
        print("\nYou manage to grab onto some roots at the river's edge. You're safe for now, but stuck.")
        print("You see a faint light further down the river, and a narrow path leading into the jungle. Do you FOLLOW the light or take the JUNGLE path?")

        choice3 = input("Choice (FOLLOW/JUNGLE): ").upper()

        if choice3 == "FOLLOW":
            print("\nYou follow the faint light. It leads you to a small, abandoned boat with a working engine. You escape the forest!")
            print("--- CONGRATULATIONS! YOU WIN! ---")
        elif choice3 == "JUNGLE":
            print("\nYou take the jungle path. It's dense and full of unknown sounds. You quickly get lost and disoriented.")
            print("--- GAME OVER!!! ---")
        else:
            print("\nInvalid choice.")
            print("--- GAME OVER!!! ---")
    else:
        print("\nInvalid choice.")
        print("--- GAME OVER!!! ---")

elif choice1 == "TRAIL":
    print("\nYou went to the trail. When you got into the forest, you heard what you think is an animal walking.")
    print("Do you HIDE behind a bush or try to SNEAK past?")

    choice2 = input("Choice (HIDE/SNEAK): ").upper()

    if choice2 == "HIDE":
        print("\nYou hide behind a thick bush. A large jaguar passes by, thankfully not seeing you.")
        print("Do you now CONTINUE on the trail, try to FIND an alternate route, or WAIT for dawn?")

        choice3 = input("Choice (CONTINUE/FIND/WAIT): ").upper()

        if choice3 == "CONTINUE":
            print("\nYou continue cautiously on the trail. You eventually find a hidden village and are rescued!")
            print("--- CONGRATULATIONS! YOU WIN! ---")
        elif choice3 == "FIND":
            print("\nYou try to find an alternate route, but the jungle is too dense. You get hopelessly lost.")
            print("--- GAME OVER!!! ---")
        elif choice3 == "WAIT":
            print("\nYou wait patiently for dawn. As the sun rises, you spot a clear path leading out of the forest!")
            print("--- CONGRATULATIONS! YOU WIN! ---")
        else:
            print("\nInvalid choice.")
            print("--- GAME OVER!!! ---")

    elif choice2 == "SNEAK":
        print("\nYou try to sneak past, but the animal hears you and turns. It's a large, territorial capybara, looking agitated.")
        print("Do you RUN away or try to CALM it?")

        choice3 = input("Choice (RUN/CALM): ").upper()

        if choice3 == "RUN":
            print("\nYou run, but the capybara is surprisingly fast. It chases you until you trip and fall.")
            print("--- GAME OVER!!! ---")
        elif choice3 == "CALM":
            print("\nYou try to calm the capybara, offering it some leaves. It surprisingly responds well and leads you to a safe path out.")
            print("--- CONGRATULATIONS! YOU WIN! ---")
        else:
            print("\nInvalid choice.")
            print("--- GAME OVER!!! ---")
    else:
        print("\nInvalid choice.")
        print("--- GAME OVER!!! ---")

else:
    print("\nInvalid choice.")
    print("--- GAME OVER!!! ---")