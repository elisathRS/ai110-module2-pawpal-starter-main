from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler

# --- Setup ---
owner = Owner(name="Jordan", phone_number="555-1234", email="jordan@example.com")

mochi = Pet(name="Mochi", species="dog", age=3, gender="female", weight=12.5, breed="Shiba Inu")
luna  = Pet(name="Luna",  species="cat", age=5, gender="female", weight=8.0,  breed="Tabby")

owner.add_pet(mochi)
owner.add_pet(luna)

# --- Tasks for Mochi ---
today = datetime.now().replace(second=0, microsecond=0)

mochi.add_task(Task(
    description="Morning walk",
    due_date_time=today.replace(hour=7, minute=0),
    pet_id=mochi.id,
    duration_minutes=30,
    priority=1,
))
mochi.add_task(Task(
    description="Flea & tick medication",
    due_date_time=today.replace(hour=8, minute=0),
    pet_id=mochi.id,
    duration_minutes=5,
    priority=2,
))

# --- Tasks for Luna ---
luna.add_task(Task(
    description="Clean litter box",
    due_date_time=today.replace(hour=7, minute=30),
    pet_id=luna.id,
    duration_minutes=10,
    priority=2,
))
luna.add_task(Task(
    description="Brush fur",
    due_date_time=today.replace(hour=9, minute=0),
    pet_id=luna.id,
    duration_minutes=15,
    priority=3,
))
luna.add_task(Task(
    description="Vet check-up",
    due_date_time=today.replace(hour=10, minute=0),
    pet_id=luna.id,
    duration_minutes=60,
    priority=1,
))

# --- Generate schedule ---
scheduler = Scheduler()
plan = scheduler.generate_daily_plan(owner)

# --- Print today's schedule ---
pet_lookup = {pet.id: pet.name for pet in owner.list_pets()}

priority_label = {1: "High", 2: "Medium", 3: "Low"}

print("=" * 44)
print("       TODAY'S SCHEDULE — PawPal+")
print("=" * 44)
print(f"  Owner : {owner.name}")
print(f"  Date  : {today.strftime('%A, %B %d %Y')}")
print(f"  Pets  : {', '.join(pet_lookup.values())}")
print("-" * 44)

for task in plan:
    from datetime import timedelta
    end_time = task.due_date_time + timedelta(minutes=task.duration_minutes)
    print(
        f"  {task.due_date_time.strftime('%I:%M %p')} – {end_time.strftime('%I:%M %p')}"
        f"  [{priority_label[task.priority]:6}]"
        f"  {pet_lookup[task.pet_id]}: {task.description}"
    )

print("=" * 44)
print(f"  {len(plan)} task(s) scheduled.")
print("=" * 44)
