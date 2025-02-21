###########################################################
# Dimension of the surfaces
# The clip session matrix definition must be matrix MATRIX_DEPTH * TRACK_NUMBER
# All other vectors referring to tracks must be TRACK_NUMBER long.
MATRIX_DEPTH = 8 #number of scenes in the box
TRACK_NUMBER = 8 #number of tracks for Mixer mapping
NUMBER_BUTTONS = 40 #number of buttons in BUTTON_VECTOR
NUMBER_SLIDERS = 4 #number of sliders in SLIDER_VECTOR
BANKS_NUMBER = 8 #number of parameter banks
PARAMS_NUMBER = 8 #number of parameters per bank
PAD_X_NUMBER = 4 #number of pad columns
PAD_Y_NUMBER = 4 #number of pad rows

###########################################################
# Combination Mode offsets for more identical surfaces
TRACK_OFFSET = -1 #offset from the left of linked session origin; set to -1 for auto-joining of multiple instances
SCENE_OFFSET = 0 #offset from the top of linked session origin (no auto-join)

###########################################################
# Tempo Range
TEMPO_TOP = 180.0 # Upper limit of tempo control in BPM (max is 999)
TEMPO_BOTTOM = 60.0 # Lower limit of tempo control in BPM (min is 0)

###########################################################
# Individual Scene Buttons 
# Note: must be at least MATRIX_DEPTH long
# Type 0 == MIDI notes, Type 1 == MIDI CC
# CH must be in the range 0 to 15 (corresponding to MIDI channels 1 to 16)

SCENELAUNCH = (-1, #Scene 1
               -1, #Scene 2
               -1, #Scene 3
               -1, #Scene 4
               -1, #Scene 5
               -1, #Scene 6
               -1, #Scene 7
               -1, #Scene 8
               -1, #Scene 9
               -1, #Scene 10
               )

SCENELAUNCH_TYPE = (0, #Scene 1
               0, #Scene 2
               0, #Scene 3
               0, #Scene 4
               0, #Scene 5
               0, #Scene 6
               0, #Scene 7
               0, #Scene 8
               0, #Scene 9
               0, #Scene 10
               )

SCENELAUNCH_CH = (0, #Scene 1
               0, #Scene 2
               0, #Scene 3
               0, #Scene 4
               0, #Scene 5
               0, #Scene 6
               0, #Scene 7
               0, #Scene 8
               0, #Scene 9
               0, #Scene 10
               )

###########################################################
# Clip Matrix
# Note: must be at least have MATRIX_DEPTH * TRACK_NUMBER dimensions 

# Track no.:     1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32
CLIPNOTEMAP = ((-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1), # 1
               (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1), # 2
               (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1), # 3
               (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1), # 4
               (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1), # 5
               (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1), # 6
               (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1), # 7
               (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1), # 8
               (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1), # 9
               (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1), # 10
               )

CLIPNOTEMAP_TYPE = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 1
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 2
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 3
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 4
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 5
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 6
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 7
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 8
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 9
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 10
               )

CLIPNOTEMAP_CH = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 1
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 2
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 3
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 4
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 5
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 6
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 7
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 8
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 9
               (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 10
               )

###########################################################
# Single Buttons
BUTTON_VECTOR = (-1, #Global play 					[0]
                -1, #Global stop 					[1]
                -1, #Global record 					[2]
                -1, #Tap tempo 						[3]
                -1, #Tempo Nudge Up 				[4]
                -1, #Tempo Nudge Down 				[5]
                -1, #Undo 							[6]
                -1, #Redo 							[7]
                -1, #Loop 							[8]
                -1, #Punch in	 					[9]
                -1, #Punch out 						[10]
                -1, #Overdub on/off 				[11]
                -1, #Metronome on/off 				[12]
                -1, #Record quantization on/off 	[13]
                -1, #Detail view switch 			[14]
                -1, #Clip/Track view switch 		[15]
                -1, #Device Lock (lock "blue hand")	[16]
                63, #Device on/off 					[17]
                59, #Device nav left 				[18]
                60, #Device nav right 				[19]
                61, #Device bank nav left 			[20]
                62, #Device bank nav right 			[21]
                -1, #Seek forward 					[22]
                -1, #Seek rewind 					[23]
                -1, #Session left 					[24]
                -1, #Session right 					[25]
                -1, #Session up 					[26]
                -1, #Session down 					[27]
                -1, #Session Zoom up 				[28]
                -1, #Session Zoom down 				[29]
                -1, #Session Zoom left 				[30]
                -1, #Session Zoom right 			[31]
                61, #Track left 					[32]
                62, #Track right 					[33]
                60, #Scene down 					[34]
                59, #Scene up 						[35]
                63, #Selected scene launch 			[36]
                -1, #Selected clip launch 			[37]
                -1, #Stop all clips 				[38]
                -1, #Master track select			[39]
                )

BUTTON_VECTOR_TYPE = (0, #Global play 				[0] Type
                 0, #Global stop 					[1] Type
                 0, #Global record 					[2] Type
                 0, #Tap tempo 						[3] Type
                 0, #Tempo Nudge Up 				[4] Type
                 0, #Tempo Nudge Down 				[5] Type
                 0, #Undo 							[6] Type
                 0, #Redo 							[7] Type
                 0, #Loop 							[8] Type
                 0, #Punch in	 					[9] Type
                 0, #Punch out 						[10] Type
                 0, #Overdub on/off 				[11] Type
                 0, #Metronome on/off 				[12] Type
                 0, #Record quantization on/off 	[13] Type
                 0, #Detail view switch 			[14] Type
                 0, #Clip/Track view switch 		[15] Type
                 0, #Device Lock (lock "blue hand")	[16] Type
                 1, #Device on/off 					[17] Type
                 1, #Device nav left 				[18] Type
                 1, #Device nav right 				[19] Type
                 1, #Device bank nav left 			[20] Type
                 1, #Device bank nav right 			[21] Type
                 0, #Seek forward 					[22] Type
                 0, #Seek rewind 					[23] Type
                 0, #Session left 					[24] Type
                 0, #Session right 					[25] Type
                 0, #Session up 					[26] Type
                 0, #Session down 					[27] Type
                 0, #Session Zoom up 				[28] Type
                 0, #Session Zoom down 				[29] Type
                 0, #Session Zoom left 				[30] Type
                 0, #Session Zoom right 			[31] Type
                 1, #Track left 					[32] Type
                 1, #Track right 					[33] Type
                 1, #Scene down 					[34] Type
                 1, #Scene up 						[35] Type
                 1, #Selected scene launch 			[36] Type
                 0, #Selected clip launch 			[37] Type
                 0, #Stop all clips 				[38] Type
                 0, #Master track select			[39] Type
                )

BUTTON_VECTOR_CH = (0, #Global play 				[0] Channel
                 0, #Global stop 					[1] Channel
                 0, #Global record 					[2] Channel
                 0, #Tap tempo 						[3] Channel
                 0, #Tempo Nudge Up 				[4] Channel
                 0, #Tempo Nudge Down 				[5] Channel
                 0, #Undo 							[6] Channel
                 0, #Redo 							[7] Channel
                 0, #Loop 							[8] Channel
                 0, #Punch in	 					[9] Channel
                 0, #Punch out 						[10] Channel
                 0, #Overdub on/off 				[11] Channel
                 0, #Metronome on/off 				[12] Channel
                 0, #Record quantization on/off 	[13] Channel
                 0, #Detail view switch 			[14] Channel
                 0, #Clip/Track view switch 		[15] Channel
                 0, #Device Lock (lock "blue hand")	[16] Channel
                 1, #Device on/off 					[17] Channel
                 1, #Device nav left 				[18] Channel
                 1, #Device nav right 				[19] Channel
                 1, #Device bank nav left 			[20] Channel
                 1, #Device bank nav right 			[21] Channel
                 0, #Seek forward 					[22] Channel
                 0, #Seek rewind 					[23] Channel
                 0, #Session left 					[24] Channel
                 0, #Session right 					[25] Channel
                 0, #Session up 					[26] Channel
                 0, #Session down 					[27] Channel
                 0, #Session Zoom up 				[28] Channel
                 0, #Session Zoom down 				[29] Channel
                 0, #Session Zoom left 				[30] Channel
                 0, #Session Zoom right 			[31] Channel
                 0, #Track left 					[32] Channel
                 0, #Track right 					[33] Channel
                 0, #Scene down 					[34] Channel
                 0, #Scene up 						[35] Channel
                 0, #Selected scene launch 			[36] Channel
                 0, #Selected clip launch 			[37] Channel
                 0, #Stop all clips 				[38] Channel
                 0, #Master track select			[39] Channel
                )

###########################################################
# Single Sliders

SLIDER_VECTOR = (7, #Master track volume			[0]
                19, #Cue level control				[1]
                18, #Crossfader control				[2]
                -1, #Tempo control					[3]
                )

SLIDER_VECTOR_TYPE = (1, #Master track volume		[0] Type
                 1, #Cue level control				[1] Type
                 1, #Crossfader control				[2] Type
                 1, #Tempo control					[3] Type
                )

SLIDER_VECTOR_CH = (0, #Master track volume			[0] Channel
                 0, #Cue level control				[1] Channel
                 0, #Crossfader control				[2] Channel
                 0, #Tempo control					[3] Channel
                )

###########################################################
# Track Stop Buttons
# Note: Must be at least TRACK_NUMBER long
TRACKSTOP = (-1, #Track 1 Clip Stop
             -1, #Track 2
             -1, #Track 3
             -1, #Track 4
             -1, #Track 5
             -1, #Track 6
             -1, #Track 7
             -1, #Track 8
             -1, #Track 9
             -1, #Track 10
             -1, #Track 11
             -1, #Track 12
             -1, #Track 13
             -1, #Track 14
             -1, #Track 15
             -1, #Track 16
             -1, #Track 17
             -1, #Track 18
             -1, #Track 19
             -1, #Track 20
             -1, #Track 21
             -1, #Track 22
             -1, #Track 23
             -1, #Track 24
             -1, #Track 25
             -1, #Track 26
             -1, #Track 27
             -1, #Track 28
             -1, #Track 29
             -1, #Track 30
             -1, #Track 31
             -1, #Track 32
             )

TRACKSTOP_TYPE = (0, # Type for Track 1
             0, # Type for Track 2
             0, # Type for Track 3
             0, # Type for Track 4
             0, # Type for Track 5
             0, # Type for Track 6
             0, # Type for Track 7
             0, # Type for Track 8
             0, # Type for Track 9
             0, # Type for Track 10
             0, # Type for Track 11
             0, # Type for Track 12
             0, # Type for Track 13
             0, # Type for Track 14
             0, # Type for Track 15
             0, # Type for Track 16
             0, # Type for Track 17
             0, # Type for Track 18
             0, # Type for Track 19
             0, # Type for Track 20
             0, # Type for Track 21
             0, # Type for Track 22
             0, # Type for Track 23
             0, # Type for Track 24
             0, # Type for Track 25
             0, # Type for Track 26
             0, # Type for Track 27
             0, # Type for Track 28
             0, # Type for Track 29
             0, # Type for Track 30
             0, # Type for Track 31
             0, # Type for Track 32
             )

TRACKSTOP_CH = (0, # Channel for Track 1
             0, # Channel for Track 2
             0, # Channel for Track 3
             0, # Channel for Track 4
             0, # Channel for Track 5
             0, # Channel for Track 6
             0, # Channel for Track 7
             0, # Channel for Track 8
             0, # Channel for Track 9
             0, # Channel for Track 10
             0, # Channel for Track 11
             0, # Channel for Track 12
             0, # Channel for Track 13
             0, # Channel for Track 14
             0, # Channel for Track 15
             0, # Channel for Track 16
             0, # Channel for Track 17
             0, # Channel for Track 18
             0, # Channel for Track 19
             0, # Channel for Track 20
             0, # Channel for Track 21
             0, # Channel for Track 22
             0, # Channel for Track 23
             0, # Channel for Track 24
             0, # Channel for Track 25
             0, # Channel for Track 26
             0, # Channel for Track 27
             0, # Channel for Track 28
             0, # Channel for Track 29
             0, # Channel for Track 30
             0, # Channel for Track 31
             0, # Channel for Track 32
             )

###########################################################
# Track Select Buttons
# Note: Must be at least TRACK_NUMBER long
TRACKSEL = (-1, #Track 1 Select
            -1, #Track 2
            -1, #Track 3
            -1, #Track 4
            -1, #Track 5
            -1, #Track 6
            -1, #Track 7
            -1, #Track 8
            -1, #Track 9
            -1, #Track 10
            -1, #Track 11
            -1, #Track 12
            -1, #Track 13
            -1, #Track 14
            -1, #Track 15
            -1, #Track 16
            -1, #Track 17
            -1, #Track 18
            -1, #Track 19
            -1, #Track 20
            -1, #Track 21
            -1, #Track 22
            -1, #Track 23
            -1, #Track 24
            -1, #Track 25
            -1, #Track 26
            -1, #Track 27
            -1, #Track 28
            -1, #Track 29
            -1, #Track 30
            -1, #Track 31
            -1, #Track 32
			 )

TRACKSEL_TYPE = (0, # Type for Track 1
             0, # Type for Track 2
             0, # Type for Track 3
             0, # Type for Track 4
             0, # Type for Track 5
             0, # Type for Track 6
             0, # Type for Track 7
             0, # Type for Track 8
             0, # Type for Track 9
             0, # Type for Track 10
             0, # Type for Track 11
             0, # Type for Track 12
             0, # Type for Track 13
             0, # Type for Track 14
             0, # Type for Track 15
             0, # Type for Track 16
             0, # Type for Track 17
             0, # Type for Track 18
             0, # Type for Track 19
             0, # Type for Track 20
             0, # Type for Track 21
             0, # Type for Track 22
             0, # Type for Track 23
             0, # Type for Track 24
             0, # Type for Track 25
             0, # Type for Track 26
             0, # Type for Track 27
             0, # Type for Track 28
             0, # Type for Track 29
             0, # Type for Track 30
             0, # Type for Track 31
             0, # Type for Track 32
             )

TRACKSEL_CH = (0, # Channel for Track 1
             0, # Channel for Track 2
             0, # Channel for Track 3
             0, # Channel for Track 4
             0, # Channel for Track 5
             0, # Channel for Track 6
             0, # Channel for Track 7
             0, # Channel for Track 8
             0, # Channel for Track 9
             0, # Channel for Track 10
             0, # Channel for Track 11
             0, # Channel for Track 12
             0, # Channel for Track 13
             0, # Channel for Track 14
             0, # Channel for Track 15
             0, # Channel for Track 16
             0, # Channel for Track 17
             0, # Channel for Track 18
             0, # Channel for Track 19
             0, # Channel for Track 20
             0, # Channel for Track 21
             0, # Channel for Track 22
             0, # Channel for Track 23
             0, # Channel for Track 24
             0, # Channel for Track 25
             0, # Channel for Track 26
             0, # Channel for Track 27
             0, # Channel for Track 28
             0, # Channel for Track 29
             0, # Channel for Track 30
             0, # Channel for Track 31
             0, # Channel for Track 32
             )

###########################################################
# Track Mute Buttons
# Note: Must be at least TRACK_NUMBER long
TRACKMUTE = (-1, #Track 1 On/Off
             -1, #Track 2
             -1, #Track 3
             -1, #Track 4
             -1, #Track 5
             -1, #Track 6
             -1, #Track 7
             -1, #Track 8
             -1, #Track 9
             -1, #Track 10
             -1, #Track 11
             -1, #Track 12
             -1, #Track 13
             -1, #Track 14
             -1, #Track 15
             -1, #Track 16
             -1, #Track 17
             -1, #Track 18
             -1, #Track 19
             -1, #Track 20
             -1, #Track 21
             -1, #Track 22
             -1, #Track 23
             -1, #Track 24
             -1, #Track 25
             -1, #Track 26
             -1, #Track 27
             -1, #Track 28
             -1, #Track 29
             -1, #Track 30
             -1, #Track 31
             -1, #Track 32
             )

TRACKMUTE_TYPE = (0, # Type for Track 1
             0, # Type for Track 2
             0, # Type for Track 3
             0, # Type for Track 4
             0, # Type for Track 5
             0, # Type for Track 6
             0, # Type for Track 7
             0, # Type for Track 8
             0, # Type for Track 9
             0, # Type for Track 10
             0, # Type for Track 11
             0, # Type for Track 12
             0, # Type for Track 13
             0, # Type for Track 14
             0, # Type for Track 15
             0, # Type for Track 16
             0, # Type for Track 17
             0, # Type for Track 18
             0, # Type for Track 19
             0, # Type for Track 20
             0, # Type for Track 21
             0, # Type for Track 22
             0, # Type for Track 23
             0, # Type for Track 24
             0, # Type for Track 25
             0, # Type for Track 26
             0, # Type for Track 27
             0, # Type for Track 28
             0, # Type for Track 29
             0, # Type for Track 30
             0, # Type for Track 31
             0, # Type for Track 32
             )

TRACKMUTE_CH = (0, # Channel for Track 1
             0, # Channel for Track 2
             0, # Channel for Track 3
             0, # Channel for Track 4
             0, # Channel for Track 5
             0, # Channel for Track 6
             0, # Channel for Track 7
             0, # Channel for Track 8
             0, # Channel for Track 9
             0, # Channel for Track 10
             0, # Channel for Track 11
             0, # Channel for Track 12
             0, # Channel for Track 13
             0, # Channel for Track 14
             0, # Channel for Track 15
             0, # Channel for Track 16
             0, # Channel for Track 17
             0, # Channel for Track 18
             0, # Channel for Track 19
             0, # Channel for Track 20
             0, # Channel for Track 21
             0, # Channel for Track 22
             0, # Channel for Track 23
             0, # Channel for Track 24
             0, # Channel for Track 25
             0, # Channel for Track 26
             0, # Channel for Track 27
             0, # Channel for Track 28
             0, # Channel for Track 29
             0, # Channel for Track 30
             0, # Channel for Track 31
             0, # Channel for Track 32
             )

###########################################################
# Track Solo Buttons
# Note: Must be at least TRACK_NUMBER long
TRACKSOLO = (-1, #Track 1 Solo
             -1, #Track 2
             -1, #Track 3
             -1, #Track 4
             -1, #Track 5
             -1, #Track 6
             -1, #Track 7
             -1, #Track 8
             -1, #Track 9
             -1, #Track 10
             -1, #Track 11
             -1, #Track 12
             -1, #Track 13
             -1, #Track 14
             -1, #Track 15
             -1, #Track 16
             -1, #Track 17
             -1, #Track 18
             -1, #Track 19
             -1, #Track 20
             -1, #Track 21
             -1, #Track 22
             -1, #Track 23
             -1, #Track 24
             -1, #Track 25
             -1, #Track 26
             -1, #Track 27
             -1, #Track 28
             -1, #Track 29
             -1, #Track 30
             -1, #Track 31
             -1, #Track 32
             )

TRACKSOLO_TYPE = (0, # Type for Track 1
             0, # Type for Track 2
             0, # Type for Track 3
             0, # Type for Track 4
             0, # Type for Track 5
             0, # Type for Track 6
             0, # Type for Track 7
             0, # Type for Track 8
             0, # Type for Track 9
             0, # Type for Track 10
             0, # Type for Track 11
             0, # Type for Track 12
             0, # Type for Track 13
             0, # Type for Track 14
             0, # Type for Track 15
             0, # Type for Track 16
             0, # Type for Track 17
             0, # Type for Track 18
             0, # Type for Track 19
             0, # Type for Track 20
             0, # Type for Track 21
             0, # Type for Track 22
             0, # Type for Track 23
             0, # Type for Track 24
             0, # Type for Track 25
             0, # Type for Track 26
             0, # Type for Track 27
             0, # Type for Track 28
             0, # Type for Track 29
             0, # Type for Track 30
             0, # Type for Track 31
             0, # Type for Track 32
             )

TRACKSOLO_CH = (0, # Channel for Track 1
             0, # Channel for Track 2
             0, # Channel for Track 3
             0, # Channel for Track 4
             0, # Channel for Track 5
             0, # Channel for Track 6
             0, # Channel for Track 7
             0, # Channel for Track 8
             0, # Channel for Track 9
             0, # Channel for Track 10
             0, # Channel for Track 11
             0, # Channel for Track 12
             0, # Channel for Track 13
             0, # Channel for Track 14
             0, # Channel for Track 15
             0, # Channel for Track 16
             0, # Channel for Track 17
             0, # Channel for Track 18
             0, # Channel for Track 19
             0, # Channel for Track 20
             0, # Channel for Track 21
             0, # Channel for Track 22
             0, # Channel for Track 23
             0, # Channel for Track 24
             0, # Channel for Track 25
             0, # Channel for Track 26
             0, # Channel for Track 27
             0, # Channel for Track 28
             0, # Channel for Track 29
             0, # Channel for Track 30
             0, # Channel for Track 31
             0, # Channel for Track 32
             )

###########################################################
# Track Record/Arm Buttons
# Note: Must be at least TRACK_NUMBER long
TRACKREC = (-1, #Track 1 Record
            -1, #Track 2
            -1, #Track 3
            -1, #Track 4
            -1, #Track 5
            -1, #Track 6
            -1, #Track 7
            -1, #Track 8
            -1, #Track 9
            -1, #Track 10
            -1, #Track 11
            -1, #Track 12
            -1, #Track 13
            -1, #Track 14
            -1, #Track 15
            -1, #Track 16
            -1, #Track 17
            -1, #Track 18
            -1, #Track 19
            -1, #Track 20
            -1, #Track 21
            -1, #Track 22
            -1, #Track 23
            -1, #Track 24
            -1, #Track 25
            -1, #Track 26
            -1, #Track 27
            -1, #Track 28
            -1, #Track 29
            -1, #Track 30
            -1, #Track 31
            -1, #Track 32
            )

TRACKREC_TYPE = (0, # Type for Track 1
             0, # Type for Track 2
             0, # Type for Track 3
             0, # Type for Track 4
             0, # Type for Track 5
             0, # Type for Track 6
             0, # Type for Track 7
             0, # Type for Track 8
             0, # Type for Track 9
             0, # Type for Track 10
             0, # Type for Track 11
             0, # Type for Track 12
             0, # Type for Track 13
             0, # Type for Track 14
             0, # Type for Track 15
             0, # Type for Track 16
             0, # Type for Track 17
             0, # Type for Track 18
             0, # Type for Track 19
             0, # Type for Track 20
             0, # Type for Track 21
             0, # Type for Track 22
             0, # Type for Track 23
             0, # Type for Track 24
             0, # Type for Track 25
             0, # Type for Track 26
             0, # Type for Track 27
             0, # Type for Track 28
             0, # Type for Track 29
             0, # Type for Track 30
             0, # Type for Track 31
             0, # Type for Track 32
             )

TRACKREC_CH = (0, # Channel for Track 1
             0, # Channel for Track 2
             0, # Channel for Track 3
             0, # Channel for Track 4
             0, # Channel for Track 5
             0, # Channel for Track 6
             0, # Channel for Track 7
             0, # Channel for Track 8
             0, # Channel for Track 9
             0, # Channel for Track 10
             0, # Channel for Track 11
             0, # Channel for Track 12
             0, # Channel for Track 13
             0, # Channel for Track 14
             0, # Channel for Track 15
             0, # Channel for Track 16
             0, # Channel for Track 17
             0, # Channel for Track 18
             0, # Channel for Track 19
             0, # Channel for Track 20
             0, # Channel for Track 21
             0, # Channel for Track 22
             0, # Channel for Track 23
             0, # Channel for Track 24
             0, # Channel for Track 25
             0, # Channel for Track 26
             0, # Channel for Track 27
             0, # Channel for Track 28
             0, # Channel for Track 29
             0, # Channel for Track 30
             0, # Channel for Track 31
             0, # Channel for Track 32
             )

###########################################################
# Track Volume Sliders
# Note: Must be at least TRACK_NUMBER long
TRACKVOL = (5, #Track 1 Volume
            84, #Track 2
            74, #Track 3
            71, #Track 4
            73, #Track 5
            72, #Track 6
            93, #Track 7
            91, #Track 8
            7, #Track 9
            -1, #Track 10
            -1, #Track 11
            -1, #Track 12
            -1, #Track 13
            -1, #Track 14
            -1, #Track 15
            -1, #Track 16
            -1, #Track 17
            -1, #Track 18
            -1, #Track 19
            -1, #Track 20
            -1, #Track 21
            -1, #Track 22
            -1, #Track 23
            -1, #Track 24
            -1, #Track 25
            -1, #Track 26
            -1, #Track 27
            -1, #Track 28
            -1, #Track 29
            -1, #Track 30
            -1, #Track 31
            -1, #Track 32
            )

TRACKVOL_TYPE = (1, # Type for Track 1
             1, # Type for Track 2
             1, # Type for Track 3
             1, # Type for Track 4
             1, # Type for Track 5
             1, # Type for Track 6
             1, # Type for Track 7
             1, # Type for Track 8
             1, # Type for Track 9
             1, # Type for Track 10
             1, # Type for Track 11
             1, # Type for Track 12
             1, # Type for Track 13
             1, # Type for Track 14
             1, # Type for Track 15
             1, # Type for Track 16
             1, # Type for Track 17
             1, # Type for Track 18
             1, # Type for Track 19
             1, # Type for Track 20
             1, # Type for Track 21
             1, # Type for Track 22
             1, # Type for Track 23
             1, # Type for Track 24
             1, # Type for Track 25
             1, # Type for Track 26
             1, # Type for Track 27
             1, # Type for Track 28
             1, # Type for Track 29
             1, # Type for Track 30
             1, # Type for Track 31
             1, # Type for Track 32
             )

TRACKVOL_CH = (1, # Channel for Track 1
             1, # Channel for Track 2
             1, # Channel for Track 3
             1, # Channel for Track 4
             1, # Channel for Track 5
             1, # Channel for Track 6
             1, # Channel for Track 7
             1, # Channel for Track 8
             1, # Channel for Track 9
             1, # Channel for Track 10
             1, # Channel for Track 11
             1, # Channel for Track 12
             1, # Channel for Track 13
             1, # Channel for Track 14
             1, # Channel for Track 15
             1, # Channel for Track 16
             1, # Channel for Track 17
             1, # Channel for Track 18
             1, # Channel for Track 19
             1, # Channel for Track 20
             1, # Channel for Track 21
             1, # Channel for Track 22
             1, # Channel for Track 23
             1, # Channel for Track 24
             1, # Channel for Track 25
             1, # Channel for Track 26
             1, # Channel for Track 27
             1, # Channel for Track 28
             1, # Channel for Track 29
             1, # Channel for Track 30
             1, # Channel for Track 31
             1, # Channel for Track 32
             )

###########################################################
# Track Pan Sliders
# Note: Must be at least TRACK_NUMBER long
TRACKPAN = (5, #Track 1 Pan
            84, #Track 2
            74, #Track 3
            71, #Track 4
            73, #Track 5
            72, #Track 6
            93, #Track 7
            91, #Track 8
            7, #Track 9
            -1, #Track 10
            -1, #Track 11
            -1, #Track 12
            -1, #Track 13
            -1, #Track 14
            -1, #Track 15
            -1, #Track 16
            -1, #Track 17
            -1, #Track 18
            -1, #Track 19
            -1, #Track 20
            -1, #Track 21
            -1, #Track 22
            -1, #Track 23
            -1, #Track 24
            -1, #Track 25
            -1, #Track 26
            -1, #Track 27
            -1, #Track 28
            -1, #Track 29
            -1, #Track 30
            -1, #Track 31
            -1, #Track 32
            )

TRACKPAN_TYPE = (1, # Type for Track 1
             1, # Type for Track 2
             1, # Type for Track 3
             1, # Type for Track 4
             1, # Type for Track 5
             1, # Type for Track 6
             1, # Type for Track 7
             1, # Type for Track 8
             1, # Type for Track 9
             1, # Type for Track 10
             1, # Type for Track 11
             1, # Type for Track 12
             1, # Type for Track 13
             1, # Type for Track 14
             1, # Type for Track 15
             1, # Type for Track 16
             1, # Type for Track 17
             1, # Type for Track 18
             1, # Type for Track 19
             1, # Type for Track 20
             1, # Type for Track 21
             1, # Type for Track 22
             1, # Type for Track 23
             1, # Type for Track 24
             1, # Type for Track 25
             1, # Type for Track 26
             1, # Type for Track 27
             1, # Type for Track 28
             1, # Type for Track 29
             1, # Type for Track 30
             1, # Type for Track 31
             1, # Type for Track 32
             )

TRACKPAN_CH = (2, # Channel for Track 1
             2, # Channel for Track 2
             2, # Channel for Track 3
             2, # Channel for Track 4
             2, # Channel for Track 5
             2, # Channel for Track 6
             2, # Channel for Track 7
             2, # Channel for Track 8
             2, # Channel for Track 9
             2, # Channel for Track 10
             2, # Channel for Track 11
             2, # Channel for Track 12
             2, # Channel for Track 13
             2, # Channel for Track 14
             2, # Channel for Track 15
             2, # Channel for Track 16
             2, # Channel for Track 17
             2, # Channel for Track 18
             2, # Channel for Track 19
             2, # Channel for Track 20
             2, # Channel for Track 21
             2, # Channel for Track 22
             2, # Channel for Track 23
             2, # Channel for Track 24
             2, # Channel for Track 25
             2, # Channel for Track 26
             2, # Channel for Track 27
             2, # Channel for Track 28
             2, # Channel for Track 29
             2, # Channel for Track 30
             2, # Channel for Track 31
             2, # Channel for Track 32
             )

###########################################################
# Track Send A Sliders
# Note: Must be at least TRACK_NUMBER long
TRACKSENDA = (5, #Track 1 Send A
              84, #Track 2
              74, #Track 3
              71, #Track 4
              73, #Track 5
              72, #Track 6
              93, #Track 7
              91, #Track 8
              7, #Track 9
              -1, #Track 10
              -1, #Track 11
              -1, #Track 12
              -1, #Track 13
              -1, #Track 14
              -1, #Track 15
              -1, #Track 16
              -1, #Track 17
              -1, #Track 18
              -1, #Track 19
              -1, #Track 20
              -1, #Track 21
              -1, #Track 22
              -1, #Track 23
              -1, #Track 24
              -1, #Track 25
              -1, #Track 26
              -1, #Track 27
              -1, #Track 28
              -1, #Track 29
              -1, #Track 30
              -1, #Track 31
              -1, #Track 32
              )

TRACKSENDA_TYPE = (1, # Type for Track 1
             1, # Type for Track 2
             1, # Type for Track 3
             1, # Type for Track 4
             1, # Type for Track 5
             1, # Type for Track 6
             1, # Type for Track 7
             1, # Type for Track 8
             1, # Type for Track 9
             1, # Type for Track 10
             1, # Type for Track 11
             1, # Type for Track 12
             1, # Type for Track 13
             1, # Type for Track 14
             1, # Type for Track 15
             1, # Type for Track 16
             1, # Type for Track 17
             1, # Type for Track 18
             1, # Type for Track 19
             1, # Type for Track 20
             1, # Type for Track 21
             1, # Type for Track 22
             1, # Type for Track 23
             1, # Type for Track 24
             1, # Type for Track 25
             1, # Type for Track 26
             1, # Type for Track 27
             1, # Type for Track 28
             1, # Type for Track 29
             1, # Type for Track 30
             1, # Type for Track 31
             1, # Type for Track 32
             )

TRACKSENDA_CH = (3, # Channel for Track 1
             3, # Channel for Track 2
             3, # Channel for Track 3
             3, # Channel for Track 4
             3, # Channel for Track 5
             3, # Channel for Track 6
             3, # Channel for Track 7
             3, # Channel for Track 8
             3, # Channel for Track 9
             3, # Channel for Track 10
             3, # Channel for Track 11
             3, # Channel for Track 12
             3, # Channel for Track 13
             3, # Channel for Track 14
             3, # Channel for Track 15
             3, # Channel for Track 16
             3, # Channel for Track 17
             3, # Channel for Track 18
             3, # Channel for Track 19
             3, # Channel for Track 20
             3, # Channel for Track 21
             3, # Channel for Track 22
             3, # Channel for Track 23
             3, # Channel for Track 24
             3, # Channel for Track 25
             3, # Channel for Track 26
             3, # Channel for Track 27
             3, # Channel for Track 28
             3, # Channel for Track 29
             3, # Channel for Track 30
             3, # Channel for Track 31
             3, # Channel for Track 32
             )

###########################################################
# Track Send B Sliders
# Note: Must be at least TRACK_NUMBER long
TRACKSENDB = (5, #Track 1 Send B
              84, #Track 2
              74, #Track 3
              71, #Track 4
              73, #Track 5
              72, #Track 6
              93, #Track 7
              91, #Track 8
              7, #Track 9
              -1, #Track 10
              -1, #Track 11
              -1, #Track 12
              -1, #Track 13
              -1, #Track 14
              -1, #Track 15
              -1, #Track 16
              -1, #Track 17
              -1, #Track 18
              -1, #Track 19
              -1, #Track 20
              -1, #Track 21
              -1, #Track 22
              -1, #Track 23
              -1, #Track 24
              -1, #Track 25
              -1, #Track 26
              -1, #Track 27
              -1, #Track 28
              -1, #Track 29
              -1, #Track 30
              -1, #Track 31
              -1, #Track 32
              )

TRACKSENDB_TYPE = (1, # Type for Track 1
             1, # Type for Track 2
             1, # Type for Track 3
             1, # Type for Track 4
             1, # Type for Track 5
             1, # Type for Track 6
             1, # Type for Track 7
             1, # Type for Track 8
             1, # Type for Track 9
             1, # Type for Track 10
             1, # Type for Track 11
             1, # Type for Track 12
             1, # Type for Track 13
             1, # Type for Track 14
             1, # Type for Track 15
             1, # Type for Track 16
             1, # Type for Track 17
             1, # Type for Track 18
             1, # Type for Track 19
             1, # Type for Track 20
             1, # Type for Track 21
             1, # Type for Track 22
             1, # Type for Track 23
             1, # Type for Track 24
             1, # Type for Track 25
             1, # Type for Track 26
             1, # Type for Track 27
             1, # Type for Track 28
             1, # Type for Track 29
             1, # Type for Track 30
             1, # Type for Track 31
             1, # Type for Track 32
             )

TRACKSENDB_CH = (4, # Channel for Track 1
             4, # Channel for Track 2
             4, # Channel for Track 3
             4, # Channel for Track 4
             4, # Channel for Track 5
             4, # Channel for Track 6
             4, # Channel for Track 7
             4, # Channel for Track 8
             4, # Channel for Track 9
             4, # Channel for Track 10
             4, # Channel for Track 11
             4, # Channel for Track 12
             4, # Channel for Track 13
             4, # Channel for Track 14
             4, # Channel for Track 15
             4, # Channel for Track 16
             4, # Channel for Track 17
             4, # Channel for Track 18
             4, # Channel for Track 19
             4, # Channel for Track 20
             4, # Channel for Track 21
             4, # Channel for Track 22
             4, # Channel for Track 23
             4, # Channel for Track 24
             4, # Channel for Track 25
             4, # Channel for Track 26
             4, # Channel for Track 27
             4, # Channel for Track 28
             4, # Channel for Track 29
             4, # Channel for Track 30
             4, # Channel for Track 31
             4, # Channel for Track 32
             )

###########################################################
# Track Send C Sliders
# Note: Must be at least TRACK_NUMBER long
TRACKSENDC = (-1, #Track 1 Send C
              -1, #Track 2
              -1, #Track 3
              -1, #Track 4
              -1, #Track 5
              -1, #Track 6
              -1, #Track 7
              -1, #Track 8
              -1, #Track 9
              -1, #Track 10
              -1, #Track 11
              -1, #Track 12
              -1, #Track 13
              -1, #Track 14
              -1, #Track 15
              -1, #Track 16
              -1, #Track 17
              -1, #Track 18
              -1, #Track 19
              -1, #Track 20
              -1, #Track 21
              -1, #Track 22
              -1, #Track 23
              -1, #Track 24
              -1, #Track 25
              -1, #Track 26
              -1, #Track 27
              -1, #Track 28
              -1, #Track 29
              -1, #Track 30
              -1, #Track 31
              -1, #Track 32
              )

TRACKSENDC_TYPE = (1, # Type for Track 1
             1, # Type for Track 2
             1, # Type for Track 3
             1, # Type for Track 4
             1, # Type for Track 5
             1, # Type for Track 6
             1, # Type for Track 7
             1, # Type for Track 8
             1, # Type for Track 9
             1, # Type for Track 10
             1, # Type for Track 11
             1, # Type for Track 12
             1, # Type for Track 13
             1, # Type for Track 14
             1, # Type for Track 15
             1, # Type for Track 16
             1, # Type for Track 17
             1, # Type for Track 18
             1, # Type for Track 19
             1, # Type for Track 20
             1, # Type for Track 21
             1, # Type for Track 22
             1, # Type for Track 23
             1, # Type for Track 24
             1, # Type for Track 25
             1, # Type for Track 26
             1, # Type for Track 27
             1, # Type for Track 28
             1, # Type for Track 29
             1, # Type for Track 30
             1, # Type for Track 31
             1, # Type for Track 32
             )

TRACKSENDC_CH = (0, # Channel for Track 1
             0, # Channel for Track 2
             0, # Channel for Track 3
             0, # Channel for Track 4
             0, # Channel for Track 5
             0, # Channel for Track 6
             0, # Channel for Track 7
             0, # Channel for Track 8
             0, # Channel for Track 9
             0, # Channel for Track 10
             0, # Channel for Track 11
             0, # Channel for Track 12
             0, # Channel for Track 13
             0, # Channel for Track 14
             0, # Channel for Track 15
             0, # Channel for Track 16
             0, # Channel for Track 17
             0, # Channel for Track 18
             0, # Channel for Track 19
             0, # Channel for Track 20
             0, # Channel for Track 21
             0, # Channel for Track 22
             0, # Channel for Track 23
             0, # Channel for Track 24
             0, # Channel for Track 25
             0, # Channel for Track 26
             0, # Channel for Track 27
             0, # Channel for Track 28
             0, # Channel for Track 29
             0, # Channel for Track 30
             0, # Channel for Track 31
             0, # Channel for Track 32
             )

###########################################################
# Device Bank
# Note: All 8 banks must be assigned to positive values in order for bank selection to work
DEVICEBANK = (5, #Bank 1
              84, #Bank 2
              74, #Bank 3
              71, #Bank 4
              73, #Bank 5
              72, #Bank 6
              93, #Bank 7
              71, #Bank 8
              )

DEVICEBANK_TYPE = (1, #Bank 1
              1, #Bank 2
              1, #Bank 3
              1, #Bank 4
              1, #Bank 5
              1, #Bank 6
              1, #Bank 7
              1, #Bank 8
              )

DEVICEBANK_CH = (15, #Bank 1
              15, #Bank 2
              15, #Bank 3
              15, #Bank 4
              15, #Bank 5
              15, #Bank 6
              15, #Bank 7
              15, #Bank 8
              )

###########################################################
# Parameter Control Sliders
# Note: All 8 params must be assigned to positive values in order for param control to work
PARAMCONTROL = (5, #Param 1
                84, #Param 2
                74, #Param 3
                71, #Param 4
                73, #Param 5
                72, #Param 6
                93, #Param 7
                91, #Param 8
                )

PARAMCONTROL_TYPE = (1, #Param 1
                1, #Param 2
                1, #Param 3
                1, #Param 4
                1, #Param 5
                1, #Param 6
                1, #Param 7
                1, #Param 8
                )

PARAMCONTROL_CH = (0, #Param 1
                0, #Param 2
                0, #Param 3
                0, #Param 4
                0, #Param 5
                0, #Param 6
                0, #Param 7
                0, #Param 8
                )

###########################################################
# Pad Translations for Drum Rack
DRUM_PADS = (-1, -1, -1, -1, # MIDI note numbers for 4 x 4 Drum Rack
             -1, -1, -1, -1, # Mapping will be disabled if any notes are set to -1
             -1, -1, -1, -1, # Notes will be "swallowed" if already mapped elsewhere
             -1, -1, -1, -1,
             )

# Channel 0 to 15 for Drum Rack notes (MIDI channels 1 to 16)
PADCHANNEL = 15
