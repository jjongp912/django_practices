from guestbook01.models import findall

def test_findall():
    results = findall()
    for result in results:
        print(f'{result["no"]}:{result["name"]}:result["message"]')

def test_insert():
    name = '둘리'
    password = '1234'
    message = '호이~'

    result = insert(name, password, maessge)
    print(f'insert result: {result}')

def main()
    # test_insert()
    test_findall()

if __name__ == '--main__':
    main()