from translate import Translator

translator = Translator(to_lang="zh")
translation = translator.translate("Good Morning!")
print("1 -", translation)


langs = ["zh", "de", "ko", "el", "ar", "bn"]

# now we can try using a for loop

for lang in langs:
	translator = Translator(to_lang=lang)
	translation = translator.translate("Good Morning!")
	print(lang, "-", translation)
