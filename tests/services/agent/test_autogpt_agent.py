
from bespokebots.services.agent.autogpt_assistant import build_agent

"""I need to add a few upcoming appointments at SeaCoast Hand Therapy to my calendar.  
I have each event listed below:
- Thursday, June 1st at 1:00 PM 1 hour appointment with Dr. Hayner
- Thursday, June 15th at 9:00 AM 1 hour appointment with Dr. Hayner
- Thursday, June 22th at 9:45 AM 1 hour appointment with Dr. Hayner

For each event, set the following fields to the corresponding values:
- Summary: SeaCoast Hand Therapy    
- Location: 308 US-1, Scarborough, ME 04074
- Description: Appointment with Dr. Hayner at SeaCoast Hand Therapy

Create the events one at a time.

"""

"""Hi Tom, can you help me out with my calendar? 
I need to pick my kids up between 5 and 5:30 PM every weekday they are with me during their next visit.
Can you add events to my calendar to remind me to pick them up at 5 PM on just the weekdays?

"""

"""You did a great job with that last request, Tom, however I noticed that all the events you created
were created with the UTC timezone, but should have been created in the America/New_York timezone.  Can you
update the events you created to have the correct timezone? Right now they all appear at 1pm on my calendar, rather than 5pm.
"""

message="""Hi Tom, you helped me create some events on my calendar to help me remeber when to pick my kids up from school.
Each of the events has a summary or title of 'Pick up kids'.  Unfortunately, each of the events was created for 1pm eastern time, rather than
5pm like I had asked.  Can you update each of these 'Pick up kids' events to be at 5pm instead of 1pm? 
Don't forget to use the America/New_York timezone.
"""




def test_ask_about_my_schedule(): 
    agent = build_agent()
    response = agent.run([message])
    print(response)
    assert response is not None