class warrior:
    name = ""
    health = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.pSuperior = False
        self.pInferior = False
        self.pHead = False

    def atackSuperior(self, enemy):
        if enemy.pSuperior == False:
            enemy.health -= 20
            print(self.name + " realized a superior atack to " + enemy.name)

    def atackInferior(self, enemy):
        if enemy.pInferior == False:
            enemy.health -= 10
            print(self.name + " realized a inferior atack to " + enemy.name)
    
    def atackHead(self, enemy):
       if enemy.pHead == False:
           enemy.health -= 50
           print(self.name + " realized a head atack to " + enemy.name)

    def protectSuperior(self):
        self.pSuperior = True
        print(self.name + "  protected superior")
    
    def protectInferior(self):
        self.pInferior = True
        print(self.name + "  protected inferior")

    def protectHead(self):
        self.pHead = True
        print(self.name + "  protected head")

    def resetProtection(self):
        self.pSuperior = False
        self.pInferior = False
        self.pHead = False