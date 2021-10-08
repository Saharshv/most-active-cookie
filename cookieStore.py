from datetime import datetime, date
from typing import Dict, List
from cookie import Cookie

# #
# A CookieStore that stores cookies inside a dictionary
# #
class CookieStore:

    def __init__(self):
        self.store: Dict[str, Cookie] = {}

    # #
    # Adds the cookie to the store
    # #
    def addCookie(self, cookieName: str, timestamp: datetime) -> None:
        if cookieName not in self.store:
            self.store[cookieName] = Cookie(cookieName)
        self.store[cookieName].addToHistory(timestamp)

    # #
    # Gets the specified cookie if it is in the store otherwise returns None
    # #
    def getCookieByName(self, cookieName: str) -> Cookie:
        if cookieName not in self.store:
            return None
        return self.store[cookieName]

    # #
    # Returns a list of the most used cookies on the given date
    # #
    def getMostUsedCookiesByDate(self, date: date) -> List[str]:
        mostUsedCookies = []
        maxCount = 0
        for cookieName in self.store:
            cookie = self.store[cookieName]
            count = cookie.getUsageFromDate(date)
            if count != 0:
                if count > maxCount:
                    maxCount = count
                    mostUsedCookies = [cookieName]
                elif count == maxCount:
                    mostUsedCookies.append(cookieName)
        return mostUsedCookies
