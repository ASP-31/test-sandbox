#write your code

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Contact:
    name: str
    email: str
    phone: Optional[str] = None

class ContactBook:
    def __init__(self):
        self.contacts: List[Contact] = []
    def add(self, c: Contact):
        self.contacts.append(c)
    def find(self, name: str) -> Optional[Contact]:
        for c in self.contacts:
            if c.name.lower() == name.lower():
                return c
        return None
    def list_all(self) -> List[Contact]:
        return sorted(self.contacts, key=lambda c: c.name)

def demo():
    book = ContactBook()
    book.add(Contact("Alice", "alice@example.com", "555-0100"))
    book.add(Contact("Bob", "bob@example.com"))
    print("All contacts:")
    for c in book.list_all():
        print(f"{c.name} — {c.email}" + (f" ({c.phone})" if c.phone else ""))

if __name__ == "__main__":
    demo()

    