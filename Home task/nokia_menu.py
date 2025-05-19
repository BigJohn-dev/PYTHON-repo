# NOKIA 3310 MENU APPLICATION

print('     _- WELCOME TO YOUR NOKIA PHONE -_ ')

home = """
	==========================
		HOME PAGE

	  Press 0 to go to menu:
	==========================
		"""
print(home)
option_menu = int(input('Enter option: '))

match option_menu:
	case 0:
 		Menu = """
	    LIST OF MENU FUNCTIONS

   1. Phone book		2. Message
   3. Chat			4. Call register
   5. Tones			6. Settings
   7. Call divert		8. Games
   9. Calculator		10. Reminders
   11. Clock			12. Profiles
   13. SIM services		0. Back
		"""
print(Menu)
phonebook_options = int(input('Enter option: '))

# First option from list of Menu functions
match phonebook_options:
	case 1:
		first = """
		  PHONE BOOK

   1. Search			2. Service Nos
   3. Add name			4. Erase
   5. Edit			6. Assign tone
   7. Send b'card		8. Options
   9. Speed dials		10. Voice tags
   0. Back
		"""
		print(first)
		phone_book_option = int(input('Enter option: '))
		match phone_book_option:

# Sub options for phone book
			case 1:
				one = """
		    SEARCH
		
		   0. Back
				"""
				print(one)

			case 2:
				two = """
		  SERVICE NOS
		
		  0. Back
				"""
				print(two)
			
			case 3:
				three = """
		   ADD NAME
		
		   0. Back
				"""
				print(three)

			case 4:
				four = """
		   ERASE
		
		   0. Back
				"""
				print(four)

			case 5:
				five = """
		    EDIT
		
		   0. Back
			   	"""
				print(five)

			case 6:
				six = """
		  ASSIGN TONE
		
		    0. Back
			   	"""
				print(six)

			case 7:
				seven = """
		  SEND B'CARD
		
		   0. Back
			    	"""
				print(seven)

			case 8:
				eight = """
		   OPTION

 1. Type of view		2. Memory status
 0. Back
				"""
				print(eight) 

# sub option for phone book (option 8)
				option_8 = int(input('Enter option: '))
				match option_8:
					case 1: 
						eight_one = """
		TYPE OF VIEW
		
		  0. Back
						"""
						print(eight_one)

					case 2:
						eight_two = """
		MEMORY STATUS
		
		  0. Back
						"""
						print(eight_two)

			case 9:
				nine = """
		SEARCH DIALS
		
		 0. Back
				"""
				print(nine)

			case 10:
				ten = """
		VOICE TAGS
		
		 0. Back
				"""
				print(ten)

# Second option from list of Menu functions
	case 2:
		second = """
		 MESSAGE

  1. Write messages		2. Inbox
  3. Outbox			4. Picture messages
  5. Templates			6. Smileys
  7. Message settings		8. Info service
  9. Voice mailbox number	10. Service command editor
  0. Back
		"""
		print(second)
		message_options = int(input('Enter option: '))

# Sub options for Message
		match message_options:
			case 1:
				One = """
		WRITE MESSAGE
		
		  0. Back
				"""
				print(One)

			case 2:
				Two = """
		   INBOX
		
		  0. Back
				"""
				print(Two)

			case 3: 
				Three = """
		   OUTBOX
		
		  0. Back
				"""
				print(Three)

			case 4:
				Four = """
		PICTURE MESSAGES
		
		   0. Back
				"""
				print(Four)

			case 5:
				Five = """
		   TEMPLATES
		
		  0. Back
				"""
				print(Five)

			case 6:
				Six = """
		   SMILEYS
		
		  0. Back
				"""
				print(Six)

			case 7:
				Seven = """
		MESSAGE SETTINGS

	1. Set 1		2. Common
	0. Back
				"""
				print(Seven)

# sub option for Message (option 7)
				option_7 = int(input('Enter option: '))
				match option_7:
					case 1:
						Seven_one = """
			SET 1

	1. Message centre number	2. Messages sent as
	3. Message validity
	0. Back
						"""
						print(Seven_one)
						option_7_one = int(input('Enter option: '))
						match option_7_one:
								case 1:
									Seven_one_one = """
		MESSAGE CENTRE NUMBER

		     0. Back
									"""
									print(Seven_one_one)
								case 2:
									Seven_one_two = """
		  MESSAGE SENT AS

		     0. Back
									"""
									print(Seven_one_two)
								case 3:
									Seven_one_three = """
		 MESSAGE VALIDITY

		     0.Back
									"""
									print(Seven_one_three)


					case 2:
						Seven_two = """
			COMMON

	1. Delivery report	2. Reply via same centre
	3. Character support	0. Back
						"""
						print(Seven_two)
						option_7_two = int(input('Enter option: '))
						match option_7_two:
								case 1:
									Seven_two_one = """
		  DELIVERY REPORT

		     0. Back
									"""
									print(Seven_two_one)
								case 2:
									Seven_two_two = """
	       REPLY VIA SAME CENTRE

		     0. Back
									"""
									print(Seven_two_two)
								case 3:
									Seven_two_three = """
		CHARACTER SUPPORT

		     0.Back
									"""
									print(Seven_two_three)


			case 8: 
				Eight = """
	         INFO SERVICE
		
		   0. Back		
				"""
				print(Eight)

			case 9:
				Nine = """
	    VOICE MAILBOX NUMBER
		
		 0. Back
				"""
				print(Nine)

			case 10:
				Ten = """
	   SERVICE COMMAND EDITOR
		
		0. Back
				"""
				print(Ten)


# Third option from list of Menu functions
	case 3: 
		third = """
		    CHAT
		
		  0. Back
		"""
		print(third)


# Fourth option from list of Menu functions
	case 4:
		fourth = """
		CALL REGISTER

   1. Missed calls		2. Received calls
   3. Dialled numbers		4. Erase recent call lists
   5. Show call duration	6. Show call costs
   7. Call cost settings	8. Prepaid credit
   0. Back
		"""
		print(fourth)
		call_register_options = int(input('Enter option: '))

# sub option for CALL REGISTER
		match call_register_options:
			case 1:
				ONE = """
		 MISSED CALLS
		
		   0. Back
				"""
				print(ONE)

			case 2:
				TWO = """
	       RECEIVED CALLS
		
		  0. Back
				"""
				print(TWO)

			case 3:
				THREE = """
	      DIALLED NUMBERS
		
		 0. Back
				"""
				print(THREE)

			case 4:
				FOUR = """
	  ERASE RECENT CALL LISTS
		
		 0. Back
				"""
				print(FOUR)

			case 5:
				FIVE = """
	    SHOW CALL DURATION

   1. Last call duration		2. All calls' duration
   3. Received calls' duration		4. Dialled calls' duration
   5. Clear timers			0. Back
				"""
				print(FIVE)
				call_register_option_5 = int(input('Enter option: '))

# Sub option for Call register (option 5)
				match call_register_option_5:
					case 1: 
						option_5_one = """
	    LAST CALL DURATION
		
		 0. Back
						"""
						print(option_5_one)

					case 2:
						option_5_two = """
	    ALL CALL'S DURATION

		  0. Back
						"""
						print(option_5_two)
	
					case 3:
						option_5_three = """
	  RECEIVED CALL'S DURATION

		  0. Back
						"""
						print(option_5_three)

					case 4:
						option_5_four = """
	  DAILLED CALL'S DURATION

		  0. Back
						"""
						print(option_5_four)

					case 5:
						option_5_five = """
	      CLEAR TIMERS

		0. Back
						"""
						print(option_5_five)
					

			case 6:
				SIX = """
	    SHOW CALL COST

   1. Last call cost	2. All calls' cost
   3. Clear counters	0. Back
				 """
				print(SIX)
				call_register_option_6 = int(input('Enter option: '))

# Sub option for Call register (option 5)
				match call_register_option_6:
					case 1:
						option_6_one = """
	    LAST CALL COST

	       0. Back
						"""
						print(option_6_one)

					case 2:
						option_6_two = """
	   ALL CALL'S COST

		0.Back
						"""
						print(option_6_two)

					case 3:
						option_6_three = """
	   CLEAR COUNTERS

	       0. Back	
						"""
						print(option_6_three)


			case 7:
				SEVEN = """
	     CALL COST SETTINGS

   1. Call cost limit	2. Show costs in
   0. Back
				"""
				print(SEVEN)
				call_register_option_7 = int(input('Enter option: '))

# Sub option for Call register (option 7)
				match call_register_option_7:
					case 1:
						option_7_one = """
	CALL COST LIMIT

	    0. Back
						"""
						print(option_7_one)

					case 2:
						option_7_two = """
	SHOW COSTS IN

	    0. Back
						"""
						print(option_7_two)

			case 8:
				EIGHT = """
       PREPAID CREDIT
		
	  0. Back
				"""
				print(EIGHT)


# Fifth option from list of Menu functions

	case 5:
		fifth = """
		        TONES

   1. Ringing tone			2. Ringing volume
   3. Incoming call alert		4. Composer
   5. Message alert tone		6. Keypad tones
   7. Warning and game tones		8. Vibrating alert
   9. Screen saver			0. Back

		"""
		print(fifth)
		Tones_options = int(input('Enter option: '))

# Sub option for Tones
		match Tones_options:
			case 1:
				one_1 = """
	RINGING TONE
		
	   0. Back
				"""
				print(one_1)

			case 2:
				two_2 = """
	RINGING VOLUME
		
	   0. Back
				"""
				print(two_2)

			case 3:
				three_3 = """
      INCOMING CALL ALERT
		
	    0. Back
				"""
				print(three_3)

			case 4:
				four_4 = """
	  COMPOSER
		
	  0. Back
				"""
				print(four_4)

			case 5:
				five_5 = """
      MESSAGE ALERT TONE
		
	  0. Back
				"""
				print(five_5)

			case 6:
				six_6 = """
        KEYPAD TONES
		
	  0. Back
				"""
				print(six_6)


			case 7:
				seven_7 = """
    WARNING AND GAME TONES
		
          0. Back
				"""
				print(seven_7)

			case 8:
				eight_8 = """
       VIBRATING ALERT
		
	  0. Back
				"""
				print(eight_8)

			case 9:
				nine_9 = """
	SCREEN SAVER
		
	   0. Back
				"""
				print(nine_9)


# Sixth option from list of Menu functions

	case 6:
		sixth = """
		     SETTINGS

   1. Call settings		2. Phone settings
   3. Security settings		4. Restore factory setting
   0. Back
		"""
		print(sixth)
		settings_options = int(input('Enter option: '))

# Sub option for Settings

		match settings_options:
			case 1: 
				setting_1 = """
	CALL SETTINGS

   1. Automatic redial		2. Speed dialling
   3. Call waiting option	4. Own number sending
   5. Phone line in use		6. Automatic answer
   0. Back
				"""
				print(setting_1)
				setting_1_one = int(input('Enter option: '))

# Sub option for Settings (option 1)
				match setting_1_one:
					case 1:
						option_6_1 = """
    AUTOMATIC REDIAL

	0. Back
						"""
						print(option_6_1)
					
					case 2:
						option_6_2 = """
    SPEED DIALLING

	0. Back
						"""
						print(option_6_2)
						
					case 3:
						option_6_3 = """
    CALL WAITING OPTION

	 0. Back
						"""
						print(option_6_3)

					case 4:
						option_6_4 = """
    OWN NUMBER SENDING

	0. Back
						"""
						print(option_6_4)

					case 5:
						option_6_5 = """
   PHONE LINE IN USE

	0. Back
						"""
						print(option_6_5)

					case 6:
						option_6_6 = """
    AUTOMATIC ANSWER

	0. Back
						"""
						print(option_6_6)

			case 2:
				setting_2 = """
	     PHONE SETTINGS

   1. Language		2. Cell info display
   3. Welcome note	4. Network selection
   5. Lights		6. Confirm SIM service actions
   0. Back
				"""
				print(setting_2)
				setting_2_two = int(input('Enter option: '))

# Sub option for Settings (option 2)
				match setting_2_two:
					case 1:
						option_6_I = """
   	LANGUAGE

	0. Back
						"""
						print(option_6_I)
					
					case 2:
						option_6_II = """
   CELL INFO DISPLAY

	0. Back
						"""
						print(option_6_II)
						
					case 3:
						option_6_III = """
   	WELCOME NOTE

	 0. Back
						"""
						print(option_6_III)

					case 4:
						option_6_IV = """
    NETWORK SELECTION

	0. Back
						"""
						print(option_6_IV)

					case 5:
						option_6_V = """
   	LIGHT

	0. Back
						"""
						print(option_6_V)

					case 6:
						option_6_VI = """
    CONFIRM SIM SERVICE ACTIONS

	0. Back
						"""
						print(option_6_VI)


			case 3:
				setting_3 = """
	    SECURITY SETTINGS

   1. PIN code request	2. Call barring service
   3. Fixed dialling	4. Closed user group
   5. Phone security	6. Change access codes
   0. Back
				"""
				print(setting_3)
				setting_3_three = int(input('Enter option: '))

# Sub option for Settings (option 3)
				match setting_3_three:
					case 1:
						option_6_3a = """
    PIN CODE REQUEST

	0. Back
						"""
						print(option_6_3a)
					
					case 2:
						option_6_3b = """
   CALL BARRING SERVICE

	0. Back
						"""
						print(option_6_3b)
						
					case 3:
						option_6_3c = """
     FIXED DIALLING

	0. Back
						"""
						print(option_6_3c)

					case 4:
						option_6_3d = """
   CLOSED USER GROUP

	0. Back
						"""
						print(option_6_3d)

					case 5:
						option_6_3e = """
     PHONE SECURITY

	0. Back
						"""
						print(option_6_3e)

					case 6:
						option_6_3f = """
    CHANGE ACCESS CODE

	0. Back
						"""
						print(option_6_3f)

			case 4: 
				setting_4 = """

	RESTORE FACTORY SETTINGS

		0. Back
				"""
				print(setting_4)


# Seventh option from list of Menu functions

	case 7:
		seventh = """
       CALL DIVERT
		
        0. Back
		"""
		print(seventh)

# Eighth option from list of Menu functions
	case 8:
		eighth = """
         GAMES
		
	0. Back
		"""
		print(eighth)

# Nineth option from list of Menu functions

	case 9:
		nineth = """
       CALCULATOR
		
	0. Back
		"""
		print(nineth)

# Tenth option from list of Menu functions

	case 10:
		tenth = """
       REMINDERS
		
        0. Back
		"""
		print(tenth)




