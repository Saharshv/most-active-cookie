from datetime import datetime, date
from cookieStore import CookieStore
from cookie import Cookie
import unittest

class MyTest(unittest.TestCase):

    def test_cookie_store(self):
        cookieStore = CookieStore()
        timestamp = datetime.fromisoformat("2018-12-08T21:30:00+00:00")
        cookieStore.addCookie("cookie1", timestamp)
        cookie = cookieStore.getCookieByName("cookie1")
        assert cookie.getName() == "cookie1"
        assert cookie.getName() != "cookie2"
        assert cookieStore.getMostUsedCookiesByDate(date.fromisoformat("2018-12-09")) == []
        assert cookieStore.getMostUsedCookiesByDate(date.fromisoformat("2018-12-08")) == ['cookie1']
        cookieStore.addCookie("cookie2", timestamp)
        assert cookieStore.getMostUsedCookiesByDate(date.fromisoformat("2018-12-08")) == ["cookie1", "cookie2"]

    def test_cookie(self):
        cookie1 = Cookie("cookie1")
        timestamp = datetime.fromisoformat("2018-12-08T21:30:00+00:00")
        cookie1.addToHistory(timestamp)
        assert cookie1.getLastUsedTimeStamp() == timestamp
        assert cookie1.getHistory() == [timestamp]
        assert cookie1.getUsageFromDate(date.fromisoformat("2018-12-09")) == 0
        assert cookie1.getUsageFromDate(date.fromisoformat("2018-12-08")) == 1
        cookie1.addToHistory(datetime.fromisoformat("2018-12-08T21:00:00+00:00"))
        assert cookie1.getUsageFromDate(date.fromisoformat("2018-12-08")) == 2



if __name__ == '__main__':
    unittest.main()