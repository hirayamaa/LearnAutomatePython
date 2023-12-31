import openpyxl
import pprint

print('ワークブックを開いています...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

print('行を読み込んでいます')
for row in range(2, sheet.max_row + 1):
    # スプレッドシートの1行に1つの人口調査標準地域のデータがある
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # この州のキーが確実に存在するようにする(キーが存在すれば何もしない)
    county_data.setdefault(state, {})
    # この州のこの郡のキーが確実に存在するようにする(キーが存在すれば何もしない)
    county_data[state].setdefault(county, {'tracks': 0, 'pop': 0})

    # 各行が人口調査標準地域を表すので、数を1つ増やす
    county_data[state][county]['tracks'] += 1
    # この人口調査標準地域の人口だけ郡の人口を増やす
    county_data[state][county]['pop'] += int(pop)

# 新しいテキストファイルを開き、county_dataの内容を書き込む
print('結果を書き込み中...')
# pythonの辞書型データとして書き込む
result_file = open('census2010.py', 'w')
result_file.write('all_data = ' + pprint.pformat(county_data))
result_file.close()
print('完了')

