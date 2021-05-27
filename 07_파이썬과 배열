# 1. 자료구조 이론
# 07. 파이썬과 배열 
'''
country = "US"
print(country)
country = country + "KO"
print(country)

#1차원
data = [1,2,3,4,5]
print(data)

#2차원
data = [[1,2,3], [4,5,6], [7,8,9]]
print(data)
print(data[0][0])

#연습1 : 위의 2차원 배열에서 9, 8, 7 순서로 출력해보기
print(data[2][2], data[2][1], data[2][0])
'''
#연습2 : 다음 dataset에서 전체 이름 안에 M이 몇번 나왔는지 빈도수 출력하기
dataset = ['Braund, Mr. Owen Harris',
  'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
  'Heikkinen, Miss. Laina',
  'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
  'Allen, Mr. William Henry',
  'Moran, Mr. James',
  'McCarthy, Mr. Timothy J',
  'Palsson, Master. Gosta Leonard',
  'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
  'Nasser, Mrs. Nicholas (Adele Achem)',
  'Sandstrom, Miss. Marguerite Rut',
  'Bonnell, Miss. Elizabeth',
  'Saundercock, Mr. William Henry',
  'Andersson, Mr. Anders Johan',
  'Vestrom, Miss. Hulda Amanda Adolfina',
  'Hewlett, Mrs. (Mary D Kingcome) ',
  'Rice, Master. Eugene',
  'Williams, Mr. Charles Eugene',
  'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
  'Masselmani, Mrs. Fatima',
  'Fynney, Mr. Joseph J',
  'Beesley, Mr. Lawrence',
  'McGowan, Miss. Anna \"Annie\"',
  'Sloper, Mr. William Thompson',
  'Palsson, Miss. Torborg Danira',
  'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
  'Emir, Mr. Farred Chehab',
  'Fortune, Mr. Charles Alexander',
  'Dwyer, Miss. Ellen \"Nellie\"',
  'Todoroff, Mr. Lalio']

m_count = 0
# 내답
for i in range(0, len(dataset)) :
  
  if 'M' in dataset[i]:
    m_count+=1
  
print(m_count)

#모범답안
m_count1 = 0
for data in dataset: # 리스트 반복문 이런 형태로 뽑아 올 수 있음 !!
  for i in range(len(data)):
    if data[i] =='M':
      m_count1 += 1
print(m_count1)

#In Java
'''
int m_count = 0;
		
		for(int i=0; i<dataset.length; i++) {
			for(int j=0; j<dataset[i].length(); j++) {
				if(dataset[i].charAt(j) == 'M') {
					//System.out.println(dataset[i]);
					m_count++;
				}
			}
		}
		System.out.println(m_count);
  '''
