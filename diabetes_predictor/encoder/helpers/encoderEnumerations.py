from enum import Enum

class SexEnum(Enum):
    male="Masculino"
    female="Feminino"

class AgeEnum(Enum):
    ageBellow45 = "Menos de 45 anos"
    ageBetween45And54 = "45-54 anos"
    ageBetween55And64 = "55-64 anos"
    ageAbove64 = "Mais de 64 anos"

class WaistEnum(Enum):
    waistCategoryOne = "Homens - Menos de 94 cm | Mulheres - Menos de 80 cm"
    waistCategoryTwo = "Homens - 94-102 cm | Mulheres - 80-88 cm"
    waistCategoryThree = "Homens - Mais de 102 cm | Mulheres - Mais de 88 cm"
    waistCategoryUnkown = "Não sei"
    
class ExerciseEnum(Enum):
    yes = "Sim"
    no = "Não"
    
class HypertensionEnum(Enum):
    yes = "Sim"
    no = "Não"
    
class FruitsAndVegetablesEnum(Enum):
    everyDay = "Todos os dias"
    sometimes = "As vezes"
    dontEat = "Não como"

class DiabeticFamilyEnum(Enum):
    yesExceptParents = "Sim: avós, tias, tios ou primos em 1º grau (excepto pais, irmãos, irmãs ou filhos)?"
    yesParents = "Sim: pais, irmãos, irmãs ou filhos"
    no = "Não"
    dontKnow = "Não sei"
    
class EatsAlotFatsEnum(Enum):
    yes = "Sim"
    no = "Não"
       
class SmokeEnum(Enum):
    no = "Não"
    yesButStoped = "Fumava, mas parei"
    yesOneToTenAday = "Fumo 1 a 10 cigarros por dia"
    yesMoreThenTenAday = "Fumo 1 a 10 cigarros por dia"    
    
class highBloodGlucoseEnum(Enum):
    yes = "Sim"
    no = "Não"
    dontKnow = "Não sei"    
    
class GlucoseAnalysisEnum(Enum):
    dontKnow = "Não sei"    
    
class GlucoseLevelChangeEnum(Enum):
    yes = "Sim"
    no = "Não"
    dontKnow = "Não sei"

class WomanGlucoseChangeEnum(Enum):
    yes = "Sim"
    no = "Não"
    notAWoman = "Não sou mulher"
    dontKnow = "Não sei"
   
class AreYouDiabeticEnum(Enum):
    yes = "Sim, diagnosticada pelo médico"
    no = "Não, de acordo com o meu médico"
    dontKnow = "Não sei"
