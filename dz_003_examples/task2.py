# Завдання 2
# Створіть XML-файл із вкладеними елементами та скористайтеся мовою пошуку XPATH.
# Спробуйте здійснити пошук вмісту за створеним документом XML,
# ускладнюючи свої запити та додаючи нові елементи, якщо буде потрібно.
import xml.etree.ElementTree as ET

xml_data = '''<materials>
    <material>
        <name>Steel</name>
        <weight>500</weight>
        <height>200</height>
    </material>
    <material>
        <name>Wood</name>
        <weight>100</weight>
        <height>150</height>
    </material>
</materials>'''

with open('materials.xml', 'w') as file:
    file.write(xml_data)

tree = ET.parse('materials.xml')
root = tree.getroot()

for material in root.findall('.//material'):
    name = material.find('name').text
    weight = material.find('weight').text
    print(f'Material: {name}, Weight: {weight}')
