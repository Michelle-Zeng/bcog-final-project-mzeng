from src.exp import Exp

def test_add_task_stores_it():
    exp = Exp(None)
    exp.add_task("BCOG200 HW1", 3)
    assert exp.get_tasks() == {"HW1": 3}

def test_add_task_rejects_empty_name():
    exp = Exp(None)
    error = exp.add_task("", 1)
    assert error != ""


def test_schedule_splits_by_difficulty():
    exp = Exp(None)
    exp.add_task("Easy", 1)
    exp.add_task("Hard", 5)
    schedule = exp.run(120)
    easy = next(s for s in schedule if s["assignment"] == "Easy")
    hard = next(s for s in schedule if s["assignment"] == "Hard")
    assert hard["study_time"] > easy["study_time"]


if __name__ == "__main__":
    test_add_task_stores_it()
    test_add_task_rejects_empty_name()
    test_schedule_splits_by_difficulty()
    print("All tests passed!")
