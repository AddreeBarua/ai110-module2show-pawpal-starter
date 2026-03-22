# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

---I designed four classes for PawPal+:

- Task: Represents one care activity. Stores the name, 
  scheduled time, duration, priority, frequency, 
  and whether it is complete.

- Pet: Represents the pet. Stores name, species, age, 
  and holds a list of tasks.

- Owner: Represents the person using the app. Stores 
  their name and contact info and manages their pets.

- Scheduler: Acts as the brain. Pulls all tasks from 
  the owner's pets and handles sorting, filtering, 
  conflict detection, and recurring tasks..

**b. Design changes**
  

----After asking Copilot to review pawpal_system.py, 
I made two small changes:

1. Added pet_name field to Task so we know which 
   pet a task belongs to without searching through 
   all pets.

2. Changed filter_tasks(criteria) to 
   filter_tasks(pet_name=None, status=None) to make 
   it clearer what the method actually filters by.

I ignored suggestions to use Enum and Dict/Set 
because they add unnecessary complexity for a 
small app like PawPal+.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?


---My scheduler considers three constraints:
1. Time - tasks are sorted by scheduled_time
2. Priority - high priority tasks are flagged first
3. Completion status - completed tasks can be filtered out

I decided time mattered most because a pet owner 
needs to know what to do first in their day.owner 
needs to know what to do first in their day.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---My scheduler only checks for exact time matches 
when detecting conflicts, not overlapping durations.

For example if one task runs 08:00 to 08:30 and 
another starts at 08:15, no conflict is detected.

This is reasonable because it keeps the logic 
simple and fast. A pet owner with a small number 
of tasks does not need complex overlap detection



## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

---1. Design brainstorming - I asked Copilot to generate 
   a Mermaid.js UML diagram based on my four classes 
   and their attributes.

2. Code generation - I used Copilot to generate class 
   skeletons in pawpal_system.py and then fill in the 
   full working logic for all methods.

3. Code review - I asked Copilot to review my skeleton 
   using #file:pawpal_system.py to find missing 
   relationships or bottlenecks.

4. Test generation - I used Copilot to write two 
   pytest tests for mark_complete() and add_task().

5. UI integration - I used Copilot to connect 
   pawpal_system.py to app.py using st.session_state.

The most helpful prompts were specific ones that 
referenced the actual file using #file:pawpal_system.py 
and included clear rules like "use dataclasses" or 
"replace each pass with real working logic".

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---When Copilot reviewed my skeleton it suggested using 
Enum for priority and frequency fields, and using 
Dict/Set instead of Lists for better performance.

I rejected both suggestions because:
1. Enums add unnecessary complexity for a small app
2. Lists are easier to read and understand
3. Performance does not matter with a small number 
   of tasks like a pet owner would have

I verified my decision by asking myself "does this 
make the app better for the user?" and the answer 
was no. I kept the simpler solution and it worked 
perfectly in testing.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

---1. Task Completion - verified that mark_complete() 
   changes is_complete from False to True. This was 
   important because the whole scheduling system 
   depends on tracking whether tasks are done.

2. Task Addition - verified that add_task() increases 
   a pet's task count by 1. This was important because 
   if tasks don't get added correctly the scheduler 
   has no data to work with.


**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---
My scheduler only checks for exact time matches 
when detecting conflicts, not overlapping durations.

For example if one task runs 08:00 to 08:30 and 
another starts at 08:15, no conflict is detected.

This is reasonable because it keeps the logic 
simple and fast. A pet owner with a small number 
of tasks does not need complex overlap detection.

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
