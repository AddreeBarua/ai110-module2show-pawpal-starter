# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

I designed four classes for PawPal+:

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
  

After Copilot reviewed pawpal_system.py I made 
two changes:

1. Added pet_name field to Task so each task 
   knows which pet it belongs to.

2. Changed filter_tasks(criteria) to 
   filter_tasks(pet_name=None, status=None) 
   to make filtering clearer.

I ignored suggestions like Enum and Dict/Set 
because they are too complex for this project.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
