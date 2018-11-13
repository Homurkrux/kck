class Telewizor:
    kanaly=["cc","zz","xx","aa","ss"]
    nrKanalu=2
    def __init__(self):
        print("odpalamy")
        print("aktualny kanał: ",self.kanaly[self.nrKanalu])
    def powitanie(self,):
        print("elo")
    def ustawkanal(self,kanal):
        self.nrKanalu=kanal
    def wysKanal(self):
        print("aktualny kanał: ",self.kanaly[self.nrKanalu])

mojTV=Telewizor()
mojTV.powitanie()
kanal=int(input("jaki chcesz kanal?"))
mojTV.ustawkanal(kanal)
mojTV.wysKanal()
