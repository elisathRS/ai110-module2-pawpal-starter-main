# PawPal+ Project Reflection

## 1. System Design

### a. Initial Design

- **Briefly describe your initial UML design:**  
  The design models a pet care system with four main classes: **Owner, Pet, Task, and Scheduler**. It organizes the relationships between owners, their pets, and tasks, while separating task management logic from the data.

- **What classes did you include, and what responsibilities did you assign to each?**  

  **Classes:**  
  - **Owner** – represents a pet owner.  
  - **Pet** – represents an individual pet.  
  - **Task** – represents a pet-related task.  
  - **Scheduler** – manages and organizes tasks across pets.  

  **Responsibilities:**  
  - **Owner:** Manage pets (add, list, remove).  
  - **Pet:** Store pet info and manage its tasks (add, list, remove).  
  - **Task:** Track task details and completion status (mark complete).  
  - **Scheduler:** Collect all tasks, organize them, generate daily plans, and resolve conflicts.  

**b. Design changes**

- Did your design change during implementation?
    Yes
- If yes, describe at least one change and why you made it.

    This update improves the code to make it safer and easier to use.
    
    ## 1. Renamed `type` → `species` in Pet
    - `type` is a built-in Python function.
    - Using it as an attribute can cause confusion and bugs.
    - `species` is clearer and avoids conflicts.
    
    ## 2. Added `TaskStatus` enum
    - Replaced `status: str` with `status: TaskStatus`.
    - Prevents errors from typos like "pendng" or "Pending".
    - Only valid values are allowed: `PENDING` and `COMPLETED`.
    
    ## 3. Added `id: UUID` to Task and Pet
    - Names are not always unique (e.g., two pets named "Bella").
    - UUID ensures each object is unique.
    - Makes removing or finding items accurate and reliable.
    
    ## 4. Added `pet_id: UUID` to Task
    - Keeps track of which pet a task belongs to.
    - Important when tasks are combined into one list.
    - Maintains the connection between task and pet.
    
    ## 5. Added `duration_minutes: int = 30` to Task
    - Helps calculate how long a task lasts.
    - Needed to detect time conflicts.
    - Default duration is 30 minutes.
    
    ## 6. Added `priority: int = 2` to Task
    - Allows tasks to be sorted by importance.
    - Priority levels:
      - `1 = High`
      - `2 = Medium` (default)
      - `3 = Low`
    - Improves task organization beyond just time.
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
