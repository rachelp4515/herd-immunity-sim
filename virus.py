class Virus(object):

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3


if __name__ == "__main__":
    test_virus_instantiation()
    cold = Virus('Cold', 0.4, 0.03)
    print(f"name {cold.name} should be cold")

