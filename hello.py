print("hello world")
class Calculator:
    def do_nested_stuff(self, items):
        total = 0
        for item in items:
            if item.is_valid:
                if item.price > 10:
                    if item.quantity > 0:
                        total += item.price * item.quantity
        return total
