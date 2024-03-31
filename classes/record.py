from .name import Name
from .phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        """
        :param phone:
        """
        self.phones.append(Phone(phone))
        pass

    def edit_phone(self, phone, new_phone):
        """
        :param phone:
        :param new_phone:
        """
        k = self._phone_index(phone)
        if k is not None:
            self.phones[k] = Phone(new_phone)

    def remove_phone(self, phone):
        """
        :param phone:
        """
        k = self._phone_index(phone)
        if k is not None:
            del self.phones[k]

    def find_phone(self, phone):
        """
        :param phone:
        :return:
        """
        try:
            return [p.value for p in self.phones if p.value == phone][0]
        except IndexError:
            return None

    def _phone_index(self, phone) -> int | None:
        for k, p in enumerate(self.phones):
            if p.value == phone:
                return k

        return None
