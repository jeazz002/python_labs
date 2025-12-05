from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                f"birthdate must be in format YYYY-MM-DD, got {self.birthdate}"
            )

        if not (0 <= self.gpa <= 5):
            raise ValueError(f"gpa must be between 0 and 5, got {self.gpa}")

    def age(self) -> int:
        """вернуть количество полных лет"""
        b = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age_years = today.year - b.year
        if today.month < b.month or (today.month == b.month and today.day < b.day):
            age_years -= 1
        return age_years

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            fio=d["fio"], birthdate=d["birthdate"], group=d["group"], gpa=d["gpa"]
        )

    def __str__(self) -> str:
        return f"{self.fio}, гр. {self.group}, GPA {self.gpa:.2f}"
