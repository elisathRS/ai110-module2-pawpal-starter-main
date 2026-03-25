from datetime import datetime
from pawpal_system import Pet, Task, TaskStatus


def make_task(pet_id, hour=9):
    return Task(
        description="Test task",
        due_date_time=datetime.now().replace(hour=hour, minute=0, second=0, microsecond=0),
        pet_id=pet_id,
    )


def test_mark_complete_changes_status():
    pet = Pet(name="Mochi", species="dog", age=3, gender="female", weight=12.5, breed="Shiba Inu")
    task = make_task(pet.id)

    assert task.status == TaskStatus.PENDING
    task.mark_complete()
    assert task.status == TaskStatus.COMPLETED


def test_add_task_increases_pet_task_count():
    pet = Pet(name="Luna", species="cat", age=5, gender="female", weight=8.0, breed="Tabby")

    assert len(pet.list_tasks()) == 0
    pet.add_task(make_task(pet.id, hour=8))
    pet.add_task(make_task(pet.id, hour=10))
    assert len(pet.list_tasks()) == 2
