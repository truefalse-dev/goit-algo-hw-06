from collections import UserDict
from .record import Record


class AddressBook(UserDict):
    def add_record(self, record):
        self.update({record.name.value: record})
        pass

    def find(self, name):
        return self.get(name)

    def delete(self, name):
        self.pop(name, None)
