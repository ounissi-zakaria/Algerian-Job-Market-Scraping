from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class JobItem:
    title: str = field(default="")
    id: str = field(default="")
    link: str = field(default="")

    published_at: datetime | None = field(default=None)
    created_at: datetime | None = field(default=None)

    technologies: list[str] = field(default_factory=list)

    company: str = field(default="")
    contract_type: str = field(default="")
    job_type: str = field(default="")
    level: str = field(default="")
