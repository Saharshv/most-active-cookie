from cookieStore import CookieStore
from datetime import date, datetime
import sys

# #
# Fills the cookie store using the file given in the command prompt
# #
def fillCookieStoreFromInput(cookieStore: CookieStore) -> None:
    fileName = sys.argv[1]
    file = open(fileName, "r")
    for line in file:
        raw_cookie = line.strip().split(",")
        if raw_cookie[0] == "cookie" and raw_cookie[1] == "timestamp":
            continue
        if len(raw_cookie) != 2:
            raise TypeError('Expected cookie string')
        cookieStore.addCookie(raw_cookie[0], datetime.fromisoformat(raw_cookie[1]))
    file.close()

def main():
    cookieStore = CookieStore()
    fillCookieStoreFromInput(cookieStore)
    dateToFind = date.fromisoformat(sys.argv[-1])
    cookieNames = cookieStore.getMostUsedCookiesByDate(dateToFind)
    for cookieName in cookieNames:
        print(cookieName)

if __name__ == "__main__":
    main()