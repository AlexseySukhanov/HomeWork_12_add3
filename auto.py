"""
Calss describes auto owners and they cars
"""

class Auto:

    def __init__(self, model, idnumber, color, owner_surname, owner_adress, to, to_date):
        if not isinstance(owner_surname, str):
            raise TypeError(f'{type(owner_surname).__name__} Surname is not valid')
        if len(idnumber) < 8:
            raise TypeError(f'{type(idnumber).__name__} Id number of auto is not valid')

        self.model = model
        self.idnumber = idnumber
        self.color = color
        self.owner_surname = owner_surname.title()
        self.owner_adress = owner_adress
        self.to = to
        self.to_date = to_date


    def get_info(self, color, model, lastnumbers):
        tmpowner = []
        tmpadress = []
        for i in self:
            if i.model == model and i.color == color and i.idnumber[4:6] == lastnumbers:
                tmpowner.append(i.owner_surname)
                tmpadress.append(i.owner_adress)
        return f'{tmpowner}\n' \
               f'{tmpadress}'



        pass