### Chinese Vocabulary Finder
This library is designed to help you bridge the gap between textbooks and real world text. Call `process_text` on a string and it will print a list of words that you haven't seen before. It will also save these words for next time. Words can be found in `known_words.txt`, and you can add words from your textbook or flashcards, at one word per line. Dictionary definitions come form the open-source `CEDICT` dictionary.

## Requirements
You will need to install Jieba to split the text into individual words.

## Example

```
process_text("""中華人民共和國，通稱中國，是一個位於東亞的社會主義國家，首都位於北京。1949年中國共產黨在內戰中勝利，推翻了中國國民黨執政的中華民國政府，於1949年10月1日在北京建立了中華人民共和國中央人民政府。中華人民共和國實行人民代表大會制度及中國共產黨領導的多黨合作和政治協商制度。中華人民共和國政府是中央政府和地方政府的總稱，各級地方政府接受中央政府（國務院）統一領導。根據「一國兩制」政策，香港、澳門回歸後保留資本主義制度，而中國內地則實行中國特色社會主義制度。全國人民代表大會授權香港、澳門特別行政區實行高度自治，特區行政長官由國務院任命。
中華人民共和國陸地總面積約960萬平方公里，依計算方法不同，可以是世界陸地總面積第三或者第四大的國家。中國省級行政區劃為4個直轄市、23個省、5個自治區和2個特別行政區，其中臺灣地區、西藏自治區的藏南地區和三沙市的部分南沙島礁未實際管轄。中國地域廣闊，地形多樣，北方有森林、草原、戈壁和乾旱的塔克拉瑪干沙漠，南方則有濕潤的亞熱帶雨林。喜馬拉雅山脈、喀喇崑崙山脈、帕米爾高原和天山山脈將中國同南亞、中亞分開。發源自青藏高原的兩條河流——長江、黃河分別為世界第三長、第六長河流。中國領海由渤海（內海）和黃海、東海、南海三大邊海組成，東部和南部大陸海岸線長1.8萬千米。內海和邊海的水域面積約470萬平方千米。海域分布有大小島嶼7600個，其中面積最大的台灣島達35798平方千米，第二大島為海南島。
中華人民共和國人口約13.6億人，約佔全球人口的1/5，是世界上人口最多的國家。中國同時是多民族國家，官方稱共有56個民族世居，合稱為中華民族，另一方面，中國社會對移民政策普遍比較保守，並不視為移民國家。其中漢族佔91.51%。中華人民共和國沒有明確規定國家語言，但以漢語普通話和規範漢字為國家通用語言文字，各地方並設有民族的官方語言文字。
中華人民共和國經濟自1979年改革開放以來快速發展，逐漸成為一個工業化國家，目前是世界上經濟增長最快的經濟體之一，是世界第二大經濟體、第一大工業國、第一大農業國、第二大服務業國、第一大製造業國、第一大貨物貿易國（第一大出口國和第二大進口國）、第三大服務貿易國、第一大吸引外資國、第三大對外投資國，擁有最多的外匯儲備和世界第五大官方黃金儲備，政府預算（包括預算收入和預算支出）居世界第二。中華人民共和國擁有眾多的世界文化與自然遺產，根據世界旅遊組織 (UNWTO)在其世界旅遊指南中的數據顯示，2014年的中國是世界第三大旅遊目的地國和世界第一大出境客源國。
1971年，中華人民共和國取代中華民國在聯合國的「中國」席次，成為聯合國安理會常任理事國。目前，中國大陸是眾多正式和非正式的多邊國際組織的成員，包括世界貿易組織、亞太經合組織、金磚五國、上海合作組織、孟中印緬區域合作論壇和20國集團等，被視為潛在超級大國之一。
中華人民共和國教育是由中華人民共和國教育部主管的教育事業。自1986年推行九年義務教育。教育階段分幼兒園、小學、初中、高中和大學。中國有數目眾多的大學，大學生數量世界第一。一些大學開辦研究生教育，有博士點。近年來，中國已建立起數所在海內外享有一定聲譽的大學，如清華大學、北京大學、北京理工大學、香港大學、上海交通大學和南京大學等。
中華人民共和國科技水平近年有了長足進步，研究開發經費投入總量目前位居世界第二。在航天領域具備獨立生產、發射、運營人造地球衛星、月球和深空探測器、載人太空飛行器和太空站以及衛星導航系統的能力。中華人民共和國國防預算世界排名第二，擁有人數最多的正規軍，由中央軍事委員會指揮，中央軍委主席是中華人民共和國武裝力量的最高統帥。中華人民共和國是世界公認的擁核國，擁有戰略核武器洲際投送（洲際彈道飛彈、戰略核潛艇和戰略轟炸機等遠程載具）和二次核打擊能力，陸基中段反彈道飛彈和反衛星作戰能力，航空母艦和反航母作戰能力。中國正在進行多型號第五代戰鬥機的研製工作，並已開始進行高超音速飛行器試驗和第六代戰鬥機的預研。""")
```
