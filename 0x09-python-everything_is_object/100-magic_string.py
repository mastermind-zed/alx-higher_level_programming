def magic_string():
    from counter import Counter
    Counter.i += 1
    return ", ".join(["BestSchool" for i in range(0, Counter.i)])
