from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(models.Model):
    table_id = models.IntegerField(primary_key = True, blank = False, null = False, unique = True)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)


class files(models.Model):
    table_id = models.IntegerField(primary_key = True, blank = False, null = False, unique = True)
    original_filename = models.CharField(max_length=255)
    renamed_filename = models.CharField(max_length=255)
    upload_date = models.DateTimeField()


class teacher(models.Model):
    table_id = models.IntegerField(primary_key = True, blank = False, null = False, unique = True)
    id = models.TextField()
    name = models.TextField()
    email = models.TextField()
    post = models.TextField()
    authorize_level = models.IntegerField()
    subjects = ArrayField(ArrayField(models.TextField()))
    classes = ArrayField(ArrayField(models.TextField()))


class class_name(models.Model):
    table_id = models.IntegerField(primary_key = True, blank = False, null = False, unique = True)
    class_no = models.IntegerField()
    class_section = models.IntegerField()
    subjects = ArrayField(ArrayField(models.TextField()))


class time_table(models.Model):
    table_id = models.IntegerField(primary_key = True, blank = False, null = False, unique = True)
    class_no = models.TextField()
    class_sections = models.TextField()
    class_no_days = models.IntegerField()
    class_no_periods = models.IntegerField()
    time_table = models.JSONField(default = list)
    
    def __init__ (self):
        self.class_no_days = 6
        self.class_no_periods = 8
        self.time_table = [[{} for _ in range(self.class_no_days)] for _ in range(self.class_no_periods)]


classes = [
    "Primary", "I", "II", "III", "IV", "V",
    "VI", "VII", "VIII", "IX", "X", "XI", "XII"
]

sections = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

subject_code = {
    "001" : "ENGLISH",
    "002" :	"HINDI",
    "003" :	"URDU",
    "022" :	"SANSKRIT",
    "027" :	"HISTORY",
    "028" :	"POLITICAL SCIENCE",
    "029" :	"GEOGRAPHY",
    "030" :	"ECONOMICS",
    "031" :	"MUSIC CARNATIC (VOCAL)",
    "032" :	"MUSIC CARNATIC (INSTRUMENT MELODIC)",
    "033" :	"MUSIC CARNATIC (INSTRUMENT PERCUSSION)",
    "034" :	"MUSIC HINDUSTANI (VOCAL)",
    "035" :	"MUSIC HINDUSTANI (INSTRUMENT MELODIC)",
    "036" :	"MUSIC HINDUSTANI (INSTRUMENT PERCUSSION)",
    "037" :	"PSYCHOLOGY",
    "039" :	"SOCIOLOGY",
    "040" :	"PHILOSOPHY",
    "041" :	"MATHEMATICS",
    "042" :	"PHYSICS",
    "043" :	"CHEMISTRY",
    "044" :	"BIOLOGY",
    "045" :	"BIOTECHNOLOGY",
    "046" :	"ENGINEERING GRPHICS",
    "048" :	"PHYSICAL EDUCATION",
    "049" :	"PAINTING",
    "050" :	"GRAPHICS",
    "051" :	"SCULPTURE",
    "052" :	"APPLIED ART/COMMERCIAL ART",
    "053" :	"FASHION STUDIES",
    "054" :	"BUSINESS STUDIES",
    "055" :	"ACCOUNTANCY",
    "056" :	"DANCE-KATHAK",
    "057" :	"DANCE-BHARATNATYAM",
    "058" :	"DANCE-KUCHIPUDI",
    "059" :	"DANCE-ODISSI",
    "060" :	"DANCE-MANIPURI",
    "061" :	"DANCE-KATHAKALI",
    "062" :	"DANCE-MOHINIYATTAM",
    "064" :	"HOME SCIENCE",
    "065" :	"INFORMATICS PRACTICE",
    "066" :	"ENTREPRENEURSHIP",
    "067" :	"MULTIMEDIA & WEB TECHNOLOGY",
    "068" :	"AGRICULTURE",
    "069" :	"CREATIVE WRITING & TRANSLATION STUDIES",
    "070" :	"HERITAGE CRAFTS",
    "071" :	"GRAPHIC DESIGN",
    "072" :	"MASS MEDIA STUDIES",
    "073" :	"KNOWLEDGE TRADITIONS AND PRACTICES OF INDIA",
    "074" :	"LEGAL STUDIES",
    "075" :	"HUMAN RIGHTS AND GENDER STUDIES",
    "076" :	"N.C.C. (NATIONAL CADET CORPS)",
    "078" :	"THEATRE STUDIES",
    "083" :	"COMPUTER SCIENCE",
    "101" :	"FUNCTIONAL ENGLISH",
    "104" :	"PUNJABI",
    "105" :	"BENGALI",
    "106" :	"TAMIL",
    "107" :	"TELUGU",
    "108" :	"SINDHI",
    "109" :	"MARATHI",
    "110" :	"GUJARATI",
    "111" :	"MANIPURI",
    "112" :	"MALAYALAM",
    "113" :	"ODIA",
    "114" :	"ASSAMESE",
    "115" :	"KANNADA",
    "116" :	"ARABIC",
    "117" :	"TIBETAN",
    "118" :	"FRENCH",
    "119" :	"PORTUGUESE",
    "120" :	"GERMAN",
    "121" :	"RUSSIAN",
    "123" :	"PERSIAN",
    "124" :	"NEPALI",
    "125" :	"LIMBOO",
    "126" :	"LEPCHA",
    "192" :	"BODO",
    "193" :	"TANGKHUL",
    "194" :	"JAPANESE",
    "195" :	"BHUTIA",
    "196" :	"SPANISH",
    "197" :	"KASHMIRI",
    "198" :	"MIZO",
    "199" :	"BHASA MELAYU",
    "301" :	"ENGLISH CORE",
    "302" :	"HINDI CORE",
    "303" :	"URDU CORE",
    "322" :	"SANSKRIT CORE",
    "604" :	"OFFICE PROCEDURE & PRACTICE",
    "605" :	"SECRETARIAL PRACTICE & ACCOUNTING",
    "606" :	"OFFICE COMMUNICATION",
    "607" :	"TYPOGRAPHY & COMPUTER APPLICATION (ENGLISH)",
    "608" :	"SHORTHAND ENGLISH",
    "609" :	"TYPOGRAPHY & COMPUTER APPLICATION (HINDI)",
    "610" :	"SHORTHAND HINDI",
    "611" :	"FINANCIAL ACCOUNTING",
    "612" :	"ELEMENT COST ACCOUNTANCY &AUDITING",
    "613" :	"MARKETING",
    "614" :	"SALESMANSHIP",
    "615" :	"CONSUMER BEHAVIOUR & PROTECTION",
    "617" :	"STOREKEEPING",
    "618" :	"STORE ACCOUNTING",
    "619" :	"CASH MANAGEMENT & HOUSE KEEPING",
    "620" :	"LENDING OPERATIONS",
    "621" :	"MANAGEMENT OF BANK OFFICE",
    "622" :	"ENGINEERING SCIENCE",
    "623" :	"ELECTRIC MACHINES",
    "624" :	"ELECTRICAL APPLICANCES",
    "625" :	"APPLIED PHYSICS",
    "626" :	"MECHANICAL ENGINEERING",
    "627" :	"AUTO ENGINEERING",
    "628" :	"AUTOSHOP REPAIRING & PRACTICE",
    "629" :	"CIVIL ENGINEERING",
    "630" :	"FABRICATION TECHNOLOGY-II",
    "631" :	"FABRICATION TECHNOLOGY-III",
    "632" :	"AIR CONDITIONING & REFRIGERATION - III",
    "633" :	"AIR CONDITIONING & REFRIGERATION - IV",
    "634" :	"ELECTRONIC DEVICES & CIRCUITS",
    "635" :	"RADIO ENGINEERING & AUDIO SYSTEM",
    "636" :	"TV & VIDEO SYSTEMS",
    "637" :	"ELECTRICAL ENGINEERING",
    "639" :	"MILK & MILK PRODUCTS",
    "640" :	"MILK PRODUCT TRANSPORT & MILK CO-OPERATIVES",
    "641" :	"DAIRY PLANT INSTRUMENTATION",
    "642" :	"VEGETABLE CULTURE",
    "643" :	"FLORICULTURE",
    "644" :	"POST HARVESTING TECHNOLOGY & PRESERVATION",
    "654" :	"BEAUTY THERAPY & HAIR DESIGNING - II",
    "655" :	"COSMETIC CHEMISTRY",
    "656" :	"YOGA ANATOMY & PHYSIOLOGY",
    "657" :	"BIOLOGY-OPTHALMIC",
    "658" :	"OPTICS",
    "659" :	"OPHTHALMIC TECHNOLOGY",
    "660" :	"LABORATORY MEDICINE (CLINICAL PATH., HEOM. & HISTO)",
    "661" :	"CLINICAL BIO-CHEMISTRY",
    "662" :	"MICROBIOLOGY",
    "663" :	"FUNDAMENTAL OF NURSING II",
    "664" :	"COMMUNITY HEALTH NURSING - II",
    "665" :	"MATERNITY & CHILD HEALTH NURSING - II",
    "666" :	"RADIATION PHYSICS",
    "667" :	"RADIOGRAPHY-I (GENERAL)",
    "668" :	"RADIOGRAPHY-II (SPECIAL)",
    "675" :	"ADVANCE FOOD PREPARATION",
    "676" :	"MEAL PLANNING & SERVICE",
    "677" :	"ESTABLISHMENT & MANAGEMENT OF FOOD SERVICE UNIT",
    "684" :	"TEXTILE SCIENCE",
    "685" :	"DESIGNING & PATTERN MAKING",
    "686" :	"CLOTHING CONSTRUCTION",
    "687" :	"BASIC DESIGN",
    "688" :	"DYEING & PRINTING",
    "690" :	"FOOD PREPARATION - II",
    "691" :	"ACCOMMODATION SERVICE",
    "692" :	"FOOD & BEVERAGES SERVICES - II",
    "693" :	"INDIA-TOURIST DESTINATION",
    "694" :	"TRAVEL TRADE MANAGEMENT",
    "695" :	"TOUR MANAGEMENT & MANPOWER PLANNING",
    "696" :	"FOOD SCIENCE & HYGIENE",
    "697" :	"BAKERY SCIENCE",
    "698" :	"CONFECTIONERY",
    "699" :	"I T SYSTEMS",
    "700" :	"BUSINESS DATA PROCESSING",
    "701" :	"DTP CAD & MULTIMEDIA",
    "702" :	"LIBRARY ADMINISTRATION & MANAGEMENT",
    "703" :	"CLASSIFICATION & CATALOGUING",
    "704" :	"REFERENCE SERVICES",
    "705" :	"PRINCIPLE & PRACTICE OF LIFE INSURANCE",
    "706" :	"COMPUTER & LIFE INSURANCE ADMINISTRATION",
    "712" :	"TRANSPORTATION SYSTEM & MANAGEMENT",
    "716" :	"POULTRY NUTRITION & PHYSIOLOGY",
    "717" :	"POULTRY PRODUCTS TECHNOLOGY",
    "718" :	"POULTRY DISEASES & THEIR CONTROL",
    "723" :	"INTRODUCTION TO FINANCIAL MARKETS-2-XII",
    "724" :	"BUSINESS PROCESS OUTSOURCING SKILLS-XII",
    "728" :	"HEALTH EDUCATION & PUBLIC RELATIONS – XII",
    "729" :	"BASIC CONCEPTS OF HEALTH DISEASE & MEDICAL TERMINOLOGY-XII",
    "730" :	"FIRST AID & EMERGENCY MEDICAL CARE-XII",
    "731" :	"CHILD HEALTH NURSING",
    "732" :	"MIDWIFERY",
    "733" :	"HEALTH CENTRE MANAGEMENT",
    "734" :	"FOOD PRODUCTION - III",
    "735" :	"FOOD PRODUCTIO - IV",
    "736" :	"FOOD SERVICE - II",
    "737" :	"FOOD & BEVERAGE:COST AND CONTROL",
    "738" :	"UNDERSTANDING THE EVOLUTION AND FORMS OF MASS MEDIA-II",
    "739" :	"THE CREATIVE & COMMERCIAL PROCESS IN MASS MEDIA - II",
    "740" :	"GEOSPATIAL TECHNOLOGY - II",
}
