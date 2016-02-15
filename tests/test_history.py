import unittest
from common import TestHypChat
from datetime import datetime, timedelta
class TestHistory(TestHypChat):
  def setUp(self):
    super(TestHistory, self).setUp()

  def runTest(self):
    date = datetime.now()
    end_date = date + timedelta(days=-7)
    messages = self.hipchat.get_room('SOME_ROOM_YOU_CAN_ACCESS').history(maxResults=999, end_date=end_date, date=date).contents()
