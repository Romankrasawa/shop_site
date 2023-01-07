from django.db import models

class Headphones_type(models.TextChoices):
    Vacum = "Vacum", "Вакумні"
    TABS = "Tabs", "Вкладки"
    TWS = "TWS", "TWS"
    LOADED = "Loaded", "Накладні"
    FULLSIZED = "Fullsized", "Повнорозмірні"

class Connection_type(models.TextChoices):
    WIRELESS = "Wireless", "Безпровідний"
    LEADING = "Leading", "Провідний"
    COMBINATED = "Combinated", "Комбінований"

class Sim_type(models.TextChoices):
    MINI_SIM = "Mini_SIM", "Mini SIM"
    MICRO_SIM = "Micro_SIM", "Micro SIM"
    NANO_SIM = "Nano_SIM", "Nano SIM"

class MobileOSes(models.TextChoices):
    IOS = "IOS", "IOS"
    ANDROID4 = "Android_4", "Android 4"
    ANDROID5 = "Android_5", "Android 5"
    ANDROID6 = "Android_6", "Android 6"
    ANDROID7 = "Android_7", "Android 7"
    ANDROID8 = "Android_8", "Android 8"
    ANDROID9 = "Android_9", "Android 9"
    ANDROID10 = "Android_10", "Android 10"
    ANDROID11 = "Android_11", "Android 11"
    ANDROID12 = "Android_12", "Android 12"
    ANDROID13 = "Android_13", "Android 13"
    WINDOWS_MOBILE = "Windows_Mobile", "Windows Mobile"
    OTHER = "Other", "Інше"

class Material(models.TextChoices):
    METAL = "Metal", "Метал"
    PLASTIC = "Plastic", "Пластик"
    GLASS = "Glass", "Скло"
    OTHER = "Other", "Інше"

class Categories(models.TextChoices):
    LAPTOP = "laptop", "Ноутбук"
    PC = "PC", "Компютер"
    PHONE = "Phone", "Телефон"
    Tablet = "Tablet", "Планшет"
    TV = "TV", "Телевізор"
    MONITOR = "Monitor", "Монітор"
    HEADPHONES = "Headphones", "Навушники"
    MOUSE = "Mouse", "Мишка"
    KEYBOARD = "Keyboard", "Клавіатура"
    FLASH_DRIVE = "Flash Drive", "Флешка"
    WATCH = "Watch", "Годинник"
    PROCESSOR = "Processor", "Процессор"
    VIDEOCARD = "Videocard", "Відеокарта"
    RAM = "RAM", "Оперативна память"
    DISK = "Disk", "Диск"
    MOTHERBOARD = "Motherboard", "Материнська плата"
    KULLER = "Kuller", "Система охолодження"
    POWER_BLOCK = "Power Block", "Блок живлення"
    CASE = "Case", "Корпус"

class Categories_plural(models.TextChoices):
    LAPTOP = "laptop", "Ноутбуки"
    PC = "PC", "Компютери"
    PHONE = "Phone", "Телефони"
    Tablet = "Tablet", "Планшети"
    TV = "TV", "Телевізори"
    MONITOR = "Monitor", "Монітори"
    HEADPHONES = "Headphones", "Навушники"
    MOUSE = "Mouse", "Мишки"
    KEYBOARD = "Keyboard", "Клавіатури"
    FLASH_DRIVE = "Flash Drive", "Флешки"
    WATCH = "Watch", "Годинники"
    PROCESSOR = "Processor", "Процессори"
    VIDEOCARD = "Videocard", "Відеокарти"
    RAM = "RAM", "Оперативна память"
    DISK = "Disk", "Диски"
    MOTHERBOARD = "Motherboard", "Материнські плати"
    KULLER = "Kuller", "Системи охолодження"
    POWER_BLOCK = "Power Block", "Блоки живлення"
    CASE = "Case", "Корпуси"

class Screen_types(models.TextChoices):
    IPS = "IPS", "IPS"
    OLED = "OLED", "OLED"
    TN = "TN", "TN"
    RETINA = "RETINA", "Retina"
    VA = "VA", "VA"
    IGZO = "IGZO", "IGZO"
    LTPS = "LTPS", "LTPS"
    LIQUID_RETINA = "Liquid_Retina", "Liquid Retina"
    LIQUID_RETINA_XDR = "Liquid_Retina_XDR", "Liquid Retina XDR"

class CustomColours(models.TextChoices):
    WHITE = "WHITE", "Білий"
    BLACK = "BLACK", "Чорний"
    RED = "RED", "Червоний"
    BLUE = "BLUE", "Синій"
    PINK = "PINK", "Рожевий"
    SILVER = "SILVER", "Сріблястий"
    VIOLET = "VIOLET", "Фіолетовий"
    GRAY = "GRAY", "Сірий"
    GOLD = "GOLD", "Золотий"
    BROWN = "BROWN", "Коричневий"
    GREEN = "GREEN", "Зелений"
    ORANGE = "ORANGE", "Оранжений"
    PAINTING = "PAINTING", "Малюнок"

class RAM_types(models.TextChoices):
    DDR5 = "DDR5", "DDR5"
    DDR4 = "DDR4", "DDR4"
    DDR3 = "DDR3", "DDR3"
    DDR2 = "DDR2", "DDR2"

class OSes(models.TextChoices):
    WIN7 = "WIN7", "Віндовс 7"
    WIN8 = "WIN8", "Віндовс 8"
    WIN10PRO = "WIN10PRO", "Віндовс 10 Pro"
    WIN10HOME = "WIN10HOME", "Віндовс 10 Home"
    MAC = "MAC", "Мак ОС"
    LIN = "LIN", "Лінукс"
    WITHOUTOS = "WITHOUTOS", "Без операційної системи"

