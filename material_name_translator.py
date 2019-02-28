import pickle
from googletrans import Translator


with open("recipes.pkl","rb") as pkl:
    recipes_list = pickle.load(pkl)


translator = Translator()
def translate_ch_to_en(material_name):
    return translator.translate(material_name).text


err_list = []
for recipe_num, recipe in enumerate(recipes_list[:100]):
    for material_num, material in enumerate(recipe["materials"]):
        ch = material.get("material_name")
        try:
            en = translate_ch_to_en(ch)
        except:
            err_msg = (recipe_num, material_num, ch)
            err_list.append(err_msg)

        material["material_name_en"] = en

# pickle a variable to a file
file = open('translated_recipes.pkl', 'wb')
pickle.dump(recipes_list, file)
file.close()

file = open('failed_translation.pkl', 'wb')
pickle.dump(err_list, file)
file.close()