








import random
from PIL import Image, ImageTk



import tkinter as tk

FPSTips=["Master your weapon recoil control.","Practice aiming for headshots consistently.","Learn to utilize grenades effectively for area denial.","Keep your crosshair placement at head level.","Use sound cues to anticipate enemy movements.","Regularly adjust your sensitivity until it feels comfortable.","Study map layouts to know key locations and choke points.","Communicate with your team to coordinate strategies.","Utilize cover to minimize exposure to enemy fire.","Practice strafing while shooting to throw off enemy aim.","Experiment with different weapons to find your preferred loadout.","Stay calm and composed during intense firefights.","Use burst fire for better accuracy over long distances.","Pre-aim common enemy positions before entering a room.","Keep an eye on your ammo count and reload strategically.","Master movement techniques like bunny hopping and strafe jumping.","Watch professional players' streams or videos to learn new strategies.","Keep your screen clean to avoid distractions during gameplay.","Practice peeking corners efficiently to minimize exposure.","Learn to quickly switch between weapons in your loadout.","Use sound masking techniques like footsteps to mask your own movements.","Don't neglect your peripheral vision; be aware of your surroundings.","Experiment with different graphics settings for optimal performance.","Stay unpredictable in your movement patterns to avoid being an easy target.","Control your breathing to maintain focus during intense moments.","Take breaks to avoid burnout and maintain peak performance.","Stay informed about game updates and patches for meta changes.","Play with a comfortable posture and setup to reduce fatigue.","Practice patience and avoid rushing into unfavorable engagements.","Learn to pre-fire common enemy positions to catch them off guard.","Utilize the minimap to track enemy movements and plan accordingly.","Stay aware of your team's positioning and adapt your strategy accordingly.","Experiment with different crosshair styles to find what works best for you.","Keep your movements fluid to maintain momentum and agility.","Stay mentally flexible and adapt to changing game dynamics.","Warm up before gaming sessions with aim training exercises.","Study your own gameplay footage to identify areas for improvement.","Stay patient and avoid tilting after a string of defeats.","Communicate enemy positions accurately and concisely to your team.","Practice quick decision-making to react to changing situations.","Use high ground advantage to control the battlefield.","Practice map control to deny enemy movement and objectives.","Stay aware of the game's meta and adjust your playstyle accordingly.","Keep your crosshair placement dynamic to anticipate enemy movements.","Utilize game mechanics like crouching and leaning to your advantage"]
StealthTips=["Master the art of silent movement to avoid detection.","Patience is key; wait for the right moment to strike or sneak past enemies.","Use distractions such as throwing objects to create diversions.","Study enemy patrol patterns and timing to plan your movements.","Stay in the shadows to remain undetected.","Learn to pick locks or hack systems to access restricted areas.","Use environmental elements like foliage or darkness for cover.","Disable security cameras or alarms to prevent detection.","Utilize stealth takedowns to silently eliminate enemies.","Use non-lethal methods whenever possible to avoid raising alarms.","Take out isolated enemies first to reduce the risk of detection.","Plan your escape route before initiating any action.","Use disguises or uniforms to blend in with enemy personnel.","Hack into security systems to manipulate enemy perceptions.","Stay out of the line of sight of guards and cameras to maintain stealth.","Use verticality to your advantage by utilizing rooftops and high vantage points.","Employ gadgets such as smoke bombs or distraction devices to create opportunities.","Observe enemy behavior to exploit weaknesses in their patrols.","Use the environment to your advantage, such as hiding in vents or behind cover.","Stay aware of your surroundings and adapt to changes in enemy behavior.","Use the darkness to your advantage by extinguishing lights or creating shadows.","Take advantage of alternate routes and hidden passages to bypass heavily guarded areas.","Use sound masking techniques such as environmental noise to cover your movements.","Hack into enemy communication channels to gather intel and create diversions.","Utilize stealth camouflage or invisibility to evade detection in plain sight.","Employ decoys or dummies to distract guards and create openings.","Stay patient and avoid rushing; observe before taking action.","Use melee weapons or tranquilizers for silent takedowns.","Disguise yourself as a civilian or blend into crowds to evade suspicion.","Employ stealthy movement techniques like crouch-walking and wall-hugging.","Study enemy behavior patterns to predict their reactions to your actions.","Use distraction items like thrown coins or noise-makers to manipulate enemy movements.","Take advantage of contextual cover like hiding behind furniture or walls.","Use the environment to your advantage, using natural obstacles for cover and concealment.","Stay vigilant for security cameras and disable them when possible to avoid detection.","Utilize the terrain to create diversions, such as triggering environmental hazards.","Stay mindful of your noise level; avoid sprinting or making unnecessary sounds.","Use hacking abilities to disable electronic locks and security systems.","Exploit enemy weaknesses, such as vulnerabilities to certain types of attacks or distractions.","Use non-lethal methods to incapacitate enemies without alerting others.","Employ stealth-enhancing upgrades or abilities to improve your infiltration capabilities.","Stay patient and observant, waiting for the opportune moment to strike or sneak past.","Use the environment to your advantage, utilizing hiding spots and cover to remain unseen.","Stay informed about enemy movements and objectives to plan your approach accordingly.","Employ diversion tactics like setting off alarms or causing disturbances to draw attention away from your position.","Utilize camouflage or disguises to blend in with your surroundings and avoid detection.","Stay adaptable, adjusting your strategy based on evolving enemy tactics and patrols.","Employ distraction techniques like throwing objects or creating noise to divert enemy attention.","Study enemy patrol routes and behavior to identify vulnerable points for infiltration.","Use stealth techniques like distraction and misdirection to outwit your adversaries.","Stay patient and methodical, taking your time to assess the situation before making a move"]
SurvivalTips=["Prioritize basic needs like food, water, and shelter to ensure survival.","Craft essential tools and weapons early on to defend yourself and gather resources.","Stay vigilant for threats such as wildlife, environmental hazards, and other players.","Explore your surroundings carefully to find valuable resources and strategic locations.","Build a secure base or shelter to protect yourself from the elements and hostile forces.","Gather and store resources efficiently to sustain yourself during lean times.","Learn to forage for edible plants and hunt wildlife for food.","Stay aware of your surroundings and be prepared to react quickly to unexpected dangers.","Manage your inventory wisely, carrying only what you need and discarding excess weight.","Keep an eye on your health and stamina levels, and prioritize rest and recovery when necessary.","Craft clothing and gear to protect yourself from the elements and improve your survival chances.","Establish alliances or join groups for mutual protection and resource sharing.","Plan your routes carefully to avoid dangerous areas and maximize resource collection.","Stay hidden and avoid unnecessary conflicts to minimize the risk of injury or death.","Use traps and defensive structures to deter hostile creatures and players from attacking your base.","Stay informed about updates and changes to the game's mechanics and environment.","Adapt to changing conditions and threats by continually evolving your survival strategies.","Stay calm and focused in stressful situations to make rational decisions and avoid panic.","Monitor your hydration and energy levels closely, as dehydration and exhaustion can be deadly.","Gather and stockpile resources for long-term survival, including food, water, and building materials.","Craft and use weapons for self-defense, but avoid unnecessary conflict whenever possible.","Use stealth and camouflage to avoid detection by hostile creatures and players.","Learn to navigate using landmarks and natural features to avoid getting lost in the wilderness.","Stay warm and dry to prevent hypothermia and other cold-related injuries.","Stay alert for signs of danger, such as animal tracks, strange noises, or hostile player activity.","Keep a backup supply of essential items in case of emergencies or unexpected events.","Investigate your surroundings carefully for hidden caches of supplies and valuable loot.","Stay well-rested to maintain peak physical and mental performance during survival challenges.","Prioritize tasks based on their urgency and importance to maximize your efficiency and effectiveness.","Build and maintain a sustainable food source, such as a garden or livestock, to reduce reliance on scavenging.","Avoid drawing unnecessary attention to yourself with loud noises, bright lights, or conspicuous behavior.","Stay informed about weather patterns and other environmental factors that could affect your survival.","Stay hydrated by drinking clean water regularly, and avoid consuming contaminated or unsafe liquids.","Use fire for warmth, cooking, and protection, but be mindful of the risk of wildfires and burns.","Keep your weapons and gear in good condition by regularly repairing and maintaining them.","Stay mentally resilient by staying positive and focused on your survival goals.","Be prepared for emergencies by keeping a first aid kit and other essential supplies on hand.","Stay flexible and adaptable to changing circumstances, and be willing to adjust your plans as needed.","Trust your instincts and intuition, but also rely on logic and rational thinking to make informed decisions.","Stay connected with other survivors through communication channels and community forums.","Learn from your mistakes and failures to improve your survival skills and strategies over time.","Stay disciplined and organized to avoid wasting time and resources on unnecessary tasks.","Stay patient and persistent in your efforts to survive, even in the face of seemingly insurmountable challenges.","Stay humble and open to learning from others, as survival is often a collective effort.","Stay motivated and focused on your long-term survival goals, even when faced with setbacks and obstacles.","Stay aware of your surroundings at all times, and be prepared to react quickly to potential threats or dangers"]
SportTips=["Master the basic controls and mechanics of the game before diving into advanced strategies.","Study real-life tactics and strategies used by professional athletes and teams.","Practice regularly to improve your skills and reaction times.","Learn to anticipate your opponent's moves and adapt your strategy accordingly.","Focus on teamwork and cooperation to achieve victory as a cohesive unit.","Study the strengths and weaknesses of your opponents to exploit their vulnerabilities.","Stay disciplined and composed, even in high-pressure situations.","Stay physically and mentally fit to maintain peak performance during games.","Communicate effectively with your teammates to coordinate plays and strategies.","Study game statistics and data to identify patterns and trends that can give you an edge.","Experiment with different formations and strategies to find what works best for your team.","Watch replays of your games to analyze your performance and identify areas for improvement.","Learn from your mistakes and use them as opportunities for growth and development.","Stay positive and motivated, even in the face of adversity or setbacks.","Practice good sportsmanship and respect your opponents, regardless of the outcome"]
MOBATips=["Communicate effectively with your team through pings, chat, or voice communication.","Understand the roles of different heroes or champions and how they contribute to the team composition.","Focus on farming or last-hitting to earn gold and experience for your hero.","Ward key areas of the map to provide vision and prevent enemy ganks.","Rotate between lanes to help teammates and apply pressure across the map.","Coordinate with your team to secure objectives such as towers, buffs, or Roshan.","Manage your resources wisely, including health, mana, and cooldowns.","Keep an eye on the minimap to track enemy movements and potential threats.","Practice good map awareness to avoid getting caught out of position.","Adapt your item builds and skill orders based on the matchup and game situation.","Stay positive and avoid flaming or blaming teammates for mistakes.","Set up ganks or ambushes with your team to secure kills and gain map control.","Prioritize objectives over kills - destroying towers and securing map control wins games.","Rotate to defend towers or respond to enemy pushes when necessary.","Coordinate team fights by focusing priority targets and communicating cooldowns.","Keep track of enemy item builds and adjust your strategy accordingly.","Maintain good positioning during team fights to maximize your impact.","Use fog of war to your advantage by setting up ambushes or juking opponents.","Be mindful of the power spikes of your hero and those of your opponents.","Practice effective last-hitting to maximize your gold income in the laning phase.","Utilize the jungle efficiently by stacking camps, farming, or setting up ganks.","Learn to predict enemy movements and anticipate their next move.","Manage your lane equilibrium to control the pace of the game and deny farm to your opponents.","Use the terrain to your advantage by juking through trees or hiding in bushes.","Stay calm and focused, especially during intense moments or team fights.","Communicate with your team to coordinate ganks, rotations, and team fights.","Maintain good map awareness by checking the minimap frequently for enemy movements.","Ward key areas of the map to gain vision and control objectives.","Communicate with your team to coordinate pushes, defenses, and rotations.","Take advantage of power spikes to press your advantage and secure objectives.","Stay positive and supportive of your teammates, even in challenging situations.","Coordinate with your team to secure kills, objectives, and map control.","Practice good positioning in team fights to maximize your impact.","Adapt your item build and skill order based on the game's progression and enemy composition.","Focus on farming efficiently to stay ahead in gold and experience.","Communicate effectively with your team to coordinate ganks, rotations, and team fights.","Keep an eye on the minimap to track enemy movements and potential ganks.","Ward key areas of the map to provide vision and control objectives.","Rotate between lanes to help teammates and apply pressure across the map.","Stay positive and focused, even in challenging situations or when behind in the game.","Practice good map awareness to avoid getting caught out of position.","Coordinate with your team to secure objectives such as towers, buffs, or objectives.","Adapt your playstyle based on the matchup and game situation.","Stay calm and avoid tilting, even if things don't go as planned.","Communicate with your team to coordinate strategies and execute them effectively.","Keep track of enemy cooldowns and use them to your advantage in fights.","Practice effective communication with your team to coordinate rotations and ganks.","Stay positive and avoid blaming teammates for mistakes or losses.","Use the fog of war to your advantage by setting up ambushes or surprising enemies.","Practice effective warding to gain vision and control over key areas of the map.","Stay focused and maintain good map awareness to avoid getting caught out of position.","Communicate with your team to coordinate objectives, ganks, and team fights.","Adapt your item builds and skill orders based on the game's progression and your team's needs.","Coordinate with your team to secure objectives such as towers, buffs, or Roshan.","Stay positive and supportive of your teammates, even in challenging situations.","Practice good positioning in team fights to maximize your impact and avoid getting caught out of position.","Communicate effectively with your team through pings, chat, or voice communication."]
DrivingTips=["Practice regularly to improve your driving skills.","Understand the handling differences between various vehicles.","Learn the tracks or maps to anticipate corners and obstacles.","Experiment with different control settings to find your preference.","Familiarize yourself with the controls through tutorials or practice modes.","Adjust the camera angle for the best view of the track.","Brake early and gradually to avoid losing control.","Be aware of other drivers to avoid collisions.","Utilize in-game assists like traction control if available.","Try different driving techniques such as drifting or drafting.","Practice fair play and avoid aggressive driving tactics.","Manage your vehicle's condition to maintain performance.","Stay focused and maintain situational awareness.","Take breaks if you feel fatigued or frustrated.","Explore different types of racing games for variety.","Join online communities for tips, strategies, and competitions.","Use your turn signals or indicators for better communication.","Be cautious when overtaking or passing other vehicles.","Keep an eye on your rearview mirror for approaching opponents.","Take advantage of shortcuts or alternate routes if available.","Avoid collisions with barriers or walls to maintain speed.","Practice cornering techniques to maintain speed through turns.","Monitor your speed, especially in tight or narrow sections.","Learn to anticipate and navigate through traffic.","Adjust your driving style based on the weather conditions.","Stay calm and composed, especially during intense moments.","Use your brakes wisely to avoid locking up or skidding.","Practice defensive driving to minimize the risk of accidents.","Experiment with different camera perspectives for better visibility.","Master the art of drafting to gain speed behind other vehicles.","Use handbrake turns strategically to navigate tight corners.","Learn from your mistakes and analyze your driving performance.","Experiment with different racing lines to find the fastest route.","Pay attention to trackside markers or visual cues for braking points.","Practice throttle control to maintain traction, especially on slippery surfaces.","Be mindful of track conditions that may change during the race.","Practice smooth steering inputs for better control.","Avoid sudden movements or jerky steering corrections.","Utilize rewind or instant replay features to learn from errors.","Take advantage of practice sessions to fine-tune your setup.","Experiment with different tire compounds for optimal grip.","Adjust your strategy based on the length and format of the race.","Study opponents' driving behaviors to anticipate their moves.","Practice consistent lap times to build endurance and consistency.","Analyze telemetry data or race replays to identify areas for improvement.","Use drafting to conserve fuel or gain a speed advantage.","Maintain a balance between aggression and caution during races.","Utilize pit stops strategically to gain an edge over competitors.","Practice proper throttle modulation to prevent wheelspin.","Enjoy the thrill of racing and celebrate your progress along the way"]
photo=[]




class GetGud:
    def __init__(self,root):
        self.root = root
        self.root.title("Get Gud") 
        self.root.geometry("420x250")
        root.config(bg='#3159a3')
        self.genre = ""
        self.first_page()


    def delete_buttons(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    # def delete_dropdowns(self):
    #     self.delete_dropdowns
    
    
    
    def first_page(self):
        self.delete_buttons()
        self.label = tk.Label(root, text = "Choose your game category",
        font = ("Calibri 24"), bg ='#dcecfa', fg = '#7092be' )
        self.label.pack(pady =20)

        self.button1 = tk.Button(root, text ="FPS", fg = "#99d9ea", command = self.Generate_FPS_tip)
        self.button2 = tk.Button(root, text ="Stealth", fg = "#99d9ea", command = self.Generate_Stealth_Tip)
        self.button3 = tk.Button(root, text ="Sport", fg = "#99d9ea", command = self.Generate_Sport_Tip)
        self.button4 = tk.Button(root, text ="MOBA", fg = "#99d9ea", command = self.Generate_MOBA_Tip)
        self.button5 = tk.Button(root, text ="Survival", fg = "#99d9ea", command = self.Generate_Survival_Tip)
        self.button6 = tk.Button(root, text ="Driving", fg = "#99d9ea", command = self.Generate_Driving_Tip)
        
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()
        self.button6.pack()

    def second_page(self):
        self.delete_buttons()
        self.button7 = tk.Button(root, text ="Generate Tip", fg = "#99d9ea", command = self.Give_Tip)
        self.button7.config( height = 2, width=10)
        self.button7.pack()
    
        self.selected_option = tk.StringVar()
        random_texts = random.choice(FPSTips)
        self.selected_option.set(random_texts)
        frame = tk.Frame(root)
        frame.config(bg='#3159a3')
        frame.pack()
        self.label = tk.Label(frame, textvariable = self.selected_option)
        self.label.pack(pady =0, fill=tk.BOTH,expand=True)
        photo = self.Insert_Image()
        self.TipImage = tk.Label(frame)
        self.TipImage.config(image=photo)
        self.TipImage.image = photo
        self.TipImage.pack()
        self.button8 = tk.Button(frame, text = "Return", fg = "#99d9ea",command = self.first_page)
        self.button8.pack()
    def button_press(self):
        self.button1.destroy
        self.button2.destroy
        self.button3.destroy
        self.button4.destroy
        self.button5.destroy
        self.button6.destroy
    
    def Generate_FPS_tip(self):
        self.genre = "FPS"
        self.second_page()

    def Generate_Stealth_Tip(self):
        self.genre = "Stealth"
        self.second_page()

    def Generate_Sport_Tip(self):
        self.genre = "Sport"
        self.second_page()    

    def Generate_MOBA_Tip(self):
        self.genre = "MOBA"
        self.second_page()

    def Generate_Survival_Tip(self):
        self.genre = "Survival"
        self.second_page()

    def Generate_Driving_Tip(self):
        self.genre = "Driving"
        self.second_page()

    def Give_Tip(self):
        if self.genre == "FPS":
            random_text = random.choice(FPSTips)
        if self.genre == "Stealth":
            random_text = random.choice(StealthTips)
        if self.genre == "Sport":
            random_text = random.choice(SportTips)
        if self.genre == "Survival":
            random_text = random.choice(SurvivalTips)
        if self.genre == "MOBA":
            random_text = random.choice(MOBATips)
        if self.genre == "Driving":
            random_text = random.choice(DrivingTips)
        
        self.selected_option.set(random_text)
        print(random_text)
    
    
    def Insert_Image(self):
        if self.genre == "FPS":
            image = Image.open("FPSScreenshot.png")
        if self.genre == "Stealth":
            image = Image.open("StealthScreenshot.png")
        if self.genre == "Sport":
            image = Image.open("SportScreenshot.png")
        if self.genre == "Survival":
            image = Image.open("SurvivalScreenshot.png")
        if self.genre == "MOBA":
            image = Image.open("MOBAScreenshot.png")
        if self.genre == "Driving":
            image = Image.open("DrivingScreenshot.png")

        photo = image.resize((200,100))
        return ImageTk.PhotoImage(photo)

root = tk.Tk()
getGud=GetGud(root)
root.mainloop()



