import random
OG_D4T3 = f'{str(random.randint(2017, 2020))}-0{str(random.randint(1, 9))}-{str(random.randint(1, 28))}T{str(random.randint(1, 24))}:{str(random.randint(1, 60))}:{str(random.randint(1, 60))}+0{str(random.randint(1, 8))}:00'

list_lang = {
"ru":{
    "F0PR1_OLIC_POCA": ["показатель", "олицетворение", "уровень", "фактор", "величина", "параметр", "важная составляющая"],
    "F0PR2_STAT0S": ["статуса", "достатка", "богатства"],
    "F0PR3_U5PX": ["успеха", "удачи", "результата", "благополучия", "триумфа", "фурора"],
    "F0PR5_4UVSTV0": ["чувство", "ощущение", "тяга"],
    "F0PR4_5TY1E": ["стиля", "образа", "моды", "эстетики", "фасона"],
    "F0PR6_0R1GIN4L": ["оригинальности", "особенности", "отличительной", "черты", "своеобразия"],
    "F0PR7_54MOD0": ["самодостаточности", "цельности", "значительности", "самостоятельности"],
    "F0PR8_SHED3VR0": ["шедевр", "изобретение", "создание", "достижение", "творение", "результат"],
    "F0PR9_V1SHEDVR": ["высокого искусства", "большого искусства", "высокого дела", "большого дела", "кропотливой работы", "усердной работы", "ответственной работы", "хорошей работы", "безупречной работы", "достойной работы"]},
"re":{
    "F0PR1_OLIC_POCA": ["metrik", "Identitätswechsel", "Ebene", "Faktor", "Größe", "Parameter", "wichtige Komponente"],
    "F0PR2_STAT0S": ["status", "Wohlstand", "Reichtum"],
    "F0PR3_U5PX": ["erfolg", "Glück", "Ergebnis", "Wohlbefinden", "Triumph", "Furore"],
    "F0PR5_4UVSTV0": ["gefühl", "Gefühl", "Verlangen"],
    "F0PR4_5TY1E": ["stil", "Bild", "Mode", "Ästhetik", "Stil"],
    "F0PR6_0R1GIN4L": ["originalität", "Besonderheiten", "unverwechselbar", "Merkmale", "Eigenheiten"],
    "F0PR7_54MOD0": ["Selbständigkeit", "Ganzheit", "Bedeutsamkeit", "Selbstständigkeit"],
    "F0PR8_SHED3VR0": ["meisterwerk", "Erfindung", "Schöpfung", "Leistung", "Schöpfung", "Ergebnis"],
    "F0PR9_V1SHEDVR": ["hohe Kunst", "große Kunst", "hohe Sache", "große Sache", "mühsame Arbeit", "harte Arbeit", "verantwortungsvolle Arbeit", "gute Arbeit", "tadellose Arbeit", "würdige Arbeit"]},
"us":{
    "F0PR1_OLIC_POCA": ["indicator", "personification", "level", "factor", "magnitude", "parameter", "important component"],
    "F0PR2_STAT0S": ["status", "prosperity", "wealth"],
    "F0PR3_U5PX": ["success", "good luck", "result", "prosperity", "triumph", "furor"],
    "F0PR5_4UVSTV0": ["feeling", "feeling", "craving"],
    "F0PR4_5TY1E": ["style", "image", "fashion", "aesthetics", "style"],
    "F0PR6_0R1GIN4L": ["originality", "features", "distinctive", "traits", "originality"],
    "F0PR7_54MOD0": ["self-sufficiency", "integrity", "significance", "independence"],
    "F0PR8_SHED3VR0": ["masterpiece", "invention", "creation", "achievement", "creation", "result"],
    "F0PR9_V1SHEDVR": ["high art", "great art", "high work", "big work", "hard work", "hard work", "responsible work", "good work", "impeccable work", "decent work"]},
"br":{
    "F0PR1_OLIC_POCA": ["indicador", "personificação", "nível", "fator", "valor", "parâmetro", "componente importante"],
    "F0PR2_STAT0S": ["status", "prosperidade", "riqueza"],
    "F0PR3_U5PX": ["sucesso", "boa sorte", "resultado", "bem-estar", "triunfo", "furor"],
    "F0PR5_4UVSTV0": ["sentimento", "sensação", "impulso"],
    "F0PR4_5TY1E": ["estilo", "imagem", "moda", "estética", "estilo"],
    "F0PR6_0R1GIN4L": ["originalidade", "características", "distintivo", "características", "originalidade"],
    "F0PR7_54MOD0": ["auto-suficiência", "integridade", "significância", "independência"],
    "F0PR8_SHED3VR0": ["obra-prima", "invenção", "criação", "conquista", "criação", "resultado"],
    "F0PR9_V1SHEDVR": ["alta arte", "grande arte", "alto trabalho", "ótimo trabalho", "trabalho duro", "trabalho duro", "trabalho responsável", "bom trabalho", "excelente trabalho", "trabalho digno"]},
"es":{
    "F0PR1_ESOLIC_POCA": ["indicador", "personificación", "nivel", "factor", "valor", "parámetro", "componente importante"],
    "F0PR2_ESSTAT0S": ["estado", "prosperidad", "riqueza"],
    "F0PR3_ESU5PX": ["éxito", "buena suerte", "resultado", "bienestar", "triunfo", "furor"],
    "F0PR5_ES4UVSTV0": ["sentimiento", "sensación", "empuje"],
    "F0PR4_ES5TY1E": ["estilo", "imagen", "moda", "estética", "estilo"],
    "F0PR6_ES0R1GIN4L": ["originalidad", "características", "distintivo", "características", "originalidad"],
    "F0PR7_ES54MOD0": ["autosuficiencia", "integridad", "importancia", "independencia"],
    "F0PR8_ESSHED3VR0": ["obra maestra", "invención", "creación", "logro", "creación", "resultado"],
    "F0PR9_ESV1SHEDVR": ["gran arte", "gran arte", "gran trabajo", "gran trabajo", "trabajo duro", "trabajo duro", "trabajo responsable", "buen trabajo", "trabajo excelente", "trabajo digno"]},
"el":{
    "F0PR1_OLIC_POCA": ["δείκτης", "προσωποποίηση", "επίπεδο", "παράγοντας", "τιμή", "παράμετρος", "σημαντικό στοιχείο"],
    "F0PR2_STAT0S": ["κατάσταση", "ευημερία", "πλούτος"],
    "F0PR3_U5PX": ["επιτυχία", "καλή τύχη", "αποτέλεσμα", "ευημερία", "θρίαμβος", "μανία"],
    "F0PR5_4UVSTV0": ["αίσθημα", "αίσθηση", "ώθηση"],
    "F0PR4_5TY1E": ["στυλ", "εικόνα", "μόδα", "αισθητική", "στυλ"],
    "F0PR6_0R1GIN4L": ["πρωτοτυπία", "χαρακτηριστικά", "διακριτικό", "χαρακτηριστικά", "πρωτοτυπία"],
    "F0PR7_54MOD0": ["αυταπάρκεια", "ακεραιότητα", "σημασία", "ανεξαρτησία"],
    "F0PR8_SHED3VR0": ["αριστούργημα", "εφεύρεση", "δημιουργία", "επίτευγμα", "δημιουργία", "αποτέλεσμα"],
    "F0PR9_V1SHEDVR": ["υψηλή τέχνη", "μεγάλη τέχνη", "υψηλή δουλειά", "μεγάλη δουλειά", "σκληρή δουλειά", "σκληρή δουλειά", "υπεύθυνη δουλειά", "καλή δουλειά", "εξαιρετική δουλειά", "άξια δουλειά"]},
"de":{
    "F0PR1_OLIC_POCA": ["Indikator", "Personifikation", "Stufe", "Faktor", "Wert", "Parameter", "wichtige Komponente"],
    "F0PR2_STAT0S": ["Status", "Wohlstand", "Vermögen"],
    "F0PR3_U5PX": ["Erfolg", "Viel Glück", "Ergebnis", "Wohlfahrt", "Triumph", "Furore"],
    "F0PR5_4UVSTV0": ["Gefühl", "Empfindung", "Schub"],
    "F0PR4_5TY1E": ["Stil", "Bild", "Mode", "Ästhetik", "Stil"],
    "F0PR6_0R1GIN4L": ["Originalität", "Merkmale", "Unterscheidungsmerkmal", "Merkmale", "Originalität"],
    "F0PR7_54MOD0": ["Autarkie", "Integrität", "Bedeutung", "Unabhängigkeit"],
    "F0PR8_SHED3VR0": ["Meisterwerk", "Erfindung", "Schöpfung", "Leistung", "Schöpfung", "Ergebnis"],
    "F0PR9_V1SHEDVR": ["hohe Kunst", "großartige Kunst", "hohe Arbeit", "großartige Arbeit", "harte Arbeit", "harte Arbeit", "verantwortungsvolle Arbeit", "gute Arbeit", "ausgezeichnete Arbeit", "würdige Arbeit"]},
"tr":{
    "F0PR1_OLIC_POCA": ["gösterge", "kişileştirme", "seviye", "faktör", "değer", "parametre", "önemli bileşen"],
    "F0PR2_STAT0S": ["statü", "refah", "zenginlik"],
    "F0PR3_U5PX": ["başarı", "iyi şanslar", "sonuç", "refah", "zafer", "şiddet"],
    "F0PR5_4UVSTV0": ["duygu", "his", "itme"],
    "F0PR4_5TY1E": ["stil", "imaj", "moda", "estetik", "stil"],
    "F0PR6_0R1GIN4L": ["özgünlük", "özellikler", "ayırt edici", "özellikler", "özgünlük"],
    "F0PR7_54MOD0": ["kendi kendine yeterlilik", "dürüstlük", "önem", "bağımsızlık"],
    "F0PR8_SHED3VR0": ["şaheser", "buluş", "yaratma", "başarı", "yaratma", "sonuç"],
    "F0PR9_V1SHEDVR": ["yüksek sanat", "harika sanat", "yüksek iş", "harika iş", "sıkı iş", "sıkı iş", "sorumlu iş", "iyi iş", "mükemmel iş", "değerli iş"]},
"pl":{
    "F0PR1_OLIC_POCA": ["miara", "podszywanie się", "poziom", "współczynnik", "wielkość", "parametr", "ważny składnik"],
    "F0PR2_STAT0S": ["status", "bogactwo", "bogactwo"],
    "F0PR3_U5PX": ["sukces", "szczęście", "wynik", "dobrobyt", "triumf", "wrzawa"],
    "F0PR5_4UVSTV0": ["uczucie", "uczucie", "pociągnięcie"],
    "F0PR4_5TY1E": ["styl", "wygląd", "moda", "estetyka", "styl"],
    "F0PR6_0R1GIN4L": ["oryginalność", "cechy", "wyróżniające się", "cechy", "osobliwości"],
    "F0PR7_54MOD0": ["samowystarczalny", "integralny", "znaczący", "samowystarczalny"],
    "F0PR8_SHED3VR0": ["arcydzieło", "wynalazek", "stworzenie", "osiągnięcie", "stworzenie", "wynik"],
    "F0PR9_V1SHEDVR": ["wysoka sztuka", "wielka sztuka", "wysoka praca", "świetna praca", "ciężka praca", "ciężka praca", "odpowiedzialna praca", "dobra robota", "doskonała praca", "godny praca"]},
"it":{
    "F0PR1_OLIC_POCA": ["misura", "rappresentazione", "livello", "fattore", "magnitudo", "parametro", "componente importante"],
    "F0PR2_STAT0S": ["stato", "ricchezza", "ricchezza"],
    "F0PR3_U5PX": ["successo", "fortuna", "risultato", "prosperità", "trionfo", "furore"],
    "F0PR5_4UVSTV0": ["sensazione", "sensazione", "tira"],
    "F0PR4_5TY1E": ["stile", "look", "moda", "estetica", "stile"],
    "F0PR6_0R1GIN4L": ["originalità", "caratteristiche", "caratteristiche", "tratti", "peculiarità"],
    "F0PR7_54MOD0": ["autosufficiente", "integrale", "significativo", "autosufficiente"],
    "F0PR8_SHED3VR0": ["capolavoro", "invenzione", "creazione", "realizzazione", "creazione", "risultato"],
    "F0PR9_V1SHEDVR": ["alta arte", "grande arte", "grande lavoro", "grande lavoro", "duro lavoro", "duro lavoro", "lavoro responsabile", "buon lavoro", "eccellente lavoro", "degno opera"]}
}

# for item in list_lang['ru']:
#     print(item)
#     print(random.choice(list_lang['ru'][item]))

# F0PR1_OLIC_POCA = ["показатель", "олицетворение", "уровень", "фактор", "величина", "параметр", "важная составляющая"]
# F0PR2_STAT0S = ["статуса", "достатка", "богатства"]
# F0PR3_U5PX = ["успеха", "удачи", "результата", "благополучия", "триумфа", "фурора"]
# F0PR5_4UVSTV0 = ["чувство", "ощущение", "тяга"]
# F0PR4_5TY1E = ["стиля", "образа", "моды", "эстетики", "фасона"]
# F0PR6_0R1GIN4L = ["оригинальности", "особенности", "отличительной", "черты", "своеобразия"]
# F0PR7_54MOD0 = ["самодостаточности", "цельности", "значительности", "самостоятельности"]
# F0PR8_SHED3VR0 = ["шедевр", "изобретение", "создание", "достижение", "творение", "результат"]
# F0PR9_V1SHEDVR = ["высокого искусства", "большого искусства", "высокого дела", "большого дела", "кропотливой работы", "усердной работы", "ответственной работы", "хорошей работы", "безупречной работы", "достойной работы"]
#
# F0PR1_REOLIC_POCA = ["metrik", "Identitätswechsel", "Ebene", "Faktor", "Größe", "Parameter", "wichtige Komponente"]
# F0PR2_RESTAT0S = ["status", "Wohlstand", "Reichtum"]
# F0PR3_REU5PX = ["erfolg", "Glück", "Ergebnis", "Wohlbefinden", "Triumph", "Furore"]
# F0PR5_RE4UVSTV0 = ["gefühl", "Gefühl", "Verlangen"]
# F0PR4_RE5TY1E = ["stil", "Bild", "Mode", "Ästhetik", "Stil"]
# F0PR6_RE0R1GIN4L = ["originalität", "Besonderheiten", "unverwechselbar", "Merkmale", "Eigenheiten"]
# F0PR7_RE54MOD0 = ["Selbständigkeit", "Ganzheit", "Bedeutsamkeit", "Selbstständigkeit"]
# F0PR8_RESHED3VR0 = ["meisterwerk", "Erfindung", "Schöpfung", "Leistung", "Schöpfung", "Ergebnis"]
# F0PR9_REV1SHEDVR = ["hohe Kunst", "große Kunst", "hohe Sache", "große Sache", "mühsame Arbeit", "harte Arbeit", "verantwortungsvolle Arbeit", "gute Arbeit", "tadellose Arbeit", "würdige Arbeit"]
#
# F0PR1_ENOLIC_POCA = ["indicator", "personification", "level", "factor", "magnitude", "parameter", "important component"]
# F0PR2_ENSTAT0S = ["status", "prosperity", "wealth"]
# F0PR3_ENU5PX = ["success", "good luck", "result", "prosperity", "triumph", "furor"]
# F0PR5_EN4UVSTV0 = ["feeling", "feeling", "craving"]
# F0PR4_EN5TY1E = ["style", "image", "fashion", "aesthetics", "style"]
# F0PR6_EN0R1GIN4L = ["originality", "features", "distinctive", "traits", "originality"]
# F0PR7_EN54MOD0 = ["self-sufficiency", "integrity", "significance", "independence"]
# F0PR8_ENSHED3VR0 = ["masterpiece", "invention", "creation", "achievement", "creation", "result"]
# F0PR9_ENV1SHEDVR = ["high art", "great art", "high work", "big work", "hard work", "hard work", "responsible work", "good work", "impeccable work", "decent work"]
#
# F0PR1_PROLIC_POCA = ["indicador", "personificação", "nível", "fator", "valor", "parâmetro", "componente importante"]
# F0PR2_PRSTAT0S = ["status", "prosperidade", "riqueza"]
# F0PR3_PRU5PX = ["sucesso", "boa sorte", "resultado", "bem-estar", "triunfo", "furor"]
# F0PR5_PR4UVSTV0 = ["sentimento", "sensação", "impulso"]
# F0PR4_PR5TY1E = ["estilo", "imagem", "moda", "estética", "estilo"]
# F0PR6_PR0R1GIN4L = ["originalidade", "características", "distintivo", "características", "originalidade"]
# F0PR7_PR54MOD0 = ["auto-suficiência", "integridade", "significância", "independência"]
# F0PR8_PRSHED3VR0 = ["obra-prima", "invenção", "criação", "conquista", "criação", "resultado"]
# F0PR9_PRV1SHEDVR = ["alta arte", "grande arte", "alto trabalho", "ótimo trabalho", "trabalho duro", "trabalho duro", "trabalho responsável", "bom trabalho", "excelente trabalho", "trabalho digno"]
#
# F0PR1_ESOLIC_POCA = ["indicador", "personificación", "nivel", "factor", "valor", "parámetro", "componente importante"]
# F0PR2_ESSTAT0S = ["estado", "prosperidad", "riqueza"]
# F0PR3_ESU5PX = ["éxito", "buena suerte", "resultado", "bienestar", "triunfo", "furor"]
# F0PR5_ES4UVSTV0 = ["sentimiento", "sensación", "empuje"]
# F0PR4_ES5TY1E = ["estilo", "imagen", "moda", "estética", "estilo"]
# F0PR6_ES0R1GIN4L = ["originalidad", "características", "distintivo", "características", "originalidad"]
# F0PR7_ES54MOD0 = ["autosuficiencia", "integridad", "importancia", "independencia"]
# F0PR8_ESSHED3VR0 = ["obra maestra", "invención", "creación", "logro", "creación", "resultado"]
# F0PR9_ESV1SHEDVR = ["gran arte", "gran arte", "gran trabajo", "gran trabajo", "trabajo duro", "trabajo duro", "trabajo responsable", "buen trabajo", "trabajo excelente", "trabajo digno"]
#
# F0PR1_ELOLIC_POCA = ["δείκτης", "προσωποποίηση", "επίπεδο", "παράγοντας", "τιμή", "παράμετρος", "σημαντικό στοιχείο"]
# F0PR2_ELSTAT0S = ["κατάσταση", "ευημερία", "πλούτος"]
# F0PR3_ELU5PX = ["επιτυχία", "καλή τύχη", "αποτέλεσμα", "ευημερία", "θρίαμβος", "μανία"]
# F0PR5_EL4UVSTV0 = ["αίσθημα", "αίσθηση", "ώθηση"]
# F0PR4_EL5TY1E = ["στυλ", "εικόνα", "μόδα", "αισθητική", "στυλ"]
# F0PR6_EL0R1GIN4L = ["πρωτοτυπία", "χαρακτηριστικά", "διακριτικό", "χαρακτηριστικά", "πρωτοτυπία"]
# F0PR7_EL54MOD0 = ["αυταπάρκεια", "ακεραιότητα", "σημασία", "ανεξαρτησία"]
# F0PR8_ELSHED3VR0 = ["αριστούργημα", "εφεύρεση", "δημιουργία", "επίτευγμα", "δημιουργία", "αποτέλεσμα"]
# F0PR9_ELV1SHEDVR = ["υψηλή τέχνη", "μεγάλη τέχνη", "υψηλή δουλειά", "μεγάλη δουλειά", "σκληρή δουλειά", "σκληρή δουλειά", "υπεύθυνη δουλειά", "καλή δουλειά", "εξαιρετική δουλειά", "άξια δουλειά"]
#
# F0PR1_DEOLIC_POCA = ["Indikator", "Personifikation", "Stufe", "Faktor", "Wert", "Parameter", "wichtige Komponente"]
# F0PR2_DESTAT0S = ["Status", "Wohlstand", "Vermögen"]
# F0PR3_DEU5PX = ["Erfolg", "Viel Glück", "Ergebnis", "Wohlfahrt", "Triumph", "Furore"]
# F0PR5_DE4UVSTV0 = ["Gefühl", "Empfindung", "Schub"]
# F0PR4_DE5TY1E = ["Stil", "Bild", "Mode", "Ästhetik", "Stil"]
# F0PR6_DE0R1GIN4L = ["Originalität", "Merkmale", "Unterscheidungsmerkmal", "Merkmale", "Originalität"]
# F0PR7_DE54MOD0 = ["Autarkie", "Integrität", "Bedeutung", "Unabhängigkeit"]
# F0PR8_DESHED3VR0 = ["Meisterwerk", "Erfindung", "Schöpfung", "Leistung", "Schöpfung", "Ergebnis"]
# F0PR9_DEV1SHEDVR = ["hohe Kunst", "großartige Kunst", "hohe Arbeit", "großartige Arbeit", "harte Arbeit", "harte Arbeit", "verantwortungsvolle Arbeit", "gute Arbeit", "ausgezeichnete Arbeit", "würdige Arbeit"]
#
# F0PR1_TROLIC_POCA = ["gösterge", "kişileştirme", "seviye", "faktör", "değer", "parametre", "önemli bileşen"]
# F0PR2_TRSTAT0S = ["statü", "refah", "zenginlik"]
# F0PR3_TRU5PX = ["başarı", "iyi şanslar", "sonuç", "refah", "zafer", "şiddet"]
# F0PR5_TR4UVSTV0 = ["duygu", "his", "itme"]
# F0PR4_TR5TY1E = ["stil", "imaj", "moda", "estetik", "stil"]
# F0PR6_TR0R1GIN4L = ["özgünlük", "özellikler", "ayırt edici", "özellikler", "özgünlük"]
# F0PR7_TR54MOD0 = ["kendi kendine yeterlilik", "dürüstlük", "önem", "bağımsızlık"]
# F0PR8_TRSHED3VR0 = ["şaheser", "buluş", "yaratma", "başarı", "yaratma", "sonuç"]
# F0PR9_TRV1SHEDVR = ["yüksek sanat", "harika sanat", "yüksek iş", "harika iş", "sıkı iş", "sıkı iş", "sorumlu iş", "iyi iş", "mükemmel iş", "değerli iş"]
#
# F0PR1_PLOLIC_POCA = ["miara", "podszywanie się", "poziom", "współczynnik", "wielkość", "parametr", "ważny składnik"]
# F0PR2_PLSTAT0S = ["status", "bogactwo", "bogactwo"]
# F0PR3_PLU5PX = ["sukces", "szczęście", "wynik", "dobrobyt", "triumf", "wrzawa"]
# F0PR5_PL4UVSTV0 = ["uczucie", "uczucie", "pociągnięcie"]
# F0PR4_PL5TY1E = ["styl", "wygląd", "moda", "estetyka", "styl"]
# F0PR6_PL0R1GIN4L = ["oryginalność", "cechy", "wyróżniające się", "cechy", "osobliwości"]
# F0PR7_PL54MOD0 = ["samowystarczalny", "integralny", "znaczący", "samowystarczalny"]
# F0PR8_PLSHED3VR0 = ["arcydzieło", "wynalazek", "stworzenie", "osiągnięcie", "stworzenie", "wynik"]
# F0PR9_PLV1SHEDVR = ["wysoka sztuka", "wielka sztuka", "wysoka praca", "świetna praca", "ciężka praca", "ciężka praca", "odpowiedzialna praca", "dobra robota", "doskonała praca", "godny praca"]
#
# F0PR1_ITOLIC_POCA = ["misura", "rappresentazione", "livello", "fattore", "magnitudo", "parametro", "componente importante"]
# F0PR2_ITSTAT0S = ["stato", "ricchezza", "ricchezza"]
# F0PR3_ITU5PX = ["successo", "fortuna", "risultato", "prosperità", "trionfo", "furore"]
# F0PR5_IT4UVSTV0 = ["sensazione", "sensazione", "tira"]
# F0PR4_IT5TY1E = ["stile", "look", "moda", "estetica", "stile"]
# F0PR6_IT0R1GIN4L = ["originalità", "caratteristiche", "caratteristiche", "tratti", "peculiarità"]
# F0PR7_IT54MOD0 = ["autosufficiente", "integrale", "significativo", "autosufficiente"]
# F0PR8_ITSHED3VR0 = ["capolavoro", "invenzione", "creazione", "realizzazione", "creazione", "risultato"]
# F0PR9_ITV1SHEDVR = ["alta arte", "grande arte", "grande lavoro", "grande lavoro", "duro lavoro", "duro lavoro", "lavoro responsabile", "buon lavoro", "eccellente lavoro", "degno opera"]
#




# F0PR1_OLIC_POCA = ["показатель", "олицетворение", "уровень", "фактор", "величина", "параметр", "важная составляющая"]
# F0PR1_REOLIC_POCA = ["metrik", "Identitätswechsel", "Ebene", "Faktor", "Größe", "Parameter", "wichtige Komponente"]
# F0PR1_ENOLIC_POCA = ["indicator", "personification", "level", "factor", "magnitude", "parameter", "important component"]
# F0PR1_PROLIC_POCA = ["indicador", "personificação", "nível", "fator", "valor", "parâmetro", "componente importante"]
# F0PR1_ESOLIC_POCA = ["indicador", "personificación", "nivel", "factor", "valor", "parámetro", "componente importante"]
# F0PR1_ELOLIC_POCA = ["δείκτης", "προσωποποίηση", "επίπεδο", "παράγοντας", "τιμή", "παράμετρος", "σημαντικό στοιχείο"]
# F0PR1_DEOLIC_POCA = ["Indikator", "Personifikation", "Stufe", "Faktor", "Wert", "Parameter", "wichtige Komponente"]
# F0PR1_TROLIC_POCA = ["gösterge", "kişileştirme", "seviye", "faktör", "değer", "parametre", "önemli bileşen"]
#
# F0PR2_STAT0S = ["статуса", "достатка", "богатства"]
# F0PR2_RESTAT0S = ["status", "Wohlstand", "Reichtum"]
# F0PR2_ENSTAT0S = ["status", "prosperity", "wealth"]
# F0PR2_PRSTAT0S = ["status", "prosperidade", "riqueza"]
# F0PR2_ESSTAT0S = ["estado", "prosperidad", "riqueza"]
# F0PR2_ELSTAT0S = ["κατάσταση", "ευημερία", "πλούτος"]
# F0PR2_DESTAT0S = ["Status", "Wohlstand", "Vermögen"]
# F0PR2_TRSTAT0S = ["statü", "refah", "zenginlik"]
#
# F0PR3_U5PX = ["успеха", "удачи", "результата", "благополучия", "триумфа", "фурора"]
# F0PR3_REU5PX = ["erfolg", "Glück", "Ergebnis", "Wohlbefinden", "Triumph", "Furore"]
# F0PR3_ENU5PX = ["success", "good luck", "result", "prosperity", "triumph", "furor"]
# F0PR3_PRU5PX = ["sucesso", "boa sorte", "resultado", "bem-estar", "triunfo", "furor"]
# F0PR3_ESU5PX = ["éxito", "buena suerte", "resultado", "bienestar", "triunfo", "furor"]
# F0PR3_ELU5PX = ["επιτυχία", "καλή τύχη", "αποτέλεσμα", "ευημερία", "θρίαμβος", "μανία"]
# F0PR3_DEU5PX = ["Erfolg", "Viel Glück", "Ergebnis", "Wohlfahrt", "Triumph", "Furore"]
# F0PR3_TRU5PX = ["başarı", "iyi şanslar", "sonuç", "refah", "zafer", "şiddet"]
#
# F0PR5_4UVSTV0 = ["чувство", "ощущение", "тяга"]
# F0PR5_RE4UVSTV0 = ["gefühl", "Gefühl", "Verlangen"]
# F0PR5_EN4UVSTV0 = ["feeling", "feeling", "craving"]
# F0PR5_PR4UVSTV0 = ["sentimento", "sensação", "impulso"]
# F0PR5_ES4UVSTV0 = ["sentimiento", "sensación", "empuje"]
# F0PR5_EL4UVSTV0 = ["αίσθημα", "αίσθηση", "ώθηση"]
# F0PR5_DE4UVSTV0 = ["Gefühl", "Empfindung", "Schub"]
# F0PR5_TR4UVSTV0 = ["duygu", "his", "itme"]
#
# F0PR4_5TY1E = ["стиля", "образа", "моды", "эстетики", "фасона"]
# F0PR4_RE5TY1E = ["stil", "Bild", "Mode", "Ästhetik", "Stil"]
# F0PR4_EN5TY1E = ["style", "image", "fashion", "aesthetics", "style"]
# F0PR4_PR5TY1E = ["estilo", "imagem", "moda", "estética", "estilo"]
# F0PR4_ES5TY1E = ["estilo", "imagen", "moda", "estética", "estilo"]
# F0PR4_EL5TY1E = ["στυλ", "εικόνα", "μόδα", "αισθητική", "στυλ"]
# F0PR4_DE5TY1E = ["Stil", "Bild", "Mode", "Ästhetik", "Stil"]
# F0PR4_TR5TY1E = ["stil", "imaj", "moda", "estetik", "stil"]
#
# F0PR6_0R1GIN4L = ["оригинальности", "особенности", "отличительной", "черты", "своеобразия"]
# F0PR6_RE0R1GIN4L = ["originalität", "Besonderheiten", "unverwechselbar", "Merkmale", "Eigenheiten"]
# F0PR6_EN0R1GIN4L = ["originality", "features", "distinctive", "traits", "originality"]
# F0PR6_PR0R1GIN4L = ["originalidade", "características", "distintivo", "características", "originalidade"]
# F0PR6_ES0R1GIN4L = ["originalidad", "características", "distintivo", "características", "originalidad"]
# F0PR6_EL0R1GIN4L = ["πρωτοτυπία", "χαρακτηριστικά", "διακριτικό", "χαρακτηριστικά", "πρωτοτυπία"]
# F0PR6_DE0R1GIN4L = ["Originalität", "Merkmale", "Unterscheidungsmerkmal", "Merkmale", "Originalität"]
# F0PR6_TR0R1GIN4L = ["özgünlük", "özellikler", "ayırt edici", "özellikler", "özgünlük"]
#
# F0PR7_54MOD0 = ["самодостаточности", "цельности", "значительности", "самостоятельности"]
# F0PR7_RE54MOD0 = ["Selbständigkeit", "Ganzheit", "Bedeutsamkeit", "Selbstständigkeit"]
# F0PR7_EN54MOD0 = ["self-sufficiency", "integrity", "significance", "independence"]
# F0PR7_PR54MOD0 = ["auto-suficiência", "integridade", "significância", "independência"]
# F0PR7_ES54MOD0 = ["autosuficiencia", "integridad", "importancia", "independencia"]
# F0PR7_EL54MOD0 = ["αυταπάρκεια", "ακεραιότητα", "σημασία", "ανεξαρτησία"]
# F0PR7_DE54MOD0 = ["Autarkie", "Integrität", "Bedeutung", "Unabhängigkeit"]
# F0PR7_TR54MOD0 = ["kendi kendine yeterlilik", "dürüstlük", "önem", "bağımsızlık"]
#
# F0PR8_SHED3VR0 = ["шедевр", "изобретение", "создание", "достижение", "творение", "результат"]
# F0PR8_RESHED3VR0 = ["meisterwerk", "Erfindung", "Schöpfung", "Leistung", "Schöpfung", "Ergebnis"]
# F0PR8_ENSHED3VR0 = ["masterpiece", "invention", "creation", "achievement", "creation", "result"]
# F0PR8_PRSHED3VR0 = ["obra-prima", "invenção", "criação", "conquista", "criação", "resultado"]
# F0PR8_ESSHED3VR0 = ["obra maestra", "invención", "creación", "logro", "creación", "resultado"]
# F0PR8_ELSHED3VR0 = ["αριστούργημα", "εφεύρεση", "δημιουργία", "επίτευγμα", "δημιουργία", "αποτέλεσμα"]
# F0PR8_DESHED3VR0 = ["Meisterwerk", "Erfindung", "Schöpfung", "Leistung", "Schöpfung", "Ergebnis"]
# F0PR8_TRSHED3VR0 = ["şaheser", "buluş", "yaratma", "başarı", "yaratma", "sonuç"]
#
# F0PR9_V1SHEDVR = ["высокого искусства", "большого искусства", "высокого дела", "большого дела", "кропотливой работы", "усердной работы", "ответственной работы", "хорошей работы", "безупречной работы", "достойной работы"]
# F0PR9_REV1SHEDVR = ["hohe Kunst", "große Kunst", "hohe Sache", "große Sache", "mühsame Arbeit", "harte Arbeit", "verantwortungsvolle Arbeit", "gute Arbeit", "tadellose Arbeit", "würdige Arbeit"]
# F0PR9_ENV1SHEDVR = ["high art", "great art", "high work", "big work", "hard work", "hard work", "responsible work", "good work", "impeccable work", "decent work"]
# F0PR9_PRV1SHEDVR = ["alta arte", "grande arte", "alto trabalho", "ótimo trabalho", "trabalho duro", "trabalho duro", "trabalho responsável", "bom trabalho", "excelente trabalho", "trabalho digno"]
# F0PR9_ESV1SHEDVR = ["gran arte", "gran arte", "gran trabajo", "gran trabajo", "trabajo duro", "trabajo duro", "trabajo responsable", "buen trabajo", "trabajo excelente", "trabajo digno"]
# F0PR9_ELV1SHEDVR = ["υψηλή τέχνη", "μεγάλη τέχνη", "υψηλή δουλειά", "μεγάλη δουλειά", "σκληρή δουλειά", "σκληρή δουλειά", "υπεύθυνη δουλειά", "καλή δουλειά", "εξαιρετική δουλειά", "άξια δουλειά"]
# F0PR9_DEV1SHEDVR = ["hohe Kunst", "großartige Kunst", "hohe Arbeit", "großartige Arbeit", "harte Arbeit", "harte Arbeit", "verantwortungsvolle Arbeit", "gute Arbeit", "ausgezeichnete Arbeit", "würdige Arbeit"]
# F0PR9_TRV1SHEDVR = ["yüksek sanat", "harika sanat", "yüksek iş", "harika iş", "sıkı iş", "sıkı iş", "sorumlu iş", "iyi iş", "mükemmel iş", "değerli iş"]

# ListENPrilog = [
# "Our"
# ]

# ListPrilog = [
# "Наш"
# "Веселый",
# "Захватывающий",
# "великолепный",
# "звездный",
# "отличный",
# "поразительнй",
# "благоприятный",
# "Впечатляющий",
# "замечательный",
# "Примечательный",
# "оптимистичный",
# "идеальный",
# "Постоянный",
# "драгоценный",
# "благоприятный",
# "выдающийся",
# "Супер",
# "уникальный",
# "отважный",
# "удивительный",
# "Великолепный",
# "Элегантный",
# "прекрасный",
# "блестящий",
# "великолепный",
# "аккуратный",
# "Великолепный",
# "Яркий",
# "прекрасный",
# "творческий",
# "полезный"
# ]
pwords_title = [
"бюстгальтер",
"сексуальное",
"нижнее белье",
"эротический",
"кружева",
"белья",
"Стринги",
"ужас",
"тапочки",
"тапки",
"сланцы",
"сланци",
"череп",
"сумка",
"игрушки",
"игрушка",
"секс",
"вибратор",
"фаллоимитатор",
"анальный",
"клитор",
"стимулятор",
"вибрационное",
"детей",
"детская",
"мальчиков",
"мальчик",
"девочка",
"ребенка",
"ребёнка",
"фаршированные",
"фаршированный",
"фаршированное",
"3 в 1",
"детский",
"детские",
"чучело",
"сирена",
"хаги",
"дети",
"убийство",
"убить",
"смерть",
"умереть",
"нарушение безопасности",
"фанкин",
"тушь",
"кукла",
"куклу",
"куклы",
"питомец",
"малыш",
"радио",
"10inch",
"уитти",
"ужасы",
"huggy",
"wuggy",
"страшные",
"кроссовки",
"ботинки",
"обувь",
"майка",
"fnaf"
]
ListNames = [
"Август",
"Августин",
"Авраам",
"Аврора",
"Агата",
"Агафон",
"Агнесса",
"Агния",
"Ада",
"Аделаида",
"Аделина",
"Адонис",
"Акайо",
"Акулина",
"Алан",
"Алевтина",
"Александр",
"Александра",
"Алексей",
"Алена",
"Алина",
"Алиса",
"Алла",
"Алсу",
"Альберт",
"Альбина",
"Альфия",
"Альфред",
"Амалия",
"Амелия",
"Анастасий",
"Анастасия",
"Анатолий",
"Ангелина",
"Андрей",
"Анжела",
"Анжелика",
"Анисий",
"Анна",
"Антон",
"Антонина",
"Анфиса",
"Аполлинарий",
"Аполлон",
"Ариадна",
"Арина",
"Аристарх",
"Аркадий",
"Арсен",
"Арсений",
"Артем",
"Артемий",
"Артур",
"Архип",
"Ася",
"Беатрис",
"Белла",
"Бенедикт",
"Берта",
"Богдан",
"Божена",
"Болеслав",
"Борис",
"Борислав",
"Бронислав",
"Бронислава",
"Булат",
"Вадим",
"Валентин",
"Валентина",
"Валерий",
"Валерия",
"Ванда",
"Варвара",
"Василий",
"Василиса",
"Венера",
"Вениамин",
"Вера",
"Вероника",
"Викентий",
"Виктор",
"Виктория",
"Вилен",
"Виолетта",
"Виссарион",
"Вита",
"Виталий",
"Влад",
"Владимир",
"Владислав",
"Владислава",
"Владлен",
"Вольдемар",
"Всеволод",
"Вячеслав",
"Габриэлла",
"Гавриил",
"Галина",
"Гарри",
"Гелла",
"Геннадий",
"Генриетта",
"Георгий",
"Герман",
"Гертруда",
"Глафира",
"Глеб",
"Глория",
"Гордей",
"Грейс",
"Грета",
"Григорий",
"Гульмира",
"Давид",
"Дана",
"Даниил",
"Даниэла",
"Дарина",
"Дарья",
"Даяна",
"Демьян",
"Денис",
"Джеймс",
"Джек",
"Джессика",
"Джозеф",
"Диана",
"Дина",
"Динара",
"Дмитрий",
"Добрыня",
"Доминика",
"Дора",
"Ева",
"Евгений",
"Евгения",
"Евдоким",
"Евдокия",
"Егор",
"Екатерина",
"Елена",
"Елизавета",
"Елисей",
"Есения",
"Ефим",
"Ефрем",
"Ефросинья",
"Жаклин",
"Жанна",
"Ждан",
"Захар",
"Зинаида",
"Зиновий",
"Злата",
"Зорий",
"Зоряна",
"Зоя",
"Иван",
"Иветта",
"Игнатий",
"Игорь",
"Изабелла",
"Изольда",
"Илга",
"Илларион",
"Илона",
"Илья",
"Инга",
"Инесса",
"Инна",
"Иннокентий",
"Иосиф",
"Ираида",
"Ираклий",
"Ирина",
"Итан",
"Ия",
"Казимир",
"Калерия",
"Камилла",
"Камиль",
"Капитолина",
"Карина",
"Каролина",
"Касьян",
"Ким",
"Кир",
"Кира",
"Кирилл",
"Клавдия",
"Клара",
"Клариса",
"Клим",
"Климент",
"Кондрат",
"Константин",
"Кристина",
"Ксения",
"Кузьма",
"Лада",
"Лариса",
"Лев",
"Леон",
"Леонид",
"Леонтий",
"Леся",
"Лидия",
"Лика",
"Лилиана",
"Лилия",
"Лина",
"Лолита",
"Луиза",
"Лукьян",
"Любовь",
"Людмила",
"Магдалина",
"Майя",
"Макар",
"Максим",
"Марат",
"Маргарита",
"Марианна",
"Марина",
"Мария",
"Марк",
"Марта",
"Мартин",
"Марфа",
"Матвей",
"Мелания",
"Мелисса",
"Милана",
"Милена",
"Мирон",
"Мирослава",
"Мирра",
"Митрофан",
"Михаил",
"Мия",
"Модест",
"Моисей",
"Мухаммед",
"Надежда",
"Назар",
"Наоми",
"Наталия",
"Наталья",
"Наум",
"Нелли",
"Ника",
"Никанор",
"Никита",
"Никифор",
"Николай",
"Николь",
"Никон",
"Нина",
"Нинель",
"Нонна",
"Нора",
"Оксана",
"Олег",
"Олеся",
"Оливер",
"Оливия",
"Ольга",
"Оскар",
"Павел",
"Парамон",
"Патрик",
"Паула",
"Петр",
"Платон",
"Полина",
"Прасковья",
"Прохор",
"Рада",
"Радмила",
"Раиса",
"Райан",
"Раймонд",
"Раяна",
"Регина",
"Ренат",
"Рената",
"Рику",
"Римма",
"Ринат",
"Рита",
"Роберт",
"Родион",
"Роза",
"Роксана",
"Роман",
"Россияна",
"Ростислав",
"Руслан",
"Рустам",
"Рэн",
"Сабина",
"Савва",
"Савелий",
"Саки",
"Сакура",
"Самсон",
"Самуил",
"Сарра",
"Светлана",
"Святослав",
"Севастьян",
"Семен",
"Серафима",
"Сергей",
"Сильвия",
"Снежана",
"Сора",
"София",
"Софья",
"Станислав",
"Стелла",
"Степан",
"Стефания",
"Таисия",
"Такеши",
"Тамара",
"Тамила",
"Тарас",
"Татьяна",
"Теодор",
"Тереза",
"Терентий",
"Тимофей",
"Тимур",
"Тина",
"Тихон",
"Томас",
"Трофим",
"Ульяна",
"Урсула",
"Фаддей",
"Фаина",
"Федор",
"Федот",
"Феликс",
"Филат",
"Филимон",
"Филипп",
"Фома",
"Фрида",
"Хина",
"Хлоя",
"Чарли",
"Шарлотта",
"Шейла",
"Шелли",
"Эдгар",
"Эдита",
"Эдуард",
"Элеонора",
"Элина",
"Элла",
"Эльвира",
"Эльдар",
"Эльза",
"Эмили",
"Эмилия",
"Эмма",
"Эрик",
"Эрика",
"Юи",
"Юлиан",
"Юлиана",
"Юлий",
"Юлия",
"Юма",
"Юна",
"Юрий",
"Яков",
"Ямато",
"Ян",
"Яна",
"Янина",
"Ярослав"
]

pwors = [
"подарочные",
"ПОДАРОЧНЫЕ",
"Подарочные",
"стерлинговое",
"СТЕРЛИНГОВОЕ",
"Стерлинговое",
"стерлингового",
"СТЕРЛИНГОВОГО",
"Стерлингового",
"стерлинги",
"СТЕРЛИНГИ",
"Стерлинги",
"шт",
"ШТ",
"Шт",
"подарков",
"ПОДАРКОВ",
"Подарков",
"симулятор",
"СИМУЛЯТОР",
"Симулятор",
"симуляторы",
"СИМУЛЯТОРЫ",
"Симуляторы",
"болтания",
"БОЛТАНИЯ",
"Болтания",
"болтание",
"БОЛТАНИЕ",
"Болтание",
"вечеринки",
"ВЕЧЕРИНКИ",
"Вечеринки",
"вечеринка",
"ВЕЧЕРИНКА",
"Вечеринка",
"подарка",
"ПОДАРКА",
"Подарка",
"для",
"ДЛЯ",
"Для",
"нерегулярный",
"НЕРЕГУЛЯРНЫЙ",
"Нерегулярный",
"нерегулярные",
"НЕРЕГУЛЯРНЫЕ",
"Нерегулярные",
"нерегулярная",
"НЕРЕГУЛЯРНАЯ",
"Нерегулярная",
"цирконий",
"ЦИРКОНИЙ",
"Цирконий",
"цирконный",
"ЦИРКОННЫЙ",
"Цирконный",
"циркона",
"ЦИРКОНА",
"Циркона",
"циркон",
"ЦИРКОН",
"Циркон",
"пробы",
"ПРОБЫ",
"Пробы",
"проба",
"ПРОБА",
"Проба",
"унисекс",
"УНИСЕКС",
"Унисекс",
"кастет",
"КАСТЕТ",
"Кастет",
"удача",
"Удача",
"УДАЧА",
"очарование",
"Очарование",
"ОЧАРОВАНИЕ",
"очарования",
"Очарования",
"ОЧАРОВАНИЯ",
"пробы",
"Пробы",
"ПРОБЫ",
"акции",
"Акции",
"АКЦИИ",
"скидки",
"Скидки",
"СКИДКИ",
"подарки",
"Подарки",
"ПОДАРКИ",
"подарок",
"Подарок",
"ПОДАРОК",
"акция",
"Акция",
"АКЦИЯ",
"скидка",
"Скидка",
"СКИДКА",
"выигрыш",
"Выигрыш",
"ВЫИГРЫШ",
"секс",
"Секс",
"СЕКС",
"алкоголь",
"Алкоголь",
"АЛКОГОЛЬ",
"наркотики",
"Наркотики",
"НАРКОТИКИ",
"интим",
"Интим",
"ИНТИМ",
"бесплатно",
"Бесплатно",
"БЕСПЛАТНО",
"бесплатная",
"Бесплатная",
"БЕСПЛАТНАЯ",
"амулеты",
"Амулеты",
"АМУЛЕТЫ",
"ТАЛИСМАНЫ",
"Талисманы",
"талисманы",
"ТАЛИСМАН",
"Талисман",
"талисман",
"амулет",
"Амулет",
"АМУЛЕТ",
"прибыльная",
"Прибыльная",
"ПРИБЫЛЬНАЯ",
"прибыль",
"Прибыль",
"ПРИБЫЛЬ",
"деньги",
"Деньги",
"ДЕНЬГИ",
]