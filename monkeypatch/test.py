from main import Calculator

def dummy_add(cal: Calculator, x: int, y: int) -> int:
    return x - y

def test_add_specific_val(monkeypatch):
    monkeypatch.setattr(Calculator, "add", dummy_add)

    cal = Calculator()
    result = cal.add(10, 10)
    print(result)

    assert result <= 10
