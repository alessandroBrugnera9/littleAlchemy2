from bs4 import BeautifulSoup
from requests import get
import auxi
import json


url="https://littlealchemy2.gambledude.com/"
classItem="c-element-list__item"
tableCombo="o-table o-table--tiny c-combo-list"

combinations={}

response = get(url)

soup = BeautifulSoup(response.text, 'html.parser')

elements = soup.find_all("li", {"class": classItem, "data-val": "1"})
contador=0
for ingredientLi in elements:
    firstIngredient=ingredientLi.a.text
    print(contador,firstIngredient)
    contador=contador+1
    url=ingredientLi.a["href"]
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all("table", {"class": tableCombo})
    recipes={}
    if len(table)>0:
        for tableRow in table[0].tbody:
            ingredientCombo = tableRow.find_all("a")
            secondIngredient = ingredientCombo[0].text
            comboResult = [x.text for x in ingredientCombo[1:] if True]
            recipes[secondIngredient]=comboResult
    combinations[firstIngredient]=recipes

auxi.saveObj(combinations, auxi.COMBINATIONS)