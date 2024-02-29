import hashlib
hash = hashlib.sha256()
members = []
posts = []




class Member():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        hash.update(password.encode('utf-8'))
        self.password = hash.hexdigest()
        #print(self.password)
        members.append(name)

    def Display(self):
        print(f'성명 : {self.name}')
        print(f'ID : {self.username}')


class Post():
    def __init__(self, title, content, username):
        self.title = title
        self.content = content
        self.author = username
        new_dict = {
            'title': title,
            'content': content,
            'author': username
        }
        posts.append(new_dict)


Member('박강균', 'pkg0203', '123456')
Member('서지원', 'Seo', '456456')
Member('박정원', 'Park0505', '456456')

for user in members:
    print(user)

Post('1', '졸업했다', 'pkg0203')
Post('123', '부트캠프한다', 'pkg0203')
Post('으으', '오늘은 졸립고 아프니 말 걸지 마라', 'pkg0203')
Post('ㅋㅋㅋㅋㅋ', '졸림ㅋㅋㅋ', 'Seo')
Post('zzzzz', '오늘도 졸림 ㅋㅋㅋ', 'Seo')
Post('zzzㅋㅋㅋ', '내일도 졸릴 듯?', 'Seo')
Post('애니 추천 간다', '원피스 보셈 재밌음', 'Park0505')
Post('애니 추천 간다-2', '나루토 보셈 재밌음', 'Park0505')
Post('애니 추천 간다-3', '최애의 아이 보셈 재밌음', 'Park0505')

specific_id = 'pkg0203'
specific_word = '음'


for user in posts:
    if specific_id in user['author']:
        print(user['title'])
print('----------')
for user in posts:
    if specific_word in user['content']:
        print(user['title'])

print('입력을 통해 자료를 추가할 수 있습니다. 추가하시겠습니까? (y/n)')
user_answer = input()
if user_answer == 'y':
    print('Member에 추가하시겠습니까? Post에 추가하시겠습니까? (M/P)')
    user_answer = input()
    if user_answer == 'M':
        print('name/username(ID)/password 형태로 입력해주세요.')
        user_answer = input()
        Member(user_answer.split('/')
        [0], user_answer.split('/')[1], user_answer.split('/')[2])
    elif user_answer == 'P':
        print('title/content/username(ID) 형태로 입력해주세요.')
        user_answer = input()
        Post(user_answer.split('/')
        [0], user_answer.split('/')[1], user_answer.split('/')[2])
