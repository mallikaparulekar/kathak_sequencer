# kathak_sequencer
Generates sequence combinations for Kathak (dance) within time constraints of the rhythm and other user specified inputs.

This algorithm can be used by a Kathak dancer to create new tihais in a given taal. A tihai is a rhythmic pattern that repeats itself three times (like 1-2-3-4-5, 1-2-3-4-5, 1-2-3-4-5). It consists of three pallas (or sections) and two gaps in between.The user can specify what beat multiples the palla and gap should be. For example, multiples of 0.5 and 0.25 are typically easier to dance with than sections with multiples of 0.3. A taal is a cycle of beats-- which range from 3 beats to as long as 128 beats (although most are between 6 and 20 beats). A tihai can start on any beat of a cycle, but typically ends on sum (the first beat of the cycle).

With this simple algorithm the user can input the name of the taal, which beat they would like to start their tihai on, and what multiples they want their pallas and gaps to be in. There is also a boolean option to only return options where the palla is longer than the gap, which is usually the case in most tihais.
