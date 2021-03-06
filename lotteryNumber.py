########### ����ũ�Ѹ� ############

# ���̺귯�� �ҷ�����(requests for html)
import requests 

lotto_url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'

# �������� html�ڵ� ��ü �޾ƿ���
# value = requests.get(url)
raw = requests.get(lotto_url)

# <response [200]> ������ ������
print(raw)

# raw������ ���� text�������� ���(���ڿ�, ������ ���� X)
print(raw.text)

# ���̺귯�� �ҷ�����(beautifulsoup4 for html searching)
from bs4 import BeautifulSoup

# html ���ڿ� �ڵ� �����ڿ� �±� ����
# Beautifulsoup(���ڿ�, 'html.parser')
soup = BeautifulSoup(raw.text, 'html.parser')
print(soup)

print(type(raw.text)) #str
print(type(soup)) #bs4.BeautifulSoup

# �����Լ� find
# ã�� ���� �ϳ��� �������� ���� ��
# (html�ڵ�).find('div')
# (html�ڵ�).find(id = 'example1')
# (html�ڵ�).find(attrs = {'id':'example1'})
# (html�ڵ�).find('div', {'id':'example1'})
# ��÷ ��ȣ�� ��� �����ϴ� ���� ���� ũ���� �±׸� ��������
box = soup.find('div', {'class':'nums'})

# �����Լ� find_all
# �ش� �±��� ��� html �ڵ� ��ü�� ����Ʈ ���·� ��ȯ
# (html�ڵ�).find_all('div')
# (html�ڵ�).find_all(id = 'example')
# (html�ڵ�).find_all(['div','span'])
# (html�ڵ�).find_all(attrs = {'id':'example1','class':'example2'})
# ������ �±׿��� ��÷ ��ȣ�� ����
numbers = box.find_all('span')
print('<�ֱ� �ζ� ��÷ ��ȣ>')
for number in numbers:
    print(number.text)