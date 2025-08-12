import weakref #weak references don't keep references alive if they are not used anywhere else -> lets them be dereferenced

class Wallet():
    all_wallets = weakref.WeakSet()

    def __init__(self, copper=0, silver=0, gold=0, platinum=0):
        self.copper = copper
        self.silver = silver
        self.gold = gold
        self.platinum = platinum
        Wallet.all_wallets.add(self)

    def add_wallet(self, other):
        self.copper += other.copper
        self.silver += other.silver
        self.gold += other.gold
        self.platinum += other.platinum
        self.normalize()

    def add_currency(self, copper=0, silver=0, gold=0, platinum=0):
        self.copper += copper
        self.silver += silver
        self.gold += gold
        self.platinum += platinum
        self.normalize()

    def normalize(self):
        if self.copper < 0:
            self.silver += self.copper // 10
            self.copper = 0
        if self.silver < 0:
            self.gold += self.silver // 10
            self.silver = 0
        if self.gold < 0:
            self.platinum += self.gold // 10
            self.gold = 0
        if self.platinum < 0:
            return False

        if self.copper > 10:
            self.silver += self.copper // 10
            self.copper = 10
        if self.silver > 10:
            self.gold += self.silver // 10
            self.silver = 10
        if self.gold > 10:
            self.platinum += self.gold // 10
            self.gold = 10

        return True
    
    @classmethod
    def normalize(cls):
        for wallet in cls.all_wallets:
            wallet.update_currency()