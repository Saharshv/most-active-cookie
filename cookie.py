from collections import defaultdict
from datetime import date, datetime
from typing import Dict, List

class Cookie:

    def __init__(self, name = "cookie"):
        self.name: str = name
        self.history: List[datetime] = []
        self.datesUsed: Dict[date, int] = defaultdict(int)

    # #
    # Returns the usage history of this cookie
    # #
    def getHistory(self) -> List[datetime]:
        return self.history

    # #
    # Returns the last timestamp this cookie was used on
    # #
    def getLastUsedTimeStamp(self) -> datetime:
        return self.history[0]

    # #
    # Returns the name of this cookie
    # #
    def getName(self) -> str:
        return self.name

    # #
    # Adds the timestamp to the usage history of this cookie
    # #
    def addToHistory(self, timestamp: datetime) -> None:
        self.history.append(timestamp)
        self.datesUsed[timestamp.date()] += 1
    
    # #
    # Returns the number of times this cookie was used on the given date.
    # #
    def getUsageFromDate(self, date: date) -> int:
        return self.datesUsed[date]