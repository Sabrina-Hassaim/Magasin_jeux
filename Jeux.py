from pydantic import BaseModel, validator, ValidationError
class Jeux (BaseModel):
    console_jeu: str
    genre : str
    prix : int
    description : str
    code_rayon : str 


    @validator('code_rayon')
    def check_code_rayon(cls, code_rayon, values):
        if len(code_rayon) != 14:
            raise ValueError('Le code rayon doit avoir 14 chiffres')
        if code_rayon[0:3].isalpha() == False:
            raise ValueError('Le code rayon doit commencer par 3 lettres')
        if code_rayon[3] != '.' or code_rayon[6] != '.' or code_rayon[9] != '.':
            raise ValueError('Le code rayon doit avoir 3 points')
        if code_rayon[4:6].isdigit() == False :
            raise ValueError('Le code rayon doit avoir 2 chiffres')
        if code_rayon[7:9].isdigit() == False :
            print(values)
            raise ValueError('Le code rayon doit avoir 2 chiffres')
        if code_rayon[10:14].isdigit() == False  or int(code_rayon[10:14]) > 2022 :
            raise ValueError('Le code rayon doit avoir 4 chiffres')
        return code_rayon
    
    @validator('genre')
    def check_genre(cls, genre):
        if genre not in {"RPG", "Sport", "Simulation"}:
            raise ValueError('Le genre doit être RPG, Sport ou Simulation')
        return genre
    
    @validator('console_jeu')
    def check_console_jeu(cls, console_jeu):
        if console_jeu == "FakeConsole" :
            raise ValueError('La console ne peut pas être FakeConsole')
        return console_jeu
    

if __name__ == "__main__":
    jeu1 = Jeux(console_jeu="PS2", genre="RPG", prix=23, description="Un jeu de RPG", code_rayon="ABC.12.35.2021")
    print(jeu1.console_jeu)
    jeu2 = Jeux(console_jeu="PS2", genre="RPG", prix=23, description="Un jeu de RPG", code_rayon="ABC.12.35.2025")
